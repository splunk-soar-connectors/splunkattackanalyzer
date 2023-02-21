[comment]: # "Auto-generated SOAR connector documentation"
# Splunk Attack Analyzer

Publisher: Splunk  
Connector Version: 1\.0\.0  
Product Vendor: Splunk  
Product Name: Splunk Attack Analyzer  
Product Version Supported (regex): "\.\*"  
Minimum Product Version: 5\.4\.0  

A threat analysis platform to reduce the friction of repetitive manual tasks typically associated with investigating threats

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
### The Splunk Attack Analyzer SOAR app can be used to connect with the <a
href="https://www.google.com/url?q=https://www.twinwave.io/&amp;sa=D&amp;source=editors&amp;ust=1644536802576291&amp;usg=AOvVaw1QbcnelmQFirXDHIRabB07"
target="_blank">Splunk Attack Analyzer analysis platform</a>

The following actions are supported by the app:

- Submitting a URL for analysis
- Submitting a file for analysis
- Fetching analysis (job) summary data
- Fetching the forensics for a job
- Downloading screenshots for a job and attaching them to the vault
- Downloading an offline PDF report for a job and attaching it to the vault


### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a Splunk Attack Analyzer asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**api\_token** |  required  | password | API token from the app
**since** |  optional  | numeric | Start of time range stated in hours\. If not specified, the default is past 3 days

### Supported Actions  
[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity using supplied configuration  
[on poll](#action-on-poll) - Callback action for the on\_poll ingest functionality  
[get job forensics](#action-get-job-forensics) - Get the consolidated forensics for a completed job  
[get job summary](#action-get-job-summary) - Get a job summary  
[list recent jobs](#action-list-recent-jobs) - Get a list of recent jobs  
[detonate file](#action-detonate-file) - Submit File for Scanning  
[detonate url](#action-detonate-url) - Submit New URL for Scanning  
[get pdf report](#action-get-pdf-report) - Get the PDF report for a completed job  
[get job screenshots](#action-get-job-screenshots) - Get screenshots for the specified job and store them in the vault  

## action: 'test connectivity'
Validate the asset configuration for connectivity using supplied configuration

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output  

## action: 'on poll'
Callback action for the on\_poll ingest functionality

Type: **ingest**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**container\_id** |  optional  | Parameter ignored in this app | string | 
**start\_time** |  optional  | Parameter ignored in this app | numeric | 
**end\_time** |  optional  | Parameter ignored in this app | numeric | 
**container\_count** |  optional  | Number of jobs to ingest | numeric | 
**artifact\_count** |  optional  | Parameter ignored in this app | numeric | 

#### Action Output
No Output  

## action: 'get job forensics'
Get the consolidated forensics for a completed job

Type: **investigate**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**job\_id** |  required  | Job id of the forensics you want pulled | string |  `splunk attack analyzer job id` 
**wait** |  optional  | Wait for job to finish before returning results | boolean | 
**timeout** |  optional  | Maximum time \(in minutes\) to wait for job to be complete | numeric | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action\_result\.status | string |  |   success  failed 
action\_result\.parameter\.job\_id | string |  `splunk attack analyzer job id`  |   63572265\-c5ae\-402f\-9fc1\-6c90547482ee 
action\_result\.parameter\.timeout | numeric |  |   30 
action\_result\.parameter\.wait | boolean |  |   True  False 
action\_result\.data | string |  |  
action\_result\.data\.\*\.DNSRequests | string |  |  
action\_result\.data\.\*\.DNSRequests\.\*\.Engines | string |  |  
action\_result\.data\.\*\.DNSRequests\.\*\.Query | string |  |  
action\_result\.data\.\*\.DNSRequests\.\*\.QueryType | string |  |  
action\_result\.data\.\*\.DNSRequests\.\*\.Responses\.\*\.Type | string |  |  
action\_result\.data\.\*\.DNSRequests\.\*\.Responses\.\*\.Value | string |  |  
action\_result\.data\.\*\.DNSRequests\.\*\.Server | string |  |  
action\_result\.data\.\*\.DNSServers | string |  |  
action\_result\.data\.\*\.Details\.engines | string |  |  
action\_result\.data\.\*\.Detections\.\*\.Description | string |  |  
action\_result\.data\.\*\.Detections\.\*\.Details\.Data\.\*\.Hit | string |  |  
action\_result\.data\.\*\.Detections\.\*\.Details\.Extracted Values\.\*\.Name | string |  |   Copyright 
action\_result\.data\.\*\.Detections\.\*\.Details\.Extracted Values\.\*\.Value | string |  |   © 2021 Intuit 
action\_result\.data\.\*\.Detections\.\*\.Details\.Forms\.\*\.Action | string |  |   /newsletter/ 
action\_result\.data\.\*\.Detections\.\*\.Details\.IsMetaRule | boolean |  |   True  False 
action\_result\.data\.\*\.Detections\.\*\.Details\.Match Source | string |  |   html\_dom 
action\_result\.data\.\*\.Detections\.\*\.Details\.Nested Detections\.\*\.Description | string |  |   Image Match \- Potential  website detected\: Intuit 
action\_result\.data\.\*\.Detections\.\*\.Details\.Nested Detections\.\*\.Details\.Extracted Values\.\*\.Name | string |  |   HtmlPostForm 
action\_result\.data\.\*\.Detections\.\*\.Details\.Nested Detections\.\*\.Details\.Extracted Values\.\*\.Value | string |  |   <form id="ius\-sign\-in\-mfa\-password\-collection\-form" action="mail\.php" method="post" autocomplete="on" novalidate=""> 
action\_result\.data\.\*\.Detections\.\*\.Details\.Nested Detections\.\*\.Details\.Forms\.\*\.Action | string |  |   mail\.php 
action\_result\.data\.\*\.Detections\.\*\.Details\.Nested Detections\.\*\.Details\.IsMetaRule | boolean |  |   True  False 
action\_result\.data\.\*\.Detections\.\*\.Details\.Nested Detections\.\*\.Details\.Match Confidence | string |  |   exact 
action\_result\.data\.\*\.Detections\.\*\.Details\.Nested Detections\.\*\.Details\.Match Source | string |  |   html\_dom 
action\_result\.data\.\*\.Detections\.\*\.Details\.Nested Detections\.\*\.Details\.Nested Detections\.\*\.Description | string |  |   Evidence of a Cloned Website \(data\-savepage\-\) 
action\_result\.data\.\*\.Detections\.\*\.Details\.Nested Detections\.\*\.Details\.Nested Detections\.\*\.Details\.Extracted Values\.\*\.Name | string |  |   String 
action\_result\.data\.\*\.Detections\.\*\.Details\.Nested Detections\.\*\.Details\.Nested Detections\.\*\.Details\.Extracted Values\.\*\.Value | string |  |   data\-savepage\-href="https\://plugin\.intuitcdn\.net/\@sbg/qbo\-logo/v1/QBOlogo\.png" 
action\_result\.data\.\*\.Detections\.\*\.Details\.Nested Detections\.\*\.Details\.Nested Detections\.\*\.Details\.Forms\.\*\.Action | string |  |   mail\.php 
action\_result\.data\.\*\.Detections\.\*\.Details\.Nested Detections\.\*\.Details\.Nested Detections\.\*\.Details\.Match Source | string |  |   html\_dom 
action\_result\.data\.\*\.Detections\.\*\.Details\.Nested Detections\.\*\.Details\.Nested Detections\.\*\.Details\.URL | string |  |   https\://boomerangdairysandbedding\.com/wp\-includes/fonts/QuickB2022/ 
action\_result\.data\.\*\.Detections\.\*\.Details\.Nested Detections\.\*\.Details\.Nested Detections\.\*\.DisplaySeverity | numeric |  |   25 
action\_result\.data\.\*\.Detections\.\*\.Details\.Nested Detections\.\*\.Details\.Nested Detections\.\*\.Engines | string |  |  
action\_result\.data\.\*\.Detections\.\*\.Details\.Nested Detections\.\*\.Details\.Nested Detections\.\*\.Name | string |  |   11c9b64a\-aea1\-11eb\-a69b\-07db8cd523bb 
action\_result\.data\.\*\.Detections\.\*\.Details\.Nested Detections\.\*\.Details\.Nested Detections\.\*\.Severity | numeric |  |   0.25 
action\_result\.data\.\*\.Detections\.\*\.Details\.Nested Detections\.\*\.Details\.Nested Detections\.\*\.Timestamp | string |  |  
action\_result\.data\.\*\.Detections\.\*\.Details\.Nested Detections\.\*\.Details\.Nested Detections\.\*\.Verdict | string |  |  
action\_result\.data\.\*\.Detections\.\*\.Details\.Nested Detections\.\*\.Details\.Resource | string |  |   https\://boomerangdairysandbedding\.com/wp\-includes/fonts/QuickB2022/ 
action\_result\.data\.\*\.Detections\.\*\.Details\.Nested Detections\.\*\.Details\.URL | string |  |   https\://boomerangdairysandbedding\.com/wp\-includes/fonts/QuickB2022/ 
action\_result\.data\.\*\.Detections\.\*\.Details\.Nested Detections\.\*\.DisplaySeverity | numeric |  |   75 
action\_result\.data\.\*\.Detections\.\*\.Details\.Nested Detections\.\*\.Engines | string |  |  
action\_result\.data\.\*\.Detections\.\*\.Details\.Nested Detections\.\*\.Name | string |  |   5ec4e953\-e68f\-4298\-9b2c\-739c3d729e16 
action\_result\.data\.\*\.Detections\.\*\.Details\.Nested Detections\.\*\.Severity | numeric |  |   0.75 
action\_result\.data\.\*\.Detections\.\*\.Details\.Nested Detections\.\*\.Timestamp | string |  |  
action\_result\.data\.\*\.Detections\.\*\.Details\.Nested Detections\.\*\.Verdict | string |  |   phish 
action\_result\.data\.\*\.Detections\.\*\.Details\.OpenPhish | string |  |   high confidence 
action\_result\.data\.\*\.Detections\.\*\.Details\.URL | string |  |   https\://boomerangdairysandbedding\.com/wp\-includes/fonts/QuickB2022/ 
action\_result\.data\.\*\.Detections\.\*\.DisplaySeverity | numeric |  |   100 
action\_result\.data\.\*\.Detections\.\*\.Engines | string |  |  
action\_result\.data\.\*\.Detections\.\*\.Name | string |  |  
action\_result\.data\.\*\.Detections\.\*\.ResourceTaskReferences\.\*\.ResourceKey | string |  |   0 
action\_result\.data\.\*\.Detections\.\*\.ResourceTaskReferences\.\*\.TaskKey | string |  |   1 
action\_result\.data\.\*\.Detections\.\*\.Severity | numeric |  |  
action\_result\.data\.\*\.Detections\.\*\.Verdict | string |  |   phish 
action\_result\.data\.\*\.DisplayScore | numeric |  |  
action\_result\.data\.\*\.EndTime | string |  |  
action\_result\.data\.\*\.Engine | string |  |  
action\_result\.data\.\*\.Files\.\*\.Context | string |  |  
action\_result\.data\.\*\.Files\.\*\.Details\.\*\.CRC32 | string |  |  
action\_result\.data\.\*\.Files\.\*\.Details\.\*\.ClamAV | string |  |  
action\_result\.data\.\*\.Files\.\*\.Details\.\*\.GuestPath | string |  |  
action\_result\.data\.\*\.Files\.\*\.Details\.\*\.SHA1 | string |  |  
action\_result\.data\.\*\.Files\.\*\.Details\.\*\.SHA512 | string |  |  
action\_result\.data\.\*\.Files\.\*\.FileName | string |  |  
action\_result\.data\.\*\.Files\.\*\.FileType | string |  |  
action\_result\.data\.\*\.Files\.\*\.MD5 | string |  |  
action\_result\.data\.\*\.Files\.\*\.MimeType | string |  |   text/plain 
action\_result\.data\.\*\.Files\.\*\.NetworkSources | string |  |  
action\_result\.data\.\*\.Files\.\*\.Path | string |  |  
action\_result\.data\.\*\.Files\.\*\.ResourceTaskReferences\.\*\.ResourceKey | string |  |   1 
action\_result\.data\.\*\.Files\.\*\.ResourceTaskReferences\.\*\.TaskKey | string |  |   3 
action\_result\.data\.\*\.Files\.\*\.SHA256 | string |  |  
action\_result\.data\.\*\.Files\.\*\.Size | numeric |  |  
action\_result\.data\.\*\.Files\.\*\.Ssdeep | string |  |  
action\_result\.data\.\*\.Forms\.\*\.Action | string |  |  
action\_result\.data\.\*\.Forms\.\*\.Engines | string |  |  
action\_result\.data\.\*\.Forms\.\*\.Inputs\.\*\.ID | string |  |  
action\_result\.data\.\*\.Forms\.\*\.Inputs\.\*\.Name | string |  |  
action\_result\.data\.\*\.Forms\.\*\.Inputs\.\*\.Placeholder | string |  |  
action\_result\.data\.\*\.Forms\.\*\.Inputs\.\*\.SourceCode | string |  |  
action\_result\.data\.\*\.Forms\.\*\.Inputs\.\*\.Type | string |  |  
action\_result\.data\.\*\.Forms\.\*\.Method | string |  |   post 
action\_result\.data\.\*\.Forms\.\*\.PageURL | string |  |  
action\_result\.data\.\*\.Forms\.\*\.ResourceTaskReferences\.\*\.ResourceKey | string |  |   0 
action\_result\.data\.\*\.Forms\.\*\.ResourceTaskReferences\.\*\.TaskKey | string |  |   1 
action\_result\.data\.\*\.Forms\.\*\.SourceCode | string |  |  
action\_result\.data\.\*\.Forms\.\*\.method | string |  |  
action\_result\.data\.\*\.HTTP\.\*\.Destination\.\*\.IP | string |  |  
action\_result\.data\.\*\.HTTP\.\*\.Destination\.\*\.Port | numeric |  |  
action\_result\.data\.\*\.HTTP\.\*\.Destination\.IP | string |  |   23\.43\.113\.24 
action\_result\.data\.\*\.HTTP\.\*\.Destination\.Port | numeric |  |   443 
action\_result\.data\.\*\.HTTP\.\*\.Details\.\_requestref | string |  |   b45353994bb050fd7d945cb88d4ef9 
action\_result\.data\.\*\.HTTP\.\*\.Hostname | string |  |  
action\_result\.data\.\*\.HTTP\.\*\.Method | string |  |  
action\_result\.data\.\*\.HTTP\.\*\.Path | string |  |  
action\_result\.data\.\*\.HTTP\.\*\.RequestHeaders | string |  |  
action\_result\.data\.\*\.HTTP\.\*\.RequestHeaders\.accept | string |  |   \*/\* 
action\_result\.data\.\*\.HTTP\.\*\.RequestHeaders\.accept\-language | string |  |   en\-US 
action\_result\.data\.\*\.HTTP\.\*\.RequestHeaders\.content\-type | string |  |   application/x\-www\-form\-urlencoded; charset=utf\-8 
action\_result\.data\.\*\.HTTP\.\*\.RequestHeaders\.cookie | string |  |   ius\_session=14F7909BDE45458800589FB8E8AAA187; thx\_guid=387999fd7aadac9dd987523e86cfb2db; tmx\_guid=AAwIREOalk\_Dxw1NYzywOdivOz8u\_B9BJBj\_A3Ep6pssv\-wezsGa\_GhNiCm3vqXfg6ysQGnDOrklg87hvlYF5UTJOWvODw; did=SHOPPER2\_d7be422703b43635e7559bf3158acf11f3841558d961b1d562f5d23de36ecb5f21994e938d400f01cf633364be072d49 
action\_result\.data\.\*\.HTTP\.\*\.RequestHeaders\.intervention | string |  |   <https\://www\.chromestatus\.com/feature/5718547946799104>; level="warning" 
action\_result\.data\.\*\.HTTP\.\*\.RequestHeaders\.intuit\-plugin\-id | string |  |   qbo\-frozen\-satellites 
action\_result\.data\.\*\.HTTP\.\*\.RequestHeaders\.ms\-cv | string |  |   853d5c00\-cc23\-4de8\-a912\-a115a30f3635 
action\_result\.data\.\*\.HTTP\.\*\.RequestHeaders\.origin | string |  |   https\://c35\.qbo\.intuit\.com 
action\_result\.data\.\*\.HTTP\.\*\.RequestHeaders\.referer | string |  |   https\://c35\.qbo\.intuit\.com/ 
action\_result\.data\.\*\.HTTP\.\*\.RequestHeaders\.upgrade\-insecure\-requests | string |  |   1 
action\_result\.data\.\*\.HTTP\.\*\.RequestHeaders\.user\-agent | string |  |   Mozilla/5\.0 \(Windows NT 10\.0; Win64; x64\) AppleWebKit/537\.36 \(KHTML, like Gecko\) Chrome/101\.0\.4951\.67 Safari/537\.36 Edg/100\.0\.1185\.39 
action\_result\.data\.\*\.HTTP\.\*\.RequestHeaders\.x\-auth\-token | string |  |   e0146ee5\-0ed8\-47f2\-abef\-e237f82fbb87 
action\_result\.data\.\*\.HTTP\.\*\.RequestHeaders\.x\-requested\-with | string |  |   XMLHttpRequest 
action\_result\.data\.\*\.HTTP\.\*\.RequestSize | numeric |  |  
action\_result\.data\.\*\.HTTP\.\*\.ResourceTaskReferences\.\*\.ResourceKey | string |  |   1 
action\_result\.data\.\*\.HTTP\.\*\.ResourceTaskReferences\.\*\.TaskKey | string |  |   3 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders | numeric |  |  
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.accept\-ch | string |  |   Sec\-CH\-UA\-Arch, Sec\-CH\-UA\-Bitness, Sec\-CH\-UA\-Full\-Version, Sec\-CH\-UA\-Mobile, Sec\-CH\-UA\-Model, Sec\-CH\-UA\-Platform, Sec\-CH\-UA\-Platform\-Version 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.accept\-ranges | string |  |   bytes 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.access\-control\-allow\-credentials | string |  |   false 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.access\-control\-allow\-headers | string |  |   Accept, Content\-Type, Content\-Encoding, Client\-Id 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.access\-control\-allow\-methods | string |  |   GET 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.access\-control\-allow\-origin | string |  |   \* 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.access\-control\-expose\-headers | string |  |   intuit\_captcha\_required,intuit\_tid,intuit\_flowid,intuit\_requires\_evaluation,intuit\_ticket\_exchanged,intuit\_data 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.access\-control\-max\-age | string |  |   86400 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.adrum\_0 | string |  |   g\:ff51ace9\-4caa\-4d10\-8b7c\-e17a0b1f75ab 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.adrum\_1 | string |  |   n\:intuit\-sbg\-prod\_87bcfab1\-ad5a\-4af1\-95e0\-7eed4f8a1800 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.adrum\_2 | string |  |   i\:257759 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.adrum\_3 | string |  |   e\:130 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.age | string |  |   401 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.alt\-svc | string |  |   h3="\:443"; ma=86400 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.api\-version | string |  |   v2 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.cache\-control | string |  |   public, max\-age=31556926, immutable 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.cf\-bgj | string |  |   imgq\:100,h2pri 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.cf\-cache\-status | string |  |   HIT 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.cf\-polished | string |  |   origSize=152090, status=webp\_bigger 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.cf\-ray | string |  |   7921e1dd3d3867cf\-MIA 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.connection | string |  |   Keep\-Alive 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.content\-disposition | string |  |   inline; filename="NetworkingInteractive\.jpg" 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.content\-encoding | string |  |   br 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.content\-language | string |  |   en\-CA 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.content\-length | string |  |   47438 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.content\-location | string |  |   https\://image\.prod\.cms\.rt\.com/cms/api/am/imageFileData/RE1Mu3b?ver=5c31 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.content\-md5 | string |  |   tfIwuCAmVOw8IfslU4qRSw== 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.content\-security\-policy | string |  |   frame\-src 'self'; connect\-src 'self'; default\-src 'self'; script\-src 'self' 'unsafe\-inline' ; style\-src 'unsafe\-inline' 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.content\-security\-policy\-report\-only | string |  |   script\-src 'none'; report\-uri https\://csp\-reporting\.cloudflare\.com/cdn\-cgi/script\_monitor/report?m=DiwktFARNqAy3a4GoEmSR7wR6atNa2qvMDQY2TUrzfQ\-1675162230\-0\-ATTPJ300FFMoEyh\_3DL72ZEo7BUuPEs\_1oEV02VM4PzghrsF3SeMSfazCuW51ungJD4K9STH7FCoBV\-L581FrnMKb1hiJ\_RbeWLNLAdDXWhc; report\-to cf\-csp\-endpoint 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.content\-type | string |  |   font/ttf 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.cross\-origin\-opener\-policy | string |  |   same\-origin\-allow\-popups 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.cross\-origin\-opener\-policy\-report\-only | string |  |   same\-origin; report\-to="static\-on\-bigtable" 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.cross\-origin\-resource\-policy | string |  |   cross\-origin 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.date | string |  |   Wed, 23 Nov 2022 00\:44\:36 GMT 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.document\-policy | string |  |   force\-load\-at\-top 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.etag | string |  |   "e54addba509" 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.expect\-ct | string |  |   max\-age=86400, report\-uri="https\://www\.linkedin\.com/platform\-telemetry/ct" 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.expires | string |  |   Thu, 01 Jan 1970 00\:00\:00 GMT 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.fly\-request\-id | string |  |   01GQDCXWGM7GR6D7NYES5CEMPT\-mia 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.identification\-source | string |  |   CACHE 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.intuit\_tid | string |  |   18375f05\-0688\-46f2\-87bd\-36b2a3056e4e 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.keep\-alive | string |  |   timeout=2, max=100 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.last\-modified | string |  |   Wed, 27 Apr 2022 18\:34\:52 GMT 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.linkedin\-action | string |  |   1 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.location | string |  |   https\://data\.xyz\.com/b/ss/xee/1/H\.20\.3/s28372352737215?AQB= 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.ms\-cv | string |  |   0TwjKmhArkqpx27S\.0 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.ms\-cv\-esi | string |  |   CASCV4deabe4\.0 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.ms\-operation\-id | string |  |   22352131e9aa584ca106a3df24b0fe 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.nel | string |  |   \{"report\_to"\:"network\-errors","max\_age"\:1296000,"success\_fraction"\:0\.00066,"failure\_fraction"\:1,"include\_subdomains"\:true\} 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.operationid | string |  |   ede2ed5a1b48ecbff5456dca5060c 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.origin\-agent\-cluster | string |  |   ?0 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.p3p | string |  |   CP="This is not a P3P policy" 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.perf | string |  |   7626143928 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.permissions\-policy | string |  |   accelerometer=\(\), camera=\(\), geolocation=\(\), gyroscope=\(\), magnetometer=\(\), microphone=\(\), payment=\(\), usb=\(\), interest\-cohort=\(\) 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.pragma | string |  |   no\-cache 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.priority | string |  |   u=3,i 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.ptime | string |  |   0\.0035480000005919 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.referrer\-policy | string |  |   no\-referrer 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.report\-to | string |  |   \{"group"\:"network\-errors","max\_age"\:2592000,"endpoints"\:\[\{"url"\:"https\://www\.linkedin\.com/li/rep"\}\],"include\_subdomains"\:true\} 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.request\-context | string |  |   appId=cid\-v1\:fc03bcad\-a752\-4f14\-8357\-64132357286d 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.request\-id | string |  |   ba7cb248\-8059\-4558\-8c44\-af85f8a13213 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.server | string |  |   DatabaseS3 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.server\-timing | string |  |   edge; dur=1, origin; dur=11, cdn\-cache; desc=MISS 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.strict\-transport\-security | string |  |   max\-age=31536000 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.time\-delta\-millis | string |  |   384 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.timing\-allow\-origin | string |  |   \*, \* 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.tls\_version | string |  |   tls1\.3 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.tmx\-nonce | string |  |   8226d90974108d 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.trace\-id | string |  |   568b46f84bb545c7 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.transfer\-encoding | string |  |   chunked 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.vary | string |  |   Accept\-Encoding 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.via | string |  |   1\.1 5ab5dc09da67e3ea794ec8a82992cc88\.cloudfront\.net \(CloudFront\) 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.www\-authenticate | string |  |   DemandBase API v2 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-activity\-id | string |  |   544275be\-d3be\-49b5\-bbb8\-18339e4220fc 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-activityid | string |  |   0b707f18\-4fe3\-4cf6\-8719\-b892441154a6 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-amz\-cf\-id | string |  |   jvi58qPvaKsS7KpFGAFMbwP3Heql0ZInZO3w9x3EPse4zY0jHgA== 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-amz\-cf\-pop | string |  |   ORD51\-C2 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-amz\-id\-2 | string |  |   yi/1AP8btDeBMNwXKzVKDmFpEb/NKNKf\+HyDKux8RfM4ZzlxA93LWImqYXQ4JZobPRlaFA= 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-amz\-meta\-id | string |  |   identity\-authn\-core\-ui 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-amz\-meta\-module | string |  |   identity\-authn\-core\-ui 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-amz\-meta\-slug | string |  |   identity\-authn\-core\-ui/1\.388\.1\-apr\.2734\.b\.7 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-amz\-meta\-type | string |  |   plugin 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-amz\-meta\-version | string |  |   1\.388\.1\-apr\.2734\.b\.7 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-amz\-request\-id | string |  |   J12AVJJT0N7SCTV4 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-amz\-storage\-class | string |  |   INTELLIGENT\_TIERING 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-amz\-version\-id | string |  |   0SaPfidEaOrnyiftYjgXNTUE9SyoELUR 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-appversion | string |  |   1\.0\.8390\.9238 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-aspnet\-version | string |  |   4\.0\.30319 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-az | string |  |   \{did\:eb10a4325ec94140a244ba6df596f910, rid\: 14, sn\: storeexp\-wcus\-prod, dt\: 2023\-01\-18T05\:15\:55\.8437711Z, bt\: 2022\-12\-21T05\:07\:56\.0000000Z\} 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-azure\-ref | string |  |   20230131T104954Z\-bqvak4nptd2c30mdndbs7zwyu40000000bqg000000001czg 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-azure\-ref\-originshield | string |  |   0WFbWYwC66tUsSIvdQIBfLyW2kyC5TU5aMjIxMDYwNjExMDExAGYxY2E3M2Q0LTg4ODMtNGNhZi1hYmRjLWZlMmQ1NjdhZmI5Ng== 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-cache | string |  |   Hit from cloudfront 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-cdn | string |  |   AKAM 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-computed | string |  |   true 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-connection\-hash | string |  |   e5deadb6db0d14073930ebfdccdf40a9d32913c27e89281abb0746eec820 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-content\-type\-options | string |  |   nosniff 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-datacenter | string |  |   westcenus 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-edgeconnect\-midmile\-rtt | string |  |   1 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-edgeconnect\-origin\-mex\-latency | string |  |   54 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-fb\-debug | string |  |   ORufSisO0ETW61nDh\+RWwxOEnwaoyIullpfm\+QN0ictsLVMaFgiqB\+PDkiIvYwWGpm6I8T/Qo\+WRyTy9gQ== 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-fb\-rlafr | string |  |   0 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-frame\-options | string |  |   SAMEORIGIN 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-li\-fabric | string |  |   prod\-ltx1 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-li\-pop | string |  |   afd\-prod\-ltx1\-x 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-li\-proto | string |  |   http/2 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-li\-uuid | string |  |   AAXzjRbzt4rxIfkgS/VpZQ== 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-ms\-blob\-type | string |  |   BlockBlob 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-ms\-lease\-status | string |  |   unlocked 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-ms\-meta\-jssdkver | string |  |   3\.2\.6 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-ms\-request\-id | string |  |   af25cca6\-701e\-003f\-77c7\-316f3a000000 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-ms\-version | string |  |   2009\-09\-19 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-msedge\-ref | string |  |   Ref A\: 8E47239F9C11469DA76EDD93DCF74F24 Ref B\: MIAEDGE1709 Ref C\: 2023\-01\-31T10\:49\:44Z 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-origin\-src | string |  |   uxf 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-powered\-by | string |  |   ASP\.NET 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-request\-id | string |  |   78fad6f9\-27f5\-470e\-83c0\-9975ca709e36 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-resizerversion | string |  |   1\.0 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-response\-time | string |  |   7 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-rtag | string |  |   Str 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-s1 | string |  |   2023\-01\-24T18\:05\:47 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-s2 | string |  |   2023\-01\-24T18\:05\:47 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-served\-by | string |  |   cache\-iad\-kcgs7200042\-IAD, cache\-bfi\-krnt7300086\-BFI 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-source\-length | string |  |   4054 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-transaction\-id | string |  |   e90b91ea84264 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-tw\-cdn | string |  |   FT 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-ua\-compatible | string |  |   IE=Edge 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders\.x\-xss\-protection | string |  |   1; mode=block 
action\_result\.data\.\*\.HTTP\.\*\.ResponseSize | numeric |  |  
action\_result\.data\.\*\.HTTP\.\*\.Source\.\*\.IP | string |  |  
action\_result\.data\.\*\.HTTP\.\*\.Source\.\*\.Port | numeric |  |  
action\_result\.data\.\*\.HTTP\.\*\.Source\.IP | string |  |  
action\_result\.data\.\*\.HTTP\.\*\.Source\.Port | numeric |  |  
action\_result\.data\.\*\.HTTP\.\*\.StatusCode | numeric |  |  
action\_result\.data\.\*\.HTTP\.\*\.TotalSize | numeric |  |  
action\_result\.data\.\*\.HTTP\.\*\.URL | string |  |  
action\_result\.data\.\*\.HTTP\.\*\.UserAgent | string |  |  
action\_result\.data\.\*\.HTTP\.\*\.UserAgent | string |  |  
action\_result\.data\.\*\.Hosts\.\*\.ASN | numeric |  |  
action\_result\.data\.\*\.Hosts\.\*\.City | string |  |  
action\_result\.data\.\*\.Hosts\.\*\.Country | string |  |  
action\_result\.data\.\*\.Hosts\.\*\.Engines | string |  |  
action\_result\.data\.\*\.Hosts\.\*\.Hostname | string |  |   c35\.qbo\.intuit\.com 
action\_result\.data\.\*\.Hosts\.\*\.Houstname | string |  |  
action\_result\.data\.\*\.Hosts\.\*\.IP | string |  |  
action\_result\.data\.\*\.Hosts\.\*\.Organization | string |  |  
action\_result\.data\.\*\.Hosts\.\*\.ResourceTaskReferences\.\*\.ResourceKey | string |  |   1 
action\_result\.data\.\*\.Hosts\.\*\.ResourceTaskReferences\.\*\.TaskKey | string |  |   3 
action\_result\.data\.\*\.Images\.\*\.ArtifactPath | string |  |  
action\_result\.data\.\*\.Images\.\*\.DetectedObjects | string |  |  
action\_result\.data\.\*\.Images\.\*\.ImageHashes | string |  |  
action\_result\.data\.\*\.Images\.\*\.ImageHashes\.ImageAvgHash | string |  |   1818181818000000 
action\_result\.data\.\*\.Images\.\*\.ImageHashes\.ImageDhash | string |  |   b2b2b2b2b24c3001 
action\_result\.data\.\*\.Images\.\*\.ImageHashes\.ImagePhash | string |  |   88dd227722772277 
action\_result\.data\.\*\.Images\.\*\.Resource | string |  |  
action\_result\.data\.\*\.Images\.\*\.ResourceTaskReferences\.\*\.ResourceKey | string |  |   0 
action\_result\.data\.\*\.Images\.\*\.ResourceTaskReferences\.\*\.TaskKey | string |  |   1 
action\_result\.data\.\*\.Images\.\*\.Type | string |  |  
action\_result\.data\.\*\.Logs | string |  |  
action\_result\.data\.\*\.MalwareConfigs | string |  |  
action\_result\.data\.\*\.MalwareFamilies | string |  |  
action\_result\.data\.\*\.MitreAttacks | string |  |  
action\_result\.data\.\*\.MitreAttacks\.\*\.Engines | string |  |  
action\_result\.data\.\*\.MitreAttacks\.\*\.ID | string |  |  
action\_result\.data\.\*\.MitreAttacks\.\*\.SubTechnique | string |  |  
action\_result\.data\.\*\.MitreAttacks\.\*\.Tactic | string |  |  
action\_result\.data\.\*\.MitreAttacks\.\*\.Technique | string |  |  
action\_result\.data\.\*\.Mutexes | string |  |  
action\_result\.data\.\*\.Mutexes\.\*\.Engines | string |  |  
action\_result\.data\.\*\.Mutexes\.\*\.Name | string |  |  
action\_result\.data\.\*\.Network | string |  |  
action\_result\.data\.\*\.Network\.\*\.Destination\.\*\.IP | string |  |  
action\_result\.data\.\*\.Network\.\*\.Destination\.\*\.Port | numeric |  |  
action\_result\.data\.\*\.Network\.\*\.Length | numeric |  |  
action\_result\.data\.\*\.Network\.\*\.Protocol | string |  |  
action\_result\.data\.\*\.Network\.\*\.Service | string |  |  
action\_result\.data\.\*\.Network\.\*\.Source\.\*\.IP | string |  |  
action\_result\.data\.\*\.Network\.\*\.Source\.\*\.Port | numeric |  |  
action\_result\.data\.\*\.PhishedBrands | string |  |  
action\_result\.data\.\*\.Processes | string |  |  
action\_result\.data\.\*\.Processes\.\*\.Details\.\*\.Calls | string |  |  
action\_result\.data\.\*\.Processes\.\*\.Details\.Arguements | string |  |  
action\_result\.data\.\*\.Processes\.\*\.Details\.Environment\.\*\.CommandLine | string |  |  
action\_result\.data\.\*\.Processes\.\*\.Details\.Environment\.\*\.ComputerName | string |  |  
action\_result\.data\.\*\.Processes\.\*\.Details\.Environment\.\*\.InstallDate | numeric |  |  
action\_result\.data\.\*\.Processes\.\*\.Details\.Environment\.\*\.MachineGUID | string |  |  
action\_result\.data\.\*\.Processes\.\*\.Details\.Environment\.\*\.MainExeBase | string |  |  
action\_result\.data\.\*\.Processes\.\*\.Details\.Environment\.\*\.MainExeSize | string |  |  
action\_result\.data\.\*\.Processes\.\*\.Details\.Environment\.\*\.OSMajor | numeric |  |  
action\_result\.data\.\*\.Processes\.\*\.Details\.Environment\.\*\.OSMinor | numeric |  |  
action\_result\.data\.\*\.Processes\.\*\.Details\.Environment\.\*\.ProductName | string |  |  
action\_result\.data\.\*\.Processes\.\*\.Details\.Environment\.\*\.RegisteredOrganization | string |  |  
action\_result\.data\.\*\.Processes\.\*\.Details\.Environment\.\*\.RegisteredOwner | string |  |  
action\_result\.data\.\*\.Processes\.\*\.Details\.Environment\.\*\.SystemVolumeGUID | string |  |  
action\_result\.data\.\*\.Processes\.\*\.Details\.Environment\.\*\.SystemVolumeSerialNumber | string |  |  
action\_result\.data\.\*\.Processes\.\*\.Details\.Environment\.\*\.TempPath | string |  |  
action\_result\.data\.\*\.Processes\.\*\.Details\.Environment\.\*\.UserName | string |  |  
action\_result\.data\.\*\.Processes\.\*\.Details\.Environment\.\*\.WindowsPath | string |  |  
action\_result\.data\.\*\.Processes\.\*\.Details\.Environment\.\*\.is\_success | string |  |  
action\_result\.data\.\*\.Processes\.\*\.Details\.Environment\.\*\.retval | numeric |  |  
action\_result\.data\.\*\.Processes\.\*\.Details\.Threads | string |  |  
action\_result\.data\.\*\.Processes\.\*\.Name | string |  |  
action\_result\.data\.\*\.Processes\.\*\.PID | numeric |  |  
action\_result\.data\.\*\.Processes\.\*\.PPID | numeric |  |  
action\_result\.data\.\*\.Processes\.\*\.Path | string |  |  
action\_result\.data\.\*\.RegistryKeys | string |  |  
action\_result\.data\.\*\.Registrykeys\.\*\.Action | string |  |  
action\_result\.data\.\*\.Registrykeys\.\*\.Engines | string |  |  
action\_result\.data\.\*\.Registrykeys\.\*\.Name | string |  |  
action\_result\.data\.\*\.ResourceMap\.0\.ID | string |  |   c6e29c54\-ca84\-4368\-8af6\-38edc2c8398e 
action\_result\.data\.\*\.ResourceMap\.0\.Name | string |  |   https\://boomerangdairysandbedding\.com/wp\-includes/fonts/QuickB2022/ 
action\_result\.data\.\*\.ResourceMap\.0\.Type | string |  |   URL 
action\_result\.data\.\*\.ResourceMap\.1\.ID | string |  |   d7d53778\-8ec3\-405a\-9ec2\-9e0a5b998913 
action\_result\.data\.\*\.ResourceMap\.1\.Name | string |  |   https\://c35\.qbo\.intuit\.com/c35/v1975\.230/0/extrequest/login/recover?source=login&locale=en\_CA 
action\_result\.data\.\*\.ResourceMap\.1\.Type | string |  |   URL 
action\_result\.data\.\*\.ResourceMap\.2\.ID | string |  |   9ce6e5cc\-7836\-4134\-8aed\-874e357696f4 
action\_result\.data\.\*\.ResourceMap\.2\.Name | string |  |   https\://www\.malwarebytes\.com/browserguard 
action\_result\.data\.\*\.ResourceMap\.2\.Type | string |  |   URL 
action\_result\.data\.\*\.ResourceMap\.3\.ID | string |  |   b56c03a9\-7bd1\-406f\-be43\-924447b3dcf7 
action\_result\.data\.\*\.ResourceMap\.3\.Name | string |  |   http\://hosts\-file\.net/ 
action\_result\.data\.\*\.ResourceMap\.3\.Type | string |  |   URL 
action\_result\.data\.\*\.ResourceMap\.4\.ID | string |  |   fe667a66\-a123\-4b0d\-8486\-ea0ef6796902 
action\_result\.data\.\*\.ResourceMap\.4\.Name | string |  |   https\://www\.rsaconference\.com/usa 
action\_result\.data\.\*\.ResourceMap\.4\.Type | string |  |   URL 
action\_result\.data\.\*\.SavedArtifacts | string |  |  
action\_result\.data\.\*\.SavedArtifacts\.\*\.ArtifactPath | string |  |   2022\-11\-23/lab/63572265\-c5ae\-402f\-9fc1\-6c90547482ee/8551cf5b\-2095\-426f\-85ec\-b8552c17bd53/7507bfcf1693c6a8f3f69d15121dc14aeb8dc9e301bac6568152fb50210e36fe\.sample\.gz 
action\_result\.data\.\*\.SavedArtifacts\.\*\.Name | string |  |   7507bfcf1693c6a8f3f6921dc14aeb8dc9e301bac6568152fb50210e36fe 
action\_result\.data\.\*\.SavedArtifacts\.\*\.ResourceTaskReferences\.\*\.ResourceKey | string |  |   1 
action\_result\.data\.\*\.SavedArtifacts\.\*\.ResourceTaskReferences\.\*\.TaskKey | string |  |   3 
action\_result\.data\.\*\.SavedArtifacts\.\*\.Type | string |  |   web\_artifact 
action\_result\.data\.\*\.Score | numeric |  |  
action\_result\.data\.\*\.Screenshots\.\*\.ArtifactPath | string |  |  
action\_result\.data\.\*\.Screenshots\.\*\.Engines | string |  |  
action\_result\.data\.\*\.Screenshots\.\*\.ImageHashes | string |  |  
action\_result\.data\.\*\.Screenshots\.\*\.ImageHashes\.ImageAvgHash | string |  |   183c1c3c18000000 
action\_result\.data\.\*\.Screenshots\.\*\.ImageHashes\.ImageDhash | string |  |   b2b2b2b2320c2000 
action\_result\.data\.\*\.Screenshots\.\*\.ImageHashes\.ImagePhash | string |  |   9999666666cc3363 
action\_result\.data\.\*\.Screenshots\.\*\.Resource | string |  |  
action\_result\.data\.\*\.Screenshots\.\*\.ResourceTaskReferences\.\*\.ResourceKey | string |  |   1 
action\_result\.data\.\*\.Screenshots\.\*\.ResourceTaskReferences\.\*\.TaskKey | string |  |   3 
action\_result\.data\.\*\.Screenshots\.\*\.URI | string |  |  
action\_result\.data\.\*\.StartTime | string |  |  
action\_result\.data\.\*\.Strings\.\*\.Details\.Source | string |  |   HTTP response content\: https\://c35\.qbo\.intuit\.com/c35/v1975\.230/0/extrequest/login/recover?source=login&locale=en\_CA 
action\_result\.data\.\*\.Strings\.\*\.Details\.Type | string |  |   http\_response 
action\_result\.data\.\*\.Strings\.\*\.Details\.URL | string |  |   https\://c35\.qbo\.intuit\.com/c35/v1975\.230/0/extrequest/login/recover?source=login&locale=en\_CA 
action\_result\.data\.\*\.Strings\.\*\.Engines | string |  |  
action\_result\.data\.\*\.Strings\.\*\.ResourceTaskReferences\.\*\.ResourceKey | string |  |   1 
action\_result\.data\.\*\.Strings\.\*\.ResourceTaskReferences\.\*\.TaskKey | string |  |   3 
action\_result\.data\.\*\.Strings\.\*\.String | string |  |  
action\_result\.data\.\*\.TLS | string |  |  
action\_result\.data\.\*\.TLS\.\*\.Destination\.IP | string |  |  
action\_result\.data\.\*\.TLS\.\*\.Destination\.Port | numeric |  |  
action\_result\.data\.\*\.TLS\.\*\.Details\.JA3 | string |  |  
action\_result\.data\.\*\.TLS\.\*\.Engines | string |  |  
action\_result\.data\.\*\.TLS\.\*\.Fingerprint | numeric |  |  
action\_result\.data\.\*\.TLS\.\*\.Issuer | string |  |  
action\_result\.data\.\*\.TLS\.\*\.Source\.IP | string |  |  
action\_result\.data\.\*\.TLS\.\*\.Source\.Port | numeric |  |  
action\_result\.data\.\*\.TLS\.\*\.Subject | string |  |  
action\_result\.data\.\*\.TaskMap\.0\.Engine | string |  |   url\_reputation 
action\_result\.data\.\*\.TaskMap\.0\.ID | string |  |   1ce8132e\-87cf\-43a5\-8076\-dce647ff2890 
action\_result\.data\.\*\.TaskMap\.0\.Score | numeric |  |  
action\_result\.data\.\*\.TaskMap\.1\.Engine | string |  |   web\_analyzer 
action\_result\.data\.\*\.TaskMap\.1\.ID | string |  |   8551cf5b\-2095\-426f\-85ec\-b8552c17bd53 
action\_result\.data\.\*\.TaskMap\.1\.Score | numeric |  |   1 
action\_result\.data\.\*\.TaskMap\.2\.Engine | string |  |   url\_reputation 
action\_result\.data\.\*\.TaskMap\.2\.ID | string |  |   c9a0139f\-9803\-4d77\-816c\-df7403d7d7bc 
action\_result\.data\.\*\.TaskMap\.2\.Score | numeric |  |   0.4 
action\_result\.data\.\*\.TaskMap\.3\.Engine | string |  |   web\_analyzer 
action\_result\.data\.\*\.TaskMap\.3\.ID | string |  |   cc46644a\-b842\-4361\-acce\-2e9febef46be 
action\_result\.data\.\*\.TaskMap\.3\.Score | numeric |  |  
action\_result\.data\.\*\.TaskMap\.4\.Engine | string |  |   web\_analyzer 
action\_result\.data\.\*\.TaskMap\.4\.ID | string |  |   837b4eaf\-8e6d\-4e1f\-92fd\-4e13c873f066 
action\_result\.data\.\*\.TaskMap\.4\.Score | numeric |  |  
action\_result\.data\.\*\.TaskMap\.5\.Engine | string |  |   url\_reputation 
action\_result\.data\.\*\.TaskMap\.5\.ID | string |  |   8bea47e8\-98ba\-4f11\-af18\-d2be3040f1af 
action\_result\.data\.\*\.TaskMap\.5\.Score | numeric |  |  
action\_result\.data\.\*\.TaskMap\.6\.Engine | string |  |   web\_analyzer 
action\_result\.data\.\*\.TaskMap\.6\.ID | string |  |   9c04d6c8\-c749\-4069\-a48c\-e5d85e42607f 
action\_result\.data\.\*\.TaskMap\.6\.Score | numeric |  |  
action\_result\.data\.\*\.TaskMap\.7\.Engine | string |  |   web\_analyzer 
action\_result\.data\.\*\.TaskMap\.7\.ID | string |  |   a1ed2738\-4184\-49c0\-9710\-44de7ffa247c 
action\_result\.data\.\*\.TaskMap\.7\.Score | numeric |  |  
action\_result\.data\.\*\.TaskMap\.8\.Engine | string |  |   url\_reputation 
action\_result\.data\.\*\.TaskMap\.8\.ID | string |  |   c9add79d\-abd4\-4e80\-bef5\-131bf5807f0f 
action\_result\.data\.\*\.TaskMap\.8\.Score | numeric |  |  
action\_result\.data\.\*\.TaskMap\.9\.Engine | string |  |   url\_reputation 
action\_result\.data\.\*\.TaskMap\.9\.ID | string |  |   f3ec2a9f\-6759\-47ef\-8ce7\-a2e7f215f9aa 
action\_result\.data\.\*\.TaskMap\.9\.Score | numeric |  |  
action\_result\.data\.\*\.URLs\.\*\.Context | string |  |  
action\_result\.data\.\*\.URLs\.\*\.Engines | string |  |  
action\_result\.data\.\*\.URLs\.\*\.LinkText | string |  |  
action\_result\.data\.\*\.URLs\.\*\.ResourceTaskReferences\.\*\.ResourceKey | string |  |   1 
action\_result\.data\.\*\.URLs\.\*\.ResourceTaskReferences\.\*\.TaskKey | string |  |   3 
action\_result\.data\.\*\.URLs\.\*\.URL | string |  |  
action\_result\.data\.\*\.Verdict | string |  |  
action\_result\.data\.\*\.Version | string |  |  
action\_result\.data\.\*\.WhoisResults\.\*\.Address | string |  |  
action\_result\.data\.\*\.WhoisResults\.\*\.City | string |  |  
action\_result\.data\.\*\.WhoisResults\.\*\.Country | string |  |  
action\_result\.data\.\*\.WhoisResults\.\*\.CreatedAt | string |  |  
action\_result\.data\.\*\.WhoisResults\.\*\.DNSSec | string |  |  
action\_result\.data\.\*\.WhoisResults\.\*\.DomainName | string |  |  
action\_result\.data\.\*\.WhoisResults\.\*\.Emails | string |  |  
action\_result\.data\.\*\.WhoisResults\.\*\.Engines | string |  |  
action\_result\.data\.\*\.WhoisResults\.\*\.ExpiresAt | string |  |  
action\_result\.data\.\*\.WhoisResults\.\*\.Name | string |  |  
action\_result\.data\.\*\.WhoisResults\.\*\.NameServers | string |  |  
action\_result\.data\.\*\.WhoisResults\.\*\.Org | string |  |  
action\_result\.data\.\*\.WhoisResults\.\*\.Registrar | string |  |  
action\_result\.data\.\*\.WhoisResults\.\*\.ResourceTaskReferences\.\*\.ResourceKey | string |  |   0 
action\_result\.data\.\*\.WhoisResults\.\*\.ResourceTaskReferences\.\*\.TaskKey | string |  |   1 
action\_result\.data\.\*\.WhoisResults\.\*\.State | string |  |  
action\_result\.data\.\*\.WhoisResults\.\*\.UpdatedAt | string |  |  
action\_result\.data\.\*\.WhoisResults\.\*\.WhoisServer | string |  |  
action\_result\.data\.\*\.WhoisResults\.\*\.ZipCode | string |  |  
action\_result\.summary | string |  |  
action\_result\.message | string |  |   Job normal forensics retrieved 
summary\.total\_objects | numeric |  |   1 
summary\.total\_objects\_successful | numeric |  |   1   

## action: 'get job summary'
Get a job summary

Type: **investigate**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**job\_id** |  required  | Job id of the job summary you want to fetch | string |  `splunk attack analyzer job id` 
**wait** |  optional  | Wait for job to finish before returning results | boolean | 
**timeout** |  optional  | Maximum time \(in minutes\) to wait for job to be complete | numeric | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action\_result\.status | string |  |   success  failed 
action\_result\.parameter\.job\_id | string |  `splunk attack analyzer job id`  |   63572265\-c5ae\-402f\-9fc1\-6c90547482ee 
action\_result\.parameter\.timeout | numeric |  |   30 
action\_result\.parameter\.wait | boolean |  |   True  False 
action\_result\.data | string |  |  
action\_result\.data\.\*\.APIKey | string |  |  
action\_result\.data\.\*\.APIKey\.\*\.ID | string |  |  
action\_result\.data\.\*\.APIKey\.\*\.Label | string |  |  
action\_result\.data\.\*\.APIKey\.ID | string |  |   e2b3f970\-3a8c\-46bd\-ac13\-e2361984d921 
action\_result\.data\.\*\.APIKey\.Label | string |  |   general key 
action\_result\.data\.\*\.APIKeyID | string |  |  
action\_result\.data\.\*\.CompletedAt | string |  |  
action\_result\.data\.\*\.CreatedAt | string |  |  
action\_result\.data\.\*\.DisplayScore | numeric |  |  
action\_result\.data\.\*\.ForensicsPath | string |  |  
action\_result\.data\.\*\.ID | string |  |   63572265\-c5ae\-402f\-9fc1\-6c90547482ee 
action\_result\.data\.\*\.Labels\.\*\.ID | numeric |  |  
action\_result\.data\.\*\.Labels\.\*\.Jobs | string |  |  
action\_result\.data\.\*\.Labels\.\*\.Type | string |  |  
action\_result\.data\.\*\.Labels\.\*\.Value | string |  |  
action\_result\.data\.\*\.Parameters | string |  |  
action\_result\.data\.\*\.Parameters\.\*\.Name | string |  |   decode\_rewritten\_urls 
action\_result\.data\.\*\.Parameters\.\*\.Value | string |  |   true 
action\_result\.data\.\*\.Priority | numeric |  |  
action\_result\.data\.\*\.Profile | string |  |  
action\_result\.data\.\*\.RequestedEngines | string |  |  
action\_result\.data\.\*\.ResourceCount | numeric |  |  
action\_result\.data\.\*\.ResourceTree | string |  |  
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.Children\.\*\.Children\.\*\.CreatedAt | string |  |   2023\-01\-31T10\:51\:32\.067Z 
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.Children\.\*\.Children\.\*\.DisplayScore | numeric |  |  
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.Children\.\*\.Children\.\*\.FileMetadata\.FileType | string |  |  
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.Children\.\*\.Children\.\*\.FileMetadata\.IsEncrypted | string |  |  
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.Children\.\*\.Children\.\*\.FileMetadata\.MD5 | string |  |  
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.Children\.\*\.Children\.\*\.FileMetadata\.MimeType | string |  |  
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.Children\.\*\.Children\.\*\.FileMetadata\.SHA256 | string |  |  
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.Children\.\*\.Children\.\*\.FileMetadata\.Size | numeric |  |  
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.Children\.\*\.Children\.\*\.ID | string |  |   9bcc64e3\-60e8\-4aef\-965c\-73a7a90427d1 
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.Children\.\*\.Children\.\*\.InjectionMetadata\.AddedBecause | string |  |   click 
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.Children\.\*\.Children\.\*\.InjectionMetadata\.AddedBy | string |  |   web\_analyzer 
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.Children\.\*\.Children\.\*\.JobID | string |  |   b29f669c\-edde\-4bf2\-b720\-3dd456c389c6 
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.Children\.\*\.Children\.\*\.Location | string |  |   https\://edge\.com/addons/detail/malwarebytes\-browser\-guar/bojobppfploabceghnmlahpoonbcbacn 
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.Children\.\*\.Children\.\*\.Name | string |  |   https\://edge\.com/addons/detail/malwarebytes\-browser\-guar/bojobppfploabceghnmlahpoonbcbacn 
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.Children\.\*\.Children\.\*\.ParentID | string |  |   9ce6e5cc\-7836\-4134\-8aed\-874e357696f4 
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.Children\.\*\.Children\.\*\.Score | numeric |  |  
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.Children\.\*\.Children\.\*\.Type | string |  |   URL 
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.Children\.\*\.CreatedAt | string |  |   2023\-01\-31T10\:51\:32\.007Z 
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.Children\.\*\.DisplayScore | numeric |  |  
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.Children\.\*\.FileMetadata\.FileType | string |  |  
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.Children\.\*\.FileMetadata\.IsEncrypted | string |  |  
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.Children\.\*\.FileMetadata\.MD5 | string |  |  
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.Children\.\*\.FileMetadata\.MimeType | string |  |  
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.Children\.\*\.FileMetadata\.SHA256 | string |  |  
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.Children\.\*\.FileMetadata\.Size | numeric |  |  
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.Children\.\*\.ID | string |  |   9ce6e5cc\-7836\-4134\-8aed\-874e357696f4 
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.Children\.\*\.InjectionMetadata\.AddedBecause | string |  |   HTTPRedirect 
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.Children\.\*\.InjectionMetadata\.AddedBy | string |  |   web\_analyzer 
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.Children\.\*\.JobID | string |  |   b29f669c\-edde\-4bf2\-b720\-3dd456c389c6 
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.Children\.\*\.Location | string |  |   https\://www\.malwarebytes\.com/browserguard 
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.Children\.\*\.Name | string |  |   https\://www\.malwarebytes\.com/browserguard 
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.Children\.\*\.ParentID | string |  |   1ff929ab\-cfc1\-49d2\-83da\-2cae20ed51f2 
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.Children\.\*\.Score | numeric |  |  
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.Children\.\*\.Type | string |  |   URL 
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.CreatedAt | string |  |   2022\-11\-23T00\:45\:27\.441Z 
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.DisplayScore | numeric |  |  
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.FileMetadata\.FileType | string |  |  
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.FileMetadata\.IsEncrypted | string |  |  
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.FileMetadata\.MD5 | string |  |  
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.FileMetadata\.MimeType | string |  |  
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.FileMetadata\.SHA256 | string |  |  
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.FileMetadata\.Size | numeric |  |  
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.ID | string |  |   d7d53778\-8ec3\-405a\-9ec2\-9e0a5b998913 
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.InjectionMetadata\.AddedBecause | string |  |   click 
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.InjectionMetadata\.AddedBy | string |  |   web\_analyzer 
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.JobID | string |  |   63572265\-c5ae\-402f\-9fc1\-6c90547482ee 
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.Location | string |  |   https\://c35\.qbo\.intuit\.com/c35/v1975\.230/0/extrequest/login/recover?source=login&locale=en\_CA 
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.Name | string |  |   https\://c35\.qbo\.intuit\.com/c35/v1975\.230/0/extrequest/login/recover?source=login&locale=en\_CA 
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.ParentID | string |  |   c6e29c54\-ca84\-4368\-8af6\-38edc2c8398e 
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.Score | numeric |  |  
action\_result\.data\.\*\.ResourceTree\.Children\.\*\.Type | string |  |   URL 
action\_result\.data\.\*\.ResourceTree\.CreatedAt | string |  |   2022\-11\-23T00\:44\:12\.857Z 
action\_result\.data\.\*\.ResourceTree\.DisplayScore | numeric |  |   100 
action\_result\.data\.\*\.ResourceTree\.FileMetadata\.FileType | string |  |  
action\_result\.data\.\*\.ResourceTree\.FileMetadata\.IsEncrypted | string |  |  
action\_result\.data\.\*\.ResourceTree\.FileMetadata\.MD5 | string |  |  
action\_result\.data\.\*\.ResourceTree\.FileMetadata\.MimeType | string |  |  
action\_result\.data\.\*\.ResourceTree\.FileMetadata\.SHA256 | string |  |  
action\_result\.data\.\*\.ResourceTree\.FileMetadata\.Size | numeric |  |  
action\_result\.data\.\*\.ResourceTree\.ID | string |  |   c6e29c54\-ca84\-4368\-8af6\-38edc2c8398e 
action\_result\.data\.\*\.ResourceTree\.InjectionMetadata\.AddedBecause | string |  |  
action\_result\.data\.\*\.ResourceTree\.InjectionMetadata\.AddedBy | string |  |  
action\_result\.data\.\*\.ResourceTree\.JobID | string |  |   63572265\-c5ae\-402f\-9fc1\-6c90547482ee 
action\_result\.data\.\*\.ResourceTree\.Location | string |  |   https\://boomerangdairysandbedding\.com/wp\-includes/fonts/QuickB2022/ 
action\_result\.data\.\*\.ResourceTree\.Name | string |  |   https\://boomerangdairysandbedding\.com/wp\-includes/fonts/QuickB2022/ 
action\_result\.data\.\*\.ResourceTree\.ParentID | string |  |  
action\_result\.data\.\*\.ResourceTree\.Score | numeric |  |   1 
action\_result\.data\.\*\.ResourceTree\.Type | string |  |   URL 
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.Children\.\*\.Children\.\*\.CreatedAt | string |  |   2023\-01\-31T10\:51\:32\.067Z 
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.Children\.\*\.Children\.\*\.DisplayScore | numeric |  |  
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.Children\.\*\.Children\.\*\.FileMetadata\.FileType | string |  |  
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.Children\.\*\.Children\.\*\.FileMetadata\.IsEncrypted | string |  |  
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.Children\.\*\.Children\.\*\.FileMetadata\.MD5 | string |  |  
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.Children\.\*\.Children\.\*\.FileMetadata\.MimeType | string |  |  
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.Children\.\*\.Children\.\*\.FileMetadata\.SHA256 | string |  |  
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.Children\.\*\.Children\.\*\.FileMetadata\.Size | numeric |  |  
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.Children\.\*\.Children\.\*\.ID | string |  |   9bcc64e3\-60e8\-4aef\-965c\-73a7a90427d1 
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.Children\.\*\.Children\.\*\.InjectionMetadata\.AddedBecause | string |  |   click 
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.Children\.\*\.Children\.\*\.InjectionMetadata\.AddedBy | string |  |   web\_analyzer 
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.Children\.\*\.Children\.\*\.JobID | string |  |   b29f669c\-edde\-4bf2\-b720\-3dd456c389c6 
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.Children\.\*\.Children\.\*\.Location | string |  |   https\://edge\.com/addons/detail/malwarebytes\-browser\-guar/bojobppfploabceghnmlahpoonbcbacn 
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.Children\.\*\.Children\.\*\.Name | string |  |   https\://edge\.com/addons/detail/malwarebytes\-browser\-guar/bojobppfploabceghnmlahpoonbcbacn 
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.Children\.\*\.Children\.\*\.ParentID | string |  |   9ce6e5cc\-7836\-4134\-8aed\-874e357696f4 
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.Children\.\*\.Children\.\*\.Score | numeric |  |  
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.Children\.\*\.Children\.\*\.Type | string |  |   URL 
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.Children\.\*\.CreatedAt | string |  |   2023\-01\-31T10\:51\:32\.067Z 
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.Children\.\*\.DisplayScore | numeric |  |  
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.Children\.\*\.FileMetadata\.FileType | string |  |  
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.Children\.\*\.FileMetadata\.IsEncrypted | string |  |  
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.Children\.\*\.FileMetadata\.MD5 | string |  |  
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.Children\.\*\.FileMetadata\.MimeType | string |  |  
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.Children\.\*\.FileMetadata\.SHA256 | string |  |  
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.Children\.\*\.FileMetadata\.Size | numeric |  |  
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.Children\.\*\.ID | string |  |   9bcc64e3\-60e8\-4aef\-965c\-73a7a90427d1 
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.Children\.\*\.InjectionMetadata\.AddedBecause | string |  |   click 
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.Children\.\*\.InjectionMetadata\.AddedBy | string |  |   web\_analyzer 
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.Children\.\*\.JobID | string |  |   b29f669c\-edde\-4bf2\-b720\-3dd456c389c6 
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.Children\.\*\.Location | string |  |   https\://edge\.com/addons/detail/malwarebytes\-browser\-guar/bojobppfploabceghnmlahpoonbcbacn 
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.Children\.\*\.Name | string |  |   https\://edge\.com/addons/detail/malwarebytes\-browser\-guar/bojobppfploabceghnmlahpoonbcbacn 
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.Children\.\*\.ParentID | string |  |   9ce6e5cc\-7836\-4134\-8aed\-874e357696f4 
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.Children\.\*\.Score | numeric |  |  
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.Children\.\*\.Type | string |  |   URL 
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.CreatedAt | string |  |   2022\-11\-23T00\:45\:27\.441Z 
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.DisplayScore | numeric |  |  
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.FileMetadata\.FileType | string |  |  
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.FileMetadata\.IsEncrypted | string |  |  
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.FileMetadata\.MD5 | string |  |  
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.FileMetadata\.MimeType | string |  |  
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.FileMetadata\.SHA256 | string |  |  
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.FileMetadata\.Size | numeric |  |  
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.ID | string |  |   d7d53778\-8ec3\-405a\-9ec2\-9e0a5b998913 
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.InjectionMetadata\.AddedBecause | string |  |   click 
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.InjectionMetadata\.AddedBy | string |  |   web\_analyzer 
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.JobID | string |  |   63572265\-c5ae\-402f\-9fc1\-6c90547482ee 
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.Location | string |  |   https\://c35\.qbo\.intuit\.com/c35/v1975\.230/0/extrequest/login/recover?source=login&locale=en\_CA 
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.Name | string |  |   https\://c35\.qbo\.intuit\.com/c35/v1975\.230/0/extrequest/login/recover?source=login&locale=en\_CA 
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.ParentID | string |  |   c6e29c54\-ca84\-4368\-8af6\-38edc2c8398e 
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.Score | numeric |  |  
action\_result\.data\.\*\.Resources\.\*\.Children\.\*\.Type | string |  |   URL 
action\_result\.data\.\*\.Resources\.\*\.CreatedAt | string |  |  
action\_result\.data\.\*\.Resources\.\*\.DisplayScore | numeric |  |  
action\_result\.data\.\*\.Resources\.\*\.FileMetadata\.\*\.FileType | string |  |  
action\_result\.data\.\*\.Resources\.\*\.FileMetadata\.\*\.IsEncrypted | string |  |  
action\_result\.data\.\*\.Resources\.\*\.FileMetadata\.\*\.MD5 | string |  |  
action\_result\.data\.\*\.Resources\.\*\.FileMetadata\.\*\.MimeType | string |  |  
action\_result\.data\.\*\.Resources\.\*\.FileMetadata\.\*\.SHA256 | string |  |  
action\_result\.data\.\*\.Resources\.\*\.FileMetadata\.\*\.Size | numeric |  |  
action\_result\.data\.\*\.Resources\.\*\.FileMetadata\.FileType | string |  |  
action\_result\.data\.\*\.Resources\.\*\.FileMetadata\.IsEncrypted | string |  |  
action\_result\.data\.\*\.Resources\.\*\.FileMetadata\.MD5 | string |  |  
action\_result\.data\.\*\.Resources\.\*\.FileMetadata\.MimeType | string |  |  
action\_result\.data\.\*\.Resources\.\*\.FileMetadata\.SHA256 | string |  |  
action\_result\.data\.\*\.Resources\.\*\.FileMetadata\.Size | numeric |  |  
action\_result\.data\.\*\.Resources\.\*\.ID | string |  |  
action\_result\.data\.\*\.Resources\.\*\.InjectionMetadata\.\*\.AddedBecause | string |  |  
action\_result\.data\.\*\.Resources\.\*\.InjectionMetadata\.\*\.AddedBy | string |  |  
action\_result\.data\.\*\.Resources\.\*\.InjectionMetadata\.AddedBecause | string |  |  
action\_result\.data\.\*\.Resources\.\*\.InjectionMetadata\.AddedBy | string |  |  
action\_result\.data\.\*\.Resources\.\*\.JobID | string |  |  
action\_result\.data\.\*\.Resources\.\*\.Location | string |  |  
action\_result\.data\.\*\.Resources\.\*\.Name | string |  |  
action\_result\.data\.\*\.Resources\.\*\.ParentID | string |  |  
action\_result\.data\.\*\.Resources\.\*\.Score | numeric |  |  
action\_result\.data\.\*\.Resources\.\*\.Type | string |  |  
action\_result\.data\.\*\.Score | numeric |  |  
action\_result\.data\.\*\.Sharing\.\*\.ShareToken | string |  |  
action\_result\.data\.\*\.Sharing\.\*\.SharedAt | string |  |  
action\_result\.data\.\*\.Sharing\.\*\.SharedBy | string |  |  
action\_result\.data\.\*\.Sharing\.ShareToken | string |  |  
action\_result\.data\.\*\.Sharing\.SharedAt | string |  |  
action\_result\.data\.\*\.Sharing\.SharedBy | string |  |  
action\_result\.data\.\*\.StartedAt | string |  |  
action\_result\.data\.\*\.State | string |  |  
action\_result\.data\.\*\.Submission\.MD5 | string |  |  
action\_result\.data\.\*\.Submission\.Name | string |  |   https\://boomerangdairysandbedding\.com/wp\-includes/fonts/QuickB2022/ 
action\_result\.data\.\*\.Submission\.SHA256 | string |  |  
action\_result\.data\.\*\.SubmissionSource | string |  |  
action\_result\.data\.\*\.Submissions\.\*\.MD5 | string |  |  
action\_result\.data\.\*\.Submissions\.\*\.Name | string |  |  
action\_result\.data\.\*\.Submissions\.\*\.SHA256 | string |  |  
action\_result\.data\.\*\.Tasks\.\*\.CreatedAt | string |  |  
action\_result\.data\.\*\.Tasks\.\*\.Engine | string |  |  
action\_result\.data\.\*\.Tasks\.\*\.ID | string |  |  
action\_result\.data\.\*\.Tasks\.\*\.Priority | numeric |  |  
action\_result\.data\.\*\.Tasks\.\*\.ResourceID | string |  |  
action\_result\.data\.\*\.Tasks\.\*\.Results\.\*\.Details | string |  |  
action\_result\.data\.\*\.Tasks\.\*\.Results\.\*\.Forensics\.\*\.Normalized | string |  |  
action\_result\.data\.\*\.Tasks\.\*\.Results\.\*\.Forensics\.\*\.Raw | string |  |  
action\_result\.data\.\*\.Tasks\.\*\.Results\.\*\.Score | numeric |  |  
action\_result\.data\.\*\.Tasks\.\*\.Results\.Details\.Engines\.apivoid\.\*\.Permalink | string |  |   https\://www\.urlvoid\.com/scan/boomerangdairysandbedding\.com/ 
action\_result\.data\.\*\.Tasks\.\*\.Results\.Details\.Engines\.apivoid\.\*\.ScanTime | string |  |   2022\-11\-23T00\:44\:14\.342421119Z 
action\_result\.data\.\*\.Tasks\.\*\.Results\.Details\.Engines\.apivoid\.\*\.Score | numeric |  |   0.4 
action\_result\.data\.\*\.Tasks\.\*\.Results\.Details\.Engines\.urlscanio\.\*\.Scans\.\*\.ScanTime | string |  |   2020\-12\-17T10\:25\:39\.434Z 
action\_result\.data\.\*\.Tasks\.\*\.Results\.Details\.Engines\.urlscanio\.\*\.Scans\.\*\.UUID | string |  |   7dd9cca2\-75c0\-43c8\-816d\-0fe5fafe6d7f 
action\_result\.data\.\*\.Tasks\.\*\.Results\.Details\.Engines\.urlscanio\.\*\.Score | numeric |  |  
action\_result\.data\.\*\.Tasks\.\*\.Results\.Details\.Engines\.urlscanio\.\*\.TotalScans | numeric |  |   6 
action\_result\.data\.\*\.Tasks\.\*\.Results\.Details\.NetworkEgress\.Endpoint | string |  |   d9cec4861bfb4c6a9137f984896c2447\.i8\.torguard\_t\_texas\_70\-125\-225\-207\_udp\.us\_residential\.vpn\.prod\-tf\:49505 
action\_result\.data\.\*\.Tasks\.\*\.Results\.Details\.NetworkEgress\.PublicIP | string |  |   70\.125\.225\.207 
action\_result\.data\.\*\.Tasks\.\*\.Results\.Details\.NetworkEgress\.Region | string |  |   us\_residential 
action\_result\.data\.\*\.Tasks\.\*\.Results\.Details\.NetworkEgress\.UserAgent | string |  |   Mozilla/5\.0 \(Windows NT 10\.0; Win64; x64\) AppleWebKit/537\.36 \(KHTML, like Gecko\) Chrome/101\.0\.4951\.67 Safari/537\.36 Edg/100\.0\.1185\.39 
action\_result\.data\.\*\.Tasks\.\*\.Results\.Details\.NetworkEgress\.UserAgentAlias | string |  |   default 
action\_result\.data\.\*\.Tasks\.\*\.Results\.Details\.RootTaskID | string |  |   8551cf5b\-2095\-426f\-85ec\-b8552c17bd53 
action\_result\.data\.\*\.Tasks\.\*\.Results\.Details\.Title | string |  |   QuickBooks Login \- Sign in to QuickBooks to manage your business 
action\_result\.data\.\*\.Tasks\.\*\.Results\.Details\.Whois\.Address | string |  |   3839 Road 160 
action\_result\.data\.\*\.Tasks\.\*\.Results\.Details\.Whois\.City | string |  |   Markham 
action\_result\.data\.\*\.Tasks\.\*\.Results\.Details\.Whois\.Country | string |  |   CA 
action\_result\.data\.\*\.Tasks\.\*\.Results\.Details\.Whois\.CreatedAt | string |  |   2012\-09\-20T17\:40\:47\+00\:00 
action\_result\.data\.\*\.Tasks\.\*\.Results\.Details\.Whois\.DNSSec | string |  |  
action\_result\.data\.\*\.Tasks\.\*\.Results\.Details\.Whois\.Details | string |  |  
action\_result\.data\.\*\.Tasks\.\*\.Results\.Details\.Whois\.DomainName | string |  |   boomerangdairysandbedding\.com 
action\_result\.data\.\*\.Tasks\.\*\.Results\.Details\.Whois\.Engines | string |  |  
action\_result\.data\.\*\.Tasks\.\*\.Results\.Details\.Whois\.ExpiresAt | string |  |   2023\-09\-20T17\:40\:47\+00\:00 
action\_result\.data\.\*\.Tasks\.\*\.Results\.Details\.Whois\.Name | string |  |   John Moses 
action\_result\.data\.\*\.Tasks\.\*\.Results\.Details\.Whois\.Org | string |  |   Private Registration 
action\_result\.data\.\*\.Tasks\.\*\.Results\.Details\.Whois\.Registrar | string |  |   BRANDON GRAY INTERNET SERVICES, INC\. DBA NAMEJUICE\.COM 
action\_result\.data\.\*\.Tasks\.\*\.Results\.Details\.Whois\.State | string |  |   ON 
action\_result\.data\.\*\.Tasks\.\*\.Results\.Details\.Whois\.Timestamp | string |  |  
action\_result\.data\.\*\.Tasks\.\*\.Results\.Details\.Whois\.UpdatedAt | string |  |   2022\-08\-31T18\:17\:28\+00\:00 
action\_result\.data\.\*\.Tasks\.\*\.Results\.Details\.Whois\.Verdict | string |  |  
action\_result\.data\.\*\.Tasks\.\*\.Results\.Details\.Whois\.WhoisServer | string |  |   whois\.namejuice\.com 
action\_result\.data\.\*\.Tasks\.\*\.Results\.Details\.Whois\.ZipCode | string |  |   unknown 
action\_result\.data\.\*\.Tasks\.\*\.Results\.DisplayScore | numeric |  |  
action\_result\.data\.\*\.Tasks\.\*\.Results\.Forensics\.Normalized | string |  |   normalized/2022\-11\-23/lab/63572265\-c5ae\-402f\-9fc1\-6c90547482ee/1ce8132e\-87cf\-43a5\-8076\-dce647ff2890/2b83ece5\-a1d4\-48a7\-8df3\-b706eec61287\.json\.gz 
action\_result\.data\.\*\.Tasks\.\*\.Results\.Forensics\.Raw | string |  |  
action\_result\.data\.\*\.Tasks\.\*\.Results\.Score | numeric |  |  
action\_result\.data\.\*\.Tasks\.\*\.StartedAt | string |  |  
action\_result\.data\.\*\.Tasks\.\*\.State | string |  |  
action\_result\.data\.\*\.Tasks\.\*\.StateText | string |  |  
action\_result\.data\.\*\.Tasks\.\*\.StateText | string |  |  
action\_result\.data\.\*\.Tasks\.\*\.UpdatedAt | string |  |  
action\_result\.data\.\*\.TenantID | string |  |  
action\_result\.data\.\*\.UpdatedAt | string |  |  
action\_result\.data\.\*\.Username | string |  |  
action\_result\.data\.\*\.Verdict | string |  |  
action\_result\.summary | string |  |  
action\_result\.summary\.JobID | string |  |   63572265\-c5ae\-402f\-9fc1\-6c90547482ee 
action\_result\.summary\.Score | numeric |  |   100 
action\_result\.summary\.Verdict | string |  |   phish 
action\_result\.message | string |  |   Jobid\: 63572265\-c5ae\-402f\-9fc1\-6c90547482ee, Score\: 100, Verdict\: phish 
summary\.total\_objects | numeric |  |   2 
summary\.total\_objects\_successful | numeric |  |   2   

## action: 'list recent jobs'
Get a list of recent jobs

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**limit** |  optional  | Number of jobs to fetch \(default\: 10\) | numeric | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action\_result\.status | string |  |   success  failed 
action\_result\.parameter\.limit | numeric |  |   100 
action\_result\.data | string |  |  
action\_result\.data\.\*\.\*\.APIKey | string |  |  
action\_result\.data\.\*\.\*\.APIKey\.ID | string |  |   e2b3f970\-3a8c\-46bd\-ac13\-e2361984d921 
action\_result\.data\.\*\.\*\.APIKey\.Label | string |  |   general key 
action\_result\.data\.\*\.\*\.APIKeyID | string |  |  
action\_result\.data\.\*\.\*\.CompletedAt | string |  |   2022\-11\-23T00\:45\:29\.544Z 
action\_result\.data\.\*\.\*\.CreatedAt | string |  |   2022\-11\-23T00\:44\:12\.855Z 
action\_result\.data\.\*\.\*\.DisplayScore | numeric |  |   100 
action\_result\.data\.\*\.\*\.ForensicsPath | string |  |   consolidated/2022\-11\-23/lab/63572265\-c5ae\-402f\-9fc1\-6c90547482ee/63572265\-c5ae\-402f\-9fc1\-6c90547482ee\.json\.gz 
action\_result\.data\.\*\.\*\.ID | string |  `splunk attack analyzer job id`  |   63572265\-c5ae\-402f\-9fc1\-6c90547482ee 
action\_result\.data\.\*\.\*\.Labels\.\*\.Type | string |  |   phished\_brand 
action\_result\.data\.\*\.\*\.Labels\.\*\.Value | string |  |   Intuit 
action\_result\.data\.\*\.\*\.Parameters | string |  |  
action\_result\.data\.\*\.\*\.Parameters\.\*\.Name | string |  |   decode\_rewritten\_urls 
action\_result\.data\.\*\.\*\.Parameters\.\*\.Value | string |  |   true 
action\_result\.data\.\*\.\*\.Priority | numeric |  |   5 
action\_result\.data\.\*\.\*\.Profile | string |  |   default 
action\_result\.data\.\*\.\*\.RequestedEngines | string |  |  
action\_result\.data\.\*\.\*\.ResourceCount | numeric |  |   2 
action\_result\.data\.\*\.\*\.Resources\.\*\.CreatedAt | string |  |   2022\-11\-23T00\:44\:12\.857Z 
action\_result\.data\.\*\.\*\.Resources\.\*\.DisplayScore | numeric |  |   100 
action\_result\.data\.\*\.\*\.Resources\.\*\.FileMetadata\.FileType | string |  |  
action\_result\.data\.\*\.\*\.Resources\.\*\.FileMetadata\.IsEncrypted | string |  |  
action\_result\.data\.\*\.\*\.Resources\.\*\.FileMetadata\.MD5 | string |  |  
action\_result\.data\.\*\.\*\.Resources\.\*\.FileMetadata\.MimeType | string |  |  
action\_result\.data\.\*\.\*\.Resources\.\*\.FileMetadata\.SHA256 | string |  |  
action\_result\.data\.\*\.\*\.Resources\.\*\.FileMetadata\.Size | numeric |  |  
action\_result\.data\.\*\.\*\.Resources\.\*\.ID | string |  |   c6e29c54\-ca84\-4368\-8af6\-38edc2c8398e 
action\_result\.data\.\*\.\*\.Resources\.\*\.InjectionMetadata\.AddedBecause | string |  |  
action\_result\.data\.\*\.\*\.Resources\.\*\.InjectionMetadata\.AddedBy | string |  |  
action\_result\.data\.\*\.\*\.Resources\.\*\.JobID | string |  |   63572265\-c5ae\-402f\-9fc1\-6c90547482ee 
action\_result\.data\.\*\.\*\.Resources\.\*\.Location | string |  |   https\://boomerangdairysandbedding\.com/wp\-includes/fonts/QuickB2022/ 
action\_result\.data\.\*\.\*\.Resources\.\*\.Name | string |  |   https\://boomerangdairysandbedding\.com/wp\-includes/fonts/QuickB2022/ 
action\_result\.data\.\*\.\*\.Resources\.\*\.ParentID | string |  |  
action\_result\.data\.\*\.\*\.Resources\.\*\.Score | numeric |  |   1 
action\_result\.data\.\*\.\*\.Resources\.\*\.Type | string |  |   URL 
action\_result\.data\.\*\.\*\.Score | numeric |  |   1 
action\_result\.data\.\*\.\*\.Sharing\.ShareToken | string |  |  
action\_result\.data\.\*\.\*\.Sharing\.SharedAt | string |  |  
action\_result\.data\.\*\.\*\.Sharing\.SharedBy | string |  |  
action\_result\.data\.\*\.\*\.StartedAt | string |  |   2022\-11\-23T00\:44\:13\.256Z 
action\_result\.data\.\*\.\*\.State | string |  |   done 
action\_result\.data\.\*\.\*\.Submission\.MD5 | string |  |  
action\_result\.data\.\*\.\*\.Submission\.Name | string |  |   https\://boomerangdairysandbedding\.com/wp\-includes/fonts/QuickB2022/ 
action\_result\.data\.\*\.\*\.Submission\.SHA256 | string |  |  
action\_result\.data\.\*\.\*\.SubmissionSource | string |  |   UI 
action\_result\.data\.\*\.\*\.Tasks\.\*\.CreatedAt | string |  |   2022\-11\-23T00\:45\:27\.453Z 
action\_result\.data\.\*\.\*\.Tasks\.\*\.Engine | string |  |   url\_reputation 
action\_result\.data\.\*\.\*\.Tasks\.\*\.ID | string |  |   1ce8132e\-87cf\-43a5\-8076\-dce647ff2890 
action\_result\.data\.\*\.\*\.Tasks\.\*\.Priority | numeric |  |   5 
action\_result\.data\.\*\.\*\.Tasks\.\*\.ResourceID | string |  |   d7d53778\-8ec3\-405a\-9ec2\-9e0a5b998913 
action\_result\.data\.\*\.\*\.Tasks\.\*\.Results\.Details | string |  |  
action\_result\.data\.\*\.\*\.Tasks\.\*\.Results\.DisplayScore | numeric |  |  
action\_result\.data\.\*\.\*\.Tasks\.\*\.Results\.Forensics\.Normalized | string |  |   normalized/2022\-11\-23/lab/63572265\-c5ae\-402f\-9fc1\-6c90547482ee/1ce8132e\-87cf\-43a5\-8076\-dce647ff2890/2b83ece5\-a1d4\-48a7\-8df3\-b706eec61287\.json\.gz 
action\_result\.data\.\*\.\*\.Tasks\.\*\.Results\.Forensics\.Raw | string |  |  
action\_result\.data\.\*\.\*\.Tasks\.\*\.Results\.Score | numeric |  |  
action\_result\.data\.\*\.\*\.Tasks\.\*\.StartedAt | string |  |   2022\-11\-23T00\:45\:27\.564Z 
action\_result\.data\.\*\.\*\.Tasks\.\*\.State | string |  |   done 
action\_result\.data\.\*\.\*\.Tasks\.\*\.StateText | string |  |  
action\_result\.data\.\*\.\*\.Tasks\.\*\.UpdatedAt | string |  |   2022\-11\-23T00\:45\:29\.113Z 
action\_result\.data\.\*\.\*\.TenantID | string |  |   lab 
action\_result\.data\.\*\.\*\.UpdatedAt | string |  |   2022\-11\-23T00\:45\:29\.545Z 
action\_result\.data\.\*\.\*\.Username | string |  |   lab\@data\.com 
action\_result\.data\.\*\.\*\.Verdict | string |  |   phish 
action\_result\.data\.\*\.APIKey\.\*\.ID | string |  |  
action\_result\.data\.\*\.APIKey\.\*\.Label | string |  |  
action\_result\.data\.\*\.APIKeyID | string |  |  
action\_result\.data\.\*\.CompletedAt | string |  |  
action\_result\.data\.\*\.CreatedAt | string |  |  
action\_result\.data\.\*\.DisplayScore | numeric |  |  
action\_result\.data\.\*\.ForensicsPath | string |  |  
action\_result\.data\.\*\.ID | string |  |  
action\_result\.data\.\*\.Labels\.\*\.ID | numeric |  |  
action\_result\.data\.\*\.Labels\.\*\.Jobs | string |  |  
action\_result\.data\.\*\.Labels\.\*\.Type | string |  |  
action\_result\.data\.\*\.Labels\.\*\.Value | string |  |  
action\_result\.data\.\*\.Parameters | string |  |  
action\_result\.data\.\*\.Priority | numeric |  |  
action\_result\.data\.\*\.Profile | string |  |  
action\_result\.data\.\*\.RequestedEngines | string |  |  
action\_result\.data\.\*\.ResourceCount | numeric |  |  
action\_result\.data\.\*\.Resources\.\*\.CreatedAt | string |  |  
action\_result\.data\.\*\.Resources\.\*\.DisplayScore | numeric |  |  
action\_result\.data\.\*\.Resources\.\*\.FileMetadata\.\*\.FileType | string |  |  
action\_result\.data\.\*\.Resources\.\*\.FileMetadata\.\*\.IsEncrypted | string |  |  
action\_result\.data\.\*\.Resources\.\*\.FileMetadata\.\*\.MD5 | string |  |  
action\_result\.data\.\*\.Resources\.\*\.FileMetadata\.\*\.MimeType | string |  |  
action\_result\.data\.\*\.Resources\.\*\.FileMetadata\.\*\.SHA256 | string |  |  
action\_result\.data\.\*\.Resources\.\*\.FileMetadata\.\*\.Size | numeric |  |  
action\_result\.data\.\*\.Resources\.\*\.ID | string |  |  
action\_result\.data\.\*\.Resources\.\*\.InjectionMetadata\.\*\.AddedBecause | string |  |  
action\_result\.data\.\*\.Resources\.\*\.InjectionMetadata\.\*\.AddedBy | string |  |  
action\_result\.data\.\*\.Resources\.\*\.JobID | string |  |  
action\_result\.data\.\*\.Resources\.\*\.Location | string |  |  
action\_result\.data\.\*\.Resources\.\*\.Name | string |  |  
action\_result\.data\.\*\.Resources\.\*\.ParentID | string |  |  
action\_result\.data\.\*\.Resources\.\*\.Score | numeric |  |  
action\_result\.data\.\*\.Resources\.\*\.Type | string |  |  
action\_result\.data\.\*\.Score | numeric |  |  
action\_result\.data\.\*\.Sharing\.\*\.ShareToken | string |  |  
action\_result\.data\.\*\.Sharing\.\*\.SharedAt | string |  |  
action\_result\.data\.\*\.Sharing\.\*\.SharedBy | string |  |  
action\_result\.data\.\*\.StartedAt | string |  |  
action\_result\.data\.\*\.State | string |  |  
action\_result\.data\.\*\.SubmissionSource | string |  |  
action\_result\.data\.\*\.Submissions\.\*\.MD5 | string |  |  
action\_result\.data\.\*\.Submissions\.\*\.Name | string |  |  
action\_result\.data\.\*\.Submissions\.\*\.SHA256 | string |  |  
action\_result\.data\.\*\.Tasks\.\*\.CreatedAt | string |  |  
action\_result\.data\.\*\.Tasks\.\*\.Engine | string |  |  
action\_result\.data\.\*\.Tasks\.\*\.ID | string |  |  
action\_result\.data\.\*\.Tasks\.\*\.Priority | numeric |  |  
action\_result\.data\.\*\.Tasks\.\*\.ResourceID | string |  |  
action\_result\.data\.\*\.Tasks\.\*\.Results\.\*\.Details | string |  |  
action\_result\.data\.\*\.Tasks\.\*\.Results\.\*\.Forensics\.\*\.Normalized | string |  |  
action\_result\.data\.\*\.Tasks\.\*\.Results\.\*\.Forensics\.\*\.Raw | string |  |  
action\_result\.data\.\*\.Tasks\.\*\.Results\.\*\.Score | numeric |  |  
action\_result\.data\.\*\.Tasks\.\*\.StartedAt | string |  |  
action\_result\.data\.\*\.Tasks\.\*\.State | string |  |  
action\_result\.data\.\*\.Tasks\.\*\.StateText | string |  |  
action\_result\.data\.\*\.Tasks\.\*\.StateText | string |  |  
action\_result\.data\.\*\.Tasks\.\*\.UpdatedAt | string |  |  
action\_result\.data\.\*\.TenantID | string |  |  
action\_result\.data\.\*\.UpdatedAt | string |  |  
action\_result\.data\.\*\.Username | string |  |  
action\_result\.summary | string |  |  
action\_result\.summary\.job\_count | numeric |  |   2 
action\_result\.message | string |  |   Job count\: 2 
summary\.total\_objects | numeric |  |   2 
summary\.total\_objects\_successful | numeric |  |   2   

## action: 'detonate file'
Submit File for Scanning

Type: **investigate**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**file** |  required  | File hash to submit | string |  `vault id` 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action\_result\.status | string |  |   success  failed 
action\_result\.parameter\.file | string |  `vault id`  |   89b238c79f7752948b176222ae0010d0a1ef 
action\_result\.data\.\*\.AppURL | string |  `url`  |  
action\_result\.data\.\*\.JobID | string |  `splunk attack analyzer job id`  |  
action\_result\.data\.\*\.QueueDepth | numeric |  |  
action\_result\.data\.\*\.QuotaRemaining | numeric |  |  
action\_result\.summary | string |  |  
action\_result\.message | string |  |   Submitted file 
summary\.total\_objects | numeric |  |   2 
summary\.total\_objects\_successful | numeric |  |   2   

## action: 'detonate url'
Submit New URL for Scanning

Type: **investigate**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**url** |  required  | URL to submit | string |  `url` 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action\_result\.status | string |  |   success  failed 
action\_result\.parameter\.url | string |  `url`  |   https\://classic\.cdn\.net/v1993\.137/scripts/sharedScripts\.js 
action\_result\.data\.\*\.AppURL | string |  `url`  |  
action\_result\.data\.\*\.JobID | string |  `splunk attack analyzer job id`  |  
action\_result\.data\.\*\.QueueDepth | numeric |  |  
action\_result\.data\.\*\.QuotaRemaining | numeric |  |  
action\_result\.summary | string |  |  
action\_result\.message | string |  |   Submitted URL 
summary\.total\_objects | numeric |  |   2 
summary\.total\_objects\_successful | numeric |  |   2   

## action: 'get pdf report'
Get the PDF report for a completed job

Type: **investigate**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**job\_id** |  required  | Job id of the job summary you want to download the PDF for | string |  `splunk attack analyzer job id` 
**wait** |  optional  | Wait for job to finish before returning results | boolean | 
**timeout** |  optional  | Maximum time \(in minutes\) to wait for job to be complete | numeric | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action\_result\.status | string |  |   success  failed 
action\_result\.parameter\.job\_id | string |  `splunk attack analyzer job id`  |   63572265\-c5ae\-402f\-9fc1\-6c90547482ee 
action\_result\.parameter\.timeout | numeric |  |   30 
action\_result\.parameter\.wait | boolean |  |   True  False 
action\_result\.data | string |  |  
action\_result\.data\.\*\.container | numeric |  |   2 
action\_result\.data\.\*\.created\_via | string |  |   automation 
action\_result\.data\.\*\.file\_name | string |  |   6b95b196e0d6d5a75fa0241d903350a7b65d0 
action\_result\.data\.\*\.hash | string |  |   6b95b196e05b2d6d5a75fa0241d903350a7b65d0 
action\_result\.data\.\*\.id | numeric |  |   6 
action\_result\.data\.\*\.message | string |  |   success 
action\_result\.data\.\*\.size | numeric |  |   1187161 
action\_result\.data\.\*\.succeeded | boolean |  |   True  False 
action\_result\.data\.\*\.vault\_id | string |  `vault id`  |   6b95b196e05b2d6d5a75fa0241d903350a7b65d0 
action\_result\.summary | string |  |  
action\_result\.message | string |  |   Successfully attached PDF report 
summary\.total\_objects | numeric |  |   2 
summary\.total\_objects\_successful | numeric |  |   2   

## action: 'get job screenshots'
Get screenshots for the specified job and store them in the vault

Type: **investigate**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**job\_id** |  required  | Job id of the job summary you want to download the PDF for | string |  `splunk attack analyzer job id` 
**wait** |  optional  | Wait for job to finish before returning results | boolean | 
**timeout** |  optional  | Maximum time \(in minutes\) to wait for job to be complete | numeric | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action\_result\.status | string |  |   success  failed 
action\_result\.parameter\.job\_id | string |  `splunk attack analyzer job id`  |   63572265\-c5ae\-402f\-9fc1\-6c90547482ee 
action\_result\.parameter\.timeout | numeric |  |   30 
action\_result\.parameter\.wait | boolean |  |   True  False 
action\_result\.data | string |  |  
action\_result\.data\.\*\.container | numeric |  |   2 
action\_result\.data\.\*\.created\_via | string |  |   automation 
action\_result\.data\.\*\.file\_name | string |  |   6b95b196e05b2d6d5a75fa0241d903350a7b65d0 
action\_result\.data\.\*\.hash | string |  |   de7403877259141c0217d19dc2f7931c913 
action\_result\.data\.\*\.id | numeric |  |   7 
action\_result\.data\.\*\.message | string |  |   success 
action\_result\.data\.\*\.screenshot\_count | numeric |  |   2 
action\_result\.data\.\*\.size | numeric |  |   470679 
action\_result\.data\.\*\.succeeded | boolean |  |   True  False 
action\_result\.data\.\*\.vault\_id | string |  `vault id`  |   de740387131d77259141c0217d19dc2f7931c913 
action\_result\.summary | string |  |  
action\_result\.summary\.screenshot\_count | numeric |  |   2 
action\_result\.message | string |  |   Screenshot count\: 2 
summary\.total\_objects | numeric |  |   2 
summary\.total\_objects\_successful | numeric |  |   2 