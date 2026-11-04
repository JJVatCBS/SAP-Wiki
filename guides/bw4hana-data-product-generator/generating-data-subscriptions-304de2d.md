---
guide: Data Product Generator for SAP Business Data Cloud
product: SAP BW/4HANA
title: "Generating Data Subscriptions"
page: 304de2d15cc049578aaafbba420c27d2.html
url: https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/304de2d15cc049578aaafbba420c27d2.html?locale=en-US
source_type: SAP Help
---

# Generating Data Subscriptions

*Using Scenario Generator · [auf help.sap.com öffnen](https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/304de2d15cc049578aaafbba420c27d2.html?locale=en-US)*

Generating Data Subscriptions
-
## Generating Data Subscriptions
You can generate the data subscriptions for the scenario in the Object Relations tab of
the Scenario Generator view in the BW Modeling Tools. Through this you can create all data
subscriptions of the scenario in at once in a single operation.

### Prerequisites

- The BW modeler user has installed the BW Modeling Tools in the latest version or
upgraded the existing installation to the latest version and can access the
Scenario Generator and Data Subscriptions views in the BW Modeling Tools. The
minimum required version is BWMT 1.27. (For more information, see [BW Data Product Generator Perspective in BW Modeling Tools (BWMT)](21393d96c2f94fdebc20ee3941b4eb02.html).)

- The BW administrator has set up and configured the Data Product Generator for
SAP Business Data Cloud. (For more information, see [Configuring the Data Product Generator](8586340e2bf647d783e4cf506559c25a.html)).

- The BW modeler has created a scenario out of one or multiple BW models and collected all
dependent objects and references. (For more information, see [Creating Scenarios](27e24efbd818463b834a1000bbaf3854.html)).

### Context

In the Object Relations tab of the Scenario Generator you can generate
all required data subscriptions for a scenario. In addition to the general settings
you have made on scenario-level, you can customize settings for the individual data
subscriptions including description, extraction mode, process chain variant,
selections, projection, target, and package.

All data subscriptions for the scenario are shown in a list under
Selection to Generate Data Subscriptions. Here, you can
view a select amount of their properties as well as perform mass operations, such as
mass assigning new packages. The button Generate starts the
operation to generate the data subscriptions for the scenario. The results of the
operation will be shown in the Messages tab of the Scenario
Generator.

### Procedure

-
Open the BW Modeling Tools and access the Scenario Generator view, either by
searching for it via CTRL+3 or selecting it under Window  Show View  Other...  Business Warehouse  Scenario Generator (Data Subscriptions).

-
Go to the section Selection to Generate Data
Subscriptions in the tab Object
Relations.
Here, you can preview all data subscriptions that will be created for the selected
BW models. The list doesn't only show data subscriptions for the top-level
objects, but also for dependent objects, which you can see if you toggle the
data subscription of the top-level object.The data subscriptions list has the
following columns with more details:

|
Column
| Information
| --- |
|

|
Data Subscription
| Shows the preliminary technical name of the data subscriptions in brackets, as well
| --- |
as the description, and the name of the source object in
braces.
The preliminary technical name is
auto-generated and cannot be changed. The
description is customer-defined and can still be
edited.
|

|
Status
| Shows the status of the to-be-created data
| --- |
subscriptions.

indicates the data subscription is new and will be
freshly created if you perform the
operation.
|

|
Selections
| Shows if you have defined selections for the data
| --- |
subscription. With a selection you can limit the dataset
to be extracted from the InfoProvider by selecting
certain fields and adding conditions for extracting data
from them.

indicates selections have been defined, otherwise
the field will be empty.
|

|
Projection
| Shows if you have defined a projection for the data
| --- |
subscription. With a projection you can limit the
dataset to be provisioned from the InfoProvider by
selecting certain fields that should be included or
excluded.

indicates a projection has been defined, in case of
a full projection (default setting) the field will
be empty.
|

|
BW Object
| Shows the name of the source object (BW InfoProvider)
| --- |
for the data subscription, as well as the object type.
The object type is visible as an icon in front of the
object name and as the TLOGO type in braces after it
(e.g. ADSO, IOBJ).
The BW object cannot be edited
anymore, as it is set via the scenario
tree.
|

|
Target Name
| Shows the name of the target you have selected for the data subscription.
| --- |
The
target shown here will be the one you have selected
generally for the scenario. You can still edit the
targets as long as you ensure all the data
subscriptions in the scenario have the same
target.
|

|
Package
| Shows the name of the package the data subscription
| --- |
belongs to.
The $TMP package is the local package and
indicates the data subscriptions are local objects
and cannot be transported. To make them
transportable, you need to select a different
package.
Packages can be assigned individually
or mass assigned to multiple data subscriptions at
once in the list.
|

Under the list you can see the overall number of data
subscriptions in the scenario, as well as the number of references between them
or other existing data subscriptions.Via the field Filter
Pattern you can filter the list according to the entered
filter value.

-
Select the Mode for the data subscription
generation.

|
Mode
| Result
| --- |
|

|
No Activation
| The data subscriptions won't be activated during the operation and you need to
| --- |
activate them manually afterwards.
|

|
Activate Directly
| The data subscriptions will be activated directly during
| --- |
the operation and are immediately executable.
|

|
Activate in Background
| The data subscriptions will be activated in the
| --- |
background during or after the operation and will be
executable afterwards.
|

Caution

The option Activate Directly takes a
lot of time and processing power, so choosing Activate in
Background is nearly always preferred to save computing
resources.

-
(Optional) Edit individual data subscriptions in the data subscriptions
list.
Before generating the data subscriptions, you can still edit the
settings for individual data subscriptions in addition to having made
generalized settings in the Scenario Core Objects
tab.Select a data subscription and right-click to access further
options:

- Edit: Change advanced settings of the data subscription.

|
Setting
| Options
| --- |
|

|
Description
| Change the description of the data
| --- |
subscription.
|

|
Package
| Select a new package for the data
| --- |
subscription.
Via Browse
you can search for existing packages in your BW
system.
|

|
Extraction Mode
| Choose between Full
| --- |
and Delta as extraction
mode.
For more information, see [Setting Extraction Mode for the Data Product Generator](608b0cbeb8ce4a59a121563f12a91c43.html).
|

|
Process Chain Variant
| Select a process chain if you want to
| --- |
schedule the extraction operation of the data
subscription.
Via Browse
you can select from all existing process chain
variants in your BW system.
Via
Remove you can remove the
process chain again to run the data subscription
manually.
|

|
Target Name
| Select a different target for the data subscription.
| --- |
Via
Browse you can choose from
all existing targets in your BW system.Caution

The data subscriptions belonging to
one scenario must all have the same target,
otherwise you will receive an error message if you
try to generate the data subscriptions and cannot
complete the operation.

|

|
Selections
| Click on Edit to
| --- |
define a new selection for the data
subscription.
On the left side, select the field
for which you want to limit the to-be-extracted
dataset.
Under Add New
Selection, enter the limiting
condition and value:

- Equal: Enter a certain
value the field value must be equal to.

- Between: Enter a
certain value range the field value must lie in
between.

- Starts With: Enter a
certain value the field value must start
with.

Select Add to add
the new selection. You can add multiple
selections. The selections including the field,
limiting condition, and value will be shown in a
list on the right side. If you right-click on the
list, you can remove a specific selection again
via Remove, or remove all
selections at once via Remove
All.
Once you're finished,
select Apply to apply the
defined selections.
|

|
Projections
| Click on Edit to add a
| --- |
projection for the data subscription.
The
default setting is Full
Projection, which means the full
dataset will be provisioned.
To define a
different projection, deselect Full
Projection. You can now select the
provisioned dataset from all existing fields. The
key field is marked up with a key icon and must be
selected as a mandatory field.
Once you're
finished, select Apply to
apply the defined projection.
|

- Copy Name: Copy the technical name of the
data subscription to the clipboard.

- Replace: Replace the data subscription with
another one matching the selected criteria. The new data
subscription must have the same BW project, source object, and
target as the old one.

- Replace Multiple: Replace multiple data
subscriptions in the list at once with another one matching the
selected criteria. The new data subscription must have the same BW
project, source object, and target as the old ones. In the selection
dialog you can also preview details such as projection and selection
to match existing configurations of the data subscriptions.

- Remove: Remove the data subscription from the
scenario.

Tip

Via CTRL + Click you can select multiple data subscriptions
in the list at once, as well as edit them simultaneously. This allows
you to apply changes (such as a choosing a certain package) to multiple
data subscriptions without affecting the whole list.

-
(Optional) Check assigned packages for the data subscriptions and mass reassign
packages.
It's best practice to assign all data subscriptions in one scenario to the same
package as this enables them to be transported together (so you can reconstruct
the BW model in other systems as well). Before generating the data
subscriptions, you should check whether the assigned packages have any
inconsistencies.To check and assign packages, right-click on the data
subscriptions list and choose:

- Check Packages: Check all packages in the
scenario for inconsistencies. The results will be displayed in an
informational message.

- Assign Package (Changed Only): Select a
package and mass assign it to all data subscriptions in the list
that have been changed for the scenario. This includes data
subscriptions that will be newly created.

- Assign Package (Local Only): Select a package
and mass assign it to all data subscriptions in the list that are
currently assigned to the local package $TMP. This allows you to
mass replace $TMP assignments in one operation.

In addition, you can assign a new package to an individual data
subscription in the list by right-clicking and choosing Edit  Package  Browse.

-
Once you're finished with all settings, choose Generate
to generate all required data subscriptions for constructing the scenario.
The results of the operation will be shown in the Messages
tab of the Scenario Generator. Here you can see which data subscriptions have
been generated successfully, as well as the BW object they correspond with, and
their proper technical name. If the creation has failed, you can view the error
messages and warnings to understand what went wrong.

### Results

The generated data subscriptions for the scenario are now available on your BW system
and can be found in the Data Subscriptions view in the BW Modeling Tools ([BW Data Product Generator Perspective in BW Modeling Tools (BWMT)](21393d96c2f94fdebc20ee3941b4eb02.html)), the Data Subscriptions app in the
SAP BW/4HANA Cockpit ([Data Subscriptions App in SAP BW/4HANA Cockpit](60146bc2b99941f2bdad39153fca5e9d.html)), and the
RSDPS transaction in the SAP GUI ([RSDPS Transaction in SAP GUI](67d73d2e2086409c8bc06ff79b116476.html)).The scenario data subscriptions can be edited ([Editing Data Subscriptions](06b37289aade411c8f289cac7095fc00.html)) and deleted ([Deleting Data Subscriptions](51f2dd2a17a14a43ba265c537cce47ed.html)) just like any other data
subscriptions.
Unless you have chosen Activate Directly
or Activate in Background as Mode, you
still need to activate the data subscriptions to make them executable. You can mass
activate the data subscriptions in the Data Subscriptions view in the BW Modeling
Tools or individually in the SAP GUI and in the SAP BW/4HANA Cockpit.

Generating the data subscriptions doesn't automatically run them as well. You
still need to do this manually afterwards to create the local tables (file) and
extract the data from the InfoProviders to reconstruct the BW model. The data
subscriptions can only be run in the SAP GUI or in the SAP BW/4HANA
Cockpit.
