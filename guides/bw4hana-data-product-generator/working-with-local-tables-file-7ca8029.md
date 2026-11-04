---
guide: Data Product Generator for SAP Business Data Cloud
product: SAP BW/4HANA
title: "Working with Local Tables (File)"
page: 7ca80294877741a6b8bc807f60e51804.html
url: https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/7ca80294877741a6b8bc807f60e51804.html?locale=en-US
source_type: SAP Help
---

# Working with Local Tables (File)

*Data Product Generator for SAP Business Data Cloud · [auf help.sap.com öffnen](https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/7ca80294877741a6b8bc807f60e51804.html?locale=en-US)*

Working with Local Tables (File)
-
## Working with Local Tables (File)
Local tables (file) are a table type in SAP Datasphere that is optimized for storing
large volumes of data in a cost-effective way using a file-based storage.

The local tables (file) are created and saved in a special file space of type BW in the
object store in SAP Datasphere. In contrary to standard spaces in SAP Datasphere, this
BW file space is based on storage in SAP HANA Cloud, data lake Files (HDLFS).Note

SAP
HANA Cloud, data lake Files (HDLFS) is a component of SAP HANA Cloud, data lake. It
provides a managed container for storing structured, semi-structured, and
unstructured data as files. In the object store of SAP Datasphere it is used to
handle large volumes of data efficiently, allowing big data workloads to run at
scale without burdening traditional HANA in-memory storage.

The Data Product Generator directly creates and deploys a local table (file) if you
create and save a data subscription. If you run the data subscription, this local table
(file) will be populated with data from the selected BW InfoProvider. For more
information, see [Creating Data Subscriptions](f2e950ed4e8c475b8571478d6c2004c0.html).

If you are using multiple targets for the Data Product Generator, you can deploy local
table (files) into different BW file spaces in the same SAP Datasphere tenant or even
into different SAP Datasphere tenants. The target can be selected when you create a new
data subscription. For more information, see [Configuring Targets for the Data Product Generator](4da38647b3d041728236df20d5a0308b.html).

In the Data Builder in SAP Datasphere you can view the local table (file), as well as its
data and metadata. You can also schedule a merge task to merge new data pushed by the
Data Product Generator into the local table (file) after initial extraction. For more
information, see [Viewing Local Table (File) and Getting Data Updates](c5b7a4fae2ce4b829914f9f825d6b471.html).

To use the BW data in the local table (file) in models and views in SAP Datasphere, you
first need to share it to another space, since the BW file space itself is read-only and
doesn't allow to create any objects except for task chains. For more information, see
[Performing Data Management Tasks and Sharing Local Table (File) to Other Spaces](692538f27de745539c551ef7e08fff53.html).

In some situations, a local table (file) can remain locked in SAP Datasphere in SAP Business
Data Cloud even after its data subscription has been deleted in the BW system. To
manually unlock the local tables (file), you can use a dedicated ABAP report. For more
information, see [Unlocking Local
Tables (File) with Missing Data Subscription](ec61e47e062c41d68585343778350823.html).
