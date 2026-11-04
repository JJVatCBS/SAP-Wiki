---
guide: Data Product Generator for SAP Business Data Cloud
product: SAP BW/4HANA
title: "Mass Deleting Data Subscriptions by Target"
page: a51ba4f698d44ccc9b71d06d0050d3d1.html
url: https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/a51ba4f698d44ccc9b71d06d0050d3d1.html?locale=en-US
source_type: SAP Help
---

# Mass Deleting Data Subscriptions by Target

*Maintaining Data Subscriptions · [auf help.sap.com öffnen](https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/a51ba4f698d44ccc9b71d06d0050d3d1.html?locale=en-US)*

Mass Deleting Data Subscriptions by Target
-
## Mass Deleting Data Subscriptions by Target
You can mass delete data subscriptions if they belong to the same target (BW file space
in SAP Datasphere or SAP Datasphere tenant). This allows for easier maintenance and to clear
up your BW system of data subscriptions if you don't need them anymore.

### Accessing Deletion Report

The mass deletion can be performed with a dedicated ABAP report in the SAP GUI.

You can access the report in two different ways:

- Call transaction SE38 and enter the program name RSDDS_DELETE_BY_SOURCE, then select
Execute () in the top bar.

- Directly access the report in the RSDPS transaction by selecting Goto  Delete Data Subscriptions by Target

As a result, the report Mass Deletion of Data Subscriptions by
Target will open.

### Deleting Data Subscriptions

To mass delete the data subscriptions based on target, perform the following
procedure:

- Go to Selection Parameters and select the
Target.
You can do so either by entering the
name of the target into the field or by selecting to open the value
help.
In the value help you can see a list of all targets
configured for your BW system including their names and descriptions. If
you have configured a user-preferred target, it will be marked up with
an X in the column Preferred Target. Here, select
the row with the target you want to choose and then confirm via .

- (Optional) Go to Deletion Options and select Simulate
Deletion if you want to test the deletion operation based on
the selected target without actually deleting any data subscriptions in your
production system.

- (Optional) Go to Deletion Options and select Force
Deletion if you want to force delete the data subscriptions
while ignoring all errors and validations during the deletion operation
(with the exception of transport/authority/lock scenarios).
Tip

A common use case for force deletion is if you want to delete the data
subscriptions even if the associated SAP Datasphere tenant or BW file
space doesn't exist anymore. This is, for example, the case if you had a
SAP Business Data Cloud trial with a limited lifetime and want to remove
the corresponding data subscriptions from your BW system
afterwards.
Caution

Before you carry out a force
deletion, check your connection to SAP Datasphere. If the connection is
not working during the force deletion, the local tables (file) might not
lose their read-only tag, which means they cannot be deleted afterwards
in SAP Datasphere.

- Select Execute () in the top
bar of the report to perform the deletion operation.
Confirm that you want
to delete all data subscriptions for the selected target while
understanding that the deletion operation cannot be undone.

As a result, the data subscriptions will be mass deleted according to the selections you have
made.

You can view the outcome of the deletion operation in a log screen that appears after
the deletion finished. Here you can also see how many data subscriptions have been
deleted and any error messages or issues that might have come up.

If you have selected Simulate Deletion the log screen will
show a preview of the results of the deletion operation that would be carried
out.
