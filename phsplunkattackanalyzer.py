# File: phsplunkattackanalyzer.py
#
# Copyright (c) 2023-2026 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions
# and limitations under the License.

import json
from datetime import UTC, datetime, timedelta
from urllib.parse import urlsplit, urlunsplit

import requests


""" CONSTANTS """
DATE_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
API_VERSION = "v1"
REQUEST_TIMEOUT = 60
MAX_POLL_PAGES = 100
MAX_POLL_JOBS = 10000
MAX_DOWNLOAD_SIZE = 100 * 1024 * 1024
DOWNLOAD_CHUNK_SIZE = 1024 * 1024


def _normalize_app_url(app_url):
    try:
        parsed = urlsplit(app_url)
        hostname = parsed.hostname
        port = parsed.port
    except (TypeError, ValueError) as exc:
        raise ValueError("App URL is not a valid URL") from exc

    if (
        parsed.scheme.casefold() != "https"
        or not hostname
        or not hostname.casefold().startswith("app.")
        or parsed.username
        or parsed.password
        or parsed.path not in ("", "/")
        or parsed.query
        or parsed.fragment
    ):
        raise ValueError("App URL must be an HTTPS origin whose hostname starts with 'app.'")

    hostname = hostname.casefold()
    app_netloc = hostname if port is None else f"{hostname}:{port}"
    api_hostname = f"api.{hostname[4:]}"
    api_netloc = api_hostname if port is None else f"{api_hostname}:{port}"
    return urlunsplit(("https", app_netloc, "", "", "")), urlunsplit(("https", api_netloc, "", "", ""))


def _read_bounded_response(response):
    try:
        content_length = response.headers.get("Content-Length")
        if content_length is not None and int(content_length) > MAX_DOWNLOAD_SIZE:
            raise ValueError(f"Download exceeds the {MAX_DOWNLOAD_SIZE}-byte size limit")

        content = bytearray()
        for chunk in response.iter_content(chunk_size=DOWNLOAD_CHUNK_SIZE):
            if not chunk:
                continue
            if len(content) + len(chunk) > MAX_DOWNLOAD_SIZE:
                raise ValueError(f"Download exceeds the {MAX_DOWNLOAD_SIZE}-byte size limit")
            content.extend(chunk)
        return bytes(content)
    finally:
        response.close()


class AuthenticationException(Exception):
    pass


class SplunkAttackAnalyzer:
    def __init__(self, config):
        self._app_url, self._api_host = _normalize_app_url(config.get("app_url", "https://app.twinwave.io"))
        self._host = f"{self._api_host}/{API_VERSION}"

        self._api_key = config["api_token"]
        self._proxy = None
        self._verify = True
        self._since = config["since"]

    def get_header(self):
        return {"X-API-KEY": self._api_key}

    def get_recent_jobs(self, num_jobs=10, username=None, source=None, state=None):
        url = f"{self._host}/jobs/recent"
        jobs_list = list()
        params = {}
        params["start"] = 0
        if username:
            params["username"] = username
        if source:
            params["source"] = source
        if state:
            params["state"] = state

        self.paginate_jobs(num_jobs, params, url, jobs_list)

        return jobs_list

    def paginate_jobs(self, num_jobs, params, url, jobs_list):
        while num_jobs > 0:
            params["count"] = 100 if num_jobs > 100 else num_jobs
            resp = requests.get(url, params=params, headers=self.get_header(), verify=self._verify, proxies=self._proxy, timeout=REQUEST_TIMEOUT)
            resp.raise_for_status()
            job_json = resp.json()
            if not job_json:
                break
            jobs_list.extend(job_json)
            params["start"] = params["start"] + 100
            num_jobs = num_jobs - 100

    def poll_for_done_jobs(self, limit, checkpoint):
        url = f"{self._host}/jobs/poll"
        return self.poll_paginate(url, limit, datetime.now(UTC), checkpoint)

    def poll_paginate(self, url, limit, action_start_time, checkpoint):
        job_list = list()
        epoch_convert_time = None
        if checkpoint:
            if checkpoint.tzinfo is None:
                checkpoint = checkpoint.replace(tzinfo=UTC)
            epoch_convert_time = checkpoint.timestamp()

        if not epoch_convert_time:
            epoch_convert_time = (action_start_time - timedelta(hours=self._since)).timestamp()
        param = {"since": int(epoch_convert_time)}
        for _ in range(MAX_POLL_PAGES):
            resp = requests.get(url, params=param, headers=self.get_header(), verify=self._verify, proxies=self._proxy, timeout=REQUEST_TIMEOUT)
            resp.raise_for_status()
            resp_json = resp.json()
            jobs = resp_json.get("Jobs") or []
            job_list.extend(jobs)
            if len(job_list) > MAX_POLL_JOBS:
                raise RuntimeError(f"Polling returned more than {MAX_POLL_JOBS} jobs")
            next_token = resp_json.get("NextToken")
            if not jobs or not next_token:
                break
            param = {"token": next_token}
        else:
            raise RuntimeError(f"Polling exceeded the {MAX_POLL_PAGES}-page safety limit")

        job_list.sort(key=lambda job: job.get("UpdatedAt") or "")
        return job_list[:limit] if limit else job_list

    def get_engines(self):
        url = f"{self._host}/engines"
        resp = requests.get(url, headers=self.get_header(), verify=self._verify, proxies=self._proxy, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
        return resp.json()

    def get_job(self, job_id):
        url = f"{self._host}/jobs/{job_id}"
        resp = requests.get(url, headers=self.get_header(), verify=self._verify, proxies=self._proxy, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
        return resp.json()

    def get_job_normalized_forensics(self, job_id):
        url = f"{self._host}/jobs/{job_id}/forensics"
        resp = requests.get(url, headers=self.get_header(), verify=self._verify, proxies=self._proxy, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
        return resp.json()

    def submit_url(self, scan_url, engine_list=[], parameters=None, priority=None, profile=None):
        parameters_to_submit = self.format_parameters_for_submission(parameters)

        url = f"{self._host}/jobs/urls"
        req = {"url": scan_url, "engines": engine_list, "parameters": parameters_to_submit}
        if priority:
            req["priority"] = priority
        if profile:
            req["profile"] = profile

        resp = requests.post(url, json=req, headers=self.get_header(), verify=self._verify, proxies=self._proxy, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
        return resp.json()

    def submit_file(self, file_name, file_obj, engine_list=[], priority=None, profile=None, parameters=None):
        url = f"{self._host}/jobs/files"
        payload = {}
        file_dict = {"filedata": file_obj}
        payload["engines"] = (None, json.dumps(engine_list))
        payload["filename"] = (None, file_name)
        payload["priority"] = priority
        payload["profile"] = profile
        payload["parameters"] = json.dumps(self.format_parameters_for_submission(parameters))

        resp = requests.post(
            url, data=payload, files=file_dict, headers=self.get_header(), verify=self._verify, proxies=self._proxy, timeout=REQUEST_TIMEOUT
        )
        resp.raise_for_status()
        return resp.json()

    def download_job_pdf(self, job_id):
        url = f"{self._host}/jobs/{job_id}/pdfreport"
        resp = requests.get(url, headers=self.get_header(), verify=self._verify, proxies=self._proxy, stream=True, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
        return _read_bounded_response(resp)

    def download_artifact(self, artifact_path):
        url = f"{self._host}/jobs/artifacts/{artifact_path}"
        resp = requests.get(url, headers=self.get_header(), verify=self._verify, proxies=self._proxy, stream=True, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
        return _read_bounded_response(resp)

    def format_parameters_for_submission(self, param_dict):
        if not param_dict:
            return []

        return [{"Name": name, "Value": value} for name, value in param_dict.items()]
