# File: splunkattackanalyzer_connector.py
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

import json
import sys
# Phantom App imports
import time
from datetime import datetime

import phantom.app as phantom
import requests
from phantom import vault
from phantom.action_result import ActionResult
from phantom.base_connector import BaseConnector
from phantom.vault import Vault

from phsplunkattackanalyzer import SplunkAttackAnalyzer
from splunkattackanalyzer_consts import *


class RetVal(tuple):
    def __new__(cls, val1, val2=None):

        return tuple.__new__(RetVal, (val1, val2))


def _make_resource_tree(resources):
    root = [root_resource for root_resource in resources if not root_resource["ParentID"]][0]

    def _get_children(root_resource, resources):
        root_resource["Children"] = [child_resource for child_resource in resources if child_resource["ParentID"] == root_resource["ID"]]
        for child_resource in root_resource["Children"]:
            _get_children(child_resource, resources)

    _get_children(root, resources)

    return root


def _validate_internet_region_options(action_result, wa_exit_region):
    # This function makes sure that - 'internet region' is selected from the dropdown menu only
    if wa_exit_region not in list(SPLUNK_ATTACK_ANALYZER_EXIT_REGIONS.keys()):
        return action_result.set_status(phantom.APP_ERROR,
        SPLUNK_ATTACK_ANALYZER_VALIDATE_EXIT_REGION_MESSAGE.format
        (list(SPLUNK_ATTACK_ANALYZER_EXIT_REGIONS.keys())))
    return phantom.APP_SUCCESS


def _validate_user_agent_options(action_result, user_agent):
    # This function makes sure that - user-agent is selected from the dropdown menu only
    if user_agent not in SPLUNK_ATTACK_ANALYZER_ACCEPTED_USER_AGENT_VALUES:
        return action_result.set_status(phantom.APP_ERROR,
        SPLUNK_ATTACK_ANALYZER_VALIDATE_USER_AGENT_MESSAGE.format
        (SPLUNK_ATTACK_ANALYZER_ACCEPTED_USER_AGENT_VALUES))
    return phantom.APP_SUCCESS


def _validate_integer(action_result, parameter, key):
    """
    Validate an integer.
    :param action_result: Action result or BaseConnector object
    :param parameter: input parameter
    :param key: input parameter message key
    :return: status phantom.APP_ERROR/phantom.APP_SUCCESS, integer value of the parameter or None in case of failure
    """
    if parameter is not None:
        try:
            if not float(parameter).is_integer():
                return action_result.set_status(phantom.APP_ERROR, SPLUNK_ATTACK_ANALYZER_VALIDATE_INTEGER_MESSAGE.format(key)), None

            parameter = int(parameter)
        except Exception:
            return action_result.set_status(phantom.APP_ERROR, SPLUNK_ATTACK_ANALYZER_VALIDATE_INTEGER_MESSAGE.format(key)), None

        if parameter < 0:
            return action_result.set_status(phantom.APP_ERROR, SPLUNK_ATTACK_ANALYZER_VALIDATE_NON_NEGATIVE_INTEGER_MESSAGE.format(key)), None

    return phantom.APP_SUCCESS, parameter


class SplunkAttackAnalyzerConnector(BaseConnector):
    def __init__(self):

        # Call the BaseConnectors init first
        super(SplunkAttackAnalyzerConnector, self).__init__()
        self._state = None

    def initialize(self):

        # Load the state in initialize, use it to store data that needs to be accessed across actions
        try:
            self._state = self.load_state()
        except:
            self.debug_print("State file is corrupted, resetting the file")
        if not isinstance(self._state, dict):
            self.debug_print("State file is corrupted, resetting the file")
            self.save_progress("State file is corrupted, resetting the file")
            self._state = {"app_version": self.get_app_json().get("app_version")}

        config = self.get_config()
        ret_val, config["since"] = _validate_integer(self, config.get("since", 24), "since")
        if phantom.is_fail(ret_val):
            return self.get_status()

        # Use the config to initialize fortisiem object to handle connections to the fortisiem server
        self._splunkattackanalyzer = SplunkAttackAnalyzer(config)

        return phantom.APP_SUCCESS

    def _get_error_message_from_exception(self, e):
        """ This method is used to get appropriate error message from the exception.
        :param e: Exception object
        :return: error message
        """

        error_code = SPLUNK_ATTACK_ANALYZER_ERROR_CODE_UNAVAILABLE
        error_message = SPLUNK_ATTACK_ANALYZER_ERROR_MESSAGE_UNAVAILABLE

        try:
            if e.args:
                if len(e.args) > 1:
                    error_code = e.args[0]
                    error_message = str(e)
                elif len(e.args) == 1:
                    error_message = e.args[0]
        except:
            pass

        return "Error Code: {0}. Error Message: {1}".format(error_code, error_message)

    def _add_to_vault(self, data, filename):
        # this temp directory uses "V" since this function is from the CLASS instance not the same as the "v" vault instance
        container_id = self.get_container_id()
        return Vault.create_attachment(data, container_id, file_name=filename)

    def _handle_test_connectivity(self, param):

        self.debug_print("In action handler for: {0}".format(self.get_action_identifier()))

        # Add an action result object to self (BaseConnector) to represent the action for this param
        action_result = self.add_action_result(ActionResult(dict(param)))

        self.save_progress("Connecting to endpoint")
        self.save_progress(f"API URL: {self._splunkattackanalyzer._api_host}")
        self.save_progress(f"App URL: {self._splunkattackanalyzer._app_url}")

        try:
            self._splunkattackanalyzer.get_engines()

        except Exception as e:
            # the call to the 3rd party device or service failed
            # action result should contain all the error details so just return from here
            error_message = self._get_error_message_from_exception(e)
            self.save_progress("{}. {}".format("Connection to server failed",
                                               error_message))
            self.save_progress("Test Connectivity Failed")
            return action_result.set_status(phantom.APP_ERROR)

        # Return success
        self.save_progress("Test Connectivity Passed")
        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_splunk_attack_analyzer_get_job_normalized_forensics(self, params):

        self.save_progress("In action handler for: {0}".format(self.get_action_identifier()))

        action_result = self.add_action_result(ActionResult(dict(params)))

        ret_val, timeout_in_minutes = _validate_integer(action_result, params.get("timeout", 0), "timeout")
        if phantom.is_fail(ret_val):
            return action_result.get_status()

        job_id = params["job_id"]

        job_summary, ret_val = self._get_job_data(action_result, job_id, timeout_in_minutes)
        if phantom.is_fail(ret_val):
            return action_result.get_status()

        if job_summary["State"] == "inprogress":
            return action_result.set_status(phantom.APP_ERROR, SPLUNK_ATTACK_ANALYZER_VALIDATE_JOB_STATE.format("find job forensics"))

        try:

            job_fore = self._splunkattackanalyzer.get_job_normalized_forensics(job_id)

        except Exception as e:
            self.debug_print("Exception occured: {}".format(self._get_error_message_from_exception(e)))
            return action_result.set_status(phantom.APP_ERROR, "Unable to retrieve forensics")

        action_result.add_data(job_fore)
        return action_result.set_status(phantom.APP_SUCCESS, "Job normal forensics retrieved")

    def _handle_splunk_attack_analyzer_submit_file(self, params):

        self.save_progress("In action handler for: {0}".format(self.get_action_identifier()))

        action_result = self.add_action_result(ActionResult(dict(params)))

        submit_data = {}

        try:
            file_id = params.get("file")
            internet_region = params.get("internet_region")
            user_agent = params.get("user_agent")
            custom_user_agent = params.get("custom_user_agent")
            archive_password = params.get("archive_password")
            profile = params.get("profile")

            if internet_region is not None:
                ret_val = _validate_internet_region_options(action_result, internet_region)
                if phantom.is_fail(ret_val):
                    self.save_progress(SPLUNK_ATTACK_ANALYZER_VALIDATE_EXIT_REGION_MESSAGE.
                        format(list(SPLUNK_ATTACK_ANALYZER_EXIT_REGIONS.keys())))
                    return action_result.get_status()
            wa_exit_region = SPLUNK_ATTACK_ANALYZER_EXIT_REGIONS.get(internet_region)

            saa_parameters = {}

            if wa_exit_region:
                saa_parameters["wa_exit_region"] = wa_exit_region

            if archive_password:
                saa_parameters["archive_document_password"] = archive_password

            if user_agent:
                if user_agent == "Default":
                    # No need to set a parameter in this case, SAA will pick the default
                    pass
                elif user_agent == "Custom" or user_agent == "custom":
                    if not custom_user_agent:
                        return action_result.set_status(phantom.APP_ERROR, "Custom user agent needs to be provided as a parameter")
                    saa_parameters["user_agent"] = custom_user_agent
                else:
                    ret_val = _validate_user_agent_options(action_result, user_agent)
                    if phantom.is_fail(ret_val):
                        self.save_progress(SPLUNK_ATTACK_ANALYZER_VALIDATE_USER_AGENT_MESSAGE.
                            format(SPLUNK_ATTACK_ANALYZER_ACCEPTED_USER_AGENT_VALUES))
                        return action_result.get_status()
                    saa_parameters["user_agent"] = f"alias:{user_agent}"

            success, message, info = vault.vault_info(vault_id=file_id)
            file_path = info[0]["path"]
            file_name = info[0]["name"]
            f = open(file_path, "rb")
            file_data = f.read()
            f.close()
            submit_data = self._splunkattackanalyzer.submit_file(file_name, file_data, parameters=saa_parameters, profile=profile)
        except Exception as err:
            self.save_progress(str(err))
            return action_result.set_status(phantom.APP_ERROR, "Unable to submit file")

        submit_data["AppURL"] = "{}/job/{}".format(self._splunkattackanalyzer._app_url, submit_data.get("JobID"))
        action_result.add_data(submit_data)
        self.debug_print("results", dump_object=submit_data)
        return action_result.set_status(phantom.APP_SUCCESS, "Submitted file")

    def _handle_splunk_attack_analyzer_submit_url(self, params):

        self.save_progress("In action handler for: {0}".format(self.get_action_identifier()))

        action_result = self.add_action_result(ActionResult(dict(params)))

        submit_data = {}

        try:
            url = params.get("url")
            internet_region = params.get("internet_region")
            user_agent = params.get("user_agent")
            custom_user_agent = params.get("custom_user_agent")
            archive_password = params.get("archive_password")
            profile = params.get("profile")

            if internet_region is not None:
                ret_val = _validate_internet_region_options(action_result, internet_region)
                if phantom.is_fail(ret_val):
                    self.save_progress(SPLUNK_ATTACK_ANALYZER_VALIDATE_EXIT_REGION_MESSAGE.
                        format(list(SPLUNK_ATTACK_ANALYZER_EXIT_REGIONS.keys())))
                    return action_result.get_status()
            wa_exit_region = SPLUNK_ATTACK_ANALYZER_EXIT_REGIONS.get(internet_region)

            saa_parameters = {}

            if wa_exit_region:
                saa_parameters["wa_exit_region"] = wa_exit_region

            if archive_password:
                saa_parameters["archive_document_password"] = archive_password

            if user_agent:
                if user_agent == "Custom" or user_agent == "custom":
                    if not custom_user_agent:
                        return action_result.set_status(phantom.APP_ERROR, "Custom user agent needs to be provided as a parameter")
                    saa_parameters["user_agent"] = custom_user_agent
                elif user_agent == "Default":
                    # No need to set a parameter in this case, SAA will pick the default
                    pass
                else:
                    ret_val = _validate_user_agent_options(action_result, user_agent)
                    if phantom.is_fail(ret_val):
                        self.save_progress(SPLUNK_ATTACK_ANALYZER_VALIDATE_USER_AGENT_MESSAGE.
                            format(SPLUNK_ATTACK_ANALYZER_ACCEPTED_USER_AGENT_VALUES))
                        return action_result.get_status()
                    saa_parameters["user_agent"] = f"alias:{user_agent}"

            submit_data = self._splunkattackanalyzer.submit_url(url, parameters=saa_parameters, profile=profile)
        except Exception as e:
            self.debug_print("Exception occured: {}".format(self._get_error_message_from_exception(e)))
            return action_result.set_status(phantom.APP_ERROR, f"Unable to submit url: {self._get_error_message_from_exception(e)}")

        submit_data["AppURL"] = "{}/job/{}".format(self._splunkattackanalyzer._app_url, submit_data.get("JobID"))
        action_result.add_data(submit_data)
        self.debug_print("results", dump_object=submit_data)
        return action_result.set_status(phantom.APP_SUCCESS, "Submitted URL")

    def _handle_splunk_attack_analyzer_list_recent_jobs(self, params):

        self.save_progress("In action handler for: {0}".format(self.get_action_identifier()))

        action_result = self.add_action_result(ActionResult(dict(params)))

        ret_val, limit = _validate_integer(action_result, params.get("limit", 10), "limit")
        if phantom.is_fail(ret_val):
            return action_result.get_status()

        try:
            job_list = self._splunkattackanalyzer.get_recent_jobs(num_jobs=limit)

            action_result.append_to_message("Gathered recent jobs")
            action_result.update_summary({"job_count": len(job_list)})
        except Exception as e:
            self.debug_print("Exception occured: {}".format(self._get_error_message_from_exception(e)))
            return action_result.set_status(phantom.APP_ERROR, "Unable to get jobs")

        for data in job_list:
            action_result.add_data(data)
        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_on_poll(self, params):

        self.save_progress("In action handler for: {0}".format(self.get_action_identifier()))

        manual_polling = self.is_poll_now()

        action_result = self.add_action_result(ActionResult(dict(params)))
        datetime_checkpoint = None

        if not manual_polling:
            self.debug_print("DEBUGGER: Starting polling now")
            checkpoint = self._state.get("UpdatedAt_Checkpoint")
            try:
                if checkpoint:
                    datetime_checkpoint = datetime.strptime(checkpoint, "%Y-%m-%dT%H:%M:%S.%fZ")
            except:
                self.debug_print("State file is corrupted, resetting the file")
                self.save_progress("State file is corrupted, resetting the file")
                self._state = {"app_version": self.get_app_json().get("app_version")}
                self._handle_on_poll(params)

        ret_val, limit = _validate_integer(action_result, params.get("container_count", 0), "container_count")
        if phantom.is_fail(ret_val):
            return action_result.get_status()

        try:
            payload = self._splunkattackanalyzer.poll_for_done_jobs(limit, datetime_checkpoint)
        except Exception as e:
            self.debug_print("Exception occured: {}".format(self._get_error_message_from_exception(e)))
            return action_result.set_status(phantom.APP_ERROR, "Unable to get jobs")
        if payload:
            for job in payload:
                self.add_to_container(job)
            if not manual_polling:
                self._state["UpdatedAt_Checkpoint"] = payload[0].get("UpdatedAt")
                self.save_state(self._state)
        else:
            self.debug_print("payload_empty")
        return action_result.set_status(phantom.APP_SUCCESS)

    def add_to_container(self, job):
        container = {}
        job_id = job["ID"]
        submission_name = job["Submission"]["Name"]
        container["name"] = submission_name
        container["source_data_identifier"] = job_id
        container["run_automation"] = True
        container["data"] = job
        container["artifacts"] = []

        for resource in job["Resources"]:
            severity = "low"
            if resource["DisplayScore"] >= 70:
                severity = "high"
            elif resource["DisplayScore"] >= 30:
                severity = "medium"

            if resource["Type"] == "URL":
                container["artifacts"].append(
                    {
                        "cef": {"requestURL": resource["Name"], "data": resource},
                        "label": "url",
                        "name": resource["Name"],
                        "severity": severity,
                        "type": "url",
                    }
                )
            elif resource["Type"] == "file":
                container["artifacts"].append(
                    {
                        "cef": {
                            "fileName": resource["Name"],
                            "fileHash": resource["FileMetadata"]["SHA256"],
                            "fileSize": resource["FileMetadata"]["Size"],
                            "fileType": resource["FileMetadata"]["MimeType"],
                            "data": resource
                        },
                        "label": "file",
                        "name": resource["Name"],
                        "severity": severity,
                        "type": "file",
                    }
                )

        ret_val, msg, cid = self.save_container(container)
        if phantom.is_fail(ret_val):
            self.save_progress("Error saving container: {}".format(msg))
            self.debug_print("Error saving container: {} -- CID: {}".format(msg, cid))

    def _get_job_data(self, action_result, job_id, timeout_in_minutes):
        start_time = time.time()
        while True:
            try:
                job_summary = self._splunkattackanalyzer.get_job(job_id)

                if not timeout_in_minutes:
                    return job_summary, action_result.set_status(phantom.APP_SUCCESS)
                elif job_summary.get("State") == "done":
                    return job_summary, action_result.set_status(phantom.APP_SUCCESS)
                elif time.time() < start_time + timeout_in_minutes * 60:
                    time.sleep(JOB_POLL_INTERVAL)
                    continue
                else:
                    return None, action_result.set_status(phantom.APP_ERROR, SPLUNK_ATTACK_ANALYZER_TIMEOUT_ERROR)
            except Exception as e:
                error_message = self._get_error_message_from_exception(e)
                return None, action_result.set_status(phantom.APP_ERROR, "Exception occured: {}".format(error_message))

    def _handle_splunk_attack_analyzer_get_job_summary(self, params):

        self.save_progress("In action handler for: {0}".format(self.get_action_identifier()))

        action_result = self.add_action_result(ActionResult(dict(params)))

        ret_val, timeout_in_minutes = _validate_integer(action_result, params.get("timeout", 0), "timeout")
        if phantom.is_fail(ret_val):
            return action_result.get_status()
        job_id = params["job_id"]

        self.debug_print(
            "Getting summary for job ID: {}, timeout: {}".format(job_id, timeout_in_minutes)
        )

        job_summary, ret_val = self._get_job_data(action_result, job_id, timeout_in_minutes)
        if phantom.is_fail(ret_val):
            return action_result.get_status()

        job_summary["ResourceTree"] = _make_resource_tree(job_summary.get("Resources"))
        app_url = "{}/job/{}".format(self._splunkattackanalyzer._app_url, job_id)

        action_result.add_data(job_summary)
        action_result.update_summary({"Job ID": job_id, "Score": job_summary.get("DisplayScore"), "AppURL": app_url})

        self.save_progress("Job Summary Retrieved")

        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_splunk_attack_analyzer_get_job_pdf(self, params):

        self.save_progress("In action handler for: {0}".format(self.get_action_identifier()))

        action_result = self.add_action_result(ActionResult(dict(params)))

        ret_val, timeout_in_minutes = _validate_integer(action_result, params.get("timeout", 0), "timeout")
        if phantom.is_fail(ret_val):
            return action_result.get_status()

        job_id = params.get("job_id")

        # do this just to make sure the job is completed
        job_summary, ret_val = self._get_job_data(action_result, job_id, timeout_in_minutes)
        if phantom.is_fail(ret_val):
            return action_result.get_status()

        if job_summary["State"] == "inprogress":
            return action_result.set_status(phantom.APP_ERROR, SPLUNK_ATTACK_ANALYZER_VALIDATE_JOB_STATE.format("download pdf"))

        try:
            pdf_data = self._splunkattackanalyzer.download_job_pdf(job_id)

            vault_detail = self._add_to_vault(data=pdf_data, filename=f"Splunk Attack Analyzer job report {job_id}.pdf")
            vault_detail["file_name"] = f"Splunk Attack Analyzer job report {job_id}.pdf"
            action_result.add_data(vault_detail)
            action_result.append_to_message("Attached PDF report")
        except Exception as e:
            self.debug_print("Exception occured: {}".format(self._get_error_message_from_exception(e)))
            return action_result.set_status(phantom.APP_ERROR, "Unable to get PDF report")

        return action_result.set_status(phantom.APP_SUCCESS, "Successfully attached PDF report")

    def _handle_splunk_attack_analyzer_get_job_screenshots(self, params):

        self.save_progress("In action handler for: {0}".format(self.get_action_identifier()))

        action_result = self.add_action_result(ActionResult(dict(params)))

        ret_val, timeout_in_minutes = _validate_integer(action_result, params.get("timeout", 0), "timeout")
        if phantom.is_fail(ret_val):
            return action_result.get_status()
        job_id = params.get("job_id")

        # do this just to make sure the job is completed
        job_summary, ret_val = self._get_job_data(action_result, job_id, timeout_in_minutes)
        if phantom.is_fail(ret_val):
            return action_result.get_status()

        if job_summary["State"] == "inprogress":
            return action_result.set_status(phantom.APP_ERROR, SPLUNK_ATTACK_ANALYZER_VALIDATE_JOB_STATE.format("download screenshots"))

        try:
            forensics = self._splunkattackanalyzer.get_job_normalized_forensics(job_id)

            for i, ss in enumerate(forensics.get("Screenshots", [])):
                self.save_progress(f"Downloading screenshot #{i}")

                shot_data = self._splunkattackanalyzer.download_artifact(ss["ArtifactPath"])
                vault_detail = self._add_to_vault(shot_data, f"Splunk Attack Analyzer screenshot {job_id} #{i}.png")
                vault_detail["file_name"] = f"Splunk Attack Analyzer screenshot {job_id} #{i}.png"
                action_result.add_data(vault_detail)

            screenshot_count = i + 1

            action_result.append_to_message(f"Attached {screenshot_count} screenshots")
            action_result.update_summary({"screenshot_count": screenshot_count})
        except Exception as e:
            self.debug_print("Exception occured: {}".format(self._get_error_message_from_exception(e)))
            return action_result.set_status(phantom.APP_ERROR, "Unable to download screenshots")

        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_splunk_attack_analyzer_get_job_system_tags(self, params):
        self.save_progress("In action handler for: {0}".format(self.get_action_identifier()))

        action_result = self.add_action_result(ActionResult(dict(params)))

        ret_val, timeout_in_minutes = _validate_integer(action_result, params.get("timeout", 0), "timeout")
        if phantom.is_fail(ret_val):
            return action_result.get_status()

        job_id = params["job_id"]

        job_summary, ret_val = self._get_job_data(action_result, job_id, timeout_in_minutes)
        if phantom.is_fail(ret_val):
            return action_result.get_status()

        # Ensure completion of job
        if job_summary["State"] == "inprogress":
            return action_result.set_status(phantom.APP_ERROR, SPLUNK_ATTACK_ANALYZER_VALIDATE_JOB_STATE.format("get system tags"))

        system_tags = []
        for label in job_summary.get("Labels", []):
            if label.get("Type") == "system_tag":
                system_tags.append(label.get("Value"))
                action_result.add_data(label)

        summary = {
            "job_id": job_id,
            "total_system_tags": len(system_tags),
            "requires_manual_review": any(tag in system_tags for tag in SPLUNK_ATTACK_ANALYZER_SYSTEM_TAGS),
        }
        action_result.update_summary(summary)

        return action_result.set_status(phantom.APP_SUCCESS, "Successfully retrieved system tags")

    def handle_action(self, param):

        ret_val = phantom.APP_SUCCESS

        # Get the action that we are supposed to execute for this App Run
        action_id = self.get_action_identifier()

        self.debug_print("action_id", self.get_action_identifier())

        if action_id == "test_connectivity":
            ret_val = self._handle_test_connectivity(param)
        elif action_id == "splunk_attack_analyzer_get_job_normalized_forensics":
            ret_val = self._handle_splunk_attack_analyzer_get_job_normalized_forensics(param)
        elif action_id == "splunk_attack_analyzer_get_job_summary":
            ret_val = self._handle_splunk_attack_analyzer_get_job_summary(param)
        elif action_id == "splunk_attack_analyzer_list_recent_jobs":
            ret_val = self._handle_splunk_attack_analyzer_list_recent_jobs(param)
        elif action_id == "splunk_attack_analyzer_submit_file":
            ret_val = self._handle_splunk_attack_analyzer_submit_file(param)
        elif action_id == "splunk_attack_analyzer_submit_url":
            ret_val = self._handle_splunk_attack_analyzer_submit_url(param)
        elif action_id == "splunk_attack_analyzer_get_job_pdf":
            ret_val = self._handle_splunk_attack_analyzer_get_job_pdf(param)
        elif action_id == "splunk_attack_analyzer_get_job_screenshots":
            ret_val = self._handle_splunk_attack_analyzer_get_job_screenshots(param)
        elif action_id == "splunk_attack_analyzer_get_job_system_tags":
            ret_val = self._handle_splunk_attack_analyzer_get_job_system_tags(param)
        elif action_id == "on_poll":
            ret_val = self._handle_on_poll(param)
        return ret_val

    def finalize(self):
        # Save the state, this data is saved accross actions and app upgrades
        self.save_state(self._state)
        return phantom.APP_SUCCESS


def main():
    import argparse

    argparser = argparse.ArgumentParser()

    argparser.add_argument('input_test_json', help='Input Test JSON file')
    argparser.add_argument('-u', '--username', help='username', required=False)
    argparser.add_argument('-p', '--password', help='password', required=False)
    argparser.add_argument('-v', '--verify', action='store_true', help='verify', required=False, default=False)

    args = argparser.parse_args()
    session_id = None
    verify = args.verify

    username = args.username
    password = args.password

    if username is not None and password is None:

        # User specified a username but not a password, so ask
        import getpass
        password = getpass.getpass("Password: ")

    if username and password:
        try:
            login_url = SplunkAttackAnalyzerConnector._get_phantom_base_url() + '/login'

            print("Accessing the Login page")
            r = requests.get(login_url, verify=verify, timeout=30)
            csrftoken = r.cookies['csrftoken']

            data = dict()
            data['username'] = username
            data['password'] = password
            data['csrfmiddlewaretoken'] = csrftoken

            headers = dict()
            headers['Cookie'] = 'csrftoken=' + csrftoken
            headers['Referer'] = login_url

            print("Logging into Platform to get the session id")
            r2 = requests.post(login_url, verify=verify, data=data, headers=headers, timeout=30)
            session_id = r2.cookies['sessionid']
        except Exception as e:
            print("Unable to get session id from the platform. Error: " + str(e))
            sys.exit(1)

    with open(args.input_test_json) as f:
        in_json = f.read()
        in_json = json.loads(in_json)
        print(json.dumps(in_json, indent=4))

        connector = SplunkAttackAnalyzerConnector()
        connector.print_progress_message = True

        if session_id is not None:
            in_json['user_session_token'] = session_id
            connector._set_csrf_info(csrftoken, headers['Referer'])

        ret_val = connector._handle_action(json.dumps(in_json), None)
        print(json.dumps(json.loads(ret_val), indent=4))

    sys.exit(0)


if __name__ == '__main__':
    main()
