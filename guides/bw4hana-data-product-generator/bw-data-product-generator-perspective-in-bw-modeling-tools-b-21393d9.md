---
guide: Data Product Generator for SAP Business Data Cloud
product: SAP BW/4HANA
title: "BW Data Product Generator Perspective in BW Modeling Tools (BWMT)"
page: 21393d96c2f94fdebc20ee3941b4eb02.html
url: https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/21393d96c2f94fdebc20ee3941b4eb02.html?locale=en-US
source_type: SAP Help
---

# BW Data Product Generator Perspective in BW Modeling Tools (BWMT)

*Data Subscriptions · [auf help.sap.com öffnen](https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/21393d96c2f94fdebc20ee3941b4eb02.html?locale=en-US)*

BW Data Product Generator Perspective in BW Modeling Tools (BWMT)
-
## BW Data Product Generator Perspective in BW Modeling Tools (BWMT)
The Scenario Generator in the BW
Modeling Tools (BWMT) provides BW modelers on an SAP BW or SAP BW/4HANA system
with a dedicated Eclipse view to mass generate data subscriptions based on object
dependencies and existing data subscriptions. The Data
Subscriptions view allows to view and mass maintain existing data subscriptions.
Both views are part of the BW Data Product Generator perspective, which
grants quick access to both Eclipse views and gives users a singular entry point to all Data
Product Generator functionalities in the BW Modeling Tools.

### Prerequisites/Installation

As a prerequisite for using the Scenario Generator and the
Data Subscriptions views, you need to install the
BW Modeling Tools in the latest version or upgrade
your existing installation to the latest version BWMT 1.27.

To use the BW Data Product Generator perspective, you need to at least
upgrade the BW Modeling Tools to the patch version BWMT 1.27.1.

The new version can be downloaded from SAP Marketplace or [SAP
Toolspage](https://tools.hana.ondemand.com/).

After first-time installation you need to connect your BW system to the BW Modeling
Tools interface by creating an associated BW project.

For more information on the installation and upgrade process, see [Installation Guide for BW Modeling Tools](https://help.sap.com/docs/SAP_BW4HANA/841c96bc79644fcfb9fa7103aad9c15b/36879a66ff114d8fbbde7431c671fb70.html).

### Accessing the BW Data Product Generator Perspective

The BW Data Product Generator perspective provides BW modelers with a comprehensive
interface to quickly access all Data Product Generator-related capabilities within
the BW Modeling Tools, including the Eclipse views for the Scenario Generator and
the Data Subscriptions.

The perspective opens with a welcoming screen showing further information about the Data
Product Generator and instructions for first usage. In addition, it does open the
two Eclipse views by default. However, the Eclipse views can also be opened and used
independently from this on their own.

To access the BW Data Product Generator perspective, go to Window  Perspective  Open Perspective  Other... and select BW Data Product Generator.

Alternatively, you can also open it by selecting the Open
Perspective icon () in the top bar and
choosing BW Data Product Generator.

### Accessing the Eclipse Views

In addition to being part of the BW Data Product Generator perspective, the Eclipse views can
also be opened and used on their own.

To access the Eclipse views on their own, go to Window  Show View   Other...:

- Select Business Warehouse  Data Subscriptions to open the Data Subscriptions
view.

- Select Business Warehouse  Scenario Generator (Data Subscriptions) to open the Scenario Generator
view.

Alternatively, you can also find the views via search, which can be opened by using
CTRL+3 or by selecting the search icon ().

### Scenario Generator View

With the Scenario Generator view you can select existing BW
models and create scenarios out of them, as well as generate all required data
subscriptions to represent these BW models in one operation.

The Scenario Generator view consists of three tabs:

- Scenario Core Objects: Select the BW objects you want to create a
scenario for and make general settings for scenario creation. If you choose
Collect, the Scenario
Generator will collect all dependent objects for the selected
top-level objects and create the scenario tree, visible in Object
Relations.

- Object Relations:

- Collected Objects: View the scenario tree for
the selected BW objects after you have collected all dependent
objects. Here, you can also view whether any of the top-level
objects or dependent objects have existing data subscriptions.

- Selection to Generate Data Subscriptions:
Select data subscriptions to be generated to reconstruct the BW
models, assign them to packages, and change their properties. If you
choose Generate, the Scenario Generator will create all these data
subscriptions in one operation.

- Messages: View all error messages, warnings, and confirmations
related to operations performed by the Scenario
Generator. This lets you debug in case you encounter errors
while creating a scenario or generating the data subscriptions.

For more information on the workflow, see [Using Scenario Generator](7f1a099f66a54e67b4d7a71aa6e954c5.html).

### Data Subscriptions View

With the Data Subscriptions view you can get an overview of
existing data subscriptions in your BW system, as well as mass maintain them.

The main screen of the Data Subscriptions view lists all
available data subscriptions for one BW project.

In the field BW Project you can choose for which BW project
you want to display the data subscriptions. A BW project corresponds with a
connection to a specific BW system.

Data Subscriptions List

The columns in the data subscriptions list display information about certain properties of the
data subscriptions.

Columns in Data Subscriptions List

|
Column
| Value
| --- |
|

|
Subscription
| Information about the data subscription.
| --- |

- Technical name of the data subscription, shown
greyed out and in brackets before the
description.

- Description of the data subscription which has been
defined by the customer.

- InfoProvider associated with the data subscription,
shown in braces behind the description.

|

|
Status
| Shows whether the data subscription has been activated or
| --- |
not.
|

|
Package
| Package to which the data subscription belongs to. The default package is the local
| --- |
package $TMP. which indicates the object is local and cannot be
transported to other systems.
|

|
Master Language
| Original language in which the data subscription was created. Descriptions, texts,
| --- |
and metadata are mainly in that language.

- E - Object has been created in
English.

- D - Object has been created in
German.

|

|
Scenario
| Scenario to which the data subscription belongs to.
| --- |
Note

This column is only visible
if you have selected Read Scenario
References in Data Subscriptions
Preferences.
|

|
Source Object
| Name of the source object selected for the data subscription.
| --- |
|

|
Target Name
| Name of the target selected for the data
| --- |
subscription.
|

|
Delta Runtime
| Shows whether delta extraction has been configured for data
| --- |
subscription.

- Full - Full extraction has been set.

- Delta - Delta extraction has been set.

|

|
Owner
| User who owns the data subscription.
| --- |
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

|
Last Run
| Shows whether data subscription has already been run and the result of the last run.
| --- |

- No Run () - Data subscription hasn't been run
yet.

- Success () - Data subscription has been run
yet and last run was successful.

- Error () - Data subscription has been run
yet, but last run has failed.

Note

This column is only visible if you have selected
Show Last Run Status in
Data Subscription
Preferences.

|

|
Local Table (File)
| CTRL + Click on Show Local Table (File) to open the local
| --- |
table (file) in the SAP Datasphere tenant.
|

|
Local Table State
| Shows the status of the local table (file) that has been created or deployed for the
| --- |
data subscription.
Note

This column is only visible if you have
selected Show Local Table Status in
Data Subscription
Preferences.
|

Configurations for Data Subscriptions List

The data subscriptions list can be configured and customized based on certain criteria.

- In the Filter Pattern field above the list, you can
enter any filter value to filter the displayed list.

- If you click on any of the column headers, you can sort the list based on
the values in this field in ascending or descending order. Clicking on the
column header again will reverse the sorting order based on the previous
configuration.

- In the top bar of the Data Subscriptions view, you can access
further options:

- Refresh () - Refresh the list of data subscriptions to see
latest changes or results of performed actions.

- Open Link in Browser () -
Open the main screen of the Data Subscriptions app in the SAP
BW/4HANA Cockpit. (For more information, see [Data Subscriptions App in SAP BW/4HANA Cockpit](60146bc2b99941f2bdad39153fca5e9d.html)).

- Preferences () - Open the
Data Subscriptions Preferences menu to
adjust columns and information displayed in the list.

- If you right-click on the data subscriptions in the list, you can make additional settings:

- Select Show Scenario Subscriptions Only to
only display data subscriptions in the list which belong to a
scenario, that is, have been created via the Scenario Generator.

Note

This option is only available if you have selected
Read Scenario References in
Data Subscriptions
Preferences.

- Select Preferences to open the
Data Subscriptions Preferences menu as an
alternative way to using the icon in the top bar.

Data Subscription Preferences

|
Menu Option
| Result
| --- |
|

|
Show Local Table Status
| Adds the column Local Table Status to
| --- |
the data subscriptions list where you can view the status of the
local tables (file) that have been created for the data
subscriptions.
Caution

Only use this option if
you really require this information. Retrieving and
displaying the status of the local tables (file) can take
significant time and processing power to complete and you
might have to wait for a while till you can see
results.
|

|
Show Last Run Status
| Adds the column Last Run to the data
| --- |
subscriptions list where you can view whether the data
subscription already has been run and if that last run has been
successful or not.
|

|
Show Active Version
| Displays data subscriptions in A (Active) version in the
| --- |
list. By default the list displays data subscriptions in M
(Modified) version. This setting changes the default
display.
Note

You can see which version is displayed in the
line below the list. Object version
'M' corresponds with the default setting of
only M versions being shown. Object version
'A' corresponds with the alternate setting
of A versions being shown.
|

|
Read Scenario References
| Retrieve information about the associated scenarios of the
| --- |
data subscriptions (if they have been created via the Scenario
Generator). This setting adds the
Scenario column to the data
subscriptions list, as well as makes it possible to use the
options Show Scenario Subscriptions Only,
Show Scenario, and Delete
Scenario.
|

|
Read Only Own
| Display only data subscriptions which have either been
| --- |
created or last changed by the user. This information can also
be viewed in the columns Owner and
Last Changed By.
|

Actions for Data Subscriptions

If you right-click on any of data subscriptions in the list, you can access a menu to perform
actions on one or multiple selected data subscriptions.Tip

If you press
CTRL and click on the data subscriptions, you can select
multiple data subscriptions at once and perform an action on these. This lets
you mass maintain data subscriptions in the Data
Subscriptions view, for example, delete multiple data subscriptions
at once.

Actions for Data Subscriptions

|
Menu Option
| Action
| --- |
|

|
Find Parent Scenarios
| Display a list of parent data subscriptions belonging to the same scenario as the
| --- |
selected data subscription.
|

|
Copy Object Name
| Copy the technical name of the selected data subscription.
| --- |
|

|
Copy Cell
| Copy the cell content of the selected cell, for example, the package name or the
| --- |
owner name.
|

|
Copy Link
| Copy the URL of the Maintain Subscription screen of the data
| --- |
subscription in the SAP BW/4HANA Cockpit.
|

|
Open in Browser
| Open the data subscription in the SAP BW/4HANA Cockpit in the Maintain
| --- |
Subscription screen, where you can view further
details as well as edit some of the properties.
|

|
Activate
| Activate the selected data subscriptions to make them executable after they have been
| --- |
created or changed. This changes their status from
Inactive to
Active.
Tip

Select
multiple data subscriptions at once via CTRL +
Click to mass activate data
subscriptions.
|

|
Deactivate
| Deactivate the selected data subscriptions to make them not executable. This changes
| --- |
their status from Active to
Inactive.
|

|
Refresh
| Refresh the entry of the data subscription to see latest changes or results of
| --- |
performed actions.
|

|
Delete
| Delete the selected data subscriptions. This doesn't delete the local table (file) if
| --- |
it has already been deployed.
Tip

Select multiple
data subscriptions at once via CTRL + Click
to mass delete data subscriptions.
|

|
Delete Scenario
| Delete the associated scenario of the data subscription. You need to confirm the
| --- |
deletion before you can carry out the action.
Note

This option
is only available if you have selected Read
Scenario References in Data
Subscriptions Preferences.
|
