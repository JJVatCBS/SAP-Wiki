---
guide: Data Product Generator for SAP Business Data Cloud
product: SAP BW/4HANA
title: "Running Task Chains in Process Chains"
page: 80e745c4a5a146909345e45c8dc4d7a6.html
url: https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/80e745c4a5a146909345e45c8dc4d7a6.html?locale=en-US
source_type: SAP Help
---

# Running Task Chains in Process Chains

*Automating Tasks and Operations · [auf help.sap.com öffnen](https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/80e745c4a5a146909345e45c8dc4d7a6.html?locale=en-US)*

Running Task Chains in Process Chains
-
## Running Task Chains in Process Chains
You can run task chains from SAP Datasphere within process chains in your SAP Business
Warehouse, private cloud edition system by using the process type "Task Chain" that's
available from within the Process Chain Editor in the SAP BW/4HANA Cockpit or the Data
Warehousing Workbench in the SAP GUI.

### Prerequisites

- The BW administrator has set up and configured the Data Product Generator for SAP Business
Data Cloud. During the configuration, the BW administrator has created at least
one target for the Data Product Generator, as well as performed all necessary
connection setup tasks to establish connectivity to SAP Datasphere. (For more
information, see [Configuring the Data Product Generator](https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/8586340e2bf647d783e4cf506559c25a.html?locale=en-US&state=DRAFT&version=1.0) and [Configuring Targets for the Data Product Generator](4da38647b3d041728236df20d5a0308b.html).)

- The BW administrator has created a task chain in a space in SAP Datasphere using the Data
Builder. You can also create task chains in the BW file spaces associated with
the Data Product Generator. While the BW file space itself is read-only and you
cannot create any objects in it, it's still possible to create task chains. (For
more information, see [Creating Task Chain (SAP Datasphere)](https://help.sap.com/docs/SAP_DATASPHERE/c8a54ee704e94e15926551293243fd1d/d1afbc2b9ee84d44a00b0b777ac243e1.html?q=task+chain).)

### Context

Process chains can be created in the Process Chain Editor in the SAP BW/4HANA Cockpit
or in the Data Warehousing Workbench in the SAP GUI. If you create a new process chain,
you need to define the steps in the process by using process types and process
variants.With the process type "Task Chain" it's possible to include a task chain
from a space in SAP Datasphere in the process chain in your BW system.

### Procedure

-
Log on to SAP Datasphere and ensure you have a task chain created in a space
for which the user who runs the process chain is authorized.

-
Open the Process Chain Editor app in the SAP BW/4HANA
Cockpit.
Here you can view all currently existing process chains in your BW
system.

-
Select Create to create a new process chain.
In the process chain canvas that opens you can visually build the
process out of the individual process types as building blocks.

-
Select Add Process to define a new step in the process
chain.

-
Make further settings for the process in the Properties of
Process dialog.

-
As Process Type select General
Services - Task Chain.

-
(Optional) Tick off the checkbox Variant if you
want to use a process variant that you have previously defined in the
Process Variant Editor.

-
Enter a Description for the process (e.g. the
name of the task chain).

-
As Target select one of the targets you have
configured for the Data Product Generator to establish the connectivity
to SAP Datasphere.
In the value help you can chose from all existing targets you
have created for the Data Product Generator, including the target name,
description, and target type (HDLFS). If you have a configured a
user-preferred target for your BW system, it will be marked up with an X
in the column Preferred.

-
As Space select the space in which you have
created the task chain.

-
As Task Chain select the task chain you have
initially created in the space.

-
Save the new process by selecting Save.
Enter a Description and a Name for the
process chain and select the Package it should belong to.
Choosing an InfoArea is optional.As a result, you will
see the process chain loaded in the Process Chain Editor with the new
information.

-
Select Activate to make the process chain
executable.

-
Then, select Execute or
Scheduling to run the process chain.
Go to Monitoring to view the results of the
process chain run or resolve any error messages.

### Results

If you run the process chain containing the task chain, not only the process chain
will be executed, but also the task chain. This way you can directly run tasks in SAP
Datasphere (such as the merge task for the local tables (file)) directly from within
your BW system.
