---
guide: Data Product Generator for SAP Business Data Cloud
product: SAP BW/4HANA
title: "Data Subscriptions App in SAP BW/4HANA Cockpit"
page: 60146bc2b99941f2bdad39153fca5e9d.html
url: https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/60146bc2b99941f2bdad39153fca5e9d.html?locale=en-US
source_type: SAP Help
---

# Data Subscriptions App in SAP BW/4HANA Cockpit

*Data Subscriptions · [auf help.sap.com öffnen](https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/60146bc2b99941f2bdad39153fca5e9d.html?locale=en-US)*

Data Subscriptions App in SAP BW/4HANA Cockpit
-
## Data Subscriptions App in SAP BW/4HANA Cockpit
The Data Subscriptions app in the SAP BW/4HANA Cockpit provides BW administrators on a
SAP BW/4HANA system with a modern and intuitive interface to view, manage, and maintain data
subscriptions.

### Accessing the Data Subscriptions App

You can access the Data Subscriptions app in the SAP BW/4HANA
Cockpit under the tab Data Product Generator for SAP Business Data
Cloud.

On the tile you can view the current number of data subscriptions in your BW
system.

Note

On SAP BW 7.5 systems you need to use the RSPDS transaction in the
SAP GUI to maintain the data subscriptions.

### Data Subscriptions List - Columns and Values

The columns in the data subscriptions list display information about certain properties
of the data subscriptions:

Columns in Data Subscriptions List

|
Column
| Value
| --- |
|

|
Subscription
| Technical name and description of the data
| --- |
subscription.
|

|
Subscription Type
| Type of the data subscription.
| --- |

- DSUB - Transportable data
subscription (TLOGO type)

- SUBS - Local data subscription
(Cannot be transported)

|

|
Status
| Shows whether the data subscription has been activated or not.
| --- |

- Active, executable - Data
subscription has been activated and can be run.

- Inactive, not executable - Data
subscription still needs to be activated to be run.

|

|
Source Object
| Name of the source object selected for the data
| --- |
subscription.
|

|
Source Type
| Type of the selected source for the data subscription.
| --- |
The source type is either
ODP (Operational Data
Provisioning) for ODP-based InfoProviders, or
Snapshot for characteristic
InfoObjects including hierarchies, master data, and texts,
and DataStore objects (advanced) (aDSOs).
|

|
Target Name
| Name of the target selected for the data
| --- |
subscription.
|

|
Target Type
| Type of the target selected for the data subscription. Target
| --- |
type for the Data Product Generator is always HDLFS (SAP HANA
Cloud, data lake Files).
|

|
Last Changed At
| Date and time at which the data subscription has last been
| --- |
changed.
|

|
Last Changed By
| User who last changed the data subscription.
| --- |
|

|
Created At
| Date and time at which the data subscription has been
| --- |
created.
|

|
Created By
| User who created the data subscription.
| --- |
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

- Immediate, Single Execution -
Data subscription has been scheduled via process
chain.

- No Scheduling - Data subscription
needs to be run manually via the
Run button.

|

|
Process Chain ID
| ID of the process chain selected for running the data
| --- |
subscription. (Only applies if scheduling settings are set to
process chain.)
|

|
Process Chain Description
| Description of the process chain selected for running the
| --- |
data subscription. (Only applies if scheduling settings are set
to process chain.)
|

|
Process Variant
| Name of the process variant selected for running the data
| --- |
subscription. (Only applies if scheduling settings are set to
process chain.)
|

|
Delta Runtime
| Shows whether delta extraction has been configured for data subscription.
| --- |

- No - Full extraction has been
set.

- Yes - Delta extraction has been
set.

|

|
Last Execution
| Shows whether data subscription has already been run.
| --- |

- Not executed - Data subscription
hasn't been run yet.

- Success - Data subscription has
been run yet and last run was successful.

- Failed - Data subscription has
been run yet, but last run has failed.

|

|
Local Table (File)
| Click on View Local Table (File) to
| --- |
open the local table (file) in the SAP Datasphere
tenant.
|

### Data Subscriptions Toolbar - Configurations for Data Subscriptions List

In the search section above the data subscriptions list, you can search and filter
the list:

- Via Adapt Filters you can add columns to the search
section. For each of these columns you can specify filters for the list
(e.g. only show data subscriptions of type SUBS). For more information on
the columns that can be added, see section "Columns and Values".

- Via Easy Filter () you can switch to a
simplified search where you can enter search queries and filters in natural
language.

You can also perform the following configurations on the list of data
subscriptions:

Configurations for Data Subscriptions List

|
Button
| Configuration
| --- |
|

|
Refresh
| Refresh the list of data subscriptions to show latest changes according to new
| --- |
sorting criteria or performed actions.
|

|
Copy to Clipboard ()
| Copy the data from the selected row in the list to the clipboard, allowing for easy
| --- |
copy/paste.
|

|
Show More per Row () /
Show Less per Row ()
| Expand or limit the information shown per row. This option is useful if you have
| --- |
configured many columns/properties to be shown for the data
subscriptions and don't have enough space to view them
all.
|

|
Settings ()
| Open the Settings menu to configure which columns/properties
| --- |
of the data subscriptions are shown in the list and in which
order they appear. You can also define filters or groups. For
more information on which columns can be shown, see section
"Columns and Values".
|

|
Export Table ()
| Save the currently displayed list as a local file. If you select the dropdown besides
| --- |
the icon () and then choose Export
As, you can make further settings for the file
format and file name, as well as whether you want to consider
current filters while exporting or split cells with multiple
values.
|

### Data Subscriptions Toolbar - Actions for Data Subscriptions

You can perform the following actions on the data subscriptions:

Actions for Data Subscriptions

|
Button
| Action
| --- |
|

|
Run
| Run the selected data subscription. This manually starts an extraction operation from
| --- |
the InfoProvider into the local table (file). Alternatively, you
can also schedule the extraction operation via process
chain.
|

|
Delete
| Delete the selected data subscription. This doesn't delete the local table (file) if
| --- |
it has already been deployed. For more information, see [Deleting Data Subscriptions](51f2dd2a17a14a43ba265c537cce47ed.html).
|

|
Create from Template
| Create a new data subscription based on a template of an existing data subscription.
| --- |
For more information, see [Creating Data Subscriptions from Template](c2c90f4fce964121a50d8f6794ea5dad.html).
|

|
Create
| Create a new data subscription. For more information, see
| --- |
[Creating Data Subscriptions](f2e950ed4e8c475b8571478d6c2004c0.html).
|

|
Toggle Status
| Activate or deactivate the selected data subscription. This
| --- |
toggles its status between Active and
Inactive. A data subscription needs
to be activated before you can run it. For more information, see
[Transporting and Migrating Data Subscriptions](985a9ac9f61047e39639ba0440465ed4.html).
|
