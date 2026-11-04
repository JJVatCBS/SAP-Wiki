---
guide: Data Product Generator for SAP Business Data Cloud
product: SAP BW/4HANA
title: "Deleting Data Subscriptions"
page: 51f2dd2a17a14a43ba265c537cce47ed.html
url: https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/51f2dd2a17a14a43ba265c537cce47ed.html?locale=en-US
source_type: SAP Help
---

# Deleting Data Subscriptions

*Maintaining Data Subscriptions · [auf help.sap.com öffnen](https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/51f2dd2a17a14a43ba265c537cce47ed.html?locale=en-US)*

Deleting Data Subscriptions
-
## Deleting Data Subscriptions
You can delete existing data subscriptions in the Data Subscriptions app or in the RSDPS
transaction. This allows you to remove unused or outdated data subscriptions from your
systems.

### Deleting Data Subscriptions in the SAP BW/4HANA Cockpit

In the SAP BW/4HANA Cockpit you can delete data subscriptions in the Data Subscriptions
app.

- Open the SAP BW/4HANA Cockpit.

- Go to the section Data Product Generator for SAP Business Data Cloud
and open the app Data Subscriptions.

- Select the data subscription you want to delete from the list.

- Choose Delete among the buttons in the top bar.

- (Optional) If you have already run the data subscription and a local table (file) has been
created and deployed in SAP Datasphere, log on to SAP Datasphere and delete
the local table (file) as well.
Note

You can only select and delete one data
subscription at once. It is not possible to delete multiple data
subscriptions in one operation.

### Deleting Data Subscriptions in the SAP GUI

In the SAP GUI you can delete data subscriptions in the RSDPS transaction.

- Open your BW system in the SAP GUI and call transaction RSDPS.

- Select the data subscription you want to delete from the list.

- Choose Delete (
![Bild](https://help.sap.com/doc/ed919380760a44388ab90e6bb3e7480a/latest/en-US/loiof06063fe84184eecac6243c68297267b_LowRes.png)
) among the icons in the
top bar.

- (Optional) If you have already run the data subscription and a local table (file) has been
created and deployed in SAP Datasphere, log on to SAP Datasphere and delete
the local table (file) as well.
Note

Similarly to the Data Subscriptions
app, it is not possible to delete multiple data subscriptions at once.
You can only do this by using the ABAP report RSDDS_DELETE_BY_SOURCE
(Mass Deletion for Data Subscriptions by Target) which deletes all data
subscriptions belonging to one target. The program is only accessible in
the SAP GUI. For more information, see [Mass Deleting Data Subscriptions by Target](a51ba4f698d44ccc9b71d06d0050d3d1.html).

### Deleting Dependent Objects

Deleting the data subscription does not automatically delete the corresponding local
table (file) as well. If the data subscription has been deleted, the local table
(file) will remain in the SAP Datasphere tenant. However, there it will now become
editable (losing the read-only tag) and can be deleted manually.Tip

In
case of an offloading scenario it is not necessary to delete the local tables
(file). Here, you move your BW data to SAP Business Data Cloud in a one-time
operation and delete it afterwards in your BW system.
Note

In some situations, the local table (file) may remain locked in SAP
Datasphere in SAP Business Data Cloud even after the data subscription has
been deleted. This can happen due to a connection error between the BW
system and SAP Datasphere in SAP Business Data Cloud at the time of
deletion, or after a forced mass deletion when the connection was not
available. To resolve this issue, you can use the ABAP report
RSDDS_UNLOCK_LOCAL_TABLE to
unlock the local tables (file) manually after the data subscription was
deleted. For more information, see [Unlocking Local Tables
(File) with Missing Data Subscription](ec61e47e062c41d68585343778350823.html).

The data products created out of the BW data in the local tables (file) do not need
to be deleted since they are released once and then need to be kept stable.

### Deleting Individual Requests from InfoProviders without Reload of Data Subscription

If a data subscription has already been run and extracted data to SAP Business Data Cloud, you
can delete individual requests from the source InfoProvider in the BW system without
having to reload the entire data subscription. This is possible if the source
InfoProvider is a DataStore object (advanced) of type data mart (SAP BW/4HANA
systems) or an InfoCube (SAP BW 7.5 systems).

To do so, you need to first delete all extracted data for the request from the local
table (file) in SAP Datasphere, and then reset its data mart status in the BW
system.

For more information, see [Deleting Requests by Resetting Data Mart
Status](https://help.sap.com/docs/SAP_BW4HANA/107a6e8a38b74ede94c833ca3b7b6f51/7e3aa67467ab4cc4b0e0448ab9700a99.html?state=DRAFT).
