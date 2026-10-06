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

import importlib.util
import sys
import types
import unittest
from pathlib import Path
from unittest.mock import patch


requests_stub = types.ModuleType("requests")
requests_stub.get = None
module_spec = importlib.util.spec_from_file_location(
    "phsplunkattackanalyzer_under_test", Path(__file__).resolve().parents[1] / "phsplunkattackanalyzer.py"
)
with patch.dict(sys.modules, {"requests": requests_stub}):
    phsplunkattackanalyzer = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(phsplunkattackanalyzer)


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


class UrlPathEncodingTest(unittest.TestCase):
    def setUp(self):
        self.client = object.__new__(phsplunkattackanalyzer.SplunkAttackAnalyzer)
        self.client._host = "https://api.example/v1"
        self.client._proxy = None
        self.client._verify = True
        self.client.get_header = lambda: {}

    def test_artifact_path_keeps_separators_and_encodes_segments(self):
        artifact_path = "2026-07-07/unitedairlines/job/screenshot #1.png"

        with patch.object(phsplunkattackanalyzer.requests, "get", return_value=FakeResponse()) as get:
            self.client.download_artifact(artifact_path)

        self.assertEqual(
            get.call_args.args[0],
            "https://api.example/v1/jobs/artifacts/2026-07-07/unitedairlines/job/screenshot%20%231%2Epng",
        )

    def test_artifact_path_rejects_invalid_segments(self):
        invalid_paths = (None, "", "/job/file.png", "job/file.png/", "job//file.png", "job/./file.png", "job/../file.png")

        with patch.object(phsplunkattackanalyzer.requests, "get") as get:
            for artifact_path in invalid_paths:
                with self.subTest(artifact_path=artifact_path), self.assertRaises(ValueError):
                    self.client.download_artifact(artifact_path)

        get.assert_not_called()

    def test_job_ids_remain_single_path_segments(self):
        job_id = "job/other?query=1"
        request_paths = (
            ("get_job", "/jobs/job%2Fother%3Fquery%3D1"),
            ("get_job_normalized_forensics", "/jobs/job%2Fother%3Fquery%3D1/forensics"),
            ("download_job_pdf", "/jobs/job%2Fother%3Fquery%3D1/pdfreport"),
        )

        for method_name, request_path in request_paths:
            with self.subTest(method_name=method_name):
                with patch.object(phsplunkattackanalyzer.requests, "get", return_value=FakeResponse()) as get:
                    getattr(self.client, method_name)(job_id)

                self.assertEqual(get.call_args.args[0], f"https://api.example/v1{request_path}")


if __name__ == "__main__":
    unittest.main()
