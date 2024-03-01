[comment]: # " File: README.md"
[comment]: # ""
[comment]: # "  Copyright (c) 2023-2024 Splunk Inc."
[comment]: # ""
[comment]: # "  Licensed under the Apache License, Version 2.0 (the 'License');"
[comment]: # "  you may not use this file except in compliance with the License."
[comment]: # "  {% comment %} You may obtain a copy of the License at"
[comment]: # ""
[comment]: # "      http://www.apache.org/licenses/LICENSE-2.0"
[comment]: # ""
[comment]: # "  Unless required by applicable law or agreed to in writing, software distributed under"
[comment]: # "  the License is distributed on an 'AS IS' BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,"
[comment]: # "  either express or implied. See the License for   and limitations under the License."
[comment]: # ""
### The Splunk Attack Analyzer SOAR app can be used to connect with the [Splunk Attack Analyzer analysis platform](https://app.twinwave.io/)

<div style="margin-left: 2em">

Common points for both Manual and Scheduled | Interval polling:



-   The on poll action fetches and ingests the done/completed jobs in the form of artifacts and
    containers.
-   One container will be created for each job and the artifacts will have information about the
    resources present in the particular job, hence for every resource present, one artifact will be
    created.
-   In case of duplicate data, containers would not be created again.

<div style="margin-left: 2em">

Manual Polling:



-   During manual polling, the app starts ingestion from the time specified in the since
    configuration parameter.
-   If 2 hours is specified in the since parameter, for every cycle jobs of the last 2 hours will be
    fetched and ingested. If no value is specified, by default jobs of the last 24 hours will be
    ingested.
-   The app will fetch the number of jobs based on the value provided in the Maximum
    containers(container_count) for manual polling
-   For manual polling, the time of the last ingested job will not be stored in the state file, and
    for every cycle all the jobs from the time mentioned in the since parameter will be fetched.

<div style="margin-left: 2em">

Schedule | Interval Polling:



-   For the first run of scheduled | interval polling, the app starts ingestion from the time
    specified in the since configuration parameter.
-   If 2 hours is specified in the since parameter, for the first run all the jobs of the last 2
    hours will be fetched, and if no value is specified, by default jobs of the last 24 hours will
    be ingested for the first run.
-   After the completion of every run, the 'UpdatedAt' time of the latest job will be stored in the
    state file against the key "UpdatedAt_Checkpoint" and for the next run, that time will be
    considered to fetch the data. Hence from the second run onwards, the jobs will be fetched from
    the time stored in the state file instead of the value given in the since parameter.

The following actions are supported by the app:

-   Submitting a URL for analysis
-   Submitting a file for analysis
-   Fetching analysis (job) summary data
-   Fetching the forensics for a job
-   Downloading screenshots for a job and attaching them to the vault
-   Downloading an offline PDF report for a job and attaching it to the vault
-   Fetching list of recently submitted jobs
