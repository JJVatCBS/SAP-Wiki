---
guide: Data Product Generator for SAP Business Data Cloud
product: SAP BW/4HANA
title: "Data Subscription (DSUB and SUBS)"
page: 5ad3c27c5f8640b39ba26a838cd93c1b.html
url: https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/5ad3c27c5f8640b39ba26a838cd93c1b.html?locale=en-US
source_type: SAP Help
---

# Data Subscription (DSUB and SUBS)

*Data Subscriptions · [auf help.sap.com öffnen](https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/5ad3c27c5f8640b39ba26a838cd93c1b.html?locale=en-US)*

Data Subscription (DSUB and SUBS)
-
## Data Subscription (DSUB and SUBS)
A data subscription is a new BW object type that allows you to extract data from your BW
system into local tables (file) in the SAP Datasphere system of your SAP Business Data Cloud
formation.

### Type of Data Subscription

Data subscriptions can have two types:

- DSUB () - This is a transportable data subscription which has either been
directly created in the DSUB format or migrated from the SUBS format via a
dedicated migration report. Data subscriptions of type DSUB can be
transported between different systems (e.g. production, development) like
any other TLOGO. With DSUB the data subscriptions also receive a dedicated
TLOGO type (similar to ELEM for BW Queries or ADSO for DataStore objects
(advanced)).

- SUBS () - This is a local data subscription which cannot be transported between
systems. Data subscriptions of type SUBS can be migrated to the TLOGO type
DSUB via a dedicated migration report.
Note

All newly created data
subscriptions will automatically be of the type DSUB. This means [Creating Data Subscriptions](f2e950ed4e8c475b8571478d6c2004c0.html) and [Creating Data Subscriptions from Template](c2c90f4fce964121a50d8f6794ea5dad.html) are now only working
for the type DSUB. Data subscriptions of type SUBS can still be
maintained via [Editing Data Subscriptions](06b37289aade411c8f289cac7095fc00.html).

### Information in a Data Subscription

A data subscription contains the information which source object you want to extract data
from, which fields and filters you have selected to define the dataset to be
extracted, as well as which further settings you have made for the extraction
operation (extraction mode, projection, …).

It doesn't contain the dataset to be extracted itself, but rather the definition of
the extraction operation to be performed on a selected source object.

Some of the information in the data subscription can be manually set while you create the data
subscription (for more information, see [Creating Data Subscriptions](f2e950ed4e8c475b8571478d6c2004c0.html)). Others, such as the technical
name and details about the local table (file) that will be generated during the
extraction operation, will be automatically filled in.

### Properties of a Data Subscription

The information in a data subscription is saved as its properties, which can be accessed
in different ways:

- In the RSDPS transaction by opening the details screen of a data subscription via
Details () or by
opening its edit screen via Edit (). In the edit screen,
you can not only view all properties in a comprehensive format, but also
change the editable ones.

- In the Data Subscriptions app by clicking on any of the data subscriptions in the list.
This opens the Maintain Subscription screen, where
you can view a select amount of properties, as well as change the editable
ones.

You can also view some of the properties as columns in the data subscriptions list, as well as
filter or search the list based on certain fields and values. For more information,
see [Data Subscriptions App in SAP BW/4HANA Cockpit](60146bc2b99941f2bdad39153fca5e9d.html), [RSDPS Transaction in SAP GUI](67d73d2e2086409c8bc06ff79b116476.html) or [BW Data Product Generator Perspective in BW Modeling Tools (BWMT)](21393d96c2f94fdebc20ee3941b4eb02.html).

Properties of a Data Subscription

|
Field
| Information
| --- |
|

|
Technical Name
| Technical name of the data subscription which is generated automatically during its
| --- |
creation.
|

|
Description
| Description of the data subscription which can be manually entered during its
| --- |
creation
|

|
Source Name
| Selected source for the data subscription (InfoProvider from the BW system)
| --- |
|

|
Source Type
| Type of the selected source for the data subscription (Source type for the Data
| --- |
Product Generator is either ODP (Operational Data Provisioning)
for BW InfoProviders or Snapshot for BW InfoObjects including
hierarchies, master data, and texts and DataStore objects
(advanced) (aDSOs).)
|

|
Target Name
| Selected target for the data subscription (Space/Tenant in SAP Datasphere)
| --- |
|

|
Target Type
| Type of the selected target for the data subscription (Target type for the Data
| --- |
Product Generator is always HDLFS (SAP HANA Cloud, data lake
Files))
|

|
Subscription Type
| Type of the data subscription (DSUB/SUBS)
| --- |
|

|
Status
| Status of the data subscription (Active/Inactive)
| --- |
|

|
Extraction Mode
| Extraction mode for the data subscription (Full/Delta)
| --- |
|

|
Scheduling
| Scheduling settings for the data subscription (None/Direct Execution or Process
| --- |
Chain)
|

|
Last Run
| Information on whether the data subscription has been run yet and whether the last
| --- |
run has been successful or not
|

|
Last Changed At
| User who has last changed the data subscription
| --- |
|

|
Last Changed By
| Date and time when the data subscription has been last
| --- |
changed (Timestamp)
|

|
Created At
| Date and time when the data subscription has been created
| --- |
(Timestamp)
|

|
Created By
| User who has created the data subscription
| --- |
|

### Data Subscriptions in the Catalog

If you have configured the metadata extraction from your BW system, you can see the data
subscriptions amongst other assets and data products in the catalog. There you can
view the details of the data subscription by opening the details screen.

Caution

The metadata extraction for data subscriptions is only available on SAP
BW/4HANA 2023 SP04 or higher. This feature works independently from the Data
Product Generator for SAP Business Data Cloud.

Caution

If you want to use this functionality, you first need to
implement SAP Note [3601550](https://me.sap.com/notes/3601550) into your BW system and perform
the manual steps at the end of the SAP Note. In addition, you need to fulfill
all necessary prerequisites to connect a SAP BW/4HANA system to the catalog. For
more information, see [Checking the BW System Setup](https://help.sap.com/docs/SAP_DATASPHERE/aca3ccb4b2f84eb8b6154e8fd2812c0e/ca5e1d2f6c9b47578751ac65da9d895a.html).

To set up the metadata extraction and connect your BW system, follow the detailed procedure in
[Creating a Connection to a BW System](https://help.sap.com/docs/SAP_DATASPHERE/aca3ccb4b2f84eb8b6154e8fd2812c0e/d88d136f6c9e4d59a6ded01408ca5c95.html).

Note

While you need to set up the metadata extraction for your BW system in the SAP
Datasphere tenant, the assets for the data subscriptions will be visible across
all catalog entry points including SAP Datasphere (for modeler users and data
analysts) and the SAP Business Data Cloud cockpit (for administrator
users).
