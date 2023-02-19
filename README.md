[comment]: # "Auto-generated SOAR connector documentation"
# Splunk Attack Analyzer

Publisher: Splunk Attack Analyzer
Connector Version: 1\.0\.1  
Product Vendor: Splunk Attack Analyzer
Product Name: Splunk Attack Analyzer
Product Version Supported (regex): "\.\*"  
Minimum Product Version: 5\.1\.0  

A threat analysis platform to reduce the friction of repetitive manual tasks typically associated with investigating threats

[comment]: # " File: README.md"
[comment]: # ""
[comment]: # "  Copyright (c) Splunk Inc., 2022"
[comment]: # ""
[comment]: # "  Licensed under the Apache License, Version 2.0 (the 'License');"
[comment]: # "  you may not use this file except in compliance with the License."
[comment]: # "  You may obtain a copy of the License at"
[comment]: # ""
[comment]: # "      http://www.apache.org/licenses/LICENSE-2.0"
[comment]: # ""
[comment]: # "  Unless required by applicable law or agreed to in writing, software distributed under"
[comment]: # "  the License is distributed on an 'AS IS' BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,"
[comment]: # "  either express or implied. See the License for the specific language governing permissions"
[comment]: # "  and limitations under the License."
[comment]: # ""
### The Splunk Attack Analyzer SOAR app can be used to connect with the [Splunk Attack Analyzer analysis platform](https://www.google.com/url?q=https://www.twinwave.io/&sa=D&source=editors&ust=1644536802576291&usg=AOvVaw1QbcnelmQFirXDHIRabB07)

The following actions are supported by the app:

-   Submitting a URL for analysis
-   Submitting a file for analysis
-   Fetching analysis (job) summary data
-   Fetching the forensics for a job
-   Downloading screenshots for a job and attaching them to the vault
-   Downloading an offline PDF report for a job and attaching it to the vault


### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a Splunk Attack Analyzer asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**api\_token** |  required  | password | API token from the app
**since** |  optional  | numeric | Start of time range stated in hours

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
**container\_id** |  optional  | Container IDs to limit the ingestion to | string | 
**start\_time** |  optional  | Start of time range, in epoch time \(milliseconds\)\. If not specified, the default is past 10 days | numeric | 
**end\_time** |  optional  | End of time range, in epoch time \(milliseconds\)\. If not specified, the default is now | numeric | 
**container\_count** |  optional  | Maximum number of container records to query for | numeric | 
**artifact\_count** |  optional  | Maximum number of artifact records to query for | numeric | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.data | string | 
action\_result\.summary | string | 
action\_result\.parameter\.container\_id | string | 
action\_result\.parameter\.start\_time | numeric | 
action\_result\.parameter\.end\_time | numeric | 
action\_result\.parameter\.container\_count | numeric | 
action\_result\.parameter\.artifact\_count | numeric | 
action\_result\.status | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get job forensics'
Get the consolidated forensics for a completed job

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**job\_id** |  required  | Job id of the forensics you want pulled | string |  `splunk attack analyzer job id` 
**wait** |  optional  | Wait for job to finish before returning results | boolean | 
**timeout** |  optional  | Maximum time \(in minutes\) to wait for job to be complete | numeric | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.job\_id | string |  `splunk attack analyzer job id` 
action\_result\.parameter\.wait | boolean | 
action\_result\.parameter\.timeout | numeric | 
action\_result\.status | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 
action\_result\.data | string | 
action\_result\.summary | string | 
action\_result\.data\.\*\.TLS\.\*\.Issuer | string | 
action\_result\.data\.\*\.TLS\.\*\.Source\.IP | string | 
action\_result\.data\.\*\.TLS\.\*\.Source\.Port | numeric | 
action\_result\.data\.\*\.TLS\.\*\.Details\.JA3 | string | 
action\_result\.data\.\*\.TLS\.\*\.Engines | string | 
action\_result\.data\.\*\.TLS\.\*\.Subject | string | 
action\_result\.data\.\*\.TLS\.\*\.Destination\.IP | string | 
action\_result\.data\.\*\.TLS\.\*\.Destination\.Port | numeric | 
action\_result\.data\.\*\.TLS\.\*\.Fingerprint | numeric | 
action\_result\.data\.\*\.HTTP\.\*\.URL | string | 
action\_result\.data\.\*\.HTTP\.\*\.Path | string | 
action\_result\.data\.\*\.HTTP\.\*\.Method | string | 
action\_result\.data\.\*\.HTTP\.\*\.Source\.\*\.IP | string | 
action\_result\.data\.\*\.HTTP\.\*\.Source\.\*\.Port | numeric | 
action\_result\.data\.\*\.HTTP\.\*\.Hostname | string | 
action\_result\.data\.\*\.HTTP\.\*\.TotalSize | string | 
action\_result\.data\.\*\.HTTP\.\*\.UserAgent | string | 
action\_result\.data\.\*\.HTTP\.\*\.TotalSize | numeric | 
action\_result\.data\.\*\.HTTP\.\*\.UserAgent | string | 
action\_result\.data\.\*\.HTTP\.\*\.StatusCode | numeric | 
action\_result\.data\.\*\.HTTP\.\*\.Destination\.\*\.IP | string | 
action\_result\.data\.\*\.HTTP\.\*\.Destination\.\*\.Port | numeric | 
action\_result\.data\.\*\.HTTP\.\*\.RequestSize | numeric | 
action\_result\.data\.\*\.HTTP\.\*\.ResponseSize | numeric | 
action\_result\.data\.\*\.HTTP\.\*\.RequestHeaders | string | 
action\_result\.data\.\*\.HTTP\.\*\.ResponseHeaders | numeric | 
action\_result\.data\.\*\.Logs | string | 
action\_result\.data\.\*\.URLs\.\*\.URL | string | 
action\_result\.data\.\*\.URLs\.\*\.Context | string | 
action\_result\.data\.\*\.URLs\.\*\.Engines | string | 
action\_result\.data\.\*\.URLs\.\*\.LinkText | string | 
action\_result\.data\.\*\.Files\.\*\.MD5 | string | 
action\_result\.data\.\*\.Files\.\*\.Path | string | 
action\_result\.data\.\*\.Files\.\*\.Size | numeric | 
action\_result\.data\.\*\.Files\.\*\.SHA256 | string | 
action\_result\.data\.\*\.Files\.\*\.Ssdeep | string | 
action\_result\.data\.\*\.Files\.\*\.Context | string | 
action\_result\.data\.\*\.Files\.\*\.Details\.\*\.SHA1 | string | 
action\_result\.data\.\*\.Files\.\*\.Details\.\*\.CRC32 | string | 
action\_result\.data\.\*\.Files\.\*\.Details\.\*\.ClamAV | string | 
action\_result\.data\.\*\.Files\.\*\.Details\.\*\.SHA512 | string | 
action\_result\.data\.\*\.Files\.\*\.Details\.\*\.GuestPath | string | 
action\_result\.data\.\*\.Files\.\*\.FileName | string | 
action\_result\.data\.\*\.Files\.\*\.FileType | string | 
action\_result\.data\.\*\.Files\.\*\.NetworkSources | string | 
action\_result\.data\.\*\.Forms\.\*\.Action | string | 
action\_result\.data\.\*\.Forms\.\*\.Inputs\.\*\.ID | string | 
action\_result\.data\.\*\.Forms\.\*\.Inputs\.\*\.Name | string | 
action\_result\.data\.\*\.Forms\.\*\.Inputs\.\*\.Type | string | 
action\_result\.data\.\*\.Forms\.\*\.Inputs\.\*\.SourceCode | string | 
action\_result\.data\.\*\.Forms\.\*\.Inputs\.\*\.Placeholder | string | 
action\_result\.data\.\*\.Forms\.\*\.method | string | 
action\_result\.data\.\*\.Forms\.\*\.Engines | string | 
action\_result\.data\.\*\.Forms\.\*\.PageURL | string | 
action\_result\.data\.\*\.Forms\.\*\.SourceCode | string | 
action\_result\.data\.\*\.Hosts\.\*\.IP | string | 
action\_result\.data\.\*\.Hosts\.\*\.ASN | numeric | 
action\_result\.data\.\*\.Hosts\.\*\.City | string | 
action\_result\.data\.\*\.Hosts\.\*\.Country | string | 
action\_result\.data\.\*\.Hosts\.\*\.Engines | string | 
action\_result\.data\.\*\.Hosts\.\*\.Houstname | string | 
action\_result\.data\.\*\.Hosts\.\*\.Organization | string | 
action\_result\.data\.\*\.Score | numeric | 
action\_result\.data\.\*\.Engine | string | 
action\_result\.data\.\*\.Images\.\*\.Type | string | 
action\_result\.data\.\*\.Images\.\*\.Resource | string | 
action\_result\.data\.\*\.Images\.\*\.ImageHashes | string | 
action\_result\.data\.\*\.Images\.\*\.ArtifactPath | string | 
action\_result\.data\.\*\.Images\.\*\.DetectedObjects | string | 
action\_result\.data\.\*\.Details\.engines | string | 
action\_result\.data\.\*\.EndTime | string | 
action\_result\.data\.\*\.Mutexes\.\*\.Name | string | 
action\_result\.data\.\*\.Mutexes\.\*\.Engines | string | 
action\_result\.data\.\*\.Network\.\*\.Length | numeric | 
action\_result\.data\.\*\.Network\.\*\.Source\.\*\.IP | string | 
action\_result\.data\.\*\.Network\.\*\.Source\.\*\.Port | numeric | 
action\_result\.data\.\*\.Network\.\*\.Service | string | 
action\_result\.data\.\*\.Network\.\*\.Protocol | string | 
action\_result\.data\.\*\.Network\.\*\.Destination\.\*\.IP | string | 
action\_result\.data\.\*\.Network\.\*\.Destination\.\*\.Port | numeric | 
action\_result\.data\.\*\.Strings\.\*\.String | string | 
action\_result\.data\.\*\.Strings\.\*\.Engines | string | 
action\_result\.data\.\*\.Verdict | string | 
action\_result\.data\.\*\.Version | string | 
action\_result\.data\.\*\.Processes\.\*\.PID | numeric | 
action\_result\.data\.\*\.Processes\.\*\.Name | string | 
action\_result\.data\.\*\.Processes\.\*\.PPID | numeric | 
action\_result\.data\.\*\.Processes\.\*\.Path | string | 
action\_result\.data\.\*\.Processes\.\*\.Details\.\*\.Calls | string | 
action\_result\.data\.\*\.Processes\.\*\.Details\.Threads | string | 
action\_result\.data\.\*\.Processes\.\*\.Details\.Environment\.\*\.retval | numeric | 
action\_result\.data\.\*\.Processes\.\*\.Details\.Environment\.\*\.OSMajor | numeric | 
action\_result\.data\.\*\.Processes\.\*\.Details\.Environment\.\*\.OSMinor | numeric | 
action\_result\.data\.\*\.Processes\.\*\.Details\.Environment\.\*\.TempPath | string | 
action\_result\.data\.\*\.Processes\.\*\.Details\.Environment\.\*\.UserName | string | 
action\_result\.data\.\*\.Processes\.\*\.Details\.Environment\.\*\.is\_success | string | 
action\_result\.data\.\*\.Processes\.\*\.Details\.Environment\.\*\.CommandLine | string | 
action\_result\.data\.\*\.Processes\.\*\.Details\.Environment\.\*\.InstallDate | numeric | 
action\_result\.data\.\*\.Processes\.\*\.Details\.Environment\.\*\.MachineGUID | string | 
action\_result\.data\.\*\.Processes\.\*\.Details\.Environment\.\*\.MainExeBase | string | 
action\_result\.data\.\*\.Processes\.\*\.Details\.Environment\.\*\.MainExeSize | string | 
action\_result\.data\.\*\.Processes\.\*\.Details\.Environment\.\*\.ProductName | string | 
action\_result\.data\.\*\.Processes\.\*\.Details\.Environment\.\*\.WindowsPath | string | 
action\_result\.data\.\*\.Processes\.\*\.Details\.Environment\.\*\.ComputerName | string | 
action\_result\.data\.\*\.Processes\.\*\.Details\.Environment\.\*\.RegisteredOwner | string | 
action\_result\.data\.\*\.Processes\.\*\.Details\.Environment\.\*\.SystemVolumeGUID | string | 
action\_result\.data\.\*\.Processes\.\*\.Details\.Environment\.\*\.RegisteredOrganization | string | 
action\_result\.data\.\*\.Processes\.\*\.Details\.Environment\.\*\.SystemVolumeSerialNumber | string | 
action\_result\.data\.\*\.Processes\.\*\.Details\.Arguements | string | 
action\_result\.data\.\*\.StartTime | string | 
action\_result\.data\.\*\.DNSServers | string | 
action\_result\.data\.\*\.Detections\.\*\.Name | string | 
action\_result\.data\.\*\.Detections\.\*\.Details\.Data\.\*\.Hit | string | 
action\_result\.data\.\*\.Detections\.\*\.Engines | string | 
action\_result\.data\.\*\.Detections\.\*\.Severity | numeric | 
action\_result\.data\.\*\.Detections\.\*\.Description | string | 
action\_result\.data\.\*\.DNSRequests\.\*\.Query | string | 
action\_result\.data\.\*\.DNSRequests\.\*\.Server | string | 
action\_result\.data\.\*\.DNSRequests\.\*\.Engines | string | 
action\_result\.data\.\*\.DNSRequests\.\*\.QueryType | string | 
action\_result\.data\.\*\.DNSRequests\.\*\.Responses\.\*\.Type | string | 
action\_result\.data\.\*\.DNSRequests\.\*\.Responses\.\*\.Value | string | 
action\_result\.data\.\*\.Screenshots\.\*\.URI | string | 
action\_result\.data\.\*\.Screenshots\.\*\.Engines | string | 
action\_result\.data\.\*\.Screenshots\.\*\.Resource | string | 
action\_result\.data\.\*\.Screenshots\.\*\.ImageHashes | string | 
action\_result\.data\.\*\.Screenshots\.\*\.ArtifactPath | string | 
action\_result\.data\.\*\.DisplayScore | numeric | 
action\_result\.data\.\*\.MitreAttacks\.\*\.ID | string | 
action\_result\.data\.\*\.MitreAttacks\.\*\.Tactic | string | 
action\_result\.data\.\*\.MitreAttacks\.\*\.Engines | string | 
action\_result\.data\.\*\.MitreAttacks\.\*\.Technique | string | 
action\_result\.data\.\*\.MitreAttacks\.\*\.SubTechnique | string | 
action\_result\.data\.\*\.Registrykeys\.\*\.Name | string | 
action\_result\.data\.\*\.Registrykeys\.\*\.Action | string | 
action\_result\.data\.\*\.Registrykeys\.\*\.Engines | string | 
action\_result\.data\.\*\.WhoisResults\.\*\.Org | string | 
action\_result\.data\.\*\.WhoisResults\.\*\.City | string | 
action\_result\.data\.\*\.WhoisResults\.\*\.Name | string | 
action\_result\.data\.\*\.WhoisResults\.\*\.State | string | 
action\_result\.data\.\*\.WhoisResults\.\*\.DNSSec | string | 
action\_result\.data\.\*\.WhoisResults\.\*\.Emails | string | 
action\_result\.data\.\*\.WhoisResults\.\*\.Address | string | 
action\_result\.data\.\*\.WhoisResults\.\*\.Country | string | 
action\_result\.data\.\*\.WhoisResults\.\*\.Engines | string | 
action\_result\.data\.\*\.WhoisResults\.\*\.ZipCode | string | 
action\_result\.data\.\*\.WhoisResults\.\*\.CreatedAt | string | 
action\_result\.data\.\*\.WhoisResults\.\*\.ExpiresAt | string | 
action\_result\.data\.\*\.WhoisResults\.\*\.Registrar | string | 
action\_result\.data\.\*\.WhoisResults\.\*\.UpdatedAt | string | 
action\_result\.data\.\*\.WhoisResults\.\*\.DomainName | string | 
action\_result\.data\.\*\.WhoisResults\.\*\.NameServers | string | 
action\_result\.data\.\*\.WhoisResults\.\*\.WhoisServer | string | 
action\_result\.data\.\*\.PhishedBrands | string | 
action\_result\.data\.\*\.MalwareConfigs | string | 
action\_result\.data\.\*\.SavedArtifacts | string | 
action\_result\.data\.\*\.MalwareFamilies | string |   

## action: 'get job summary'
Get a job summary

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**job\_id** |  required  | Job id of the job summary you want to fetch | string |  `splunk attack analyzer job id` 
**wait** |  optional  | Wait for job to finish before returning results | boolean | 
**timeout** |  optional  | Maximum time \(in minutes\) to wait for job to be complete | numeric | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.job\_id | string |  `splunk attack analyzer job id` 
action\_result\.parameter\.wait | boolean | 
action\_result\.parameter\.timeout | numeric | 
action\_result\.status | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 
action\_result\.data | string | 
action\_result\.summary | string | 
action\_result\.\*\.data\.\*\.ID | string |  `splunk attack analyzer job id` 
action\_result\.data\.\*\.Score | numeric | 
action\_result\.data\.\*\.State | string | 
action\_result\.data\.\*\.Tasks\.\*\.ID | string | 
action\_result\.data\.\*\.Tasks\.\*\.State | string | 
action\_result\.data\.\*\.Tasks\.\*\.Engine | string | 
action\_result\.data\.\*\.Tasks\.\*\.Results\.\*\.Score | numeric | 
action\_result\.data\.\*\.Tasks\.\*\.Results\.\*\.Details | string | 
action\_result\.data\.\*\.Tasks\.\*\.Results\.\*\.Forensics\.\*\.Raw | string | 
action\_result\.data\.\*\.Tasks\.\*\.Results\.\*\.Forensics\.\*\.Normalized | string | 
action\_result\.data\.\*\.Tasks\.\*\.Priority | numeric | 
action\_result\.data\.\*\.Tasks\.\*\.CreatedAt | string | 
action\_result\.data\.\*\.Tasks\.\*\.StartedAt | string | 
action\_result\.data\.\*\.Tasks\.\*\.StateText | string | 
action\_result\.data\.\*\.Tasks\.\*\.StateText | string | 
action\_result\.data\.\*\.Tasks\.\*\.UpdatedAt | string | 
action\_result\.data\.\*\.Tasks\.\*\.ResourceID | string | 
action\_result\.data\.\*\.APIKey\.\*\.ID | string | 
action\_result\.data\.\*\.APIKey\.\*\.Label | string | 
action\_result\.data\.\*\.Labels\.\*\.ID | numeric | 
action\_result\.data\.\*\.Labels\.\*\.Jobs | string | 
action\_result\.data\.\*\.Labels\.\*\.Type | string | 
action\_result\.data\.\*\.Labels\.\*\.Value | string | 
action\_result\.data\.\*\.Profile | string | 
action\_result\.data\.\*\.Sharing\.\*\.SharedAt | string | 
action\_result\.data\.\*\.Sharing\.\*\.SharedBy | string | 
action\_result\.data\.\*\.Sharing\.\*\.ShareToken | string | 
action\_result\.data\.\*\.APIKeyID | string | 
action\_result\.data\.\*\.Priority | numeric | 
action\_result\.data\.\*\.TenantID | string | 
action\_result\.data\.\*\.Username | string | 
action\_result\.data\.\*\.CreatedAt | string | 
action\_result\.data\.\*\.Resources\.\*\.ID | string | 
action\_result\.data\.\*\.Resources\.\*\.Name | string | 
action\_result\.data\.\*\.Resources\.\*\.Type | string | 
action\_result\.data\.\*\.Resources\.\*\.JobID | string | 
action\_result\.data\.\*\.Resources\.\*\.Score | numeric | 
action\_result\.data\.\*\.Resources\.\*\.Location | string | 
action\_result\.data\.\*\.Resources\.\*\.ParentID | string | 
action\_result\.data\.\*\.Resources\.\*\.CreatedAt | string | 
action\_result\.data\.\*\.Resources\.\*\.DisplayScore | numeric | 
action\_result\.data\.\*\.Resources\.\*\.FileMetadata\.\*\.MD5 | string | 
action\_result\.data\.\*\.Resources\.\*\.FileMetadata\.\*\.Size | numeric | 
action\_result\.data\.\*\.Resources\.\*\.FileMetadata\.\*\.SHA256 | string | 
action\_result\.data\.\*\.Resources\.\*\.FileMetadata\.\*\.FileType | string | 
action\_result\.data\.\*\.Resources\.\*\.FileMetadata\.\*\.MimeType | string | 
action\_result\.data\.\*\.Resources\.\*\.FileMetadata\.\*\.IsEncrypted | string | 
action\_result\.data\.\*\.Resources\.\*\.InjectionMetadata\.\*\.AddedBy | string | 
action\_result\.data\.\*\.Resources\.\*\.InjectionMetadata\.\*\.AddedBecause | string | 
action\_result\.data\.\*\.ResourceTree | string | 
action\_result\.data\.\*\.StartedAt | string | 
action\_result\.data\.\*\.UpdatedAt | string | 
action\_result\.data\.\*\.Parameters | string | 
action\_result\.data\.\*\.Submissions\.\*\.MD5 | string | 
action\_result\.data\.\*\.Submissions\.\*\.Name | string | 
action\_result\.data\.\*\.Submissions\.\*\.SHA256 | string | 
action\_result\.data\.\*\.CompletedAt | string | 
action\_result\.data\.\*\.DisplayScore | numeric | 
action\_result\.data\.\*\.Verdict | string | 
action\_result\.data\.\*\.ForensicsPath | string | 
action\_result\.data\.\*\.ResourceCount | numeric | 
action\_result\.data\.\*\.RequestedEngines | string | 
action\_result\.data\.\*\.SubmissionSource | string |   

## action: 'list recent jobs'
Get a list of recent jobs

Type: **generic**  
Read only: **False**

#### Action Parameters
No parameters are required for this action

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 
action\_result\.data | string | 
action\_result\.data\.\*\.ID | string | 
action\_result\.data\.\*\.Score | numeric | 
action\_result\.data\.\*\.State | string | 
action\_result\.data\.\*\.Tasks\.\*\.ID | string | 
action\_result\.data\.\*\.Tasks\.\*\.State | string | 
action\_result\.data\.\*\.Tasks\.\*\.Engine | string | 
action\_result\.data\.\*\.Tasks\.\*\.Results\.\*\.Score | numeric | 
action\_result\.data\.\*\.Tasks\.\*\.Results\.\*\.Details | string | 
action\_result\.data\.\*\.Tasks\.\*\.Results\.\*\.Forensics\.\*\.Raw | string | 
action\_result\.data\.\*\.Tasks\.\*\.Results\.\*\.Forensics\.\*\.Normalized | string | 
action\_result\.data\.\*\.Tasks\.\*\.Priority | numeric | 
action\_result\.data\.\*\.Tasks\.\*\.CreatedAt | string | 
action\_result\.data\.\*\.Tasks\.\*\.StartedAt | string | 
action\_result\.data\.\*\.Tasks\.\*\.StateText | string | 
action\_result\.data\.\*\.Tasks\.\*\.StateText | string | 
action\_result\.data\.\*\.Tasks\.\*\.UpdatedAt | string | 
action\_result\.data\.\*\.Tasks\.\*\.ResourceID | string | 
action\_result\.data\.\*\.APIKey\.\*\.ID | string | 
action\_result\.data\.\*\.APIKey\.\*\.Label | string | 
action\_result\.data\.\*\.Labels\.\*\.ID | numeric | 
action\_result\.data\.\*\.Labels\.\*\.Jobs | string | 
action\_result\.data\.\*\.Labels\.\*\.Type | string | 
action\_result\.data\.\*\.Labels\.\*\.Value | string | 
action\_result\.data\.\*\.Profile | string | 
action\_result\.data\.\*\.Sharing\.\*\.SharedAt | string | 
action\_result\.data\.\*\.Sharing\.\*\.SharedBy | string | 
action\_result\.data\.\*\.Sharing\.\*\.ShareToken | string | 
action\_result\.data\.\*\.APIKeyID | string | 
action\_result\.data\.\*\.Priority | numeric | 
action\_result\.data\.\*\.TenantID | string | 
action\_result\.data\.\*\.Username | string | 
action\_result\.data\.\*\.CreatedAt | string | 
action\_result\.data\.\*\.Resources\.\*\.ID | string | 
action\_result\.data\.\*\.Resources\.\*\.Name | string | 
action\_result\.data\.\*\.Resources\.\*\.Type | string | 
action\_result\.data\.\*\.Resources\.\*\.JobID | string | 
action\_result\.data\.\*\.Resources\.\*\.Score | numeric | 
action\_result\.data\.\*\.Resources\.\*\.Location | string | 
action\_result\.data\.\*\.Resources\.\*\.ParentID | string | 
action\_result\.data\.\*\.Resources\.\*\.CreatedAt | string | 
action\_result\.data\.\*\.Resources\.\*\.DisplayScore | numeric | 
action\_result\.data\.\*\.Resources\.\*\.FileMetadata\.\*\.MD5 | string | 
action\_result\.data\.\*\.Resources\.\*\.FileMetadata\.\*\.Size | numeric | 
action\_result\.data\.\*\.Resources\.\*\.FileMetadata\.\*\.SHA256 | string | 
action\_result\.data\.\*\.Resources\.\*\.FileMetadata\.\*\.FileType | string | 
action\_result\.data\.\*\.Resources\.\*\.FileMetadata\.\*\.MimeType | string | 
action\_result\.data\.\*\.Resources\.\*\.FileMetadata\.\*\.IsEncrypted | string | 
action\_result\.data\.\*\.Resources\.\*\.InjectionMetadata\.\*\.AddedBy | string | 
action\_result\.data\.\*\.Resources\.\*\.InjectionMetadata\.\*\.AddedBecause | string | 
action\_result\.data\.\*\.StartedAt | string | 
action\_result\.data\.\*\.UpdatedAt | string | 
action\_result\.data\.\*\.Parameters | string | 
action\_result\.data\.\*\.Submissions\.\*\.MD5 | string | 
action\_result\.data\.\*\.Submissions\.\*\.Name | string | 
action\_result\.data\.\*\.Submissions\.\*\.SHA256 | string | 
action\_result\.data\.\*\.CompletedAt | string | 
action\_result\.data\.\*\.DisplayScore | numeric | 
action\_result\.data\.\*\.ForensicsPath | string | 
action\_result\.data\.\*\.ResourceCount | numeric | 
action\_result\.data\.\*\.RequestedEngines | string | 
action\_result\.data\.\*\.SubmissionSource | string | 
action\_result\.summary | string |   

## action: 'detonate file'
Submit File for Scanning

Type: **investigate**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**file** |  required  | File hash to submit | string |  `vault id` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.file | string |  `vault id` 
action\_result\.status | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 
action\_result\.data\.\*\.JobID | string |  `splunk attack analyzer job id` 
action\_result\.data\.\*\.QueueDepth | numeric | 
action\_result\.data\.\*\.QuotaRemaining | numeric | 
action\_result\.data\.\*\.AppURL | string |  `url` 
action\_result\.summary | string |   

## action: 'detonate url'
Submit New URL for Scanning

Type: **investigate**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**url** |  required  | URL to submit | string |  `url` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.url | string |  `url` 
action\_result\.status | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 
action\_result\.data\.\*\.JobID | string |  `splunk attack analyzer job id` 
action\_result\.data\.\*\.QueueDepth | numeric | 
action\_result\.data\.\*\.QuotaRemaining | numeric | 
action\_result\.data\.\*\.AppURL | string |  `url` 
action\_result\.summary | string |   

## action: 'get pdf report'
Get the PDF report for a completed job

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**job\_id** |  required  | Job id of the job summary you want to download the PDF for | string |  `splunk attack analyzer job id` 
**wait** |  optional  | Wait for job to finish before returning results | boolean | 
**timeout** |  optional  | Maximum time \(in minutes\) to wait for job to be complete | numeric | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.job\_id | string |  `splunk attack analyzer job id` 
action\_result\.parameter\.wait | boolean | 
action\_result\.parameter\.timeout | numeric | 
action\_result\.status | string | 
action\_result\.data | string | 
action\_result\.summary | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get job screenshots'
Get screenshots for the specified job and store them in the vault

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**job\_id** |  required  | Job id of the job summary you want to download the PDF for | string |  `splunk attack analyzer job id` 
**wait** |  optional  | Wait for job to finish before returning results | boolean | 
**timeout** |  optional  | Maximum time \(in minutes\) to wait for job to be complete | numeric | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.job\_id | string |  `splunk attack analyzer job id` 
action\_result\.parameter\.wait | boolean | 
action\_result\.parameter\.timeout | numeric | 
action\_result\.status | string | 
action\_result\.data\.\*\.screenshot\_count | numeric | 
action\_result\.summary | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 