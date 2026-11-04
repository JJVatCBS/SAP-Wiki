---
guide: Data Product Generator for SAP Business Data Cloud
product: SAP BW/4HANA
title: "Automating Tasks and Operations"
page: 5d2a9ac9813c4680bb3a3d50d30c7b58.html
url: https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/5d2a9ac9813c4680bb3a3d50d30c7b58.html?locale=en-US
source_type: SAP Help
---

# Automating Tasks and Operations

*Data Product Generator for SAP Business Data Cloud · [auf help.sap.com öffnen](https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/5d2a9ac9813c4680bb3a3d50d30c7b58.html?locale=en-US)*

Automating Tasks and Operations
-
## Automating Tasks and Operations
SAP Business Warehouse, private cloud edition provides advanced capabilities for the
automation of tasks and operations, scheduling of processes, and integration with similar
options from SAP Datasphere and SAP Business Data Cloud.

### Important Concepts

Scheduling of processes and tasks is possible via process chains in
SAP BW and SAP BW/4HANA and via task chains in SAP
Datasphere.

A process chain is an automated sequence of processes in SAP BW
and SAP BW/4HANA which can be used to manage and control data loading and
transformation tasks in a structured way. Process chains link multiple steps (called
processes) together and run them in a defined order. This automates ETL (Extract,
Transform, Load) operations in BW, such as loading data from source systems,
activating DataStore objects (DSOs), running transformations and aggregations, and
starting reports or alerts after completion. If you create a process chain, you need
to enter its process type and process variant.

The process type is predefined by SAP or can be created by
users. There are standard process types available for all activities around data
loading and data maintenance as well as some general services (e.g. activate
DataStore objects, delete requests, start ABAP program).

The process variant is a reusable configuration for the process
types to define specific settings applying to them (e.g. in the process type for
task chains you can configure which task chain you want to include and in which SAP
Datasphere space it is located). The variants correspond with the process steps. You
can create multiple variants for the same process type and include them in the same
process chain (e.g. for loading data from multiple different sources via the same
loading mechanism).

A task chain is an automation option available in SAP Datasphere
to streamline and orchestrate data integration processes. Task chains can be created
in the Data Builder in SAP Datasphere by adding different elements to the task chain
canvas. As elements you can add, for example, local tables, remote tables and views,
data flows, replication flows, transformation flows, and even other task chains.

While the BW file space (inbound space) of the Data Product Generator is read-only
and it's not possible to create any objects in it, you can still use it to create
task chains. In addition, task chains can be created in other spaces in your SAP
Datasphere tenant. With SAP Business Warehouse, private cloud edition, it's possible
to link these task chains with process chains created in your BW environment. This
enables you to schedule end-to-end processes between your BW system and your SAP
Business Data Cloud landscape.

You can find more information on process chains in SAP BW/4HANA ([Process Chain (SAP BW/4HANA)](https://help.sap.com/docs/SAP_BW4HANA/107a6e8a38b74ede94c833ca3b7b6f51/8fc08b3baaa59649e10000000a11402f.html?q=process+chain)) and in SAP BW ([Process Chain (SAP BW 7.5)](https://help.sap.com/docs/SAP_NETWEAVER_750/2e90b26cf7484203a523bf0f4b1bc137/8fc08b3baaa59649e10000000a11402f.html?q=process+chain)).

### Key Use Cases

You can not only schedule data subscriptions via process chains, but also include
subsequent processes in SAP Datasphere via task chains.

- You can schedule the extraction of data with the Data Product Generator via
process chain from within your BW environment. This enables you to run a
data subscription through a process chain instead of having to run it
manually. It's also possible to schedule extraction via scenarios through
process chains. For more information, see [Scheduling Data Subscriptions With Process Chains](72807766954d4b49b03b039946ad490e.html).

- You can link task chains from your connected SAP Datasphere tenant with
process chains in your BW system. This lets you, for example, schedule a
merge task to automatically merge new data pushed by a data subscription
into the local table (file) in SAP Datasphere. For more information, see
[Running Task Chains in Process Chains](80e745c4a5a146909345e45c8dc4d7a6.html) and [Viewing Local Table (File) and Getting Data Updates](c5b7a4fae2ce4b829914f9f825d6b471.html).
