# File: phsplunkattackanalyzer.py
#
# Copyright (c) 2023 Splunk Inc.
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
import time
from datetime import datetime, timedelta

import requests

""" CONSTANTS """
DATE_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
API_HOST = "https://api.twinwave.io"
API_VERSION = "v1"
REQUEST_TIMEOUT = 60


class AuthenticationException(Exception):
    pass


class SplunkAttackAnalyzer:
    def __init__(self, config):
        self._host = f"{API_HOST}/{API_VERSION}"
        self._base_url = "https://app.twinwave.io/"
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
        time_now = datetime.now()
        jobs = []

        try:
            jobs = self.poll_paginate(url, limit, time_now, checkpoint)
        except Exception:
            time.sleep(10)

        return jobs

    def poll_paginate(self, url, limit, action_start_time, checkpoint):
        job_list = list()
        epoch_convert_time = None
        if checkpoint:
            epoch_convert_time = checkpoint.timestamp()

        if not epoch_convert_time:
            epoch_convert_time = (action_start_time - timedelta(hours=self._since)).timestamp()
        param = {"since": int(epoch_convert_time)}
        while True:
            resp = requests.get(url, params=param, headers=self.get_header(), timeout=REQUEST_TIMEOUT)
            resp_json = resp.json()
            job_list.extend(resp_json.get("Jobs"))
            if not resp_json.get("Jobs"):
                break
            if limit and limit <= len(job_list):
                return job_list[:limit]
            param = {"token": resp_json.get("NextToken")}
        return job_list

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
        url = f"{self._host}/jobs/urls"
        req = {"url": scan_url, "engines": engine_list, "parameters": parameters}
        if priority:
            req["priority"] = priority
        if profile:
            req["profile"] = profile

        resp = requests.post(url, json=req, headers=self.get_header(), verify=self._verify, proxies=self._proxy, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
        return resp.json()

    def submit_file(self, file_name, file_obj, engine_list=[], priority=None, profile=None):
        url = f"{self._host}/jobs/files"
        payload = {}
        file_dict = {"filedata": file_obj}
        payload["engines"] = (None, json.dumps(engine_list))
        payload["filename"] = (None, file_name)
        payload["priority"] = priority
        payload["profile"] = profile

        resp = requests.post(url, data=payload, files=file_dict, headers=self.get_header(), verify=self._verify, proxies=self._proxy,
            timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
        return resp.json()

    def download_job_pdf(self, job_id):
        url = f"{self._host}/jobs/{job_id}/pdfreport"
        resp = requests.get(url, headers=self.get_header(), verify=self._verify, proxies=self._proxy, stream=True, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
        return resp.content

    def download_artifact(self, artifact_path):
        url = f"{self._host}/jobs/artifacts/{artifact_path}"
        resp = requests.get(url, headers=self.get_header(), verify=self._verify, proxies=self._proxy, stream=True, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
        return resp.content
