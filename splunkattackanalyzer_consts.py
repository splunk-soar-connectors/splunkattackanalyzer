# File: splunkattackanalyzer_consts.py
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

SPLUNK_ATTACK_ANALYZER_VALIDATE_INTEGER_MESSAGE = "Please provide a valid integer value in the '{0}' parameter"
SPLUNK_ATTACK_ANALYZER_VALIDATE_USER_AGENT_MESSAGE = "Please provide a valid value of 'user agent' parameter from {0}"
SPLUNK_ATTACK_ANALYZER_VALIDATE_NON_NEGATIVE_INTEGER_MESSAGE = "Please provide a valid non-negative integer value in the '{0}' parameter"
SPLUNK_ATTACK_ANALYZER_VALIDATE_EXIT_REGION_MESSAGE = "Please provide a valid value of 'Internet Region' parameter from {0}"
SPLUNK_ATTACK_ANALYZER_VALIDATE_JOB_STATE = "Unable to {0}. The job is still in in-progress state"
SPLUNK_ATTACK_ANALYZER_TIMEOUT_ERROR = "Timed out while waiting for job to be completed. Please retry the action again after sometime"
JOB_POLL_INTERVAL = 30
SPLUNK_ATTACK_ANALYZER_ERROR_MESSAGE_UNAVAILABLE = "Error message unavailable. \
    Please check the asset configuration and|or the action parameters."
SPLUNK_ATTACK_ANALYZER_ERROR_CODE_UNAVAILABLE = "Error code unavailable"
SPLUNK_ATTACK_ANALYZER_EXIT_REGIONS = {
    "US Residential": "us_residential",
    "US": "us",
    "Asia": "asia",
    "Europe": "europe"
}

# Update this if user-agent dropdown is updated
SPLUNK_ATTACK_ANALYZER_ACCEPTED_USER_AGENT_VALUES = [
    "Desktop Chrome",
    "Desktop Edge",
    "Desktop Firefox",
    "Desktop Safari",
    "Galaxy S8",
    "iPhone 6",
    "iPhone 8",
    "iPhone 12",
    "Pixel 5"
]
