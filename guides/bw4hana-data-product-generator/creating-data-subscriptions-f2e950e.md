---
guide: Data Product Generator for SAP Business Data Cloud
product: SAP BW/4HANA
title: "Creating Data Subscriptions"
page: f2e950ed4e8c475b8571478d6c2004c0.html
url: https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/f2e950ed4e8c475b8571478d6c2004c0.html?locale=en-US
source_type: SAP Help
---

# Creating Data Subscriptions

*Maintaining Data Subscriptions · [auf help.sap.com öffnen](https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/f2e950ed4e8c475b8571478d6c2004c0.html?locale=en-US)*

Creating Data Subscriptions
-
## Creating Data Subscriptions
To extract data from InfoProviders in your BW system into local tables (file) in your
SAP Datasphere tenant, you need to create a data subscription.

### Prerequisites

- The BW administrator has set up and configured the Data Product Generator for SAP Business
Data Cloud. During the configuration, the BW administrator has created a space
to receive data pushed by the Data Product Generator (BW file space). (For more
information, see [Configuring the Data Product Generator](8586340e2bf647d783e4cf506559c25a.html).)

- The BW administrator has created one or multiple targets for the Data Product Generator that
can be selected for the data subscription. (For more information, see [Configuring Targets for the Data Product Generator](4da38647b3d041728236df20d5a0308b.html)).

### Creating Data Subscriptions in the SAP BW/4HANA Cockpit

In the SAP BW/4HANA Cockpit you can create data subscriptions in the Data Subscriptions
app.

- In the SAP BW/4HANA Cockpit, go to the section Data Product
Generator for SAP Business Data Cloud and open the app
Data Subscriptions.

- Select Create among the buttons in the top bar.

- In the field Source Type select from which type of BW object you want
to extract data from. If you select ODP, you can extract
data from ODP-based sources, such as BW InfoProviders. If you select
Snapshot, you can extract data from BW InfoObjects,
including hierarchies, master data, and texts, and DataStore objects (advanced) (aDSOs).

Note

Via the ODP option you can extract data from
InfoObjects, DataStore objects (DSOs), CompositeProviders,
MultiProviders, InfoCubes, or Queries as InfoProviders. Only select
Snapshot if you want to create hierarchy data
subscriptions, extract master data and texts (including
language-independent texts) from BW InfoObjects, or extract
transactional data from DataStore objects (advanced) (aDSOs).

- In the field Source Name, select the BW object you want to extract
data from. If you click on , a value help will open
where you can search for available objects in your BW system based on the
selected source type. Search results will show their name and description.

- In the field Target Name, select the target for the data subscription.
If you toggle , you can view all available targets for your BW system including their name
and description. For more information, see [Configuring Targets for the Data Product Generator](4da38647b3d041728236df20d5a0308b.html).

- Select Save to save the data subscription.

- Select the Package the data subscription will belong to for transport
requests. If you click on , a value help will open
where you can search for available packages in your BW system. Search results
will show their name and description.
Note

By default, the package $TMP is
selected. This is a special package dedicated to creating local objects that
won't be transportable. Only leave this package selected if there is no need
to transport the created data subscription to quality or production systems,
such as for tests or prototyping.

- Select the Transport Request the data subscription will
belong to.

- Choose from requests in which I am involved: Here
you can preview a list of requests you're actively involved in on your
BW system and select one of them for transporting the data subscription.
This means, you've either created the request, have added objects to the
request, or have been explicitly added as a user to the request.

- Create new request: Here you can create an
entirely new request for your transport scenario.

- Enter a request number: Here you can select
amongst all requests on your BW system by entering the request number
and choosing Browse.

If the data subscription has been saved successfully, you will see a
confirmation message appearing on the screen.

- The data subscription will now be created. During the creation some of the properties are
automatically generated or filled in.

- The technical name of the data subscription (Technical
Name) will be automatically generated and cannot be
changed.

- The description of the data subscription
(Description) will be filled in based on
the description of the BW InfoProvider, but still can be adjusted
afterwards.

- The timestamp when the data subscription was created
(Last Changed At) and user who created it
(Last Changed By) will be automatically
filled in by the system and cannot be adjusted.
These details can
be viewed in the header section of the Maintain
Subscription screen. Here, you can also see the
current status of the data subscription (Active
Version), the current status of the local table
(file) (Local Table State) and whether
the local table (file) already has been filled with data or not
(Has Data). (For more information on
possible versions/states of the data subscription, see [Transporting and Migrating Data Subscriptions](985a9ac9f61047e39639ba0440465ed4.html).)

- (Optional) In the Maintain Subscription screen you can now make
further settings for your data subscription.

- Go to the General tab and enter a custom description for your data
subscription in the Description field.

- Go to the General tab and set a custom technical
name for the local table (file) via the Base Name
field. For more information, see [Custom Technical Names for Local
Tables (File)](https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/87a6fd1da8cd44509e77c232f39c8449.html).

- Go to the Settings tab and select the Extraction
Mode. You can choose between Full
and Delta. For more information, see [Setting Extraction Mode for the Data Product Generator](608b0cbeb8ce4a59a121563f12a91c43.html).

Note

If you create a hierarchy data subscription, only full extraction is available. The
extraction mode field will therefore be automatically set to
Full and cannot be changed.

- Go to the Settings tab and open Selections
to limit the data set to be extracted via the data subscription. A value
help will open, displaying all fields for which you can limit the data
set. Enter conditions for the fields and confirm via
OK to apply the them.

- Go to the Settings tab and select the Process
Variant if you want to use a process chain for the
extraction. If you click on , a value help will
open, displaying all available process variants in your BW system
including their name, the ID of the associated process chain, the
process chain description, the trigger description and condition, and
the period of executions. You can also search for variants.
Note

The
process type needs to be Load Process and Postprocessing
- Data Provisioning Subscription.
Only process
variants in data subscription-driven assignment mode are
available for selection. Process variants configured with the
process variant-driven assignment mode are managed from within
the process variant itself and do not appear in this value help.
For more information, see [Assigning Data Subscriptions to a Process Variant](535a0f490c544314b6c9c3cd019e94f3.html).

- Go to the Projections tab to define from which fields in the
InfoProvider the data subscription should extract data. By default all
fields/the entire data set will be extracted (Full
Projection). If you deselect Full
Projection, the table with the fields will become
editable. You can now add fields to the projection by choosing them via
the checkbox in the first column. Key fields always need to be selected
and therefore will not be editable.

- Select Activate to activate the data subscription and make it
executable. This will change its status from Not
Executable to Executable.
You will see
a confirmation message appearing on the screen informing you that an SAP
Datasphere entity will be created and deployed asynchronously. The local
table (file) in SAP Datasphere will now be created with the data
subscription ID as its qualified name. If you go to the tab
Datasphere Logs you can monitor these operations
and confirm their success or failure.

- Select Run to run the data subscription manually if you don't use a
process chain.
You will see a confirmation message appearing on the screen
stating that the data subscription has been started. The data will now be
extracted from the selected InfoProvider into the local table
(file).

- Go to View Executions to view a log of recent runs of all
subscription.
Locate your data subscription via the column
Subscription and view whether the execution was
successful or not (Status), how many records have
been transferred from the InfoProvider to the local table (file)
(Transferred Records), and how long the
extraction operation took (Duration).

- Select the button View Local Table (File) to open the local table
(file) with the extracted data in the SAP Datasphere tenant.
Note

The local
table (file) is stored in a dedicated BW file space of type SAP HANA Cloud,
data lake Files (HDLFS) and is not editable. For each BW system a separate
space must be created during the configuration of the Data Product
Generator. You cannot create any objects in this space except for task
chains.
All objects in the space are read-only, but data management
tasks (such as deleting data) are still possible. In addition, you can
share the local tables (file) in this space to other spaces where you
can use them for modeling. The structure of the local table (file)
cannot be changed as long as the data subscription exists. This ensures
that extractions via process chain will continue to work.
For more
information, see [Viewing Local Table (File) and Getting Data Updates](c5b7a4fae2ce4b829914f9f825d6b471.html).

### Creating Data Subscriptions in the SAP GUI

In the SAP GUI you can create data subscriptions in the RSDPS transaction.

- Open your BW system in the SAP GUI and call transaction RSDPS.

- Select Create () among the icons in the
top bar.

- In the field Source Type select from which type of BW object you
want to extract data from. If you select ODP, you can
extract data from ODP-based sources, such as BW InfoProviders. If you select
Snapshot, you can extract data from BW
InfoObjects including hierarchies, master data, and texts, and DataStore
objects (advanced) (aDSOs).

- In the field Source Name, select the BW object you want to extract
data from. If you click on , a value help will open,
displaying all available objects in your BW system depending on selected
type including their name, description and type (shown through a small
icon). Select the row for the object you want to choose and confirm via
.

- In the field Target Name, select the target for the data
subscription. If you click on , a value help will open,
displaying all available targets for your BW system including the name,
description, and whether they're a preferred target (marked through an X).
Select the row for the target you want to choose and confirm via .
Note

The
field Target Type will be automatically set to
HDLFS (SAP HANA Cloud, data lake Files) as this is the only available
target type for the Data Product Generator.

- Select Save () in the top bar to save
the data subscription.

- Select the Package the data subscription will belong
to for transport requests and confirm via Save
().
Alternatively, you can also create the data subscription as a local object
by clicking on Local Object instead.
Note

If you
create the data subscription as a local object, it will be assigned to
the special package $TMP. This means it won't be transportable and only
stays in the current development system.

- The data subscription will now be created. During the creation some of the
properties are automatically generated or filled in.

- The technical name of the data subscription
(Subscription) will be automatically
generated and cannot be changed.

- The description of the data subscription
(Description) will be filled in based
on the description of the BW InfoProvider, but still can be
adjusted afterwards.

- The timestamp when the data subscription was created (Last Changed
At) and user who created it (Created
By) will be automatically filled in by the
system and cannot be adjusted.

- The owner of the data subscription
(Owner) will be automatically filled in
based on who created it and cannot be adjusted.

- Further information about the BW InfoProvider will be
automatically provided in the section Source
Object. Here, you can now view the name of the
InfoProvider (Name), the type of the
InfoProvider (e.g. aDSO) (Object Type),
the user who last changed the InfoProvider (Last
Changed By) and the InfoArea it belongs to
(InfoArea). None of these settings
can be changed since they have been pulled from the metadata of
the InfoProvider.

- Further information about the local table (file) that will be
created and deployed are now also available in the section
Target. Here, you can view the
technical name of the local table (file) (Technical
Name), the inbound buffer path in the object
store (File Path), as well as its CSV
properties such as how meta information are saved
(Meta Information) and what separator
(Separator) and escape character
(Escape Character) are used.

- (Optional) In edit mode you can now make further settings for your data subscription.

- Set the extraction mode between full extraction (Full) or delta
extraction (Delta) in the field
Extraction Mode. For more
information, see [Setting Extraction Mode for the Data Product Generator](608b0cbeb8ce4a59a121563f12a91c43.html).

Note

If you create a hierarchy data subscription, only full extraction is available. The
extraction mode field will therefore be automatically
set to Full and cannot be
changed.

- Set a custom technical name for the local table (file) in the field Base
Name under Datasphere Local
Table. For more information, see [Custom Technical Names for
Local Tables (File)](https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/87a6fd1da8cd44509e77c232f39c8449.html?state=DRAFT).

- Toggle the scheduling settings between manual/direct execution
of the data subscription (No Scheduling)
and scheduling data subscription runs via process chain
(Process Chain) in the field
Scheduling.
If you want to run the data subscription via process chain, you also need to enter the process
variant in a pop-up field Process
Variant. If you click on , a value
help will open, displaying all available process variants in
your BW system including their name, description, the name
of the associated process chain, and the conditions and
period for the execution. Select the row for the process
variant you want to choose and confirm via .Note

The process type needs to be Load
Process and Postprocessing - Data Provisioning
Subscription.
Only process variants in
data subscription-driven assignment mode are
available for selection. Process variants configured
with the process variant-driven assignment mode are
managed from within the process variant itself and
do not appear in this value help. For more
information, see [Assigning Data Subscriptions to a Process Variant](535a0f490c544314b6c9c3cd019e94f3.html).

- Click on Edit Selection to limit the data
set to be extracted via the data subscription. A value help will
open, displaying all fields for which you can limit the data
set. Enter conditions for the fields and confirm via
to apply the filters.

- Click on Edit Projection to define from which fields in the
InfoProvider the data subscription should extract data. A value
help will open, displaying all available fields in the selected
InfoProvider including their name, whether they're a key field,
their description, their data type, and some further
information. All selected fields are marked with an .
If you click on the icon, you
can add or remove the fields as needed. Confirm via
to save the changes.
Note

Key fields always need to be selected
in the projection.

- Select Save () in the top bar to save
the changes.

- Select Activate Data Subscription () to activate
the data subscription and make it executable. This will change its status
from Inactive to Active.

- Go back to the main screen, select the data subscription you have just
created in the list, and choose Run () in the top
bar. This will start the data extraction according to the defined settings
manually if you don't use a process chain.
As a result, the local table
(file) will be filled with the data from the BW InfoProvider. You can
access the local table (file) as well as perform further actions on your
data in your SAP Datasphere tenant. For more information, see [Viewing Local Table (File) and Getting Data Updates](c5b7a4fae2ce4b829914f9f825d6b471.html).
