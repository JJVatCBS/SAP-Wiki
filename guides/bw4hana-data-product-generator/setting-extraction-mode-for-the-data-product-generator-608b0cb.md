---
guide: Data Product Generator for SAP Business Data Cloud
product: SAP BW/4HANA
title: "Setting Extraction Mode for the Data Product Generator"
page: 608b0cbeb8ce4a59a121563f12a91c43.html
url: https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/608b0cbeb8ce4a59a121563f12a91c43.html?locale=en-US
source_type: SAP Help
---

# Setting Extraction Mode for the Data Product Generator

*Configuring the Data Product Generator · [auf help.sap.com öffnen](https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/608b0cbeb8ce4a59a121563f12a91c43.html?locale=en-US)*

Setting Extraction Mode for the Data Product Generator
-
## Setting Extraction Mode for the Data Product Generator
With the Data Product Generator you can run a full extraction or a delta extraction to
the local table (file). Depending on the InfoProvider you're extracting from, capabilities
for delta extraction are available. You can make the necessary settings in the data
subscription.

### Extraction Modes for the Data Product Generator

There are two types of extraction modes available for the Data Product Generator:

- Full extraction (Full): Extracts all data from the
InfoProvider at once (also called snapshot) in a one-time operation.

- Delta extraction (Delta): Extracts after initial
extraction only delta data from the InfoProvider.

In both modes the extracted data arrives in the inbound buffer of the object store in SAP
Datasphere and you need to schedule and run a merge task (either manually or via
task chain) to merge the new snapshot data or delta data into the local table
(file). (For more information, see [Viewing Local Table (File) and Getting Data Updates](c5b7a4fae2ce4b829914f9f825d6b471.html)).

### Availability of Delta Extraction based on BW System and InfoProvider

Delta extraction is only available for specific InfoProviders based on the BW
system.Caution

Before you try to configure delta extraction for
your data subscription, check the type of InfoProvider you want to extract data
from and the BW system you're on.

Delta Extraction for InfoProviders in SAP BW/4HANA and SAP BW 7.5

|
InfoProvider
| SAP BW/4HANA
| --- |
| SAP BW 7.5
|

|
Standard DataStore object (advanced) (aDSO)
| Yes
| --- |
| Yes
|

|
DataStore object (advanced) (aDSO) of type data mart
| Yes
| --- |
| Yes
|

|
Staging DataStore object (advanced) (aDSOs) with properties Inbound Queue Only,
Compress Data, or Reporting-Enabled
| Yes
| --- |
| Yes
|

|
InfoObjects with Enhanced Master Data Update
| Yes
| --- |
| n/a
|

|
Characteristic InfoObjects with Hierarchies
| No
| --- |
| No
|

|
Characteristic InfoObjects with Master Data and Texts
(Including Language-Independent Texts)
| Yes
| --- |
| Yes
|

|
Standard and Write-Optimized DataStore object (classic) (ODSO)
| n/a
| --- |
| Yes
|

|
InfoCube
| n/a
| --- |
| Yes
|

|
CompositeProvider (HCPR) *
| Yes
| --- |
| Yes
|

|
MultiProvider (MPRO) *
| No
| --- |
| Yes
|

Note

(*) The following restrictions apply to delta extraction capabilities of HCPRs and MPROs:

- Delta extraction from MultiProviders (MPROs) is only supported for MultiProviders that only
contain InfoCubes. For MultiProviders containing other InfoProviders (such
as DataStore objects) or a mix of InfoCubes and other InfoProviders only
full extraction is possible.

- Delta extraction from CompositeProviders (HCPRs) is only supported for
CompositeProviders that only contain InfoCubes, Standard DataStore objects
(advanced) (aDSOs) or Cube-Like DataStore objects (advanced) (aDSOs). In
addition, all contained objects must be of the same type, for example
several InfoCubes. It's not possible to use delta extraction for
CompositeProviders containing a mix of different objects, such as an
InfoCube and a DataStore object (advanced).

- Delta extraction from CompositeProviders (HCPRs) is not supported if the
CompositeProvider contains SAP HANA Views.

### Delta Extraction with Snapshot Data Subscriptions (RSPM-Based)

In addition to the ODP-based delta extraction listed in the table above, delta
extraction is also available for DataStore objects (advanced) (aDSOs) and master
data/texts from BW InfoObjects using the Snapshot source
type. This extraction is based on the RSPM (Request Status and Process Management)
framework and uses SQL services to extract data from the BW source object.

The first run of the data subscription performs a full initial load and stores a
delta pointer in RSPM; each subsequent run reads that delta pointer and extracts
only the records changed since the last successful run. Changed records are applied
to the local table (file) using an upsert/merge strategy (insert for new records,
update for changed records, delete for records flagged for deletion by the
source).

The following types of BW source objects support RSPM-based delta extraction:

- Standard DataStore object (advanced) (aDSO) with change log table

- DataStore object (advanced) (aDSO) of type data mart (Cube-Like aDSO)

- Write-Optimized DataStore object (advanced) (aDSO)

- Master data and texts from BW InfoObjects including language-dependent and
language-independent texts, and time-dependent and time-independent
characteristic attributes

This type of delta extraction however is not supported for non-cumulative aDSOs,
aDSOs with cold store archiving or NLS (Near-Line Storage) archiving, or aDSOs with
DTO configured.

Managing Delta State for Snapshot Data Subscriptions with Delta
Extraction

For data subscriptions using the Snapshot source type with
delta extraction, BW tracks the delta state independently of SAP Datasphere in SAP
Business Data Cloud using the RSPM framework. You can monitor and manage this delta
state in the RSDPS transaction using the Request Management
function.

To open Request Management, go to the RSDPS transaction,
select the data subscription in the list, and choose Goto  Request Management. The screen shows the requests that have been processed for the data
subscription, including the BW request reference and the corresponding ODQ
representatio, the number of records transferred per request, the status of each
request, and the date and time of each request. You can filter the request list by
date and status.

If you need to reset the delta state and restart from an initial load - for example,
after deleting data in the target local table (file) — delete the corresponding
entry in Request Management on the BW side and then run the
data subscription again. The next run will perform a full initial load and create a
new delta pointer.

### Extracting Archived Data from BW Systems

The Data Product Generator can also extract data directly from NLS (Near-Line Storage)
into the local table (files), which applies to both SAP BW 7.5 and SAP BW/4HANA.
This, however, is not possible for data archived with the ADK-based Data Archiving
Process (DAP), which only applies to SAP BW 7.5.

NLS allows you to offload historical or rarely accessed data from SAP HANA, the primary
database used for BW, into a secondary database like SAP IQ while keeping the data
accessible for reporting and analysis. It is the modern data archiving solution
available in SAP BW 7.5 and SAP BW/4HANA.

The classic data archiving in SAP BW 7.5 works through the ADK-based Data Archiving Process
(DAP) and stores archived data outside the BW system. Here, the archived data is not
queryable anymore and therefore not available for reporting and analysis (or
extraction with the Data Product Generator). NLS also uses DAP as an archiving
mechanism, however not the ADK-based DAP from SAP BW 7.5.

### Setting Extraction Mode for Data Subscriptions

You can select the extraction mode for a data subscription when you create it:

- Data Subscriptions app (SAP BW/4HANA Cockpit): If you create a data
subscription in the SAP BW/4HANA Cockpit, you can set the extraction mode in
the Extraction Mode field. For this, you need to
switch to the Settings tab in the Maintain
Subscription screen. (For more information, see [Creating Data Subscriptions](f2e950ed4e8c475b8571478d6c2004c0.html)).

- RSDPS transaction (SAP GUI): If you create a data subscription in the
SAP GUI, you can set the extraction mode in the Extraction
Mode field in the General section of
the Edit Subscription screen. (For more information,
see [Creating Data Subscriptions](f2e950ed4e8c475b8571478d6c2004c0.html)).

Note

You can still change the extraction mode of a data subscription after its
initial creation, but only if you haven't run it yet. After first run, the
extraction mode will become read-only and cannot be changed anymore. (For more
information, see [Editing Data Subscriptions](06b37289aade411c8f289cac7095fc00.html).)

You can also select the extraction mode for data subscriptions in a scenario:

- Scenario Generator view (BW Modeling Tools): If you have created a scenario and want to
generate the associated data subscriptions, you can change the extraction
mode of the individual data subscriptions in the Selection to
Generate Data Subscriptions section of the Object
Relations tab. Here, select the data subscriptions for which
you want to set a different extraction mode, right-click and choose
Edit, then set the extraction mode in the
Extraction Mode field. (For more information, see
[Generating Data Subscriptions](304de2d15cc049578aaafbba420c27d2.html).)

Note

It's not possible to set the extraction mode on scenario-level. If you want to change the
extraction mode from the default (full extraction), you need to edit it for the
individual data subscriptions.
