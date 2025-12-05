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
    context["results"] = results = []
    for summary, action_results in all_app_runs:
        for result in action_results:
            ctx_result = get_ctx_result(result)
            if not ctx_result or not ctx_result.get("data"):
                continue

            data = ctx_result["data"]

            # Extract executive summary (handle both list and other formats)
            ctx_result["executive_summary"] = data.get("executive_summary", [])
            if not isinstance(ctx_result["executive_summary"], list):
                ctx_result["executive_summary"] = [ctx_result["executive_summary"]] if ctx_result["executive_summary"] else []

            # Extract technical analysis
            ctx_result["technical_analysis"] = data.get("technical_analysis", [])
            if not isinstance(ctx_result["technical_analysis"], list):
                ctx_result["technical_analysis"] = [ctx_result["technical_analysis"]] if ctx_result["technical_analysis"] else []

            # Extract recommendations
            ctx_result["recommendations"] = data.get("recommendations", [])
            if not isinstance(ctx_result["recommendations"], list):
                ctx_result["recommendations"] = [ctx_result["recommendations"]] if ctx_result["recommendations"] else []

            # Extract IOCs
            iocs = data.get("IOCs", {})
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
                [
                    ctx_result["iocs"]["urls"],
                    ctx_result["iocs"]["hostnames"],
                    ctx_result["iocs"]["ip_addresses"],
                    ctx_result["iocs"]["file_paths"],
                    ctx_result["iocs"]["registry_keys"],
                    ctx_result["iocs"]["relevant_code"],
                ]
            )

            # Extract hallucinations if present
            hallucinations = iocs.get("hallucinations", {})
            if hallucinations and (hallucinations.get("urls") or hallucinations.get("domains")):
                ctx_result["hallucinations"] = {
                    "urls": hallucinations.get("urls", []),
                    "domains": hallucinations.get("domains", []),
                }
            else:
                ctx_result["hallucinations"] = None

            # Extract domain investigation data
            domain_investigations = data.get("domain_investigations", {})
            ctx_result["domain_ages"] = domain_investigations.get("domain_ages", [])

            results.append(ctx_result)

    return "ai_malware_analysis.html"
