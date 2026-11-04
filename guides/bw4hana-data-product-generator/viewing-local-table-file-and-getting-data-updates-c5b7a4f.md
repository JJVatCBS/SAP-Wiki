---
guide: Data Product Generator for SAP Business Data Cloud
product: SAP BW/4HANA
title: "Viewing Local Table (File) and Getting Data Updates"
page: c5b7a4fae2ce4b829914f9f825d6b471.html
url: https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/c5b7a4fae2ce4b829914f9f825d6b471.html?locale=en-US
source_type: SAP Help
---

# Viewing Local Table (File) and Getting Data Updates

*Working with Local Tables (File) · [auf help.sap.com öffnen](https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/c5b7a4fae2ce4b829914f9f825d6b471.html?locale=en-US)*

Viewing Local Table (File) and Getting Data Updates
-
## Viewing Local Table (File) and Getting Data Updates
You can view the local table (file) including its data and metadata in the Data
Builder in SAP Datasphere. The local table (file) can also be directly accessed from the SAP
BW/4HANA Cockpit, the SAP GUI, or the BW Modeling Tools. To merge new data pushed by the Data
Product Generator into the local table (file), you need to schedule a merge task manually or
via task chain.

### Prerequisites

- The BW administrator has set up and configured the Data Product Generator for
SAP Business Data Cloud. During the configuration, the BW administrator has
created a space to receive data pushed by the Data Product Generator (BW file
space). (For more information, see [Configuring the Data Product Generator](https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/8586340e2bf647d783e4cf506559c25a.html?locale=en-US&state=DRAFT&version=1.0).)

- The BW administrator has created, saved, and run a data subscription to replicate
data from a BW InfoProvider into a local table (file) in the BW file space in SAP
Datasphere. As a result, the local table (file) has been successfully generated
and deployed in the space. (For more information, see [Creating Data Subscriptions](f2e950ed4e8c475b8571478d6c2004c0.html).)

Note

For each data subscription a separate local table (file) will be created.
The local table (file) will contain the data extracted from the selected
ODP-based source (InfoProvider). This means one InfoProvider maps to one
data subscription and through this to one local table (file).

### Viewing Data and Fields of Local Table (File)

You can view the read-only data and properties of the local table (file) in your SAP
Datasphere tenant, either by logging on to SAP Datasphere and using the Data Builder or
by accessing the local table (file) directly from the data subscription.

- In the Data Subscriptions app in the SAP BW/4HANA Cockpit, you can directly open
the local table (file) from within your BW system by selecting View
Local Table (File) in the Local Table (File)
column in the data subscriptions list (you might first have to toggle this column
via Settings ()), or by using the equivalent
button in the Maintain Data Subscription screen.

- In the RSDPS transaction in the SAP GUI, you can preview the remote data in the
local table (file) by selecting the data subscription and then choosing
Browse () in the top bar.

- In the Data Subscriptions view in the BW Modeling Tools, you can open the local
table (file) via CTRL + Click on Show Local Table
(File) in the Local Table (File) column in
the data subscriptions list.

- In the Data Builder in SAP Datasphere, you can open a preview of the data in the
local table (file) by selecting View () in the top
bar.
The preview will show the columns of the local table (file) and a select
amount of records.

Note

The data subscription is not only extracting the data out of the InfoProvider, but also some
of its metadata (such as fields, data types, …). This metadata will be carried over
into the local table (file), making semantic context from BW objects accessible for
further usage.
In the Data Builder, you can also view this semantic context by
clicking on the name of the local table (file). Here, you can see its definition
including fields, data types, and further properties.

### Getting Data Updates for Local Table (File) from BW System

If a data subscription pushes new data or delta data into the same local table (file),
the new data will first arrive in the inbound buffer of the object store of SAP
Datasphere.

To update the data in the local table (file), you need to manually schedule a merge task
or use a task chain in SAP Datasphere.

- Manually schedule a merge task: To merge the data updates
manually, you need to create and schedule a Data Task in your SAP Datasphere
tenant. Go to the tab Tasks, create a new task, select
Merge as the task type, and configure the source tables
(snapshot/delta) and the target tables. Then, schedule the task to run as needed.
For more information, see [Merge or Optimize Local Table (File)](https://help.sap.com/docs/SAP_DATASPHERE/be5967d099974c69b77f4549425ca4c0/e533b154ed3e49ce9a03e4421a5296e7.html).

- Run a task chain: To automate this process, you can create a
task chain that includes the merge task. Go to the tab Task
Chains, create a new task chain, add the merge task, and configure
a schedule. This way the merge will run automatically according to the defined
schedule. For more information, see [Creating Task Chain](https://help.sap.com/docs/SAP_DATASPHERE/c8a54ee704e94e15926551293243fd1d/d1afbc2b9ee84d44a00b0b777ac243e1.html).

Note

In the inbound buffer, no duplication will happen. The data subscription will
continue to push data updates into the inbound buffer in the same table until a merge
task has emptied it. For this, it doesn't matter whether the data arrives in several
batches at different times (having different timestamps).
Tip

If
you have created a data product out of the local table (file) via the Data Sharing
Cockpit, the data in this data product is updated automatically if the data
subscription pushed new data from the BW system and you merge it into the local table
(file). There is no manual update for the data product required.
