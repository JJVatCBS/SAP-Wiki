---
product: SAP Datasphere
title: What's New
url: https://help.sap.com/whats-new/48017b2cc4834fc6b6cae87097bd9e4d?locale=en-US
source_type: SAP Help
---

HomeSAP Datasphere
What's New in SAP DatasphereEnglish
SAP Datasphere constantly delivers new innovations and enhancements. Get an overview of the new and changed features below.

Hide Filters (3)
Table View
Download
Favorite
Subscribe
PDF
Share
Help
Category:
[No selection]
Version:
[No selection]
Release Date:
May 3, 2026–Nov 10, 2026
Reset
Clear
What's New Archive | SAP BDC What’s New
Page size:
25
Showing 1–25 of 109

1
2
3
…
5

Oct 20, 2026
Administration－Assign More Than 100 Spaces to Users
There is no longer any limit to the number of spaces you can assign a user to via scoped roles.
See Create a Scoped Role to Assign Privileges to Users in Spaces.
Info only
2026.22
Data Cataloging－Release State Metadata for SAP Datasphere Views
Users can review release state information for SAP Datasphere views. The release states help catalog users understand the view's lifecycle stage. They can also filter to find views at different release states in their lifecycle.
See Catalog Asset Details.
Info only
2026.22
Data Integration－Connect to External REST APIs via Custom Connections
You can now connect SAP Datasphere to external applications that offer a REST API by creating custom connection types.
A custom connection type is a reusable blueprint that maps external API resources to structured entities, allowing you to load compatible JSON-based data from third-party systems or customer-built REST APIs into the SAP Datasphere object store using replication flows.
Custom connection types extend standard SAP Datasphere-managed connectivity when predefined connection types do not exist. They are available in spaces with storage type SAP HANA Data Lake Files (file spaces). Connections created from a custom connection type are independent of the connection type, meaning that later changes to the connection type do not affect existing connections.
See:
Creating a Custom Connection Type
Create a Connection from a Custom Connection Type
Rest API Custom Connection Sources for Replication Flows
Info only
2026.22
Data Integration－Monitor Task Chain Status with a Graphical Display
The new task chain monitor graphical view feature provides a visual view of a task chain that is representative of the data builder editor.
This helps identify the flow of task chains and provides color coded object level status of tasks in the task chain.
See Monitoring Task Chains.
Info only
2026.22
Data Integration－Automatic Data-Product Provider Connection During Content Transport
The BD Administrator can now define system mappings to help your transported content automatically connect to the correct data products. When you import a content package installed from an SAP Business Data Cloud data product into an SAP Datasphere tenant, SAP Datasphere will automatically connect to the correct data-product provider system instance.
For more information, see System Mapping for Content Transport Between SAP Datasphere Tenants in SAP Business Data Cloud documentation.
Info only
2026.22
Data Integration－Data Pipeline Analyzer Displays Impact on related SAP Analytics Cloud Stories
When issues occur in analytical models or exposed views, related SAP Analytics Cloud stories can be displayed in the impact summary and pipeline graph. This enables you to identify affected analytics content, navigate directly to impacted objects, and gain visibility into downstream business impact from a single location.
See Viewing SAP Analytics Cloud Objects in the Data Pipeline Analyzer.
Info only
2026.22
Data Integration－Define a Time Zone When Deleting Records With Filters on Date or Datetime Columns
If your filter is defined on a column where values are of data type "Date" or "Datetime", you can add a time zone using the selector. A suffix with the time zone in brackets is then added to the column name in the deletion filter.
See:
Controlling Deletion of Local Table Records
Delete Data From Your Local Tables (File)
Info only
2026.22
Data Modeling－Expression Evaluator Task for Dynamic Task Chain Calculation
With the new Expression Evaluator task you can evaluate expressions using input and output parameters within task chains. Use it to transform data, perform calculations, and create conditional values that can be reused as input parameters in subsequent tasks.
See Run Expression Evaluator Tasks in a Task Chain.
Info only
2026.22
Data Modeling－AI SQL Code Generation in Transformation Flows on File
You can now generate SQL code in transformation flows on file by prompting the built-in SAP Business AI. You can create a view from scratch by specifying your sources and what you want to output or modify existing SQL code. CTEs (Common Table Expressions) WITH clauses are supported.
See :
Generate SQL Code with AI in a File Space
Create a SQL View in a Transformation Flow on File
Info only
2026.22
Oct 7, 2026
Business Modeling－Deprecation of the Business Builder
The Business Builder is deprecated and will not receive further updates. We recommend that you migrate your consumption models to analytic models, which are now the preferred way to expose data to SAP Analytics Cloud and other clients, tools and apps.
Info only
2026.21
Data Cataloging－Manual Check for Data Product Schema Changes
Data products sometimes have schema changes that aren't updated in the installed versions. As a result, installed data products can have inconsistencies when compared to the corresponding catalog version.
You can check for schema inconsistencies on the Data Product Access page. Once you identify the affected data products, you can resolve the inconsistencies by updating their installations.
See Resolving Schema Inconsistencies.
Info only
2026.21
Data Integration－Restart Replication Flow Objects via API
You can now restart replication flow objects via API.
See Controlling Replication Flows via API.
Info only
2026.21
Data Integration－Consistent Size Display Across All Monitors
We've standardized size displays across all monitors using a dynamic decimal format for improved readability and consistency.
With dynamic scaling, values are automatically adjusted so they remain between 1 and 1,000. Instead of displaying very large or very small numbers, the unit changes automatically:
KB for sizes greater than 1,000 bytes
MB for sizes greater than 1,000,000 bytes
GB for sizes greater than 1,000,000,000 bytes
TB for sizes greater than 1,000,000,000,000 bytes, etc...
This makes size values easier to read and compare across SAP Datasphere.
Info only
2026.21
Sep 28, 2026
Administration－Simplified Metric Names for Transformation Flow Monitoring
Metric names and values in transformation flow monitoring Run Details now display in simplified format instead of technical wording. For example, EXECUTION_MODE: 0 now shows as Execution Mode: Sequential. You can immediately understand run results without referencing internal documentation.
See Metrics for Transformation Flows.
Info only
2026.20
Data Integration－New Replication Flow Monitoring APIs
You can now start, stop, pause, and resume replication flows (and pause and resume individual replication flow objects) via API.
See Controlling Replication Flows via API.
Info only
2026.20
Data Integration－Use Short-Lived Access Tokens for Google BigQuery Connections
You can now use the Workload Identity Federation authentication type to let replication flows securely access Google BigQuery with short-lived access tokens.
See:
Google BigQuery Connections
Configuring Workload Identity Federation for Google BigQuery Connections
Info only
2026.20
Data Integration－Use OAuth 2.0 Authentication with X.509 Client Certificate for ABAP-based Connections
You can now use authentication type OAuth 2.0 with the Client Credentials with X.509 Client Certificate grant type for SAP ABAP (on-premise), SAP S/4HANA On-Premise, SAP ECC, and SAP BW connections. This certificate-based grant type is the most secure option for the connection types and is selected by default when you choose OAuth 2.0 as the authentication type.
This authentication type is available for connections that use Cloud Connector. For SAP ABAP (on-premise) and SAP S/4HANA On-Premise, the OAuth 2.0 authentication type with client credentials was introduced in an earlier version of SAP Datasphere. For SAP BW and SAP ECC connections, OAuth 2.0 authentication is new and supports both grant types: client credentials and client credentials with X.509 client certificate.
Note the following for all connection types:
Remote tables are not supported with the OAuth 2.0 authentication type. This also applies to model import for SAP S/4HANA connections.
For SAP BW and SAP ECC connections, only replication flows are supported.
For SAP ABAP and SAP S/4HANA On-Premise connections, replication flows and data flows are supported.
When you change an existing connection from basic authentication to authentication type OAuth 2.0, remote tables are disabled. For SAP BW and SAP ECC connections, data flows are also disabled.
See:
SAP ABAP Connections
SAP BW Connections
SAP ECC Connections
SAP S/4HANA On-Premise Connections
Info only
2026.20
Data Marketplace－New API Endpoint and New Command for Data Providers
The API endpoint /dsc/providers/:providerIdentifier/assignUsers is available to assign and activate data provider memberships.
For more information, see the API documentation on the SAP Business Accelerator Hub.
You can also use the command datasphere marketplace providers assign-users in the SAP Datasphere command line interface.
See Managing Data Marketplace Data Providers via the Command Line.
Info only
2026.20
Data Modeling－Tags for Sensitive Data in Analytic Models
Information-sensitive data is now visually highlighted in the analytic model with the tags Sensitive Personal Data and Personal Data.
This improves data security awareness and compliance.
Info only
2026.20
Data Modeling－Export Data of Data Preview
In the data preview of an analytic model, you can export the data as an Excel or CSV file. This enables you to share the intermediate results with colleagues, and to validate the calculations and measures.
See: Preview Data in an Analytic Model
Info only
2026.20
Data Modeling－Data Protection: Tracking of Personal and Sensitive Data in Transformation Flows in SAP HANA Runtime or Apache Spark Runtime
Trace personal and sensitive personal data installed from an SAP BDC data product as it is processed in transformation flows. Flow operators display the personal data tags on relevant columns and these tags are inherited by target tables to which personal data is written.
See :
Creating a Transformation Flow
Creating a Transformation Flow in a File Space
Modeling with Personal Data
Info only
2026.20
Sep 9, 2026
Administration－Object Store Requests Consumed by Category
Object Store Requests are now metered and consumed in three separate categories: Control Plane, Read, and Write. Each category has its own price per 1,000 requests. Previously, all request types were charged at a single blended rate.
You can view your consumption per category in the Capacity Monitor and in the consumption cards on the Tenant Configuration screen.
See Configure the Size of Your SAP Datasphere Tenant
Info only
2026.19
Administration－Certificate-Based Authentication for Database Analysis Users
X.509 certificate-based authentication is now available for database analysis users. This enhancement strengthens security for technical users by reducing reliance on passwords, while maintaining password-based authentication as the default method.
See Create a Database Analysis User to Debug Database Issues.
Info only
2026.19
Data Cataloging－Automatic Extraction of Account Dimension Members from SAP Analytics Cloud Classic Models
When account dimension members are added, deleted, or updated for classic models, the catalog automatically extracts the latest metadata from the SAP Analytics Cloud source system. This ensures that the catalog assets are current with account dimension member changes.
Info only
2026.19
Data Cataloging－Data Product Life Cycle Status
The data product details page shows the lifecycle status. Consumers can filter by lifecycle status, such as active, provisioning, or data-loading. This information helps data stewards track and manage data products throughout their operational lifecycle.
See Data Product Details.
Info only
2026.19
Page size:
25
Showing 1–25 of 109

1
2
3
…
5

Was this What's New helpful?

Yes
No
