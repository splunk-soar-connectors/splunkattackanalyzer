[comment]: # "Auto-generated SOAR connector documentation"
# Splunk Attack Analyzer Connector for Splunk SOAR

Publisher: Splunk  
Connector Version: 1.0.1  
Product Vendor: Splunk  
Product Name: Splunk Attack Analyzer  
Product Version Supported (regex): ".\*"  
Minimum Product Version: 5.5.0  

This connector integrates with the Splunk Attack Analyzer platform to reduce the friction of repetitive manual tasks typically associated with investigating threats

[comment]: # " File: README.md"
[comment]: # ""
[comment]: # "  Copyright (c) 2023 Splunk Inc."
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


### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a Splunk Attack Analyzer asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**api_token** |  required  | password | API token from the app
**since** |  optional  | numeric | Start of time range stated in hours. If not specified, the default is past 24 hours

### Supported Actions  
[get job screenshots](#action-get-job-screenshots) - Get screenshots for the specified job and store them in the vault  
[get pdf report](#action-get-pdf-report) - Get the PDF report for a completed job  
[get job forensics](#action-get-job-forensics) - Get the consolidated forensics for a completed job  
[get job summary](#action-get-job-summary) - Get a job summary for a submitted job  
[list recent jobs](#action-list-recent-jobs) - Get a list of recent jobs  
[detonate file](#action-detonate-file) - Submit File for Scanning  
[detonate url](#action-detonate-url) - Submit New URL for Scanning  
[on poll](#action-on-poll) - Callback action for the on_poll ingest functionality  
[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity using supplied configuration  

## action: 'get job screenshots'
Get screenshots for the specified job and store them in the vault

Type: **investigate**  
Read only: **True**

Timeout parameter accepts integer value in minutes to wait for action to get finished (by default the value is 0), value 0 is for immediate output.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**job_id** |  required  | Job id of the job summary you want to download the PDF for | string |  `splunk attack analyzer job id` 
**timeout** |  optional  | Maximum time (in minutes) to wait for job to be completed | numeric | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success  failed 
action_result.parameter.job_id | string |  `splunk attack analyzer job id`  |   63572265-c5ae-402f-9fc1-6c90547482xx 
action_result.parameter.timeout | numeric |  |   30 
action_result.data | string |  |  
action_result.data.\*.container | numeric |  |   2 
action_result.data.\*.created_via | string |  |   automation 
action_result.data.\*.file_name | string |  |   test_file.html 
action_result.data.\*.hash | string |  |   de7403877259141c0217d19dc2f7931c900 
action_result.data.\*.id | numeric |  |   7 
action_result.data.\*.message | string |  |   success 
action_result.data.\*.screenshot_count | numeric |  |   2 
action_result.data.\*.size | numeric |  |   470679 
action_result.data.\*.succeeded | boolean |  |   True  False 
action_result.data.\*.vault_id | string |  `vault id`  |   de7403877259141c0217d19dc2f7931c900 
action_result.summary | string |  |  
action_result.summary.screenshot_count | numeric |  |   2 
action_result.message | string |  |   Screenshot count: 2 
summary.total_objects | numeric |  |   2 
summary.total_objects_successful | numeric |  |   2   

## action: 'get pdf report'
Get the PDF report for a completed job

Type: **investigate**  
Read only: **True**

Timeout parameter accepts integer value in minutes to wait for action to get finished (by default the value is 0), value 0 is for immediate output.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**job_id** |  required  | Job id of the job summary you want to download the PDF for | string |  `splunk attack analyzer job id` 
**timeout** |  optional  | Maximum time (in minutes) to wait for job to be completed | numeric | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success  failed 
action_result.parameter.job_id | string |  `splunk attack analyzer job id`  |   63572265-c5ae-402f-9fc1-6c90547482ee 
action_result.parameter.timeout | numeric |  |   30 
action_result.data | string |  |  
action_result.data.\*.container | numeric |  |   2 
action_result.data.\*.created_via | string |  |   automation 
action_result.data.\*.file_name | string |  |   test_file.html 
action_result.data.\*.hash | string |  |   6b95b196e05b2d6d5a75fa0241d903350a7b65d0 
action_result.data.\*.id | numeric |  |   6 
action_result.data.\*.message | string |  |   success 
action_result.data.\*.size | numeric |  |   1187161 
action_result.data.\*.succeeded | boolean |  |   True  False 
action_result.data.\*.vault_id | string |  `vault id`  |   6b95b196e05b2d6d5a75fa0241d903350a7b65d0 
action_result.summary | string |  |  
action_result.message | string |  |   Successfully attached PDF report 
summary.total_objects | numeric |  |   2 
summary.total_objects_successful | numeric |  |   2   

## action: 'get job forensics'
Get the consolidated forensics for a completed job

Type: **investigate**  
Read only: **True**

Timeout parameter accepts integer value in minutes to wait for action to get finished (by default the value is 0), value 0 is for immediate output.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**job_id** |  required  | Job id of the forensics you want pulled | string |  `splunk attack analyzer job id` 
**timeout** |  optional  | Maximum time (in minutes) to wait for job to be completed | numeric | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success  failed 
action_result.parameter.job_id | string |  `splunk attack analyzer job id`  |   63572265-c5ae-402f-9fc1-6c90547482ee 
action_result.parameter.timeout | numeric |  |   30 
action_result.data | string |  |  
action_result.data.\*.DNSRequests | string |  |  
action_result.data.\*.DNSRequests.\*.Engines | string |  |  
action_result.data.\*.DNSRequests.\*.Query | string |  |  
action_result.data.\*.DNSRequests.\*.QueryType | string |  |  
action_result.data.\*.DNSRequests.\*.ResourceTaskReferences.\*.ResourceKey | string |  |   4 
action_result.data.\*.DNSRequests.\*.ResourceTaskReferences.\*.TaskKey | string |  |   14 
action_result.data.\*.DNSRequests.\*.Responses | string |  |  
action_result.data.\*.DNSRequests.\*.Responses.\*.Type | string |  |  
action_result.data.\*.DNSRequests.\*.Responses.\*.Value | string |  |  
action_result.data.\*.DNSRequests.\*.Server | string |  |  
action_result.data.\*.DNSServers | string |  |  
action_result.data.\*.Details.engines | string |  |  
action_result.data.\*.Detections.\*.Description | string |  |  
action_result.data.\*.Detections.\*.Details.Data.\*.Hit | string |  |  
action_result.data.\*.Detections.\*.Details.Data.\*.count | numeric |  |   2 
action_result.data.\*.Detections.\*.Details.Data.\*.description | string |  |   Test forensics report 
action_result.data.\*.Detections.\*.Details.Data.\*.id | string |  |   fa34b441-961a-42fa-a100-ecc28c886725 
action_result.data.\*.Detections.\*.Details.Data.\*.rule_level | string |  |   high 
action_result.data.\*.Detections.\*.Details.Data.\*.sigmafile | string |  |   test_forensics_report.yml 
action_result.data.\*.Detections.\*.Details.Data.\*.title | string |  |   Test forensics report 
action_result.data.\*.Detections.\*.Details.Data.\*.url | string |  |   http://www.test_forensics_report.com 
action_result.data.\*.Detections.\*.Details.Extracted Values.\*.Name | string |  |   Copyright 
action_result.data.\*.Detections.\*.Details.Extracted Values.\*.Value | string |  |   © 2021 Test 
action_result.data.\*.Detections.\*.Details.Forms.\*.Action | string |  |   /newsletter/ 
action_result.data.\*.Detections.\*.Details.IsMetaRule | boolean |  |   True  False 
action_result.data.\*.Detections.\*.Details.Match Source | string |  |   html_dom 
action_result.data.\*.Detections.\*.Details.Nested Detections.\*.Description | string |  |   Image Match - Potential  website detected: Test 
action_result.data.\*.Detections.\*.Details.Nested Detections.\*.Details.Extracted Values.\*.Name | string |  |   HtmlPostForm 
action_result.data.\*.Detections.\*.Details.Nested Detections.\*.Details.Extracted Values.\*.Value | string |  |   <form id="sign-in-mfa-password-collection-form" action="verify.php" method="post" autocomplete="on" novalidate=""> 
action_result.data.\*.Detections.\*.Details.Nested Detections.\*.Details.Forms.\*.Action | string |  |   verify.php 
action_result.data.\*.Detections.\*.Details.Nested Detections.\*.Details.IsMetaRule | boolean |  |   True  False 
action_result.data.\*.Detections.\*.Details.Nested Detections.\*.Details.Match Confidence | string |  |   exact 
action_result.data.\*.Detections.\*.Details.Nested Detections.\*.Details.Match Source | string |  |   html_dom 
action_result.data.\*.Detections.\*.Details.Nested Detections.\*.Details.Nested Detections.\*.Description | string |  |   Test Evidence of a Cloned Website 
action_result.data.\*.Detections.\*.Details.Nested Detections.\*.Details.Nested Detections.\*.Details.Extracted Values.\*.Name | string |  |   String 
action_result.data.\*.Detections.\*.Details.Nested Detections.\*.Details.Nested Detections.\*.Details.Extracted Values.\*.Value | string |  |   data-savepage-href="https://www.testurl.com/QBOlogo.png" 
action_result.data.\*.Detections.\*.Details.Nested Detections.\*.Details.Nested Detections.\*.Details.Forms.\*.Action | string |  |   test.php 
action_result.data.\*.Detections.\*.Details.Nested Detections.\*.Details.Nested Detections.\*.Details.Match Source | string |  |   html_dom 
action_result.data.\*.Detections.\*.Details.Nested Detections.\*.Details.Nested Detections.\*.Details.URL | string |  |   https://www.testurl_forensics.com/ 
action_result.data.\*.Detections.\*.Details.Nested Detections.\*.Details.Nested Detections.\*.DisplaySeverity | numeric |  |   25 
action_result.data.\*.Detections.\*.Details.Nested Detections.\*.Details.Nested Detections.\*.Engines | string |  |  
action_result.data.\*.Detections.\*.Details.Nested Detections.\*.Details.Nested Detections.\*.Name | string |  |   11c9b64a-aea1-11eb-a69b-07db8cd523bb 
action_result.data.\*.Detections.\*.Details.Nested Detections.\*.Details.Nested Detections.\*.Severity | numeric |  |   0.25 
action_result.data.\*.Detections.\*.Details.Nested Detections.\*.Details.Nested Detections.\*.Timestamp | string |  |  
action_result.data.\*.Detections.\*.Details.Nested Detections.\*.Details.Nested Detections.\*.Verdict | string |  |  
action_result.data.\*.Detections.\*.Details.Nested Detections.\*.Details.Resource | string |  |   https://www.testurl_forensics.com/ 
action_result.data.\*.Detections.\*.Details.Nested Detections.\*.Details.URL | string |  |   https://www.testurl_forensics.com/ 
action_result.data.\*.Detections.\*.Details.Nested Detections.\*.DisplaySeverity | numeric |  |   75 
action_result.data.\*.Detections.\*.Details.Nested Detections.\*.Engines | string |  |  
action_result.data.\*.Detections.\*.Details.Nested Detections.\*.Name | string |  |   5ec4e953-e68f-4298-9b2c-739c3d729e16 
action_result.data.\*.Detections.\*.Details.Nested Detections.\*.Severity | numeric |  |   0.75 
action_result.data.\*.Detections.\*.Details.Nested Detections.\*.Timestamp | string |  |  
action_result.data.\*.Detections.\*.Details.Nested Detections.\*.Verdict | string |  |   phish 
action_result.data.\*.Detections.\*.Details.OpenPhish | string |  |   high confidence 
action_result.data.\*.Detections.\*.Details.URL | string |  |   https://www.testurl_forensics.com/ 
action_result.data.\*.Detections.\*.DisplaySeverity | numeric |  |   100 
action_result.data.\*.Detections.\*.Engines | string |  |  
action_result.data.\*.Detections.\*.Name | string |  |  
action_result.data.\*.Detections.\*.ResourceTaskReferences.\*.ResourceKey | string |  |   0 
action_result.data.\*.Detections.\*.ResourceTaskReferences.\*.TaskKey | string |  |   1 
action_result.data.\*.Detections.\*.Severity | numeric |  |  
action_result.data.\*.Detections.\*.Verdict | string |  |   phish 
action_result.data.\*.DisplayScore | numeric |  |  
action_result.data.\*.EndTime | string |  |  
action_result.data.\*.Engine | string |  |  
action_result.data.\*.Files.\*.Context | string |  |  
action_result.data.\*.Files.\*.Details.\*.CRC32 | string |  |  
action_result.data.\*.Files.\*.Details.\*.ClamAV | string |  |  
action_result.data.\*.Files.\*.Details.\*.GuestPath | string |  |  
action_result.data.\*.Files.\*.Details.\*.SHA1 | string |  |  
action_result.data.\*.Files.\*.Details.\*.SHA512 | string |  |  
action_result.data.\*.Files.\*.Details.CRC32 | string |  |   060FAA1E 
action_result.data.\*.Files.\*.Details.SHA1 | string |  |   f5af1304ac683afad5de8b6fd98847d884d512aa 
action_result.data.\*.Files.\*.Details.SHA512 | string |  |   4ba716accde1cb97a95320fe4ce86182a888dc18d99cf4f26cf384397ee017aadbc65a3b54e70cb90aeea3c85d419fc3342fbfa217b0bbd19edda971368070aa 
action_result.data.\*.Files.\*.FileName | string |  |  
action_result.data.\*.Files.\*.FileType | string |  |  
action_result.data.\*.Files.\*.MD5 | string |  |  
action_result.data.\*.Files.\*.MimeType | string |  |   text/plain 
action_result.data.\*.Files.\*.NetworkSources | string |  |  
action_result.data.\*.Files.\*.Path | string |  |  
action_result.data.\*.Files.\*.ResourceTaskReferences.\*.ResourceKey | string |  |   1 
action_result.data.\*.Files.\*.ResourceTaskReferences.\*.TaskKey | string |  |   3 
action_result.data.\*.Files.\*.SHA256 | string |  |  
action_result.data.\*.Files.\*.Size | numeric |  |  
action_result.data.\*.Files.\*.Ssdeep | string |  |  
action_result.data.\*.Forms.\*.Action | string |  |  
action_result.data.\*.Forms.\*.Engines | string |  |  
action_result.data.\*.Forms.\*.Inputs.\*.ID | string |  |  
action_result.data.\*.Forms.\*.Inputs.\*.Name | string |  |  
action_result.data.\*.Forms.\*.Inputs.\*.Placeholder | string |  |  
action_result.data.\*.Forms.\*.Inputs.\*.SourceCode | string |  |  
action_result.data.\*.Forms.\*.Inputs.\*.Type | string |  |  
action_result.data.\*.Forms.\*.Method | string |  |   post 
action_result.data.\*.Forms.\*.PageURL | string |  |  
action_result.data.\*.Forms.\*.ResourceTaskReferences.\*.ResourceKey | string |  |   0 
action_result.data.\*.Forms.\*.ResourceTaskReferences.\*.TaskKey | string |  |   1 
action_result.data.\*.Forms.\*.SourceCode | string |  |  
action_result.data.\*.Forms.\*.method | string |  |  
action_result.data.\*.HTTP.\*.Destination.\*.IP | string |  |  
action_result.data.\*.HTTP.\*.Destination.\*.Port | numeric |  |  
action_result.data.\*.HTTP.\*.Destination.IP | string |  |   XX.43.113.24 
action_result.data.\*.HTTP.\*.Destination.Port | numeric |  |   443 
action_result.data.\*.HTTP.\*.Details._requestref | string |  |   b45353994bb050fd7d945cb88d4eaa 
action_result.data.\*.HTTP.\*.Hostname | string |  |  
action_result.data.\*.HTTP.\*.Method | string |  |  
action_result.data.\*.HTTP.\*.Path | string |  |  
action_result.data.\*.HTTP.\*.RequestHeaders | string |  |  
action_result.data.\*.HTTP.\*.RequestHeaders.Accept-Encoding | string |  |   gzip, deflate, br 
action_result.data.\*.HTTP.\*.RequestHeaders.Accept-Language | string |  |   en-US,en;q=0.9 
action_result.data.\*.HTTP.\*.RequestHeaders.Connection | string |  |   keep-alive 
action_result.data.\*.HTTP.\*.RequestHeaders.Content-Length | string |  |   1 
action_result.data.\*.HTTP.\*.RequestHeaders.Content-Type | string |  |   application/x-www-form-urlencoded 
action_result.data.\*.HTTP.\*.RequestHeaders.Origin | string |  |   https://www.testyy.com 
action_result.data.\*.HTTP.\*.RequestHeaders.Sec-Fetch-Dest | string |  |   empty 
action_result.data.\*.HTTP.\*.RequestHeaders.Sec-Fetch-Mode | string |  |   no-cors 
action_result.data.\*.HTTP.\*.RequestHeaders.Sec-Fetch-Site | string |  |   none 
action_result.data.\*.HTTP.\*.RequestHeaders.User-Agent | string |  |  
action_result.data.\*.HTTP.\*.RequestHeaders.accept | string |  |  
action_result.data.\*.HTTP.\*.RequestHeaders.accept-language | string |  |   en-US 
action_result.data.\*.HTTP.\*.RequestHeaders.content-type | string |  |  
action_result.data.\*.HTTP.\*.RequestHeaders.cookie | string |  |  
action_result.data.\*.HTTP.\*.RequestHeaders.intervention | string |  |  
action_result.data.\*.HTTP.\*.RequestHeaders.intuit-plugin-id | string |  |  
action_result.data.\*.HTTP.\*.RequestHeaders.ms-cv | string |  |   853d5c00-cc23-4de8-a912-a115a30f36aa 
action_result.data.\*.HTTP.\*.RequestHeaders.origin | string |  |  
action_result.data.\*.HTTP.\*.RequestHeaders.referer | string |  |  
action_result.data.\*.HTTP.\*.RequestHeaders.upgrade-insecure-requests | string |  |   1 
action_result.data.\*.HTTP.\*.RequestHeaders.user-agent | string |  |  
action_result.data.\*.HTTP.\*.RequestHeaders.x-auth-token | string |  |  
action_result.data.\*.HTTP.\*.RequestHeaders.x-requested-with | string |  |  
action_result.data.\*.HTTP.\*.RequestSize | numeric |  |  
action_result.data.\*.HTTP.\*.ResourceTaskReferences.\*.ResourceKey | string |  |   1 
action_result.data.\*.HTTP.\*.ResourceTaskReferences.\*.TaskKey | string |  |   3 
action_result.data.\*.HTTP.\*.ResponseHeaders | numeric |  |  
action_result.data.\*.HTTP.\*.ResponseHeaders.Accept-Ch | string |  |  
action_result.data.\*.HTTP.\*.ResponseHeaders.Accept-Ranges | string |  |   bytes 
action_result.data.\*.HTTP.\*.ResponseHeaders.Access-Control-Allow-Credentials | string |  |   true 
action_result.data.\*.HTTP.\*.ResponseHeaders.Access-Control-Allow-Origin | string |  |   https://www.testyy.com 
action_result.data.\*.HTTP.\*.ResponseHeaders.Age | string |  |   0 
action_result.data.\*.HTTP.\*.ResponseHeaders.Alt-Svc | string |  |   h3=":443"; ma=2592000,h3-29=":443"; ma=2592000 
action_result.data.\*.HTTP.\*.ResponseHeaders.Cache-Control | string |  |   public, max-age=0 
action_result.data.\*.HTTP.\*.ResponseHeaders.Content-Encoding | string |  |   gzip 
action_result.data.\*.HTTP.\*.ResponseHeaders.Content-Length | string |  |   482 
action_result.data.\*.HTTP.\*.ResponseHeaders.Content-Security-Policy | string |  |  
action_result.data.\*.HTTP.\*.ResponseHeaders.Content-Type | string |  |   application/json 
action_result.data.\*.HTTP.\*.ResponseHeaders.Cross-Origin-Opener-Policy | string |  |   same-origin; report-to="test_account" 
action_result.data.\*.HTTP.\*.ResponseHeaders.Cross-Origin-Opener-Policy-Report-Only | string |  |   same-origin; report-to="test_account" 
action_result.data.\*.HTTP.\*.ResponseHeaders.Cross-Origin-Resource-Policy | string |  |   cross-origin 
action_result.data.\*.HTTP.\*.ResponseHeaders.Date | string |  |   Fri, 24 Feb 2023 10:33:39 GMT 
action_result.data.\*.HTTP.\*.ResponseHeaders.Expires | string |  |   Fri, 24 Feb 2023 10:33:39 GMT 
action_result.data.\*.HTTP.\*.ResponseHeaders.Last-Modified | string |  |   Mon, 11 Jan 2021 18:45:00 GMT 
action_result.data.\*.HTTP.\*.ResponseHeaders.Permissions-Policy | string |  |  
action_result.data.\*.HTTP.\*.ResponseHeaders.Pragma | string |  |   no-cache 
action_result.data.\*.HTTP.\*.ResponseHeaders.Report-To | string |  |   {"group":"test_account","max_age":2592000,"endpoints":[{"url":"https://www.testaccount.com"}]} 
action_result.data.\*.HTTP.\*.ResponseHeaders.Server | string |  |   sffe 
action_result.data.\*.HTTP.\*.ResponseHeaders.Strict-Transport-Security | string |  |   max-age=31536000; includeSubDomains 
action_result.data.\*.HTTP.\*.ResponseHeaders.Vary | string |  |   Accept-Encoding 
action_result.data.\*.HTTP.\*.ResponseHeaders.X-Content-Type-Options | string |  |   nosniff 
action_result.data.\*.HTTP.\*.ResponseHeaders.X-Xss-Protection | string |  |   0 
action_result.data.\*.HTTP.\*.ResponseHeaders.accept-ch | string |  |  
action_result.data.\*.HTTP.\*.ResponseHeaders.accept-ranges | string |  |   bytes 
action_result.data.\*.HTTP.\*.ResponseHeaders.access-control-allow-credentials | string |  |   false 
action_result.data.\*.HTTP.\*.ResponseHeaders.access-control-allow-headers | string |  |   Accept, Content-Type, Content-Encoding, Client-Id 
action_result.data.\*.HTTP.\*.ResponseHeaders.access-control-allow-methods | string |  |   GET 
action_result.data.\*.HTTP.\*.ResponseHeaders.access-control-allow-origin | string |  |   \* 
action_result.data.\*.HTTP.\*.ResponseHeaders.access-control-expose-headers | string |  |  
action_result.data.\*.HTTP.\*.ResponseHeaders.access-control-max-age | string |  |   86400 
action_result.data.\*.HTTP.\*.ResponseHeaders.adrum_0 | string |  |   g:ff51ace9-4caa-4d10-8b7c-e17a0b1f75ab 
action_result.data.\*.HTTP.\*.ResponseHeaders.adrum_1 | string |  |   n:test_87bcfab1-ad5a-4af1-95e0-7eed4f8a18aa 
action_result.data.\*.HTTP.\*.ResponseHeaders.adrum_2 | string |  |   i:257759 
action_result.data.\*.HTTP.\*.ResponseHeaders.adrum_3 | string |  |   e:130 
action_result.data.\*.HTTP.\*.ResponseHeaders.age | string |  |   401 
action_result.data.\*.HTTP.\*.ResponseHeaders.alt-svc | string |  |   h3=":443"; ma=86400 
action_result.data.\*.HTTP.\*.ResponseHeaders.api-version | string |  |   v2 
action_result.data.\*.HTTP.\*.ResponseHeaders.cache-control | string |  |   public, max-age=31556926, immutable 
action_result.data.\*.HTTP.\*.ResponseHeaders.cdn-cache | string |  |   HIT 
action_result.data.\*.HTTP.\*.ResponseHeaders.cdn-cachedat | string |  |   12/23/2022 08:50:57 
action_result.data.\*.HTTP.\*.ResponseHeaders.cdn-edgestorageid | string |  |   1067 
action_result.data.\*.HTTP.\*.ResponseHeaders.cdn-proxyver | string |  |   1.03 
action_result.data.\*.HTTP.\*.ResponseHeaders.cdn-pullzone | string |  |   252412 
action_result.data.\*.HTTP.\*.ResponseHeaders.cdn-requestcountrycode | string |  |   US 
action_result.data.\*.HTTP.\*.ResponseHeaders.cdn-requestid | string |  |   5c7dc3361f86f01351790a8205750f20 
action_result.data.\*.HTTP.\*.ResponseHeaders.cdn-requestpullcode | string |  |   200 
action_result.data.\*.HTTP.\*.ResponseHeaders.cdn-requestpullsuccess | string |  |   True 
action_result.data.\*.HTTP.\*.ResponseHeaders.cdn-status | string |  |   200 
action_result.data.\*.HTTP.\*.ResponseHeaders.cdn-uid | string |  |   b1941f61-b576-4f40-80de-5677acb38f74 
action_result.data.\*.HTTP.\*.ResponseHeaders.cf-bgj | string |  |   imgq:100,h2pri 
action_result.data.\*.HTTP.\*.ResponseHeaders.cf-cache-status | string |  |   HIT 
action_result.data.\*.HTTP.\*.ResponseHeaders.cf-cdnjs-via | string |  |   test/kv 
action_result.data.\*.HTTP.\*.ResponseHeaders.cf-polished | string |  |   origSize=152090, status=webp_bigger 
action_result.data.\*.HTTP.\*.ResponseHeaders.cf-ray | string |  |   7921e1dd3d3867cf-MIA 
action_result.data.\*.HTTP.\*.ResponseHeaders.connection | string |  |   Keep-Alive 
action_result.data.\*.HTTP.\*.ResponseHeaders.content-disposition | string |  |   inline; filename="test_file.jpg" 
action_result.data.\*.HTTP.\*.ResponseHeaders.content-encoding | string |  |   br 
action_result.data.\*.HTTP.\*.ResponseHeaders.content-language | string |  |   en-CA 
action_result.data.\*.HTTP.\*.ResponseHeaders.content-length | string |  |   47438 
action_result.data.\*.HTTP.\*.ResponseHeaders.content-location | string |  |   https://image.test.url/RE1Mu3b?ver=aaaa 
action_result.data.\*.HTTP.\*.ResponseHeaders.content-md5 | string |  |   tfIwuCAmVOw8IfslU4qRSw== 
action_result.data.\*.HTTP.\*.ResponseHeaders.content-security-policy | string |  |   frame-src 'self'; connect-src 'self'; default-src 'self'; script-src 'self' 'unsafe-inline' ; style-src 'unsafe-inline' 
action_result.data.\*.HTTP.\*.ResponseHeaders.content-security-policy-report-only | string |  |  
action_result.data.\*.HTTP.\*.ResponseHeaders.content-type | string |  |   font/ttf 
action_result.data.\*.HTTP.\*.ResponseHeaders.cross-origin-embedder-policy | string |  |   require-corp 
action_result.data.\*.HTTP.\*.ResponseHeaders.cross-origin-opener-policy | string |  |   same-origin-allow-popups 
action_result.data.\*.HTTP.\*.ResponseHeaders.cross-origin-opener-policy-report-only | string |  |   same-origin; report-to="static-on-test" 
action_result.data.\*.HTTP.\*.ResponseHeaders.cross-origin-resource-policy | string |  |   cross-origin 
action_result.data.\*.HTTP.\*.ResponseHeaders.date | string |  |   Wed, 23 Nov 2022 00:44:36 GMT 
action_result.data.\*.HTTP.\*.ResponseHeaders.document-policy | string |  |   force-load-at-top 
action_result.data.\*.HTTP.\*.ResponseHeaders.etag | string |  |   "e54addba5aa" 
action_result.data.\*.HTTP.\*.ResponseHeaders.expect-ct | string |  |   max-age=86400, report-uri="https://www.test.com/platform-telemetry/ct" 
action_result.data.\*.HTTP.\*.ResponseHeaders.expires | string |  |   Thu, 01 Jan 1970 00:00:00 GMT 
action_result.data.\*.HTTP.\*.ResponseHeaders.fly-request-id | string |  |   01GQDCXWGM7GR6D7NYES5CEMAA 
action_result.data.\*.HTTP.\*.ResponseHeaders.identification-source | string |  |   CACHE 
action_result.data.\*.HTTP.\*.ResponseHeaders.intuit_tid | string |  |   18375f05-0688-46f2-87bd-36b2a3056eaa 
action_result.data.\*.HTTP.\*.ResponseHeaders.keep-alive | string |  |   timeout=2, max=100 
action_result.data.\*.HTTP.\*.ResponseHeaders.last-modified | string |  |   Wed, 27 Apr 2022 18:34:52 GMT 
action_result.data.\*.HTTP.\*.ResponseHeaders.link | string |  |   <https://fonts.test.com>; rel=preconnect; crossorigin 
action_result.data.\*.HTTP.\*.ResponseHeaders.test-action | string |  |   1 
action_result.data.\*.HTTP.\*.ResponseHeaders.location | string |  |   https://data.xyz.com/b/ss/xee/1/H.20.3/s28372352737215?AQB= 
action_result.data.\*.HTTP.\*.ResponseHeaders.ms-cv | string |  |   0TwjKmhArkqpx27S.0 
action_result.data.\*.HTTP.\*.ResponseHeaders.ms-cv-esi | string |  |   CASCV4deabe4.0 
action_result.data.\*.HTTP.\*.ResponseHeaders.ms-operation-id | string |  |   22352131e9aa584ca106a3df24b0aa 
action_result.data.\*.HTTP.\*.ResponseHeaders.nel | string |  |   {"report_to":"network-errors","max_age":1296000,"success_fraction":0.00066,"failure_fraction":1,"include_subdomains":true} 
action_result.data.\*.HTTP.\*.ResponseHeaders.operationid | string |  |   ede2ed5a1b48ecbff5456dca506aa 
action_result.data.\*.HTTP.\*.ResponseHeaders.origin-agent-cluster | string |  |   ?0 
action_result.data.\*.HTTP.\*.ResponseHeaders.p3p | string |  |   CP="This is not a P3P policy" 
action_result.data.\*.HTTP.\*.ResponseHeaders.perf | string |  |   7626143928 
action_result.data.\*.HTTP.\*.ResponseHeaders.permissions-policy | string |  |  
action_result.data.\*.HTTP.\*.ResponseHeaders.pragma | string |  |   no-cache 
action_result.data.\*.HTTP.\*.ResponseHeaders.priority | string |  |   u=3,i 
action_result.data.\*.HTTP.\*.ResponseHeaders.ptime | string |  |   0.0035480000005919 
action_result.data.\*.HTTP.\*.ResponseHeaders.referrer-policy | string |  |   no-referrer 
action_result.data.\*.HTTP.\*.ResponseHeaders.report-to | string |  |   {"group":"network-errors","max_age":2592000,"endpoints":[{"url":"https://www.test.com/li/rep"}],"include_subdomains":true} 
action_result.data.\*.HTTP.\*.ResponseHeaders.request-context | string |  |   appId=cid-v1:fc03bcad-a752-4f14-8357-6413235728aa 
action_result.data.\*.HTTP.\*.ResponseHeaders.request-id | string |  |   ba7cb248-8059-4558-8c44-af85f8a132aa 
action_result.data.\*.HTTP.\*.ResponseHeaders.server | string |  |   DatabaseS3 
action_result.data.\*.HTTP.\*.ResponseHeaders.server-timing | string |  |   edge; dur=1, origin; dur=11, cdn-cache; desc=MISS 
action_result.data.\*.HTTP.\*.ResponseHeaders.strict-transport-security | string |  |   max-age=31536000 
action_result.data.\*.HTTP.\*.ResponseHeaders.time-delta-millis | string |  |   384 
action_result.data.\*.HTTP.\*.ResponseHeaders.timing-allow-origin | string |  |   \*, \* 
action_result.data.\*.HTTP.\*.ResponseHeaders.tls_version | string |  |   tls1.3 
action_result.data.\*.HTTP.\*.ResponseHeaders.tmx-nonce | string |  |   8226d90974108d 
action_result.data.\*.HTTP.\*.ResponseHeaders.trace-id | string |  |   568b46f84bb545c7 
action_result.data.\*.HTTP.\*.ResponseHeaders.transfer-encoding | string |  |   chunked 
action_result.data.\*.HTTP.\*.ResponseHeaders.vary | string |  |   Accept-Encoding 
action_result.data.\*.HTTP.\*.ResponseHeaders.via | string |  |   1.1 5ab5dc09da67e3ea794ec8a82992ccaa.test.net (test) 
action_result.data.\*.HTTP.\*.ResponseHeaders.www-authenticate | string |  |   API v2 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-activity-id | string |  |   544275be-d3be-49b5-bbb8-18339e4220aa 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-activityid | string |  |   0b707f18-4fe3-4cf6-8719-b892441154aa 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-amz-cf-id | string |  |   jvi58qPvaKsS7KpFGAFMbwP3Heql0ZInZO3w9x3EPse4zY0AAgA== 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-amz-cf-pop | string |  |   ORD51-C2 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-amz-id-2 | string |  |   yi/1AP8btDeBMNwXKzVKDmFpEb/NKNKf+HyDKux8RfM4ZzlxA93LWImqYXQ4JZobPRlAAA= 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-amz-meta-id | string |  |   identity-test-ui 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-amz-meta-module | string |  |   identity-test-ui 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-amz-meta-slug | string |  |   identity-test-ui/1.388.1-apr.2734.b.7 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-amz-meta-type | string |  |   plugin 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-amz-meta-version | string |  |   1.388.1-dummy.2734.b.7 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-amz-request-id | string |  |   J12AVJJT0N7SCTV4 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-amz-storage-class | string |  |   INTELLIGENT_TIERING 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-amz-version-id | string |  |   0SaPfidEaOrnyiftYjgXNTUE9SyoELAA 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-appversion | string |  |   1.0.8390.9238 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-aspnet-version | string |  |   4.0.30319 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-az | string |  |   {did:testhash123, rid: 14, sn: test-prod, dt: 2023-01-18T05:15:55.8437711Z, bt: 2022-12-21T05:07:56.0000000Z} 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-azure-ref | string |  |   20230131T104954Z-bqvak4nptd2c30mdndbs7zwyu40000000bqg000000001caa 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-azure-ref-originshield | string |  |   0WFbWYwC66tUsSIvdQIBfLyW2kyC5TU5aMjIxMDYwNjExMDExAGYxY2E3M2Q0LTg4ODMtNGNhZi1hYmRjLWZlMmQ1NjdhZmI5aa== 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-cache | string |  |   Hit from test 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-cdn | string |  |   AKAM 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-computed | string |  |   true 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-connection-hash | string |  |   e5deadb6db0d14073930ebfdccdf40a9d32913c27e89281abb0746eec8aa 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-content-type-options | string |  |   nosniff 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-datacenter | string |  |   westcenus 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-edgeconnect-midmile-rtt | string |  |   1 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-edgeconnect-origin-mex-latency | string |  |   54 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-fb-debug | string |  |   ORufSisO0ETW61nDh+RWwxOEnwaoyIullpfm+QN0ictsLVMaFgiqB+PDkiIvYwWGpm6I8T/Qo+WRyTy9aa== 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-fb-rlafr | string |  |   0 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-frame-options | string |  |   SAMEORIGIN 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-li-fabric | string |  |   prod-ltx1 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-li-pop | string |  |   afd-prod-ltx1-a 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-li-proto | string |  |   http/2 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-li-uuid | string |  |   AAXzjRbzt4rxIfkgS/Vpaa== 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-ms-blob-type | string |  |   BlockBlob 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-ms-lease-status | string |  |   unlocked 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-ms-meta-jssdkver | string |  |   3.2.6 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-ms-request-id | string |  |   af25cca6-701e-003f-77c7-316f3a000000 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-ms-version | string |  |   2009-09-19 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-msedge-ref | string |  |   Ref A: 8E47239F9C11469DA76EDD93DCF74XX4 Ref B: MIAEDGE1XX9 Ref C: 2023-01-31T10:49:44Z 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-origin-src | string |  |   uxf 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-powered-by | string |  |   ASP.NET 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-request-id | string |  |   78fad6f9-27f5-470e-83c0-9975ca709eaa 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-resizerversion | string |  |   1.0 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-response-time | string |  |   7 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-rtag | string |  |   Str 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-s1 | string |  |   2023-01-24T18:05:47 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-s2 | string |  |   2023-01-24T18:05:47 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-served-by | string |  |   cache-iad-kcgs7200042-IAD, cache-bfi-krnt7300086-BFI 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-source-length | string |  |   4054 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-transaction-id | string |  |   e90b91ea84264 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-tw-cdn | string |  |   FT 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-ua-compatible | string |  |   IE=Edge 
action_result.data.\*.HTTP.\*.ResponseHeaders.x-xss-protection | string |  |   1; mode=block 
action_result.data.\*.HTTP.\*.ResponseSize | numeric |  |  
action_result.data.\*.HTTP.\*.Source.\*.IP | string |  |  
action_result.data.\*.HTTP.\*.Source.\*.Port | numeric |  |  
action_result.data.\*.HTTP.\*.Source.IP | string |  |  
action_result.data.\*.HTTP.\*.Source.Port | numeric |  |  
action_result.data.\*.HTTP.\*.StatusCode | numeric |  |  
action_result.data.\*.HTTP.\*.TotalSize | numeric |  |  
action_result.data.\*.HTTP.\*.URL | string |  |  
action_result.data.\*.HTTP.\*.UserAgent | string |  |  
action_result.data.\*.HTTP.\*.UserAgent | string |  |  
action_result.data.\*.Hosts.\*.ASN | numeric |  |  
action_result.data.\*.Hosts.\*.City | string |  |  
action_result.data.\*.Hosts.\*.Country | string |  |  
action_result.data.\*.Hosts.\*.Engines | string |  |  
action_result.data.\*.Hosts.\*.Hostname | string |  |   test.host.com 
action_result.data.\*.Hosts.\*.Houstname | string |  |  
action_result.data.\*.Hosts.\*.IP | string |  |  
action_result.data.\*.Hosts.\*.Organization | string |  |  
action_result.data.\*.Hosts.\*.ResourceTaskReferences.\*.ResourceKey | string |  |   1 
action_result.data.\*.Hosts.\*.ResourceTaskReferences.\*.TaskKey | string |  |   3 
action_result.data.\*.Images.\*.ArtifactPath | string |  |  
action_result.data.\*.Images.\*.DetectedObjects | string |  |  
action_result.data.\*.Images.\*.ImageHashes | string |  |  
action_result.data.\*.Images.\*.ImageHashes.ImageAvgHash | string |  |   1818181818000000 
action_result.data.\*.Images.\*.ImageHashes.ImageDhash | string |  |   b2b2b2b2b24c3001aa 
action_result.data.\*.Images.\*.ImageHashes.ImagePhash | string |  |   88dd227722772277aa 
action_result.data.\*.Images.\*.Resource | string |  |  
action_result.data.\*.Images.\*.ResourceTaskReferences.\*.ResourceKey | string |  |   0 
action_result.data.\*.Images.\*.ResourceTaskReferences.\*.TaskKey | string |  |   1 
action_result.data.\*.Images.\*.Type | string |  |  
action_result.data.\*.Logs | string |  |  
action_result.data.\*.MalwareConfigs | string |  |  
action_result.data.\*.MalwareFamilies | string |  |  
action_result.data.\*.MitreAttacks | string |  |  
action_result.data.\*.MitreAttacks.\*.Engines | string |  |  
action_result.data.\*.MitreAttacks.\*.ID | string |  |  
action_result.data.\*.MitreAttacks.\*.ResourceTaskReferences.\*.ResourceKey | string |  |   4 
action_result.data.\*.MitreAttacks.\*.ResourceTaskReferences.\*.TaskKey | string |  |   14 
action_result.data.\*.MitreAttacks.\*.SubTechnique | string |  |  
action_result.data.\*.MitreAttacks.\*.Tactic | string |  |  
action_result.data.\*.MitreAttacks.\*.Technique | string |  |  
action_result.data.\*.Mutexes | string |  |  
action_result.data.\*.Mutexes.\*.Engines | string |  |  
action_result.data.\*.Mutexes.\*.Name | string |  |  
action_result.data.\*.Network | string |  |  
action_result.data.\*.Network.\*.Destination.\*.IP | string |  |  
action_result.data.\*.Network.\*.Destination.\*.Port | numeric |  |  
action_result.data.\*.Network.\*.Destination.IP | string |  |   23.62.164.112 
action_result.data.\*.Network.\*.Destination.Port | numeric |  |   443 
action_result.data.\*.Network.\*.Length | numeric |  |  
action_result.data.\*.Network.\*.Protocol | string |  |  
action_result.data.\*.Network.\*.ResourceTaskReferences.\*.ResourceKey | string |  |   4 
action_result.data.\*.Network.\*.ResourceTaskReferences.\*.TaskKey | string |  |   20 
action_result.data.\*.Network.\*.Service | string |  |  
action_result.data.\*.Network.\*.Source.\*.IP | string |  |  
action_result.data.\*.Network.\*.Source.\*.Port | numeric |  |  
action_result.data.\*.Network.\*.Source.IP | string |  |   192.168.2.106 
action_result.data.\*.Network.\*.Source.Port | numeric |  |   49431 
action_result.data.\*.PhishedBrands | string |  |  
action_result.data.\*.Processes | string |  |  
action_result.data.\*.Processes.\*.Arguments | string |  |   "C:\\Program Files\\testy\\Chrome\\Application\\chrome.exe" --no-sandbox --test-type --ignore-ssl-errors "C:\\Users\\user1\\AppData\\Local\\Temp\\test_html.html" 
action_result.data.\*.Processes.\*.Details.\*.Calls | string |  |  
action_result.data.\*.Processes.\*.Details.Arguements | string |  |  
action_result.data.\*.Processes.\*.Details.Environment.\*.CommandLine | string |  |  
action_result.data.\*.Processes.\*.Details.Environment.\*.ComputerName | string |  |  
action_result.data.\*.Processes.\*.Details.Environment.\*.InstallDate | numeric |  |  
action_result.data.\*.Processes.\*.Details.Environment.\*.MachineGUID | string |  |  
action_result.data.\*.Processes.\*.Details.Environment.\*.MainExeBase | string |  |  
action_result.data.\*.Processes.\*.Details.Environment.\*.MainExeSize | string |  |  
action_result.data.\*.Processes.\*.Details.Environment.\*.OSMajor | numeric |  |  
action_result.data.\*.Processes.\*.Details.Environment.\*.OSMinor | numeric |  |  
action_result.data.\*.Processes.\*.Details.Environment.\*.ProductName | string |  |  
action_result.data.\*.Processes.\*.Details.Environment.\*.RegisteredOrganization | string |  |  
action_result.data.\*.Processes.\*.Details.Environment.\*.RegisteredOwner | string |  |  
action_result.data.\*.Processes.\*.Details.Environment.\*.SystemVolumeGUID | string |  |  
action_result.data.\*.Processes.\*.Details.Environment.\*.SystemVolumeSerialNumber | string |  |  
action_result.data.\*.Processes.\*.Details.Environment.\*.TempPath | string |  |  
action_result.data.\*.Processes.\*.Details.Environment.\*.UserName | string |  |  
action_result.data.\*.Processes.\*.Details.Environment.\*.WindowsPath | string |  |  
action_result.data.\*.Processes.\*.Details.Environment.\*.is_success | string |  |  
action_result.data.\*.Processes.\*.Details.Environment.\*.retval | numeric |  |  
action_result.data.\*.Processes.\*.Details.Environment.CommandLine | string |  |   "C:\\Program Files\\testy\\Chrome\\Application\\chrome.exe" --no-sandbox --test-type --ignore-ssl-errors "C:\\Users\\user1\\AppData\\Local\\Temp\\test_html.html" 
action_result.data.\*.Processes.\*.Details.Environment.ComputerName | string |  |   USER-PC 
action_result.data.\*.Processes.\*.Details.Environment.InstallDate | numeric |  |  
action_result.data.\*.Processes.\*.Details.Environment.MachineGUID | string |  |  
action_result.data.\*.Processes.\*.Details.Environment.MainExeBase | string |  |  
action_result.data.\*.Processes.\*.Details.Environment.MainExeSize | string |  |  
action_result.data.\*.Processes.\*.Details.Environment.OSMajor | numeric |  |  
action_result.data.\*.Processes.\*.Details.Environment.OSMinor | numeric |  |  
action_result.data.\*.Processes.\*.Details.Environment.ProductName | string |  |  
action_result.data.\*.Processes.\*.Details.Environment.RegisteredOrganization | string |  |  
action_result.data.\*.Processes.\*.Details.Environment.RegisteredOwner | string |  |  
action_result.data.\*.Processes.\*.Details.Environment.SystemVolumeGUID | string |  |   3852cdae-8280-11e9-89e4-806e6f6e69aa 
action_result.data.\*.Processes.\*.Details.Environment.SystemVolumeSerialNumber | string |  |   70ed-e877 
action_result.data.\*.Processes.\*.Details.Environment.TempPath | string |  |   C:\\Users\\user1\\AppData\\Local\\Temp\\ 
action_result.data.\*.Processes.\*.Details.Environment.UserName | string |  |   QButler 
action_result.data.\*.Processes.\*.Details.Environment.WindowsPath | string |  |   C:\\Windows 
action_result.data.\*.Processes.\*.Details.Environment.is_success | numeric |  |  
action_result.data.\*.Processes.\*.Details.Environment.retval | numeric |  |  
action_result.data.\*.Processes.\*.Details.Threads | string |  |  
action_result.data.\*.Processes.\*.Name | string |  |  
action_result.data.\*.Processes.\*.PID | numeric |  |  
action_result.data.\*.Processes.\*.PPID | numeric |  |  
action_result.data.\*.Processes.\*.Path | string |  |  
action_result.data.\*.Processes.\*.ResourceTaskReferences.\*.ResourceKey | string |  |   4 
action_result.data.\*.Processes.\*.ResourceTaskReferences.\*.TaskKey | string |  |   14 
action_result.data.\*.RegistryKeys | string |  |  
action_result.data.\*.Registrykeys.\*.Action | string |  |  
action_result.data.\*.Registrykeys.\*.Engines | string |  |  
action_result.data.\*.Registrykeys.\*.Name | string |  |  
action_result.data.\*.ResourceMap.0.ID | string |  |   c6e29c54-ca84-4368-8af6-38edc2c8398e 
action_result.data.\*.ResourceMap.0.Name | string |  |   https://testurl.com/wp-includes/fonts/test_fonts/ 
action_result.data.\*.ResourceMap.0.Type | string |  |   URL 
action_result.data.\*.ResourceMap.1.ID | string |  |   d7d53778-8ec3-405a-9ec2-9e0a5b998913 
action_result.data.\*.ResourceMap.1.Name | string |  |   https://test.host.com/c35/1/0/test_location/data 
action_result.data.\*.ResourceMap.1.Type | string |  |   URL 
action_result.data.\*.ResourceMap.2.ID | string |  |   9ce6e5cc-7836-4134-8aed-874e357696f4 
action_result.data.\*.ResourceMap.2.Name | string |  |   https://www.detect.com/detection 
action_result.data.\*.ResourceMap.2.Type | string |  |   URL 
action_result.data.\*.ResourceMap.3.ID | string |  |   b56c03a9-7bd1-406f-be43-924447b3dcaa 
action_result.data.\*.ResourceMap.3.Name | string |  |   http://hosts-file.net/ 
action_result.data.\*.ResourceMap.3.Type | string |  |   URL 
action_result.data.\*.ResourceMap.4.ID | string |  |   fe667a66-a123-4b0d-8486-ea0ef6796902 
action_result.data.\*.ResourceMap.4.Name | string |  |   https://www.detection.com/usa 
action_result.data.\*.ResourceMap.4.Type | string |  |   URL 
action_result.data.\*.ResourceMap.5.ID | string |  |   d0f98453-3c93-41da-b739-98b8a3d277aa 
action_result.data.\*.ResourceMap.5.Name | string |  |   http://www.testdomain/01_Basics/00_simple_noHead.html?281090039# 
action_result.data.\*.ResourceMap.5.Type | string |  |   URL 
action_result.data.\*.ResourceMap.6.ID | string |  |   d37d321b-e0ca-4048-9daf-72ab53ec3fb4 
action_result.data.\*.ResourceMap.6.Name | string |  |   https://www.testdomain.com/page/contact 
action_result.data.\*.ResourceMap.6.Type | string |  |   URL 
action_result.data.\*.ResourceMap.7.ID | string |  |   d70f289f-1e9e-4855-b522-cd946b617507 
action_result.data.\*.ResourceMap.7.Name | string |  |   https://www.testdomain.com/page/buy 
action_result.data.\*.ResourceMap.7.Type | string |  |   URL 
action_result.data.\*.SavedArtifacts | string |  |  
action_result.data.\*.SavedArtifacts.\*.ArtifactPath | string |  |   2022-11-23/lab/63572265-c5ae-402f-9fc1-6c90547482ee/8551cf5b-2095-426f-85ec-b8552c17bd53/7507bfcf1693c6a8f3f69d15121dc14aeb8dc9e301bac6568152fb50210aabbc.sample.gz 
action_result.data.\*.SavedArtifacts.\*.Name | string |  |   7507bfcf1693c6a8f3f69d15121dc14aeb8dc9e301bac6568152fb50210aabbc 
action_result.data.\*.SavedArtifacts.\*.ResourceTaskReferences.\*.ResourceKey | string |  |   1 
action_result.data.\*.SavedArtifacts.\*.ResourceTaskReferences.\*.TaskKey | string |  |   3 
action_result.data.\*.SavedArtifacts.\*.Type | string |  |   web_artifact 
action_result.data.\*.Score | numeric |  |  
action_result.data.\*.Screenshots.\*.ArtifactPath | string |  |  
action_result.data.\*.Screenshots.\*.Engines | string |  |  
action_result.data.\*.Screenshots.\*.ImageHashes | string |  |  
action_result.data.\*.Screenshots.\*.ImageHashes.ImageAvgHash | string |  |   183c1c3c18000000 
action_result.data.\*.Screenshots.\*.ImageHashes.ImageDhash | string |  |   b2b2b2b2320c2000 
action_result.data.\*.Screenshots.\*.ImageHashes.ImagePhash | string |  |   9999666666cc3363 
action_result.data.\*.Screenshots.\*.Resource | string |  |  
action_result.data.\*.Screenshots.\*.ResourceTaskReferences.\*.ResourceKey | string |  |   1 
action_result.data.\*.Screenshots.\*.ResourceTaskReferences.\*.TaskKey | string |  |   3 
action_result.data.\*.Screenshots.\*.URI | string |  |  
action_result.data.\*.StartTime | string |  |  
action_result.data.\*.Strings.\*.Details.ImageAvgHash | string |  |   8f81803f3fffffff 
action_result.data.\*.Strings.\*.Details.ImageDhash | string |  |   393f254050004000 
action_result.data.\*.Strings.\*.Details.ImagePhash | string |  |   be3c789987c3c04e 
action_result.data.\*.Strings.\*.Details.Source | string |  |   HTTP response content: https://test.host.com/c35/1/0/test_location/data 
action_result.data.\*.Strings.\*.Details.SourceDisplay | string |  |   Normalized Output (No Image OCR) 
action_result.data.\*.Strings.\*.Details.Type | string |  |   http_response 
action_result.data.\*.Strings.\*.Details.URL | string |  |   https://test.host.com/c35/1/0/test_location/data 
action_result.data.\*.Strings.\*.Engines | string |  |  
action_result.data.\*.Strings.\*.ResourceTaskReferences.\*.ResourceKey | string |  |   1 
action_result.data.\*.Strings.\*.ResourceTaskReferences.\*.TaskKey | string |  |   3 
action_result.data.\*.Strings.\*.String | string |  |  
action_result.data.\*.TLS | string |  |  
action_result.data.\*.TLS.\*.Destination.IP | string |  |  
action_result.data.\*.TLS.\*.Destination.Port | numeric |  |  
action_result.data.\*.TLS.\*.Details.JA3 | string |  |  
action_result.data.\*.TLS.\*.Details.JA3S | string |  |   771,49195,23-65281-11-35 
action_result.data.\*.TLS.\*.Engines | string |  |  
action_result.data.\*.TLS.\*.Fingerprint | numeric |  |  
action_result.data.\*.TLS.\*.Issuer | string |  |  
action_result.data.\*.TLS.\*.ResourceTaskReferences.\*.ResourceKey | string |  |   4 
action_result.data.\*.TLS.\*.ResourceTaskReferences.\*.TaskKey | string |  |   20 
action_result.data.\*.TLS.\*.Source.IP | string |  |  
action_result.data.\*.TLS.\*.Source.Port | numeric |  |  
action_result.data.\*.TLS.\*.Subject | string |  |  
action_result.data.\*.TaskMap.0.Engine | string |  |   url_reputation 
action_result.data.\*.TaskMap.0.ID | string |  |   1ce8132e-87cf-43a5-8076-dce647ff28aa 
action_result.data.\*.TaskMap.0.Score | numeric |  |  
action_result.data.\*.TaskMap.1.Engine | string |  |   web_analyzer 
action_result.data.\*.TaskMap.1.ID | string |  |   8551cf5b-2095-426f-85ec-b8552c17bdaa 
action_result.data.\*.TaskMap.1.Score | numeric |  |   1 
action_result.data.\*.TaskMap.10.Engine | string |  |   web_analyzer 
action_result.data.\*.TaskMap.10.ID | string |  |   4dda943d-82c9-43c2-bff3-6b37cecb0faa 
action_result.data.\*.TaskMap.10.Score | numeric |  |  
action_result.data.\*.TaskMap.11.Engine | string |  |   web_analyzer 
action_result.data.\*.TaskMap.11.ID | string |  |   4e320fb1-5304-4c38-9594-a8ee2d1147Aa 
action_result.data.\*.TaskMap.11.Score | numeric |  |   0.15 
action_result.data.\*.TaskMap.12.Engine | string |  |   web_analyzer 
action_result.data.\*.TaskMap.12.ID | string |  |   70282082-544b-4f80-a5f9-cb159b0846aa 
action_result.data.\*.TaskMap.12.Score | numeric |  |  
action_result.data.\*.TaskMap.13.Engine | string |  |   url_reputation 
action_result.data.\*.TaskMap.13.ID | string |  |   7aeb7c87-e23f-4aff-b25a-1857963d1baa 
action_result.data.\*.TaskMap.13.Score | numeric |  |  
action_result.data.\*.TaskMap.14.Engine | string |  |   test_engine 
action_result.data.\*.TaskMap.14.ID | string |  |   7f017b55-710f-40ab-9175-61af88525790 
action_result.data.\*.TaskMap.14.Score | numeric |  |  
action_result.data.\*.TaskMap.15.Engine | string |  |   test_engine 
action_result.data.\*.TaskMap.15.ID | string |  |   8031c0f4-4c7d-44f2-8ed0-28b6cbbdc7ed 
action_result.data.\*.TaskMap.15.Score | numeric |  |  
action_result.data.\*.TaskMap.16.Engine | string |  |   web_analyzer 
action_result.data.\*.TaskMap.16.ID | string |  |   86f53325-b04e-43f2-b08f-9c755ec2b1aa 
action_result.data.\*.TaskMap.16.Score | numeric |  |  
action_result.data.\*.TaskMap.17.Engine | string |  |   url_reputation 
action_result.data.\*.TaskMap.17.ID | string |  |   9212b1a1-cf6d-476b-afd6-b4d865e02aaa 
action_result.data.\*.TaskMap.17.Score | numeric |  |  
action_result.data.\*.TaskMap.18.Engine | string |  |   web_analyzer 
action_result.data.\*.TaskMap.18.ID | string |  |   9687a607-3a39-42cb-a5be-4b8f6b327baa 
action_result.data.\*.TaskMap.18.Score | numeric |  |  
action_result.data.\*.TaskMap.19.Engine | string |  |   test_engine 
action_result.data.\*.TaskMap.19.ID | string |  |   b2b075bd-5693-4d36-8529-4652fc074202 
action_result.data.\*.TaskMap.19.Score | numeric |  |  
action_result.data.\*.TaskMap.2.Engine | string |  |   url_reputation 
action_result.data.\*.TaskMap.2.ID | string |  |   c9a0139f-9803-4d77-816c-df7403d7d7bc 
action_result.data.\*.TaskMap.2.Score | numeric |  |   0.4 
action_result.data.\*.TaskMap.20.Engine | string |  |   test_engine 
action_result.data.\*.TaskMap.20.ID | string |  |   b3818f0e-2202-496a-9f11-a9485ab29369 
action_result.data.\*.TaskMap.20.Score | numeric |  |  
action_result.data.\*.TaskMap.21.Engine | string |  |   static_file 
action_result.data.\*.TaskMap.21.ID | string |  |   b909b18e-fe52-4e8e-a531-9c6f62577169 
action_result.data.\*.TaskMap.21.Score | numeric |  |  
action_result.data.\*.TaskMap.22.Engine | string |  |   web_analyzer 
action_result.data.\*.TaskMap.22.ID | string |  |   bae8c0a7-6b37-4da0-b22c-d6a65e2c89fa 
action_result.data.\*.TaskMap.22.Score | numeric |  |  
action_result.data.\*.TaskMap.23.Engine | string |  |   web_analyzer 
action_result.data.\*.TaskMap.23.ID | string |  |   c6f67d90-e408-48df-ba96-9a7319adbfa7 
action_result.data.\*.TaskMap.23.Score | numeric |  |  
action_result.data.\*.TaskMap.24.Engine | string |  |   web_analyzer 
action_result.data.\*.TaskMap.24.ID | string |  |   e4606afd-63f3-4505-81da-053d49d2ae6c 
action_result.data.\*.TaskMap.24.Score | numeric |  |  
action_result.data.\*.TaskMap.25.Engine | string |  |   static_doc 
action_result.data.\*.TaskMap.25.ID | string |  |   f2cc48a2-76f5-4527-9460-bcc1de4e9cfa 
action_result.data.\*.TaskMap.25.Score | numeric |  |  
action_result.data.\*.TaskMap.26.Engine | string |  |   url_reputation 
action_result.data.\*.TaskMap.26.ID | string |  |   fb56fd9a-c168-4375-ae09-fdf6c5b5ffa9 
action_result.data.\*.TaskMap.26.Score | numeric |  |  
action_result.data.\*.TaskMap.3.Engine | string |  |   web_analyzer 
action_result.data.\*.TaskMap.3.ID | string |  |   cc46644a-b842-4361-acce-2e9febef46be 
action_result.data.\*.TaskMap.3.Score | numeric |  |  
action_result.data.\*.TaskMap.4.Engine | string |  |   web_analyzer 
action_result.data.\*.TaskMap.4.ID | string |  |   837b4eaf-8e6d-4e1f-92fd-4e13c873f0aa 
action_result.data.\*.TaskMap.4.Score | numeric |  |  
action_result.data.\*.TaskMap.5.Engine | string |  |   url_reputation 
action_result.data.\*.TaskMap.5.ID | string |  |   8bea47e8-98ba-4f11-af18-d2be3040f1af 
action_result.data.\*.TaskMap.5.Score | numeric |  |  
action_result.data.\*.TaskMap.6.Engine | string |  |   web_analyzer 
action_result.data.\*.TaskMap.6.ID | string |  |   9c04d6c8-c749-4069-a48c-e5d85e426aaf 
action_result.data.\*.TaskMap.6.Score | numeric |  |  
action_result.data.\*.TaskMap.7.Engine | string |  |   web_analyzer 
action_result.data.\*.TaskMap.7.ID | string |  |   a1ed2738-4184-49c0-9710-44de7ffa2aac 
action_result.data.\*.TaskMap.7.Score | numeric |  |  
action_result.data.\*.TaskMap.8.Engine | string |  |   url_reputation 
action_result.data.\*.TaskMap.8.ID | string |  |   c9add79d-abd4-4e80-bef5-131bf5807faa 
action_result.data.\*.TaskMap.8.Score | numeric |  |  
action_result.data.\*.TaskMap.9.Engine | string |  |   url_reputation 
action_result.data.\*.TaskMap.9.ID | string |  |   f3ec2a9f-6759-47ef-8ce7-a2e7f215f9aa 
action_result.data.\*.TaskMap.9.Score | numeric |  |  
action_result.data.\*.URLs.\*.Context | string |  |  
action_result.data.\*.URLs.\*.Engines | string |  |  
action_result.data.\*.URLs.\*.LinkText | string |  |  
action_result.data.\*.URLs.\*.ResourceTaskReferences.\*.ResourceKey | string |  |   1 
action_result.data.\*.URLs.\*.ResourceTaskReferences.\*.TaskKey | string |  |   3 
action_result.data.\*.URLs.\*.URL | string |  |  
action_result.data.\*.Verdict | string |  |  
action_result.data.\*.Version | string |  |  
action_result.data.\*.WhoisResults.\*.Address | string |  |  
action_result.data.\*.WhoisResults.\*.City | string |  |  
action_result.data.\*.WhoisResults.\*.Country | string |  |  
action_result.data.\*.WhoisResults.\*.CreatedAt | string |  |  
action_result.data.\*.WhoisResults.\*.DNSSec | string |  |  
action_result.data.\*.WhoisResults.\*.DomainName | string |  |  
action_result.data.\*.WhoisResults.\*.Emails | string |  |  
action_result.data.\*.WhoisResults.\*.Engines | string |  |  
action_result.data.\*.WhoisResults.\*.ExpiresAt | string |  |  
action_result.data.\*.WhoisResults.\*.Name | string |  |  
action_result.data.\*.WhoisResults.\*.NameServers | string |  |  
action_result.data.\*.WhoisResults.\*.Org | string |  |  
action_result.data.\*.WhoisResults.\*.Registrar | string |  |  
action_result.data.\*.WhoisResults.\*.ResourceTaskReferences.\*.ResourceKey | string |  |   0 
action_result.data.\*.WhoisResults.\*.ResourceTaskReferences.\*.TaskKey | string |  |   1 
action_result.data.\*.WhoisResults.\*.State | string |  |  
action_result.data.\*.WhoisResults.\*.UpdatedAt | string |  |  
action_result.data.\*.WhoisResults.\*.WhoisServer | string |  |  
action_result.data.\*.WhoisResults.\*.ZipCode | string |  |  
action_result.summary | string |  |  
action_result.message | string |  |   Job normal forensics retrieved 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1   

## action: 'get job summary'
Get a job summary for a submitted job

Type: **investigate**  
Read only: **True**

Timeout parameter accepts integer value in minutes to wait for action to get finished (by default the value is 0), value 0 is for immediate output.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**job_id** |  required  | Job id of the job summary you want to fetch | string |  `splunk attack analyzer job id` 
**timeout** |  optional  | Maximum time (in minutes) to wait for job to be completed | numeric | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success  failed 
action_result.parameter.job_id | string |  `splunk attack analyzer job id`  |   63572265-c5ae-402f-9fc1-6c90547482aa 
action_result.parameter.timeout | numeric |  |   30 
action_result.data | string |  |  
action_result.data.\*.APIKey | string |  |  
action_result.data.\*.APIKey.\*.ID | string |  |  
action_result.data.\*.APIKey.\*.Label | string |  |  
action_result.data.\*.APIKey.ID | string |  |   e2b3f970-3a8c-46bd-ac13-e2361984d9XX 
action_result.data.\*.APIKey.Label | string |  |   general key 
action_result.data.\*.APIKeyID | string |  |  
action_result.data.\*.CompletedAt | string |  |  
action_result.data.\*.CreatedAt | string |  |  
action_result.data.\*.DisplayScore | numeric |  |  
action_result.data.\*.ForensicsPath | string |  |  
action_result.data.\*.ID | string |  |   63572265-c5ae-402f-9fc1-6c90547482aa 
action_result.data.\*.Labels.\*.ID | numeric |  |  
action_result.data.\*.Labels.\*.Jobs | string |  |  
action_result.data.\*.Labels.\*.Type | string |  |  
action_result.data.\*.Labels.\*.Value | string |  |  
action_result.data.\*.Parameters | string |  |  
action_result.data.\*.Parameters.\*.Name | string |  |   decode_rewritten_urls 
action_result.data.\*.Parameters.\*.Value | string |  |   true 
action_result.data.\*.Priority | numeric |  |  
action_result.data.\*.Profile | string |  |  
action_result.data.\*.RequestedEngines | string |  |  
action_result.data.\*.ResourceCount | numeric |  |  
action_result.data.\*.ResourceTree | string |  |  
action_result.data.\*.ResourceTree.Children.\*.Children.\*.Children.\*.CreatedAt | string |  |   2023-01-31T10:51:32.067Z 
action_result.data.\*.ResourceTree.Children.\*.Children.\*.Children.\*.DisplayScore | numeric |  |  
action_result.data.\*.ResourceTree.Children.\*.Children.\*.Children.\*.FileMetadata.FileType | string |  |  
action_result.data.\*.ResourceTree.Children.\*.Children.\*.Children.\*.FileMetadata.IsEncrypted | string |  |  
action_result.data.\*.ResourceTree.Children.\*.Children.\*.Children.\*.FileMetadata.MD5 | string |  |  
action_result.data.\*.ResourceTree.Children.\*.Children.\*.Children.\*.FileMetadata.MimeType | string |  |  
action_result.data.\*.ResourceTree.Children.\*.Children.\*.Children.\*.FileMetadata.SHA256 | string |  |  
action_result.data.\*.ResourceTree.Children.\*.Children.\*.Children.\*.FileMetadata.Size | numeric |  |  
action_result.data.\*.ResourceTree.Children.\*.Children.\*.Children.\*.ID | string |  |   9bcc64e3-60e8-4aef-965c-73a7a90427d1 
action_result.data.\*.ResourceTree.Children.\*.Children.\*.Children.\*.InjectionMetadata.AddedBecause | string |  |   click 
action_result.data.\*.ResourceTree.Children.\*.Children.\*.Children.\*.InjectionMetadata.AddedBy | string |  |   web_analyzer 
action_result.data.\*.ResourceTree.Children.\*.Children.\*.Children.\*.JobID | string |  |   b29f669c-edde-4bf2-b720-3dd456c389c6 
action_result.data.\*.ResourceTree.Children.\*.Children.\*.Children.\*.Location | string |  |   https://edge.com/test_path/data 
action_result.data.\*.ResourceTree.Children.\*.Children.\*.Children.\*.Name | string |  |   https://edge.com/test_path/data 
action_result.data.\*.ResourceTree.Children.\*.Children.\*.Children.\*.ParentID | string |  |   9ce6e5cc-7836-4134-8aed-874e357696f4 
action_result.data.\*.ResourceTree.Children.\*.Children.\*.Children.\*.Score | numeric |  |  
action_result.data.\*.ResourceTree.Children.\*.Children.\*.Children.\*.Type | string |  |   URL 
action_result.data.\*.ResourceTree.Children.\*.Children.\*.CreatedAt | string |  |   2023-01-31T10:51:32.007Z 
action_result.data.\*.ResourceTree.Children.\*.Children.\*.DisplayScore | numeric |  |  
action_result.data.\*.ResourceTree.Children.\*.Children.\*.FileMetadata.FileType | string |  |  
action_result.data.\*.ResourceTree.Children.\*.Children.\*.FileMetadata.IsEncrypted | string |  |  
action_result.data.\*.ResourceTree.Children.\*.Children.\*.FileMetadata.MD5 | string |  |  
action_result.data.\*.ResourceTree.Children.\*.Children.\*.FileMetadata.MimeType | string |  |  
action_result.data.\*.ResourceTree.Children.\*.Children.\*.FileMetadata.SHA256 | string |  |  
action_result.data.\*.ResourceTree.Children.\*.Children.\*.FileMetadata.Size | numeric |  |  
action_result.data.\*.ResourceTree.Children.\*.Children.\*.ID | string |  |   9ce6e5cc-7836-4134-8aed-874e357696aa 
action_result.data.\*.ResourceTree.Children.\*.Children.\*.InjectionMetadata.AddedBecause | string |  |   HTTPRedirect 
action_result.data.\*.ResourceTree.Children.\*.Children.\*.InjectionMetadata.AddedBy | string |  |   web_analyzer 
action_result.data.\*.ResourceTree.Children.\*.Children.\*.JobID | string |  |   b29f669c-edde-4bf2-b720-3dd456c389c6 
action_result.data.\*.ResourceTree.Children.\*.Children.\*.Location | string |  |   https://www.detect.com/detection 
action_result.data.\*.ResourceTree.Children.\*.Children.\*.Name | string |  |   https://www.detect.com/detection 
action_result.data.\*.ResourceTree.Children.\*.Children.\*.ParentID | string |  |   1ff929ab-cfc1-49d2-83da-2cae20ed51f2 
action_result.data.\*.ResourceTree.Children.\*.Children.\*.Score | numeric |  |  
action_result.data.\*.ResourceTree.Children.\*.Children.\*.Type | string |  |   URL 
action_result.data.\*.ResourceTree.Children.\*.CreatedAt | string |  |   2022-11-23T00:45:27.441Z 
action_result.data.\*.ResourceTree.Children.\*.DisplayScore | numeric |  |  
action_result.data.\*.ResourceTree.Children.\*.FileMetadata.FileType | string |  |  
action_result.data.\*.ResourceTree.Children.\*.FileMetadata.IsEncrypted | string |  |  
action_result.data.\*.ResourceTree.Children.\*.FileMetadata.MD5 | string |  |  
action_result.data.\*.ResourceTree.Children.\*.FileMetadata.MimeType | string |  |  
action_result.data.\*.ResourceTree.Children.\*.FileMetadata.SHA256 | string |  |  
action_result.data.\*.ResourceTree.Children.\*.FileMetadata.Size | numeric |  |  
action_result.data.\*.ResourceTree.Children.\*.ID | string |  |   d7d53778-8ec3-405a-9ec2-9e0a5b998aa3 
action_result.data.\*.ResourceTree.Children.\*.InjectionMetadata.AddedBecause | string |  |   click 
action_result.data.\*.ResourceTree.Children.\*.InjectionMetadata.AddedBy | string |  |   web_analyzer 
action_result.data.\*.ResourceTree.Children.\*.JobID | string |  |   63572265-c5ae-402f-9fc1-6c90547482aa 
action_result.data.\*.ResourceTree.Children.\*.Location | string |  |   https://test.host.com/c35/1/0/test_location/data 
action_result.data.\*.ResourceTree.Children.\*.Name | string |  |   https://test.host.com/c35/1/0/test_location/data 
action_result.data.\*.ResourceTree.Children.\*.ParentID | string |  |   c6e29c54-ca84-4368-8af6-38edc2c839aa 
action_result.data.\*.ResourceTree.Children.\*.Score | numeric |  |  
action_result.data.\*.ResourceTree.Children.\*.Type | string |  |   URL 
action_result.data.\*.ResourceTree.CreatedAt | string |  |   2022-11-23T00:44:12.857Z 
action_result.data.\*.ResourceTree.DisplayScore | numeric |  |   100 
action_result.data.\*.ResourceTree.FileMetadata.FileType | string |  |  
action_result.data.\*.ResourceTree.FileMetadata.IsEncrypted | string |  |  
action_result.data.\*.ResourceTree.FileMetadata.MD5 | string |  |  
action_result.data.\*.ResourceTree.FileMetadata.MimeType | string |  |  
action_result.data.\*.ResourceTree.FileMetadata.SHA256 | string |  |  
action_result.data.\*.ResourceTree.FileMetadata.Size | numeric |  |  
action_result.data.\*.ResourceTree.ID | string |  |   c6e29c54-ca84-4368-8af6-38edc2c839aa 
action_result.data.\*.ResourceTree.InjectionMetadata.AddedBecause | string |  |  
action_result.data.\*.ResourceTree.InjectionMetadata.AddedBy | string |  |  
action_result.data.\*.ResourceTree.JobID | string |  |   63572265-c5ae-402f-9fc1-6c90547482aa 
action_result.data.\*.ResourceTree.Location | string |  |   https://testurl.com/wp-includes/fonts/test_fonts/ 
action_result.data.\*.ResourceTree.Name | string |  |   https://testurl.com/wp-includes/fonts/test_fonts/ 
action_result.data.\*.ResourceTree.ParentID | string |  |  
action_result.data.\*.ResourceTree.Score | numeric |  |   1 
action_result.data.\*.ResourceTree.Type | string |  |   URL 
action_result.data.\*.Resources.\*.Children.\*.Children.\*.Children.\*.CreatedAt | string |  |   2023-01-31T10:51:32.067Z 
action_result.data.\*.Resources.\*.Children.\*.Children.\*.Children.\*.DisplayScore | numeric |  |  
action_result.data.\*.Resources.\*.Children.\*.Children.\*.Children.\*.FileMetadata.FileType | string |  |  
action_result.data.\*.Resources.\*.Children.\*.Children.\*.Children.\*.FileMetadata.IsEncrypted | string |  |  
action_result.data.\*.Resources.\*.Children.\*.Children.\*.Children.\*.FileMetadata.MD5 | string |  |  
action_result.data.\*.Resources.\*.Children.\*.Children.\*.Children.\*.FileMetadata.MimeType | string |  |  
action_result.data.\*.Resources.\*.Children.\*.Children.\*.Children.\*.FileMetadata.SHA256 | string |  |  
action_result.data.\*.Resources.\*.Children.\*.Children.\*.Children.\*.FileMetadata.Size | numeric |  |  
action_result.data.\*.Resources.\*.Children.\*.Children.\*.Children.\*.ID | string |  |   9bcc64e3-60e8-4aef-965c-73a7a9042aa1 
action_result.data.\*.Resources.\*.Children.\*.Children.\*.Children.\*.InjectionMetadata.AddedBecause | string |  |   click 
action_result.data.\*.Resources.\*.Children.\*.Children.\*.Children.\*.InjectionMetadata.AddedBy | string |  |   web_analyzer 
action_result.data.\*.Resources.\*.Children.\*.Children.\*.Children.\*.JobID | string |  |   b29f669c-edde-4bf2-b720-3dd456c389c6 
action_result.data.\*.Resources.\*.Children.\*.Children.\*.Children.\*.Location | string |  |   https://edge.com/test_path/data 
action_result.data.\*.Resources.\*.Children.\*.Children.\*.Children.\*.Name | string |  |   https://edge.com/test_path/data 
action_result.data.\*.Resources.\*.Children.\*.Children.\*.Children.\*.ParentID | string |  |   9ce6e5cc-7836-4134-8aed-874e35769aa4 
action_result.data.\*.Resources.\*.Children.\*.Children.\*.Children.\*.Score | numeric |  |  
action_result.data.\*.Resources.\*.Children.\*.Children.\*.Children.\*.Type | string |  |   URL 
action_result.data.\*.Resources.\*.Children.\*.Children.\*.CreatedAt | string |  |   2023-01-31T10:51:32.067Z 
action_result.data.\*.Resources.\*.Children.\*.Children.\*.DisplayScore | numeric |  |  
action_result.data.\*.Resources.\*.Children.\*.Children.\*.FileMetadata.FileType | string |  |  
action_result.data.\*.Resources.\*.Children.\*.Children.\*.FileMetadata.IsEncrypted | string |  |  
action_result.data.\*.Resources.\*.Children.\*.Children.\*.FileMetadata.MD5 | string |  |  
action_result.data.\*.Resources.\*.Children.\*.Children.\*.FileMetadata.MimeType | string |  |  
action_result.data.\*.Resources.\*.Children.\*.Children.\*.FileMetadata.SHA256 | string |  |  
action_result.data.\*.Resources.\*.Children.\*.Children.\*.FileMetadata.Size | numeric |  |  
action_result.data.\*.Resources.\*.Children.\*.Children.\*.ID | string |  |   9bcc64e3-60e8-4aef-965c-73a7a9042aa1 
action_result.data.\*.Resources.\*.Children.\*.Children.\*.InjectionMetadata.AddedBecause | string |  |   click 
action_result.data.\*.Resources.\*.Children.\*.Children.\*.InjectionMetadata.AddedBy | string |  |   web_analyzer 
action_result.data.\*.Resources.\*.Children.\*.Children.\*.JobID | string |  |   b29f669c-edde-4bf2-b720-3dd456c38aa6 
action_result.data.\*.Resources.\*.Children.\*.Children.\*.Location | string |  |   https://edge.com/test_path/data 
action_result.data.\*.Resources.\*.Children.\*.Children.\*.Name | string |  |   https://edge.com/test_path/data 
action_result.data.\*.Resources.\*.Children.\*.Children.\*.ParentID | string |  |   9ce6e5cc-7836-4134-8aed-874e357696f4 
action_result.data.\*.Resources.\*.Children.\*.Children.\*.Score | numeric |  |  
action_result.data.\*.Resources.\*.Children.\*.Children.\*.Type | string |  |   URL 
action_result.data.\*.Resources.\*.Children.\*.CreatedAt | string |  |   2022-11-23T00:45:27.441Z 
action_result.data.\*.Resources.\*.Children.\*.DisplayScore | numeric |  |  
action_result.data.\*.Resources.\*.Children.\*.FileMetadata.FileType | string |  |  
action_result.data.\*.Resources.\*.Children.\*.FileMetadata.IsEncrypted | string |  |  
action_result.data.\*.Resources.\*.Children.\*.FileMetadata.MD5 | string |  |  
action_result.data.\*.Resources.\*.Children.\*.FileMetadata.MimeType | string |  |  
action_result.data.\*.Resources.\*.Children.\*.FileMetadata.SHA256 | string |  |  
action_result.data.\*.Resources.\*.Children.\*.FileMetadata.Size | numeric |  |  
action_result.data.\*.Resources.\*.Children.\*.ID | string |  |   d7d53778-8ec3-405a-9ec2-9e0a5b998913 
action_result.data.\*.Resources.\*.Children.\*.InjectionMetadata.AddedBecause | string |  |   click 
action_result.data.\*.Resources.\*.Children.\*.InjectionMetadata.AddedBy | string |  |   web_analyzer 
action_result.data.\*.Resources.\*.Children.\*.JobID | string |  |   63572265-c5ae-402f-9fc1-6c90547482aa 
action_result.data.\*.Resources.\*.Children.\*.Location | string |  |   https://test.host.com/c35/1/0/test_location/data 
action_result.data.\*.Resources.\*.Children.\*.Name | string |  |   https://test.host.com/c35/1/0/test_location/data 
action_result.data.\*.Resources.\*.Children.\*.ParentID | string |  |   c6e29c54-ca84-4368-8af6-38edc2c83aae 
action_result.data.\*.Resources.\*.Children.\*.Score | numeric |  |  
action_result.data.\*.Resources.\*.Children.\*.Type | string |  |   URL 
action_result.data.\*.Resources.\*.CreatedAt | string |  |  
action_result.data.\*.Resources.\*.DisplayScore | numeric |  |  
action_result.data.\*.Resources.\*.FileMetadata.\*.FileType | string |  |  
action_result.data.\*.Resources.\*.FileMetadata.\*.IsEncrypted | string |  |  
action_result.data.\*.Resources.\*.FileMetadata.\*.MD5 | string |  |  
action_result.data.\*.Resources.\*.FileMetadata.\*.MimeType | string |  |  
action_result.data.\*.Resources.\*.FileMetadata.\*.SHA256 | string |  |  
action_result.data.\*.Resources.\*.FileMetadata.\*.Size | numeric |  |  
action_result.data.\*.Resources.\*.FileMetadata.FileType | string |  |  
action_result.data.\*.Resources.\*.FileMetadata.IsEncrypted | string |  |  
action_result.data.\*.Resources.\*.FileMetadata.MD5 | string |  |  
action_result.data.\*.Resources.\*.FileMetadata.MimeType | string |  |  
action_result.data.\*.Resources.\*.FileMetadata.SHA256 | string |  |  
action_result.data.\*.Resources.\*.FileMetadata.Size | numeric |  |  
action_result.data.\*.Resources.\*.ID | string |  |  
action_result.data.\*.Resources.\*.InjectionMetadata.\*.AddedBecause | string |  |  
action_result.data.\*.Resources.\*.InjectionMetadata.\*.AddedBy | string |  |  
action_result.data.\*.Resources.\*.InjectionMetadata.AddedBecause | string |  |  
action_result.data.\*.Resources.\*.InjectionMetadata.AddedBy | string |  |  
action_result.data.\*.Resources.\*.JobID | string |  |  
action_result.data.\*.Resources.\*.Location | string |  |  
action_result.data.\*.Resources.\*.Name | string |  |  
action_result.data.\*.Resources.\*.ParentID | string |  |  
action_result.data.\*.Resources.\*.Score | numeric |  |  
action_result.data.\*.Resources.\*.Type | string |  |  
action_result.data.\*.Score | numeric |  |  
action_result.data.\*.Sharing.\*.ShareToken | string |  |  
action_result.data.\*.Sharing.\*.SharedAt | string |  |  
action_result.data.\*.Sharing.\*.SharedBy | string |  |  
action_result.data.\*.Sharing.ShareToken | string |  |  
action_result.data.\*.Sharing.SharedAt | string |  |  
action_result.data.\*.Sharing.SharedBy | string |  |  
action_result.data.\*.StartedAt | string |  |  
action_result.data.\*.State | string |  |  
action_result.data.\*.Submission.MD5 | string |  |  
action_result.data.\*.Submission.Name | string |  |   https://testurl.com/wp-includes/fonts/test_fonts/ 
action_result.data.\*.Submission.SHA256 | string |  |  
action_result.data.\*.SubmissionSource | string |  |  
action_result.data.\*.Submissions.\*.MD5 | string |  |  
action_result.data.\*.Submissions.\*.Name | string |  |  
action_result.data.\*.Submissions.\*.SHA256 | string |  |  
action_result.data.\*.Tasks.\*.CreatedAt | string |  |  
action_result.data.\*.Tasks.\*.Engine | string |  |  
action_result.data.\*.Tasks.\*.ID | string |  |  
action_result.data.\*.Tasks.\*.Priority | numeric |  |  
action_result.data.\*.Tasks.\*.ResourceID | string |  |  
action_result.data.\*.Tasks.\*.Results.\*.Details | string |  |  
action_result.data.\*.Tasks.\*.Results.\*.Forensics.\*.Normalized | string |  |  
action_result.data.\*.Tasks.\*.Results.\*.Forensics.\*.Raw | string |  |  
action_result.data.\*.Tasks.\*.Results.\*.Score | numeric |  |  
action_result.data.\*.Tasks.\*.Results.Details.Cache.IsExact | string |  |   true 
action_result.data.\*.Tasks.\*.Results.Details.Cache.Key | string |  |   r/test_tenant/7B5F5D1sdfbnm,kjhgD75BCEF87 
action_result.data.\*.Tasks.\*.Results.Details.Cache.OriginalTaskCachedAt | string |  |   2023-02-24T10:32:18Z 
action_result.data.\*.Tasks.\*.Results.Details.Content-Encoding | string |  |   windows-1252 
action_result.data.\*.Tasks.\*.Results.Details.Content-Type | string |  |   text/html; charset=windows-1252 
action_result.data.\*.Tasks.\*.Results.Details.Content-Type-Hint | string |  |   text/html; charset=windows-1252 
action_result.data.\*.Tasks.\*.Results.Details.EXIFMetadata.File:FileSize | string |  |   1580 bytes 
action_result.data.\*.Tasks.\*.Results.Details.EXIFMetadata.File:FileType | string |  |   TXT 
action_result.data.\*.Tasks.\*.Results.Details.EXIFMetadata.File:FileTypeExtension | string |  |   txt 
action_result.data.\*.Tasks.\*.Results.Details.EXIFMetadata.File:LineCount | numeric |  |   28 
action_result.data.\*.Tasks.\*.Results.Details.EXIFMetadata.File:MIMEEncoding | string |  |   us-ascii 
action_result.data.\*.Tasks.\*.Results.Details.EXIFMetadata.File:MIMEType | string |  |   text/plain 
action_result.data.\*.Tasks.\*.Results.Details.EXIFMetadata.File:Newlines | string |  |   Unix LF 
action_result.data.\*.Tasks.\*.Results.Details.EXIFMetadata.File:WordCount | numeric |  |   95 
action_result.data.\*.Tasks.\*.Results.Details.Engines.apivoid.\*.Permalink | string |  |   https://www.url.com/scan/testurl.com/ 
action_result.data.\*.Tasks.\*.Results.Details.Engines.apivoid.\*.ScanTime | string |  |   2022-11-23T00:44:14.342421119Z 
action_result.data.\*.Tasks.\*.Results.Details.Engines.apivoid.\*.Score | numeric |  |   0.4 
action_result.data.\*.Tasks.\*.Results.Details.Engines.urlscanio.\*.Scans.\*.ScanTime | string |  |   2020-12-17T10:25:39.434Z 
action_result.data.\*.Tasks.\*.Results.Details.Engines.urlscanio.\*.Scans.\*.UUID | string |  |   7dd9cca2-75c0-43c8-816d-0fe5fafe6aaf 
action_result.data.\*.Tasks.\*.Results.Details.Engines.urlscanio.\*.Score | numeric |  |  
action_result.data.\*.Tasks.\*.Results.Details.Engines.urlscanio.\*.TotalScans | numeric |  |   6 
action_result.data.\*.Tasks.\*.Results.Details.Found | boolean |  |   True  False 
action_result.data.\*.Tasks.\*.Results.Details.NetworkEgress.Endpoint | string |  |   d9cec4861bfb4c6a9137f984896c2447.70-125-225-207_udp.test_residential.com 
action_result.data.\*.Tasks.\*.Results.Details.NetworkEgress.PublicIP | string |  |   XX.125.225.207 
action_result.data.\*.Tasks.\*.Results.Details.NetworkEgress.Region | string |  |   us_residential 
action_result.data.\*.Tasks.\*.Results.Details.NetworkEgress.UserAgent | string |  |  
action_result.data.\*.Tasks.\*.Results.Details.NetworkEgress.UserAgentAlias | string |  |   default 
action_result.data.\*.Tasks.\*.Results.Details.NumEngines | numeric |  |   58 
action_result.data.\*.Tasks.\*.Results.Details.Package | string |  |   chrome 
action_result.data.\*.Tasks.\*.Results.Details.Positives | numeric |  |  
action_result.data.\*.Tasks.\*.Results.Details.RootTaskID | string |  |   8551cf5b-2095-426f-85ec-b8552c17bdaa 
action_result.data.\*.Tasks.\*.Results.Details.ScanDate | string |  |   2021-05-04T16:56:18Z 
action_result.data.\*.Tasks.\*.Results.Details.Tasks.\*.Completed | string |  |   2023-02-24 10:35:25 
action_result.data.\*.Tasks.\*.Results.Details.Tasks.\*.Duration | numeric |  |   196 
action_result.data.\*.Tasks.\*.Results.Details.Tasks.\*.FileSize | numeric |  |   1580 
action_result.data.\*.Tasks.\*.Results.Details.Tasks.\*.GuestLabel | string |  |   win7 
action_result.data.\*.Tasks.\*.Results.Details.Tasks.\*.GuestName | string |  |   win7 
action_result.data.\*.Tasks.\*.Results.Details.Tasks.\*.ID | numeric |  |   18814 
action_result.data.\*.Tasks.\*.Results.Details.Tasks.\*.MD5 | string |  |   d31b3c6a0214862bf4f8099b8ee9aaa3 
action_result.data.\*.Tasks.\*.Results.Details.Tasks.\*.Package | string |  |   chrome 
action_result.data.\*.Tasks.\*.Results.Details.Tasks.\*.ParentID | numeric |  |  
action_result.data.\*.Tasks.\*.Results.Details.Tasks.\*.SHA256 | string |  |   7b43cfb0cc6228c92dcf2ab53eafd9488e56fd95226a3d0f7143c49e9e315aac 
action_result.data.\*.Tasks.\*.Results.Details.Tasks.\*.Score | numeric |  |  
action_result.data.\*.Tasks.\*.Results.Details.Tasks.\*.Ssdeep | string |  |   48:CT6y7yCTFYV6rt7g:NBMBK/5drf6tg7 
action_result.data.\*.Tasks.\*.Results.Details.Tasks.\*.Target | string |  |   test_html.html 
action_result.data.\*.Tasks.\*.Results.Details.Title | string |  |   Manage your tasks 
action_result.data.\*.Tasks.\*.Results.Details.UIURL | string |  |   https://www.url.com/gui/file/7b43cfb0cc6228c92dcf2ab53eafd948aa56fd95226a3d0f7143c49e9e3153aa 
action_result.data.\*.Tasks.\*.Results.Details.Whois.Address | string |  |   3839 Road 160 
action_result.data.\*.Tasks.\*.Results.Details.Whois.City | string |  |   Markham 
action_result.data.\*.Tasks.\*.Results.Details.Whois.Country | string |  |   CA 
action_result.data.\*.Tasks.\*.Results.Details.Whois.CreatedAt | string |  |   2012-09-20T17:40:47+00:00 
action_result.data.\*.Tasks.\*.Results.Details.Whois.DNSSec | string |  |  
action_result.data.\*.Tasks.\*.Results.Details.Whois.Details | string |  |  
action_result.data.\*.Tasks.\*.Results.Details.Whois.DomainName | string |  |   testurl.com 
action_result.data.\*.Tasks.\*.Results.Details.Whois.Engines | string |  |  
action_result.data.\*.Tasks.\*.Results.Details.Whois.ExpiresAt | string |  |   2023-09-20T17:40:47+00:00 
action_result.data.\*.Tasks.\*.Results.Details.Whois.Name | string |  |   Test Name 
action_result.data.\*.Tasks.\*.Results.Details.Whois.Org | string |  |   Private Registration 
action_result.data.\*.Tasks.\*.Results.Details.Whois.Registrar | string |  |   Test Registrar 
action_result.data.\*.Tasks.\*.Results.Details.Whois.State | string |  |   ON 
action_result.data.\*.Tasks.\*.Results.Details.Whois.Timestamp | string |  |  
action_result.data.\*.Tasks.\*.Results.Details.Whois.UpdatedAt | string |  |   2022-08-31T18:17:28+00:00 
action_result.data.\*.Tasks.\*.Results.Details.Whois.Verdict | string |  |  
action_result.data.\*.Tasks.\*.Results.Details.Whois.WhoisServer | string |  |   test.name 
action_result.data.\*.Tasks.\*.Results.Details.Whois.ZipCode | string |  |   unknown 
action_result.data.\*.Tasks.\*.Results.Details.X-TIKA:content_handler | string |  |   ToTextContentHandler 
action_result.data.\*.Tasks.\*.Results.Details.X-TIKA:embedded_depth | string |  |   0 
action_result.data.\*.Tasks.\*.Results.Details.X-TIKA:parse_time_millis | string |  |   284 
action_result.data.\*.Tasks.\*.Results.Details.exiftool.File:FileAccessDate | string |  |   2023:02:24 10:32:09+00:00 
action_result.data.\*.Tasks.\*.Results.Details.exiftool.File:FileInodeChangeDate | string |  |   2023:02:24 10:32:09+00:00 
action_result.data.\*.Tasks.\*.Results.Details.exiftool.File:FileModifyDate | string |  |   2023:02:24 10:32:09+00:00 
action_result.data.\*.Tasks.\*.Results.Details.exiftool.File:FileName | string |  |   tmpicj3cnw3 
action_result.data.\*.Tasks.\*.Results.Details.exiftool.File:FilePermissions | string |  |   -rw-r--r-- 
action_result.data.\*.Tasks.\*.Results.Details.exiftool.File:FileSize | string |  |   1580 bytes 
action_result.data.\*.Tasks.\*.Results.Details.exiftool.File:FileType | string |  |   TXT 
action_result.data.\*.Tasks.\*.Results.Details.exiftool.File:FileTypeExtension | string |  |   txt 
action_result.data.\*.Tasks.\*.Results.Details.exiftool.File:LineCount | numeric |  |   28 
action_result.data.\*.Tasks.\*.Results.Details.exiftool.File:MIMEEncoding | string |  |   us-ascii 
action_result.data.\*.Tasks.\*.Results.Details.exiftool.File:MIMEType | string |  |   text/plain 
action_result.data.\*.Tasks.\*.Results.Details.exiftool.File:Newlines | string |  |   Unix LF 
action_result.data.\*.Tasks.\*.Results.Details.exiftool.File:WordCount | numeric |  |   95 
action_result.data.\*.Tasks.\*.Results.Details.magic | string |  |   HTML document, ASCII text, with very long lines 
action_result.data.\*.Tasks.\*.Results.Details.md5 | string |  |   d31b3c6a0214862bf4f8099b8ee9a563 
action_result.data.\*.Tasks.\*.Results.Details.mime | string |  |   text/html 
action_result.data.\*.Tasks.\*.Results.Details.resourceName | string |  |   test_html.html 
action_result.data.\*.Tasks.\*.Results.Details.sha1 | string |  |   23c09b5e82170349ce99a0a00bec6c476a342aa4 
action_result.data.\*.Tasks.\*.Results.Details.sha256 | string |  |   7b43cfb0cc6228c92dcf2ab53eafd9488e56fd95226a3d0f7143c49e9e3153aa 
action_result.data.\*.Tasks.\*.Results.Details.sha512 | string |  |   66734528d03faf82aa0fda1b97e54e8afdce95a677107389fab5a11d1ebda39f701393cadeca65464c4a12429e7538332e3bb230a7236bf82c59d3bedcdf6aab 
action_result.data.\*.Tasks.\*.Results.Details.size | numeric |  |   1580 
action_result.data.\*.Tasks.\*.Results.Details.ssdeep | string |  |   48:CT6y7yCTFYV6rt7g:NBMBK/5drf6tg7 
action_result.data.\*.Tasks.\*.Results.Details.task-mime-type | string |  |   text/html 
action_result.data.\*.Tasks.\*.Results.Details.task-resource-name | string |  |   test_html.html 
action_result.data.\*.Tasks.\*.Results.Details.tlsh | string |  |   T1A93111A588118C7587B7B045B0FDA62DEF41C557B241CDCC15ECE668F688E925CB3Eaa 
action_result.data.\*.Tasks.\*.Results.DisplayScore | numeric |  |  
action_result.data.\*.Tasks.\*.Results.Forensics.Normalized | string |  |   normalized/2023-02-24/test_tenant/path_to_report.json.gz 
action_result.data.\*.Tasks.\*.Results.Forensics.Raw | string |  |  
action_result.data.\*.Tasks.\*.Results.Score | numeric |  |  
action_result.data.\*.Tasks.\*.StartedAt | string |  |  
action_result.data.\*.Tasks.\*.State | string |  |  
action_result.data.\*.Tasks.\*.StateText | string |  |  
action_result.data.\*.Tasks.\*.StateText | string |  |  
action_result.data.\*.Tasks.\*.UpdatedAt | string |  |  
action_result.data.\*.TenantID | string |  |  
action_result.data.\*.UpdatedAt | string |  |  
action_result.data.\*.Username | string |  |  
action_result.data.\*.Verdict | string |  |  
action_result.summary | string |  |  
action_result.summary.Job ID | string |  |   63572265-c5ae-402f-9fc1-6c90547482aa 
action_result.summary.Score | numeric |  |   100 
action_result.summary.Verdict | string |  |   phish 
action_result.message | string |  |   Job ID: 63572265-c5ae-402f-9fc1-6c90547482aa, Score: 100, Verdict: phish 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1   

## action: 'list recent jobs'
Get a list of recent jobs

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**limit** |  optional  | Number of jobs to fetch (default: 10) | numeric | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success  failed 
action_result.parameter.limit | numeric |  |  
action_result.data.\*.APIKey | string |  |  
action_result.data.\*.APIKey.ID | string |  |   e2b3f970-3a8c-46bd-ac13-e2361984d9XX 
action_result.data.\*.APIKey.Label | string |  |   soar-lab general key 
action_result.data.\*.APIKeyID | string |  |   e2b3f970-3a8c-46bd-ac13-e2361984d9XX 
action_result.data.\*.CompletedAt | string |  |   2023-02-24T10:40:31.934Z 
action_result.data.\*.CreatedAt | string |  |   2023-02-24T10:40:28.542Z 
action_result.data.\*.DisplayScore | numeric |  |   15 
action_result.data.\*.ForensicsPath | string |  |   consolidated/2023-02-24/test_tenant/path_to_report/.json.gz 
action_result.data.\*.ID | string |  `splunk attack analyzer job id`  |   014aeac1-1c49-41a6-aaf8-8033022b9afe 
action_result.data.\*.Parameters | string |  |  
action_result.data.\*.Parameters.\*.Name | string |  |   decode_rewritten_urls 
action_result.data.\*.Parameters.\*.Value | string |  |   true 
action_result.data.\*.Priority | numeric |  |   10 
action_result.data.\*.Profile | string |  |   default 
action_result.data.\*.RequestedEngines | string |  |  
action_result.data.\*.ResourceCount | numeric |  |   8 
action_result.data.\*.Resources.\*.CreatedAt | string |  |   2023-02-24T10:40:29.058Z 
action_result.data.\*.Resources.\*.DisplayScore | numeric |  |  
action_result.data.\*.Resources.\*.FileMetadata.FileType | string |  |  
action_result.data.\*.Resources.\*.FileMetadata.IsEncrypted | string |  |  
action_result.data.\*.Resources.\*.FileMetadata.MD5 | string |  |  
action_result.data.\*.Resources.\*.FileMetadata.MimeType | string |  |  
action_result.data.\*.Resources.\*.FileMetadata.SHA256 | string |  |  
action_result.data.\*.Resources.\*.FileMetadata.Size | numeric |  |  
action_result.data.\*.Resources.\*.ID | string |  |   47c74e9a-ec3d-4571-b67f-4bcf2f8e4aa0 
action_result.data.\*.Resources.\*.InjectionMetadata.AddedBecause | string |  |   link 
action_result.data.\*.Resources.\*.InjectionMetadata.AddedBy | string |  |   static_doc 
action_result.data.\*.Resources.\*.JobID | string |  |   014aeac1-1c49-41a6-aaf8-8033022b9afe 
action_result.data.\*.Resources.\*.Location | string |  |   https://www.testdomain.com/ 
action_result.data.\*.Resources.\*.Name | string |  |   https://www.testdomain.com/ 
action_result.data.\*.Resources.\*.ParentID | string |  |   c5443fd6-17f7-4456-a421-801f07599aad 
action_result.data.\*.Resources.\*.Score | numeric |  |  
action_result.data.\*.Resources.\*.Type | string |  |   URL 
action_result.data.\*.Score | numeric |  |   0.15 
action_result.data.\*.Sharing.ShareToken | string |  |  
action_result.data.\*.Sharing.SharedAt | string |  |  
action_result.data.\*.Sharing.SharedBy | string |  |  
action_result.data.\*.StartedAt | string |  |   2023-02-24T10:40:28.609Z 
action_result.data.\*.State | string |  |   done 
action_result.data.\*.Submission.MD5 | string |  |   d31b3c6a0214862bf4f8099b8ee9aaa3 
action_result.data.\*.Submission.Name | string |  |   test_html.html 
action_result.data.\*.Submission.SHA256 | string |  |   7b43cfb0cc6228c92dcf2ab53eafd9488e56fd95226a3d0f7143c49e9e315aac 
action_result.data.\*.SubmissionSource | string |  |   API 
action_result.data.\*.Tasks.\*.CreatedAt | string |  |   2023-02-24T10:40:29.128Z 
action_result.data.\*.Tasks.\*.Engine | string |  |   url_reputation 
action_result.data.\*.Tasks.\*.ID | string |  |   09ee728b-d73e-4e99-8a51-8684bceb3aa6 
action_result.data.\*.Tasks.\*.Priority | numeric |  |   10 
action_result.data.\*.Tasks.\*.ResourceID | string |  |   d0f98453-3c93-41da-b739-98b8a3d27aa1 
action_result.data.\*.Tasks.\*.Results.Details | string |  |  
action_result.data.\*.Tasks.\*.Results.DisplayScore | numeric |  |  
action_result.data.\*.Tasks.\*.Results.Forensics.Normalized | string |  |   normalized/2023-02-24/test_tenant/path_to_report.json.gz 
action_result.data.\*.Tasks.\*.Results.Forensics.Raw | string |  |  
action_result.data.\*.Tasks.\*.Results.Score | numeric |  |  
action_result.data.\*.Tasks.\*.StartedAt | string |  |  
action_result.data.\*.Tasks.\*.State | string |  |   done 
action_result.data.\*.Tasks.\*.StateText | string |  |  
action_result.data.\*.Tasks.\*.UpdatedAt | string |  |   2023-02-24T10:40:29.228Z 
action_result.data.\*.TenantID | string |  |   test-tenant 
action_result.data.\*.UpdatedAt | string |  |   2023-02-24T10:40:31.936Z 
action_result.data.\*.Username | string |  |  
action_result.data.\*.Verdict | string |  |  
action_result.message | string |  |   Job count: 11 
action_result.summary.job_count | numeric |  |   11 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1   

## action: 'detonate file'
Submit File for Scanning

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**file** |  required  | File hash to submit | string |  `vault id` 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success  failed 
action_result.parameter.file | string |  `vault id`  |   89b238c79f7752948b176222ae0010d0a1aa 
action_result.data.\*.AppURL | string |  `url`  |  
action_result.data.\*.JobID | string |  `splunk attack analyzer job id`  |   63572265-c5ae-402f-9fc1-6c90547482XX 
action_result.data.\*.QueueDepth | numeric |  |  
action_result.data.\*.QuotaRemaining | numeric |  |  
action_result.summary | string |  |  
action_result.message | string |  |   Submitted file 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1   

## action: 'detonate url'
Submit New URL for Scanning

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**url** |  required  | URL to submit | string |  `url` 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success  failed 
action_result.parameter.url | string |  `url`  |   https://test_url.com 
action_result.data.\*.AppURL | string |  `url`  |  
action_result.data.\*.JobID | string |  `splunk attack analyzer job id`  |   63572265-c5ae-402f-9fc1-6c90547481XX 
action_result.data.\*.QueueDepth | numeric |  |  
action_result.data.\*.QuotaRemaining | numeric |  |  
action_result.summary | string |  |  
action_result.message | string |  |   Submitted URL 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1   

## action: 'on poll'
Callback action for the on_poll ingest functionality

Type: **ingest**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**container_id** |  optional  | Parameter ignored in this app | string | 
**start_time** |  optional  | Parameter ignored in this app | numeric | 
**end_time** |  optional  | Parameter ignored in this app | numeric | 
**container_count** |  optional  | Number of jobs to ingest | numeric | 
**artifact_count** |  optional  | Parameter ignored in this app | numeric | 

#### Action Output
No Output  

## action: 'test connectivity'
Validate the asset configuration for connectivity using supplied configuration

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output