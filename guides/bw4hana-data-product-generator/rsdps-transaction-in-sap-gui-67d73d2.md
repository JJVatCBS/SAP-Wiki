---
guide: Data Product Generator for SAP Business Data Cloud
product: SAP BW/4HANA
title: "RSDPS Transaction in SAP GUI"
page: 67d73d2e2086409c8bc06ff79b116476.html
url: https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/67d73d2e2086409c8bc06ff79b116476.html?locale=en-US
source_type: SAP Help
---

# RSDPS Transaction in SAP GUI

*Data Subscriptions · [auf help.sap.com öffnen](https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/67d73d2e2086409c8bc06ff79b116476.html?locale=en-US)*

RSDPS Transaction in SAP GUI
-
## RSDPS Transaction in SAP GUI
The RSDPS transaction in the SAP GUI provides BW administrators on an SAP BW or SAP
BW/4HANA system with an advanced interface to view, manage, and maintain data subscriptions.
In the SAP GUI you can also access further functions to maintain targets and mass-delete
data subscriptions based on target.

### Accessing the RSDPS Transaction

You can access the RSDPS transaction in the SAP GUI after logging on to your BW
system.

The main screen of the RSDPS transaction shows the list of all current data
subscriptions in your BW system belonging to the Data Product Generator.

The list view can be filtered according to certain field values (e.g. only show data
subscriptions of type DSUB).

### Data Subscriptions List - Columns and Values

The columns in the data subscriptions list display information about certain
properties of the data subscriptions:Columns in Data Subscriptions List

|
Column
| Value
| --- |
|

|
Selection
| Shows whether data subscription is included in current selection in list.
| --- |
|

|
Subscription
| Technical name of the data subscription.
| --- |
|

|
Type
| Type of the data subscription.
| --- |

- DSUB () -
Transportable data subscription (TLOGO type)

- SUBS () - Local data subscription (Cannot be
transported)

|

|
Long Description
| Description of the data subscription.
| --- |
|

|
Status
| Shows whether the data subscription has been activated or not.
| --- |

- Active () - Data subscription has been
activated and can be run.

- Inactive () - Data subscription still needs to be
activated to be run.

|

|
Revision
| Shows whether A (Active) and M (Modified) versions of data subscription are equal.
| --- |

- Equal () - A und M version of data
subscription have no differences. The object is ready to
be transported.

- Not Equal () - Data subscription has changes in M
version that haven't been activated yet. The object
should be activated before you try to transport it.

|

|
Source Name
| Name of the source object selected for the data subscription.
| --- |
|

|
Target Name
| Name of the target selected for the data subscription.
| --- |
|

|
Delta
| Shows whether delta extraction has been configured for data subscription.
| --- |

- If field is empty, full extraction is set.

- If field shows a checkbox (),
delta extraction is set.

|

|
Owner
| User who owns the data subscription.
| --- |
|

|
Scheduling
| Shows scheduling settings configured for data subscription.
| --- |

- Process Chain () -
Data subscription will be scheduled via process
chain.

- None/Direct Execution () - Data subscription needs to be run
manually via the Run button.

|

|
Last Run
| Shows whether data subscription has already been run.
| --- |

- Not Run () - Data subscription hasn't been run
yet.

- Last Run Successful () - Data subscription has been run yet
and last run was successful.

- Last Run Failed () - Data subscription has been run yet,
but last run has failed.

|

|
Last Changed By
| User who last changed the data subscription.
| --- |
|

|
Last Changed At
| Date and time at which the data subscription has last been
| --- |
changed.
|

### RSDPS Toolbar - Configurations for Data Subscriptions List

You can perform the following configurations on the list of the data subscriptions:

Configurations for Data Subscriptions List

|
Icon
| Configuration
| --- |
|

|

| Select a data subscription from the list and display its
| --- |
details screen. For more information on the shown properties,
see [Data Subscription (DSUB and SUBS)](5ad3c27c5f8640b39ba26a838cd93c1b.html).
|

|

| Save the currently displayed list in a local file (e.g. HTML,
| --- |
Rich Text, …).
|

|

| Select all data subscriptions in the list.
| --- |
|

|

| Deselect all data subscriptions in the list.
| --- |
|

|

| Sort the data subscriptions in the list in ascending order.
| --- |
You can specify the fields for which you want to sort in a
separate screen.
|

|

| Sort the data subscriptions in the list in descending order.
| --- |
You can specify the fields for which you want to sort in a
separate screen.
|

|

| Filter the list of data subscriptions according to certain
| --- |
fields and their values. For example, select the field "Type"
and specify the value "SUBS" to only display data subscriptions
from the old SUBS format that still need to be migrated.
|

|

| Refresh the list of data subscriptions to show latest changes
| --- |
according to new sorting criteria or performed actions.
|

### RSDPS Toolbar - Actions for Data Subscriptions

You can perform the following actions on the data subscriptions:

Actions for Data Subscriptions

|
Icon
| Action
| --- |
|

|

| Create a new data subscription. For more information, see [Creating Data Subscriptions](f2e950ed4e8c475b8571478d6c2004c0.html).
| --- |
|

|

| Create a new data subscription based on a template of an existing data subscription.
| --- |
For more information, see [Creating Data Subscriptions from Template](c2c90f4fce964121a50d8f6794ea5dad.html).
|

|

| Edit the selected data subscription. After the local table (file) has been created
| --- |
and deployed, options for editing become very limited. For more
information, see [Editing Data Subscriptions](06b37289aade411c8f289cac7095fc00.html).
|

|

| Delete the selected data subscription. This doesn't delete the local table (file) if
| --- |
it has already been deployed. For more information, see [Deleting Data Subscriptions](51f2dd2a17a14a43ba265c537cce47ed.html).
|

|

| Check the selected data subscription for any potential issues. In the results screen
| --- |
you can see any warnings or error messages concerning the status
of the source (InfoProvider), the target, the connection to SAP
Datasphere, and the local table (file).
|

|

| Run the selected data subscription. This manually starts an extraction operation from
| --- |
the InfoProvider into the local table (file). Alternatively, you
can also schedule the extraction operation via process
chain.
|

|

| Manually reset delta extractions for the selected data subscription. This is only
| --- |
relevant if you have delta extraction enabled as the extraction
mode. For more information, see [Setting Extraction Mode for the Data Product Generator](608b0cbeb8ce4a59a121563f12a91c43.html).
|

|

| View more information about the last run for the selected data subscriptions. This is
| --- |
only possible for data subscriptions you have already run,
otherwise you will receive an error message.
|

|

| View the data in the local table (file) of the selected data subscription. For more
| --- |
information, see [Viewing Local Table (File) and Getting Data Updates](c5b7a4fae2ce4b829914f9f825d6b471.html).
|

### SAP GUI Toolbar - Access to other RSDPS Programs

In the topbar of the SAP GUI in the RSDPS transaction, you have access to further
programs related to the Data Product Generator and the data subscriptions.

Select Goto and from there access:

- Maintain Target System: Lets you create new targets
for the Data Product Generator, as well as view and maintain existing ones.
For more information, see [Configuring Targets for the Data Product Generator](4da38647b3d041728236df20d5a0308b.html).

- Mass-Delete Data Subscriptions by Target: Lets you
mass-delete all data subscriptions for one target. For more information, see
[Mass Deleting Data Subscriptions by Target](a51ba4f698d44ccc9b71d06d0050d3d1.html).

- Unlock Local Tables (File) without Data Subscription:
Lets you unlock local tables (file) in SAP Datasphere in SAP Business Data
Cloud that have remained locked after their data subscription in the BW system
was deleted. For more information, see
[Unlocking Local Tables
(File) with Missing Data Subscription](ec61e47e062c41d68585343778350823.html).
