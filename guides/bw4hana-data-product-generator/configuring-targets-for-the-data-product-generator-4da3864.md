---
guide: Data Product Generator for SAP Business Data Cloud
product: SAP BW/4HANA
title: "Configuring Targets for the Data Product Generator"
page: 4da38647b3d041728236df20d5a0308b.html
url: https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/4da38647b3d041728236df20d5a0308b.html?locale=en-US
source_type: SAP Help
---

# Configuring Targets for the Data Product Generator

*Configuring the Data Product Generator · [auf help.sap.com öffnen](https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/4da38647b3d041728236df20d5a0308b.html?locale=en-US)*

Configuring Targets for the Data Product Generator
-
## Configuring Targets for the Data Product Generator
You can configure multiple targets for the Data Product Generator, which allows you
to separate extracted BW data into different BW file spaces or SAP Datasphere tenants based
on functional area (e.g. FI, HCM)). The target for a data subscription can be selected if
you create the data subscription.

### Viewing and Maintaining Targets

You can view and maintain all targets for your BW system in the RSDPS transaction in the SAP
GUI.

If you navigate to Goto  Maintain Target System, a new screen will open that lets you view all existing targets, as
well as create new ones, or edit and delete existing ones.

In the Display Target System screen, you can perform the
following actions for targets:

Actions for Targets

|
Action
| Procedure
| --- |
|

|
View target details
| To view the properties of any existing target in your BW system, select the target in
| --- |
the Target Name field. As a result, the
fields will be filled in with the information from the selected
target.
|

|
Check connectivity for target
| Select Check Connectivity () to check
| --- |
the connection to SAP Datasphere for the displayed
target.
|

|
Edit target
| Select Display ↔ Change () to open the
| --- |
edit mode for the displayed target. Change the settings you want
to adjust, then select Save ()
to confirm.
|

|
Delete target
| Select Display ↔ Change () and then
| --- |
Delete Target System ()
to delete the displayed target. You need to confirm the deletion
in an additional pop-up window.
|

|
Create new target
| Select Display ↔ Change () and then
| --- |
Create Target System ()
to add new targets.
|

### Creating New Targets

You can create a new target for the Data Product Generator in the RSDPS transaction
in the SAP GUI.

- In the top bar of the RSDPS transaction, select Goto  Maintain Target System.

- Select Display ↔ Change () and then
Create Target System ().

- Enter a Target Name in the pop-up window.

- Input further information about the new target as required.

- Set the Target Type to HDLFS (SAP HANA Cloud,
data lake Files) as this is the only target type supported by the
Data Product Generator.

- Tick off the checkbox Preferred System if you
want to set the new target as the user-preferred target for your BW
system.

- Enter a Description for your target.

- Enter details about the connection to SAP Datasphere for the new target. For more
information, see SAP Note [3590400](https://me.sap.com/notes/3590400).

- (Optional) Select Check Connectivity () to test the connection
to SAP Datasphere and resolve connection errors as required.

- Select Save () to save the new
target.
You can now use this target if you create new data
subscriptions.

Note

For each new target you need to implement the configuration task list for the Data Product
Generator which includes the setup of a dedicated BW file space in the SAP
Datasphere tenant to receive pushed data. For the full procedure, see SAP Note
[3590400](https://me.sap.com/notes/3590400).

After the targets have been configured they can be selected if you create a new data
subscription, as well as viewed in the data subscriptions list.

### Selecting Targets for Data Subscriptions

You can select the target for a data subscription when you create it:

- Creating a data subscription:

- Data Subscriptions app (SAP BW/4HANA Cockpit):
If you create a data subscription in the SAP BW/4HANA Cockpit, you
can set the target in the Target Name field.
If you toggle the arrow icon, you can choose from all existing
targets in your BW system. The value help will display their names
and descriptions. (For more information, see [Creating Data Subscriptions](f2e950ed4e8c475b8571478d6c2004c0.html).)

- RSDPS transaction (SAP GUI): If you create a
data subscription in the SAP GUI, you can set the target in the
Target Name field. If you click on the
file icon, you can choose from all existing targets in your BW
system. The value help will display their names, descriptions, and
whether they're a preferred target (marked with an X). The
Target Type field will be pre-filled with
HDLFS (SAP HANA Cloud, data lake Files) since this is the only
available target type for the Data Product Generator. (For more
information, see [Creating Data Subscriptions](f2e950ed4e8c475b8571478d6c2004c0.html).)

Note

If a user-preferred target has been configured, the
Target Name field will be
initially filled with this target. If no user-preferred
target has been configured, it will be filled with the
system-preferred target. The Target
Name field cannot be left empty or filled
with invalid input (such as a target that doesn't exist),
otherwise the data subscription cannot be saved.

Caution

Once the data subscription has been
created, it's not possible to adjust the target anymore.
Therefore, make sure to select the correct target during
first-time creation.

- Creating a data subscription from template: If you create a data
subscription from template, the target will be taken over from the template
data subscription. However, before saving the new data subscription, you can
still select a different target. This allows you to copy existing data
subscriptions but enable them for different targets. (For more information,
see [Creating Data Subscriptions from Template](c2c90f4fce964121a50d8f6794ea5dad.html).)

You can also select the target for a scenario in the Scenario Generator:

- Creating a scenario: In the Scenario Core
Objects tab of the Scenario Generator view you can
pre-define the target for the entire scenario in the Target
Name field. Select Browse to choose
from all existing targets in your BW system. This target will be applied to
all to-be-generated data subscriptions of the scenario which will be visible
in the Objects Relations tab under
Selection to Generate Data Subscriptions. In the
second step you can here still adjust the targets of the individual data
subscriptions. (For more information, see [Creating Scenarios](27e24efbd818463b834a1000bbaf3854.html).)

- Generating data subscriptions: Before you generate the
data subscriptions out of the scenario tree, you still can change the target
for the individual data subscriptions in the scenario. To do this, go to the
Object Relations tab of the Scenario Generator
view. In the section Selection to Generate Data
Subscriptions, select the data subscriptions for which you
want to set a different target, then right-click and select
Edit. Go to the field Target
Name and select Browse to choose from
all existing targets on your BW system. (For more information, see [Generating Data Subscriptions](304de2d15cc049578aaafbba420c27d2.html).)
Caution

Generally, you can use multiple targets for the Data Product Generator
in the BW Modeling Tools. However, all data subscriptions in a scenario
must belong to the same target to enable the data subscriptions to be
generated. It's possible to have multiple different targets for
different scenarios. For this reason, the target is best to be defined
on scenario-level in the Scenario Generator, and not for the individual
data subscriptions.

### Viewing Targets for Data Subscriptions

You can view the targets of the data subscriptions in the Target
Name column, which is visible in the various different interfaces of
the Data Product Generator.

|
Interface
| Viewing Targets
| --- |
|

|
RSDPS transaction (SAP GUI)
|

- Target Name column in the data
subscriptions list.

- Target Name and Target
Type fields in the
Details screen of a data
subscription.

- Target Name and Target
Type fields in the Edit
Subscription screen. (For more
information, see [Editing Data Subscriptions](06b37289aade411c8f289cac7095fc00.html).)

|

|
Data Subscriptions app (SAP BW/4HANA Cockpit)
|

- Target Name column in the data
subscriptions list.

- Target Name field in the
Maintain Subscription screen.
(For more information, see [Editing Data Subscriptions](06b37289aade411c8f289cac7095fc00.html).)
Note

The Target Name
column must first be toggled via
Settings () to make it visible in the data
subscriptions list. This is different than in the
SAP GUI and in the BW Modeling Tools, where it is
visible by default. In the SAP BW/4HANA Cockpit it's
also possible to filter the data subscriptions list
by Target Name via the
respective filter settings.

|

|
Data Subscriptions view (BW Modeling Tools)
|

- Target Name column in the data
subscriptions list. (For more information, see [BW Data Product Generator Perspective in BW Modeling Tools (BWMT)](21393d96c2f94fdebc20ee3941b4eb02.html).)

|

|
Scenario Generator view (BW Modeling Tools)
|

- Target Name column under
Collected Objects in the
Object Relations tab. Here
you can see the targets for existing data subscriptions
associated with the selected BW models and its
dependencies. (For more information, see [Creating Scenarios](27e24efbd818463b834a1000bbaf3854.html).)

- Target Name column under
Selection to Generate Data
Subscriptions in the Object
Relations tab. Here you can see the
targets you selected individually for the data
subscriptions to be generated for the scenario. (For
more information, see [Generating Data Subscriptions](304de2d15cc049578aaafbba420c27d2.html).)

|
