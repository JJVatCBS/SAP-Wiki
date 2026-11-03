---
product: SAP HANA Cloud
title: What's New
url: https://help.sap.com/whats-new/2495b34492334456a49084831c2bea4e?locale=en-US
source_type: SAP Help
---

HomeSAP HANA Cloud
What's New in SAP HANA CloudEnglish

Hide Filters (8)
List View
Download
Favorite
Subscribe
PDF
Share
Component:
[No selection]
Version:
[No selection]
Area:
[No selection]
Category:
[No selection]
Action:
[No selection]
Type:
[No selection]
Environment:
[No selection]
Release Date:
May 3, 2026–Nov 3, 2026
Reset
Clear
New versions of SAP HANA Cloud components ‒ SAP HANA Cloud, SAP HANA database and SAP HANA Cloud, data lake ‒ are available on a quarterly release cycle (QRC). To use new and enhanced features available in a particular database component version, you must ensure that your instance is upgraded to that version. For more information about versions and upgrading, see Releases and Upgrades in SAP HANA Cloud.
SAP HANA Cloud tools such as SAP HANA Cloud Central and SAP HANA cockpit do not need to be upgraded. All new and enhanced features are automatically available to you on their release date. However, some features require a minimum component version and may not be visible until you upgrade your instance.
To learn about what’s new in other SAP Business Technology Platform services, visit the SAP BTP What’s New.
Page size:
25
Showing 1–25 of 153

1
2
3
…
7

Columns:
9 selected
Component	Version	Category	Title	Description	Action	Type	Environment	Release Date
Component	Version	Category	Title	Description	Action	Type	Environment	Release Date
SAP HANA Cloud
Version independent
SAP HANA Cloud Central
	Data Points Metric in the Consumption Monitor
SAP HANA Cloud now tracks SAP-RPT-TS tabular foundation model consumption as data points, a new usage-based billing unit. Data points are visible in the Consumption Monitor alongside memory, compute, storage, and network data transfer.
See Consumption Monitor in SAP HANA Cloud Central.
Info only
New
Other
	Oct 21, 2026
SAP HANA Cloud
Version independent
SAP HANA Cloud Central
	Instance-Specific Certificates and DNS Configuration
You can now configure instance-specific DNS and certificates directly from SAP HANA Cloud Central.
See SAP HANA Database Configuration.
Info only
New
Other
	Oct 21, 2026
SAP HANA Cloud
Version independent
SAP HANA Cloud Central
	Request capacity for 12TB instance on Azure	Before provisioning an SAP HANA database instance with a memory size of 12 TB on Azure, you must complete an additional step to pre-reserve the required hardware needed for your instance. Once the pre-reservation process is complete, you can proceed with provisioning the instance. For more information, see SAP Note 3717342 .
Info only
Changed
Other
	Oct 21, 2026
SAP HANA Cloud
Version independent
SAP HANA Cloud Central
	Enhanced Audit Policy Features
SAP HANA Cloud Central now lets you limit selected data definition actions to specific schemas, or audit data manipulation actions on an object across all schemas by omitting the schema during object selection. A policy must target either specific schemas or all schemas, but not both.
See:
Audit Policies
Auditing Details
Info only
New
Other
	Oct 21, 2026
SAP HANA Cloud
Version independent
SAP HANA Cloud Central
	Multiple Issuer DNs for X.509 Providers
SAP HANA Cloud Central now lets you configure multiple issuer DNs for a single X.509 provider. When creating or editing a provider, you can add or remove issuers using a certificate file, PEM string, or a certificate from the store. The issuer DN is extracted automatically.
See:
Add an X.509 Identity Provider
Identity Providers Details
X.509 Certificate-Based User Authentication
Info only
New
Other
	Oct 21, 2026
SAP HANA Cloud
Version independent
Multitenancy
	Aggregated resource usage
The memory consumption can be displayed including dropped tenants (Total Memory Consumption) and excluding dropped tenants (Memory Consumption).
See: Managing SAP HANA Cloud Database Tenants
Info only
New
Other
	Oct 13, 2026
SAP HANA Cloud
Version independent
Multitenancy
	Database objects browser
Access the Open in Database Objects browser directly from the schema or HDI container page and establish a connection using the latest credential.
See: Managing SAP HANA Cloud Database Tenants
Info only
New
Other
	Oct 13, 2026
SAP HANA Cloud
Version independent
SAP HANA Cloud Central
	Cookie Consent Banner Removal	The cookie consent banner has been removed. Usage data is now collected by default. You can opt out of cookie collection in the Settings dialog. The Functional Cookies toggle is in the Cookies tab.
Info only
Changed
Other
	Oct 7, 2026
SAP HANA Cloud
Version independent
SAP HANA Cloud Central
	Import and Export RDF Files
SAP HANA Cloud Central now supports importing data from RDF files and exporting RDF knowledge graph catalog objects to RDF files. RDF is available as a data type in the create import and export wizards, with support for SAP Data Lake Files, Azure Storage, Amazon S3, and Google Cloud Storage.
See:
Using Import and Export in SAP HANA Cloud Central
Importing Data in HANA Cloud Central
Exporting Data in HANA Cloud Central
Info only
New
Other
	Oct 7, 2026
SAP HANA Cloud
Version independent
SAP HANA Cloud Central
	SQL Script Analyzer in Database Objects	Function and Procedure detail view now contains an additional tab called SQL Script Analysis. In this tab, you can select Analyze SQL Script to run the analysis and populate a table of issues.
Info only
New
Other
	Oct 7, 2026
SAP HANA Cloud
Version independent
SAP HANA Cloud Central
	Data Access Agent alerts
The Alerts app now supports Data Access Agent instances. You can view alerts for your Data Access Agent instances and enable or disable alert rules for these instances. Data Access Agent instances appear in the instance filter grouped under the HANA database instance they're associated with.
See Using Alerts in SAP HANA Cloud Central.
Info only
New
Other
	Oct 7, 2026
SAP HANA Cloud
Version independent
SAP HANA Cloud Central
	Consolidated Trends View in the SQL Statements App
The Performance Heatmap and Statement Trend Chart tabs in the SQL Statement Overview are now combined into a single Trends tab, so you can view heatmap charts and statement trends without switching between tabs.
See:
Monitor and Manage Active SQL Statements
Monitor and Manage Cached SQL Statements
Trace and Manage Expensive SQL Statements
Info only
Changed
Other
	Oct 2, 2026
SAP HANA Cloud
Version independent
SAP HANA Cloud Central
	Improved cube metadata display in Database Objects	New columns have been added to the Attributes, Hierarchies, Variables, and Measures tabs to display additional cube properties in Database Objects.
Info only
New
Other
	Oct 2, 2026
SAP HANA Cloud
Version independent
SAP HANA Cloud Central
	Manage Statement Hints
You can now view, add, enable, disable, and remove SQL statement hints in the SQL Statements app.
See:
Monitoring SQL Statements in SAP HANA Cloud Central
Manage Statement Hints
Info only
New
Other
	Oct 2, 2026
SAP HANA Cloud
Version independent
SAP HANA Cloud Central
	Move Database Tenants Across Subaccounts	In SAP HANA Cloud Central, you can now move tenants to instances in other BTP subaccounts within the same region. The Target Database Instance field in the Move Tenant dialog lists both instances in the current subaccount and instances from other subaccounts that have been shared with the current subaccount via an instance mapping.
Info only
New
Other
	Oct 2, 2026
SAP HANA Cloud
Version independent
SAP HANA Cloud Central
	Preview image files in SQL Console	You can now see a preview of image files in SQL Console.
Info only
New
Other
	Oct 2, 2026
SAP HANA Cloud
Version independent
SAP HANA Cloud Central
	View service managed HDI containers	In the Schemas & HDI Containers app, you can now:
View HDI containers managed using SAP Service Manager instances in your Cloud Foundry spaces separately.
Open a service managed HDI container directly in the SQL console.
See Using Schemas & HDI Containers in SAP HANA Cloud Central.
Info only
New
Other
	Oct 2, 2026
SAP HANA Cloud
Version independent
SAP HANA Cloud Central
	Visualize Data in the SQL console	You can now use the Visualize Data by selecting the  (Visualize Data) icon in the Result toolbar to view statement results as charts and graphs in the SQL Console.
Info only
Changed
Other
	Oct 2, 2026
SAP HANA Cloud
Version independent
SAP HANA Cloud Central
	Three-Level HASH-RANGE-RANGE and HASH-HASH-RANGE Partitioning
You can now partition tables using two new three-level heterogeneous schemes: HASH-RANGE-RANGE and HASH-HASH-RANGE.
See Three-Level HASH-RANGE-RANGE and HASH-HASH-RANGE Partitioning.
Info only
New
Other
	Sep 30, 2026
SAP HANA Cloud
Version independent
Other
	SAP HANA Cloud Agent Memory Service
SAP HANA Cloud now offers Agent Memory Service, a service plan (hana-agent-memory) that gives AI agents persistent memory. Provisioned on SAP BTP through SAP HANA Cloud, it stores durable, semantically searchable memories and chronological messages, associated with an agent and invoker, through a standard OData REST API with OAuth 2.0 authentication.
See SAP HANA Cloud Agent Memory Service Guide.
Info only
New
Other
	Sep 28, 2026
SAP HANA Cloud
Version independent
Administration
	HANA Cloud available in Sovereign Cloud	SAP HANA Cloud is available in the following SAP sovereign cloud landscapes: Australia (AWS), Canada (AWS), United Kingdom (AWS), USA (AWS GovCloud), India (AWS), and Europe (SAP Cloud Infrastructure). For more information, see Data Center Availability in SAP HANA Cloud and Memory and Storage Sizes Supported by SAP HANA Database.
Info only
New
Other
	Sep 23, 2026
SAP HANA Database
2026.28 (QRC 3/2026)
Administration
	Support for small 16GB database instances
You can now provision database instances with 16GB memory for Microsoft Azure regions. Use this option for cost-sensitive workloads that don't require larger instance sizes.
See Managing Smaller SAP HANA Instances.
Info only
New
Cloud Foundry
Other
	Sep 21, 2026
SAP HANA Database
2026.28 (QRC 3/2026)
Alerts and Notifications
	Alert support for Data Access Agent instances
The SAP Alert Notification service for SAP BTP now supports alerts for Data Access Agent instances. Three lifecycle alert rules are available for Data Access Agent instances and can be retrieved and managed via the Alerts API. You can enable or disable these rules per instance, but check interval and severity thresholds cannot be modified.
See SAP Business Accelerator Hub.
Info only
New
Cloud Foundry
Other
	Sep 21, 2026
SAP HANA Database
2026.28 (QRC 3/2026)
Metrics
	Metrics for SAP HANA Data Lake File Services
The Metering API now includes two new metrics for SAP HANA data lake file services: HDLFSNodeRequestCategory1 and HDLFSNodeRequestCategory2, which track the number of object store read and write requests. You can use these metrics to monitor and attribute object store request usage in detail.
See Metering Metrics.
Info only
New
Cloud Foundry
Other
	Sep 21, 2026
SAP HANA Database
2026.28 (QRC 3/2026)
Multi-Region Disaster Recovery
	Near-zero downtime operations on primary source instance
In a multi-region disaster recovery setup, you can upgrade and apply configuration changes without a restart only on the primary region source instance.
See Multi-Region Disaster Recovery.
Info only
New
Cloud Foundry
Other
	Sep 21, 2026
Page size:
25
Showing 1–25 of 153

1
2
3
…
7

Was this What's New helpful?

Yes
No
