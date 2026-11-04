---
guide: Data Product Generator for SAP Business Data Cloud
product: SAP BW/4HANA
title: "Unlocking Local Tables (File) with Missing Data Subscription"
page: ec61e47e062c41d68585343778350823.html
url: https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/ec61e47e062c41d68585343778350823.html?locale=en-US
source_type: SAP Help
---

# Unlocking Local Tables (File) with Missing Data Subscription

*Working with Local Tables (File) · [auf help.sap.com öffnen](https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/ec61e47e062c41d68585343778350823.html?locale=en-US)*

Unlocking Local Tables (File) with Missing Data Subscription
-
## Unlocking Local Tables (File) with Missing Data Subscription
With the ABAP report RSDDS_UNLOCK_LOCAL_TABLE you can unlock a local table (file) in SAP
Datasphere in SAP Business Data Cloud that has remained locked after its data subscription
in the BW system was deleted.

### Prerequisites

- The data subscription for the local table (file) has already been deleted from the BW
system. Using this ABAP report is not part of the standard deletion workflow -
it should only be used if there was an issue when deleting the data
subscription, and the local table (file) has remained locked afterwards.

- You have retrieved the technical name of the affected local table (file). Technical
names for text tables or hierarchy-related tables may contain lowercase
characters such as _text or
_hierarchy_node.

- You are authorized on the authorization object
S_RS_DDS with a
Delete authorization.

### Context

If a data subscription is activated, the Data Product Generator creates and locks the
corresponding local table (file) in SAP Datasphere in SAP Business Data Cloud. This
means it will appear as read-only in SAP Datasphere in SAP Business Data Cloud and
cannot be edited or deleted as long as the data subscription exists. Under normal
circumstances, if you delete the data subscription in the BW system, the lock of the
local table (file) will be released, making it editable. You then can also delete
the local tables (file) manually if you don't need them anymore.

However, in certain situations the local tables (file) can remain locked even if
there corresponding data subscriptions were deleted.

Causes for this can include:

- There was a connection issue with SAP Datasphere in SAP Business Data Cloud when you
deleted the data subscriptions in the BW system.

- The connection to SAP Datasphere in SAP Business Data Cloud was not available
when you used the force delete option during a mass deletion of data
subscriptions with the associated ABAP report.

- The deletion process of the data subscriptions was interrupted by other system
inconsistencies.

In these cases, the local table (file) remains locked and cannot be edited or maintained,
even though the associated data subscription does not exist in the BW system anymore. The
report RSDDS_UNLOCK_LOCAL_TABLE is a manual repair
tool allowing you to unlock specified local tables (file) without a data subscription by
entering their technical names.

### Procedure

-
Open your BW system in the SAP GUI and call transaction
RSDPS.

-
In the top bar, choose
Goto  Unlock Local Tables (File) without Data Subscription.
The report
RSDDS_UNLOCK_LOCAL_TABLE
opens.

-
Under Selection Target, enter the Target
for which you want to unlock local tables (file).

You can enter the target name directly or use the value help to select from the list of
configured targets.

-
Under Select Local Tables (File), enter the technical name of
the local table (file) you want to unlock in the Local Table (File)
field.

To process multiple local tables (file) in one operation, use the multiple selection
option to add additional technical names. This only works if all of the local tables
(file) exist in the same target which you previously selected.

-
Under Simulate Unlocking Local Tables (File), select
Enable Simulation.

Note

The simulation mode is active by default.
When simulation mode is active, the
report runs all validation checks and writes a full log entry, but does not make any
changes to local tables (file) in SAP Datasphere in SAP Business Data Cloud. Always
run the report in simulation mode first to verify the outcome before applying any
changes to your production system.

-
Choose Execute in the top bar.
The report runs all validation checks and writes the result to the log. No
changes are made to local tables (file) in SAP Datasphere in SAP Business Data
Cloud.

-
Review the log that appears after the report finishes.

The log shows what would happen to each local table (file) if you ran
the report without simulation mode. Check for the following:

- If the log shows that the unlock operation would be performed for all specified
local tables (file), proceed with the next step.

- If the log shows an error message indicating that the data subscription for the
specified local table (file) still exists, do not proceed. The local table (file)
cannot be unlocked using this report while its data subscription is present in the BW
system. If you want to unlock the local table (file), first try to delete the data
subscription in the BW system, after which the local table (file) should become
editable in SAP Datasphere in SAP Business Data Cloud.

- If the log shows a warning message indicating that the local table (file) is already
editable, no further action is needed. This means the local table (file) has already
been unlocked in SAP Datasphere in SAP Business Data Cloud.

-
Deselect Simulation Mode.

-
Choose Execute in the top bar again.
The report unlocks the specified local tables (file) in SAP Datasphere in SAP
Business Data Cloud. The local tables (file) are now editable and can be
maintained or manually deleted.

-
Review the log to confirm that the unlock operation completed successfully.

All messages generated during the report run are saved to the log, providing a
transparent record of the operation.

### Results

The selected local tables (file) are unlocked in SAP Datasphere in SAP Business Data Cloud
and can now be edited, maintained, or manually deleted.

Related Information
[RSDPS Transaction in SAP GUI](67d73d2e2086409c8bc06ff79b116476.html)
[Deleting Data Subscriptions](51f2dd2a17a14a43ba265c537cce47ed.html)
[Performing Data Management Tasks and Sharing Local Table (File)
to Other Spaces](692538f27de745539c551ef7e08fff53.html)
