# Copyright (c) 2026 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import importlib
import sys
import types
import unittest
from unittest.mock import patch


requests_stub = types.ModuleType("requests")
requests_stub.get = None
sys.modules["requests"] = requests_stub
phsplunkattackanalyzer = importlib.import_module("phsplunkattackanalyzer")


class FakeResponse:
    headers = {}

    def raise_for_status(self):
        pass

    def json(self):
        return {}

    def iter_content(self, chunk_size):
        return iter(())

    def close(self):
        pass


class RequestCapture:
    def __init__(self):
        self.url = None

    def __call__(self, url, **_kwargs):
        self.url = url
        return FakeResponse()


class UrlPathEncodingTest(unittest.TestCase):
    def setUp(self):
        self.client = object.__new__(phsplunkattackanalyzer.SplunkAttackAnalyzer)
        self.client._host = "https://api.example/v1"
        self.client._proxy = None
        self.client._verify = True
        self.client.get_header = lambda: {}

    def test_job_id_is_encoded_in_all_job_request_paths(self):
        job_id = "../engines?count=100#fragment"
        expected_job_id = "%2E%2E%2Fengines%3Fcount%3D100%23fragment"
        request_paths = (
            ("get_job", f"/jobs/{expected_job_id}"),
            ("get_job_normalized_forensics", f"/jobs/{expected_job_id}/forensics"),
            ("download_job_pdf", f"/jobs/{expected_job_id}/pdfreport"),
        )

        for method_name, request_path in request_paths:
            with self.subTest(method_name=method_name):
                capture = RequestCapture()
                with patch.object(phsplunkattackanalyzer.requests, "get", capture):
                    getattr(self.client, method_name)(job_id)

                self.assertEqual(capture.url, f"https://api.example/v1{request_path}")

    def test_artifact_path_is_encoded_as_one_path_segment(self):
        artifact_path = "../../etc/passwd?name=report#fragment"
        encoded_artifact_path = "%2E%2E%2F%2E%2E%2Fetc%2Fpasswd%3Fname%3Dreport%23fragment"
        capture = RequestCapture()

        with patch.object(phsplunkattackanalyzer.requests, "get", capture):
            self.client.download_artifact(artifact_path)

        self.assertEqual(capture.url, f"https://api.example/v1/jobs/artifacts/{encoded_artifact_path}")

    def test_valid_job_id_remains_unchanged(self):
        job_id = "63572265-c5ae-402f-9fc1-6c90547482ee"
        capture = RequestCapture()

        with patch.object(phsplunkattackanalyzer.requests, "get", capture):
            self.client.get_job(job_id)

        self.assertEqual(capture.url, f"https://api.example/v1/jobs/{job_id}")


if __name__ == "__main__":
    unittest.main()
