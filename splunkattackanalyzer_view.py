# File: splunkattackanalyzer_view.py
#
# Copyright (c) 2023-2024 Splunk Inc.
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

            ctx_result["ordered_resources"] = _tree_order_resources([r for r in resources if not r["ParentID"]][0])

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
