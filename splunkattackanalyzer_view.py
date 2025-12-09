# File: splunkattackanalyzer_view.py
#
# Copyright (c) 2023-2025 Splunk Inc.
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


def _tree_order_resources(current_node, ordered_resources=None, depth=0):
    if not ordered_resources:
        ordered_resources = []

    ordered_resources.append({"depth": depth, "node": current_node})

    for c in current_node["_children"]:
        _tree_order_resources(c, ordered_resources, depth + 1)

    return ordered_resources


def job_summary(provides, all_app_runs, context):
    context["results"] = results = []
    for summary, action_results in all_app_runs:
        for result in action_results:
            ctx_result = get_ctx_result(result)
            if not ctx_result or not ctx_result.get("data"):
                continue

            job = ctx_result["data"]

            resources = job.get("Resources", [])

            for r in resources:
                r["_children"] = [r2 for r2 in resources if r2["ParentID"] == r["ID"]]

            ctx_result["ordered_resources"] = _tree_order_resources(next(r for r in resources if not r["ParentID"]))

            ctx_result["phished_brands"] = [label["Value"] for label in job["Labels"] if label["Type"] == "phished_brand"]
            ctx_result["malware_families"] = [label["Value"] for label in job["Labels"] if label["Type"] == "malware_family"]
            ctx_result["phishkit_families"] = [label["Value"] for label in job["Labels"] if label["Type"] == "phishkit_family"]

            results.append(ctx_result)

    return "job_summary.html"


def get_ctx_result(result):
    ctx_result = {}
    param = result.get_param()
    summary = result.get_summary()
    data = result.get_data()

    ctx_result["param"] = param

    if data:
        ctx_result["data"] = data[0]

    if summary:
        ctx_result["summary"] = summary

    return ctx_result


def ai_malware_analysis(provides, all_app_runs, context):
    """Process AI malware analysis results for display."""

    def _ensure_list(value):
        """Convert a value to a list if it isn't already."""
        if value is None:
            return []
        return value if isinstance(value, list) else [value]

    context["results"] = results = []

    for summary, action_results in all_app_runs:
        for result in action_results:
            ctx_result = get_ctx_result(result)
            if not ctx_result or not ctx_result.get("data"):
                continue

            data = ctx_result["data"]

            # Extract top-level analysis metadata
            ctx_result["verdict"] = data.get("verdict")
            ctx_result["maliciousness_score"] = data.get("maliciousness_score")
            ctx_result["analysis_timestamp"] = data.get("analysis_timestamp")
            ctx_result["cached"] = data.get("cached")

            # Extract and normalize list fields
            ctx_result["executive_summary"] = _ensure_list(data.get("executive_summary"))
            ctx_result["technical_analysis"] = _ensure_list(data.get("technical_analysis"))
            ctx_result["recommendations"] = _ensure_list(data.get("recommendations"))

            # Extract IOCs with type validation
            iocs = data.get("IOCs", {})
            if not isinstance(iocs, dict):
                iocs = {}

            ctx_result["iocs"] = {
                "urls": iocs.get("urls", []),
                "hostnames": iocs.get("hostnames", []),
                "ip_addresses": iocs.get("ip_addresses", []),
                "file_paths": iocs.get("file_paths", []),
                "registry_keys": iocs.get("registry_keys", []),
                "relevant_code": iocs.get("relevant_code", []),
            }

            # Check if there are any IOCs
            ctx_result["has_iocs"] = any(
                (
                    ctx_result["iocs"]["urls"],
                    ctx_result["iocs"]["hostnames"],
                    ctx_result["iocs"]["ip_addresses"],
                    ctx_result["iocs"]["file_paths"],
                    ctx_result["iocs"]["registry_keys"],
                    ctx_result["iocs"]["relevant_code"],
                )
            )

            # Extract hallucinations if present
            hallucinations = iocs.get("hallucinations", {})
            if isinstance(hallucinations, dict) and hallucinations:
                urls = hallucinations.get("urls", [])
                domains = hallucinations.get("domains", [])

                # Only set hallucinations if there are actual items
                if urls or domains:
                    ctx_result["hallucinations"] = {
                        "urls": urls,
                        "domains": domains,
                    }
                else:
                    ctx_result["hallucinations"] = None
            else:
                ctx_result["hallucinations"] = None

            # Extract domain investigation data
            domain_investigations = data.get("domain_investigations", {})
            if isinstance(domain_investigations, dict):
                ctx_result["domain_ages"] = domain_investigations.get("domain_ages", [])
                ctx_result["valid_domains"] = domain_investigations.get("valid_domains", [])
            else:
                ctx_result["domain_ages"] = []
                ctx_result["valid_domains"] = []

            # Extract truncation info
            truncation_info = data.get("truncation_info", {})
            if isinstance(truncation_info, dict):
                ctx_result["was_truncated"] = truncation_info.get("was_truncated", False)
            else:
                ctx_result["was_truncated"] = False

            results.append(ctx_result)

    return "ai_malware_analysis.html"
