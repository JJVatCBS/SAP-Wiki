---
guide: Data Product Generator for SAP Business Data Cloud
product: SAP BW/4HANA
title: "Assigning Data Subscriptions to a Process Variant"
page: 535a0f490c544314b6c9c3cd019e94f3.html
url: https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/535a0f490c544314b6c9c3cd019e94f3.html?locale=en-US
source_type: SAP Help
---

# Assigning Data Subscriptions to a Process Variant

*Automating Tasks and Operations · [auf help.sap.com öffnen](https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/535a0f490c544314b6c9c3cd019e94f3.html?locale=en-US)*

Assigning Data Subscriptions to a Process Variant
-
## Assigning Data Subscriptions to a Process Variant
You can assign data subscriptions directly to a process variant using the process
variant-driven assignment mode, which is the default mode for new process variants of type
Load Process and Postprocessing – Data Provisioning
Subscription.

### Prerequisites

- The BW administrator has set up and configured the Data Product Generator for SAP
Business Data Cloud. For more information, see [Configuring the Data Product Generator](8586340e2bf647d783e4cf506559c25a.html).

- The data subscriptions you want to assign to the process variant have been created and
activated. For more information, see [Creating Data Subscriptions](f2e950ed4e8c475b8571478d6c2004c0.html).

### Context

The Data Product Generator for SAP Business Data Cloud supports two assignment modes that
control how a process variant is linked to data subscriptions:

- Process variant-driven assignment mode: Data subscriptions are
assigned directly within the process variant. You add them to the data
subscription table in the process variant maintenance screen. This mode
gives you full control over the relationship from within the process variant
and allows you to assign multiple data subscriptions to a single process
variant. It also allows a single data subscription to be reused across
multiple process variants.

- Data subscription-driven assignment mode: The process variant is
selected from within the data subscription configuration. The relationship
is managed in the data subscription, not in the process variant.

The active assignment mode is controlled by the Use Variant-Driven
Mode checkbox in the process variant maintenance screen:

- When the checkbox is selected, the process variant is in the process variant-driven
assignment mode. The data subscription table in the maintenance screen is editable, and
you can add, edit, or delete data subscriptions directly.

- When the checkbox is cleared, the process variant is in the data subscription-driven
assignment mode. The data subscription table becomes read-only and shows data
subscriptions that reference the process variant from within their own configuration.
You manage the assignment in those data subscriptions, not in the process variant.

Note

Once you have added data subscriptions to the process variant, the Use
Variant-Driven Mode checkbox is disabled and you cannot change the
assignment mode. To switch modes, you must first remove all data subscriptions from the
data subscription table of the process variant.

On SAP BW/4HANA systems, you can maintain process variants in the Process Variant Editor
app in the SAP BW/4HANA Cockpit or in the RSPC transaction in the SAP GUI. On SAP BW 7.5
systems, use the RSPC transaction in the SAP GUI.

### Procedure

Assigning Data Subscriptions to a Process Variant in the SAP BW/4HANA
Cockpit

-
1. In the SAP BW/4HANA Cockpit, open the Process Variant Editor app and open or create
a process variant of type Load Process and Postprocessing – Data Provisioning
Subscription.

-
2. On the Properties tab, go to the Assignment
Mode section.

-
3. Verify that the Use Variant-Driven Mode checkbox is
selected.

For new process variants, the checkbox is selected by default. If the checkbox is not
selected yet and you want to use the process variant-driven assignment mode, select it.
If the checkbox is disabled, data subscriptions are already assigned and the mode is
locked.

-
4. In the Data Subscription section, select
+ to add a new row to the data subscription table.

-
5. In the new row, select the value help icon in the Data
Subscription column to search for and select a data subscription.

The value help displays available data subscriptions including their technical name,
description, and source name (name of the source BW object). Select the data
subscription you want to assign and confirm your selection.

-
6. Repeat the previous two steps for each additional data subscription you want to
assign.

-
7. Select Save to save the process variant with all assigned
data subscriptions.

Assigning Data Subscriptions to a Process Variant in the SAP GUI

-
1. Open your BW system in the SAP GUI and call transaction RSPC.

-
2. Open or create a process chain that includes a process variant of type
Load Process and Postprocessing – Data Provisioning
Subscription.

-
3. Open the process variant maintenance screen for the relevant process variant.

-
4. Verify that the Use Variant-Driven Mode checkbox is
selected.

For new process variants, the checkbox is selected by default. If the checkbox is not
selected and you want to use the process variant-driven assignment mode, select it. If
the checkbox is disabled, data subscriptions are already assigned and the mode is
locked.

-
5. In the Data Subscriptions section, place the cursor in an
empty row in the data subscription table and use the value help (F4) in the
Data Subscription column to search for and select a data
subscription.

The value help displays available data subscriptions including their technical name,
description, and source name (name of the source BW object).

-
6. Repeat the previous step for each additional data subscription you want to
assign.

-
7. Select Save to save the process variant with all assigned
data subscriptions.

### Results

The data subscriptions are now assigned to the process variant. The process variant is in
the process variant-driven assignment mode and the Use Variant-Driven
Mode checkbox is disabled to prevent mode changes while data subscriptions are
assigned. You can now include the process variant in a process chain to schedule the
extraction of data. For more information, see [Scheduling Data Subscriptions With Process Chains](72807766954d4b49b03b039946ad490e.html).
