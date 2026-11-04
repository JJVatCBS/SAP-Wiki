---
guide: Data Product Generator for SAP Business Data Cloud
product: SAP BW/4HANA
title: "Creating Scenarios"
page: 27e24efbd818463b834a1000bbaf3854.html
url: https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/27e24efbd818463b834a1000bbaf3854.html?locale=en-US
source_type: SAP Help
---

# Creating Scenarios

*Using Scenario Generator · [auf help.sap.com öffnen](https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/27e24efbd818463b834a1000bbaf3854.html?locale=en-US)*

Creating Scenarios
-
## Creating Scenarios
You can create a scenario for a BW model in the Scenario Core Objects tab of the
Scenario Generator view in the BW Modeling Tools. By creating a scenario, all dependent
objects and existing data subscriptions for the BW model are collected and the scenario tree
is built.

### Prerequisites

- The BW modeler user has installed the BW Modeling Tools in the latest version or
upgraded the existing installation to the latest version and can access the
Scenario Generator and Data Subscriptions views in the BW Modeling Tools. The
minimum required version is BWMT 1.27. (For more information, see [BW Data Product Generator Perspective in BW Modeling Tools (BWMT)](21393d96c2f94fdebc20ee3941b4eb02.html).)

- The BW modeler user has created BW objects, such as InfoObjects, DataStore
objects (advanced) (aDSOs), or CompositeProviders which are available in the BW
Modeling Tools.

- The BW administrator has set up and configured the Data Product Generator for
SAP Business Data Cloud. (For more information, see [Configuring the Data Product Generator](8586340e2bf647d783e4cf506559c25a.html)).

### Context

In the Scenario Core Objects tab of the Scenario Generator you can
create new scenarios by adding BW objects (such as InfoObjects, DataStore objects
(advanced) (aDSOs) and CompositeProviders) from your BW system to the object list.
Via Collect you can built the scenario tree out of the BW
objects in the object list. Depending on the settings you have made, existing data
subscriptions and dependent objects of the BW models are collected and shown as
dependencies of the top-level objects.

On a scenario-level you can also make general settings for the data subscriptions to
be generated for the scenario, including choosing the target and the process chain
variant. Further settings for the data subscriptions can be made once you have built
the scenario tree and the data subscriptions list.

### Procedure

-
Open the BW Modeling Tools and access the Scenario Generator view, either by
searching for it via CTRL+3 or selecting it under Window  Show View  Other...  Business Warehouse  Scenario Generator (Data Subscriptions).

-
Go to the tab Scenario Core Objects.

-
Select Add BW Object (
![Bild](https://help.sap.com/doc/ed919380760a44388ab90e6bb3e7480a/latest/en-US/loio52f06d88d31e49a8b380de7a6cbc3fe4_LowRes.png)
) by clicking on the icon in
the top bar or by right-clicking on the objects list and choosing the menu
option.

-
Search for the BW objects you want to add and confirm your selection. You can
add one or multiple BW models to the scenario of all previously existing ones in
your BW system.
Added objects will appear in the object list on the left side. List entries include
the name and the type of the BW object.If you right-click on the object list,
you can access further options:

- Add Object List: Open a dialogue to access all saved object lists
on your BW system, download these lists as files to your local
machine to save them permanently in-between sessions, and restore
lists previously saved as files.

- Copy List: Copy the currently displayed object list to the
clipboard. If you copy the current list, you can also access it in
the Add Object List screen where you can save
it permanently on your local machine to restore it in later sessions
in the BW Modeling Tools.

- Paste List: Paste the previously copied list
from the clipboard.

- Remove: Remove the selected BW object from
the list again.

-
Once you have completed the object list with all BW objects you want to include
in the scenario, you can make further settings to build the scenario tree:

-
Select the Collection Grouping to define whether
the scenario tree should only be built from the selected BW objects or
should also include further objects along the data flow before or
afterwards.

|
Collection Grouping
| Result
| --- |
|

|
Only Necessary Objects
| The scenario will only include the necessary objects in the context of the
| --- |
selected BW objects. This is the recommended
mode.
|

|
Data Flow Before and Afterwards
| The scenario tree include the selected BW objects and any other objects related to
| --- |
them upstream or downstream in the data
flow.
|

|
Data Flow Before
| The scenario will include the selected BW objects and any other objects related to
| --- |
them upstream in the data flow.
|

|
Data Flow Before (Direct)
| The scenario will include the selected BW objects and any other objects directly
| --- |
related to them upstream in the data flow.
|

|
Data Flow Afterwards
| The scenario will include the selected BW objects and any other objects related to
| --- |
them downstream in the data flow.
|

-
Select the Association Levels to define the
amount of levels included in the dependency tree. The default number of
levels is 4. The minimum number is 1 and you can adjust the setting
counting upwards in steps of 1.

-
Select the target for the data subscriptions in the scenario. Via
Browse you can choose from all existing targets in
your BW system.

Note

You can still adjust the target for the individual data subscriptions
later on in the Selection to Generate Data
Subscriptions section in the Object
Relations tab. (For more information, see [Generating Data Subscriptions](304de2d15cc049578aaafbba420c27d2.html).)

-
(Optional) Select the process chain variant for the scenario. Via
Browse you can choose from all available variants for
running the data subscriptions.

Note

While it's mandatory to select a target, you don't need to select a
process chain variant. If you leave the field empty, the data subscriptions
can be run manually and are not executable via process chain.

-
(Optional) Tick off the check boxes for further settings for the
scenario:

|
Setting
| Result
| --- |
|

|
Perform Target Check
| Checks connection for selected target in advance. This allows to avoid or resolve
| --- |
connection errors due to faulty target configuration before
even trying to generate new data subscriptions for the
scenario. You are forced to select a valid or correctly
connected target, making operations with the scenario easier
and less prone to throwing errors.
|

|
Consider Transport Configuration
| Activates transport handling for data subscriptions in
| --- |
the scenario. This allows to assign packages to the data
subscriptions other than $TMP (local package), which makes
them transportable between systems.
|

|
Use Existing Data Subscriptions
| Includes existing data subscriptions in the scenario tree
| --- |
so they won't be duplicated. For example, if you want to
rebuilt a DataStore object (advanced) (aDSO) which includes
the InfoObject 0COUNTRY and the InfoObject already has an
existing data subscription in the BW system, it can be
reused for the scenario and doesn't need to be newly
generated. If you select this option the scenario tree in
Collected Objects will also show
the existing data subscriptions for the objects.
|

|
Hide Non-Relevant Objects
| Hides objects from the scenario tree for which you can't
| --- |
create any data subscriptions, such as 0CALDAY. This allows
to build a cleaner scenario tree. While all dependent
objects are always collected, they don't necessarily need to
be shown in the scenario tree, which is why this option is
active by default.
|

-
Choose Collect to collect all top-level objects and
dependent objects of the selected BW models and create the scenario.

-
Switch to the tab Object Relations and go to
Collected Objects to view the scenario tree.
You can toggle dependent objects and existing data subscriptions for the top-level
objects. Existing data subscriptions are only shown in the table if you have
selected Use Existing Data Subscriptions in the scenario
options. The table shows more details about the collected objects and data
subscriptions in several columns.

|
Column
| Value
| --- |
|

|
Object Name
| Technical name of the BW object, dependent object, or
| --- |
data subscription.
|

|
Data Subscription
| If a data subscription is already existing for the
| --- |
object, this column will receive a green check
mark.
Note

The green check marks will only be visible,
if you have selected Use Existing Data
Subscriptions in the scenario
options.
|

|
Target Name
| The target of the data subscription, if it already exists
| --- |
for the object.
Note

This column will only be used if you
have selected Use Existing Data
Subscriptions in the scenario
options.
|

|
Process Chain Variant
| The process chain variant of the data subscription, if it
| --- |
already exists for the object.
Note

This column will only be
used if you have selected Use Existing Data
Subscriptions in the scenario
options.
|

|
Association Type
| How the top-level object and dependent object are related
| --- |
to each other.
|

### Results

You have created the scenario with the selected BW objects and settings. If you want
to generate the corresponding data subscriptions, you need to select
Generate in the Object Relations tab.
(For more information, see [Generating Data Subscriptions](304de2d15cc049578aaafbba420c27d2.html).)
