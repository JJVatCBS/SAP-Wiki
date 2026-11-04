---
guide: Data Product Generator for SAP Business Data Cloud
product: SAP BW/4HANA
title: "Scheduling Data Subscriptions With Process Chains"
page: 72807766954d4b49b03b039946ad490e.html
url: https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/72807766954d4b49b03b039946ad490e.html?locale=en-US
source_type: SAP Help
---

# Scheduling Data Subscriptions With Process Chains

*Automating Tasks and Operations · [auf help.sap.com öffnen](https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/72807766954d4b49b03b039946ad490e.html?locale=en-US)*

Scheduling Data Subscriptions With Process Chains
-
## Scheduling Data Subscriptions With Process Chains
You can use process chains to schedule the extraction of data from BW objects with the
Data Product Generator. To do this, you create a process variant in your BW system and
select it for the data subscription you want to schedule.

### Prerequisites

- You have set up and configured the Data Product Generator for SAP Business Data Cloud. For
more information, see [Configuring the Data Product Generator](8586340e2bf647d783e4cf506559c25a.html).

Note

Create and save the process chain and its variant before you configure the
data subscription. The value help in the data subscription only shows variants
that already exist in the system.

### Context

There are two assignment modes for linking the process variant to the data
subscriptions:

- Process variant-driven assignment mode (default): You assign the data
subscriptions while you create or edit the process variant.

- Data subscription-driven assignment mode: You assign
the process variant while you create or edit the data subscription.

For more information, see [Assigning Data Subscriptions to a Process Variant](535a0f490c544314b6c9c3cd019e94f3.html).

### Procedure

Scheduling Data Subscriptions in the Process Variant-Driven Assignment Mode
(Default)

-
1. Create a process chain in your BW system and add a process variant with the
process type Load Process and Postprocessing – Data Provisioning
Subscription. On SAP BW/4HANA, this can be done via transaction
RSA1 or RSPC1 in the SAP GUI, or via the Process Chain Editor and Process
Variant Editor apps in the SAP BW/4HANA Cockpit. On SAP BW 7.5, use transaction
RSA1 or RSPC1 in the SAP GUI.

-
2. Assign the data subscriptions you want to schedule directly to the process
variant using the Use Variant-Driven Mode checkbox and
the data subscription table in the process variant maintenance screen. For
detailed steps, see [Assigning Data Subscriptions to a Process Variant](535a0f490c544314b6c9c3cd019e94f3.html).

-
3. Run the process chain to start the data extraction.
You can also run the data subscriptions directly from within the
Subscriptions in Variant screen, or alternatively
switch to the RSDPS transaction or the Data Subscriptions app and run the data
subscriptions from there.

Scheduling Data Subscriptions Using the Data
Subscription-Driven Assignment Mode

-
1. In your BW system, create a process chain.

-
2. Add a process variant with the process type Load Process and
Postprocessing – Data Provisioning Subscription to the process
chain. Leave the variant empty at this point.

-
3. Open the process variant maintenance screen and clear the Use
Variant-Driven Mode checkbox to enable data subscription-driven
mode.

-
4. In transaction RSDPS or in the Data Subscriptions app, create a new data
subscription or open an existing one. In the Scheduling
field, choose Process Variant and select the process
variant you created in step 2 from the value help.

Note

Only process variants in data subscription-driven mode are available for
selection. Process variants configured with the variant-driven mode do
not appear in this value help.

-
5. Activate the data subscription. For more information, see [Creating Data Subscriptions](f2e950ed4e8c475b8571478d6c2004c0.html).

-
6. Optional: To verify that the data subscription is now shown in the process
variant, open transaction RSA1 and open the Subscriptions in
Variant screen for the process variant.

In data subscription-driven mode, the Subscriptions in
Variant screen shows the data subscriptions that reference
the process variant from within their own configuration. You can also run
the data subscription directly from this screen.

-
7. Save and activate the process chain.

### Results

Your BW system now has a process chain that is linked to your data subscriptions. You can
run the data subscriptions via this process chain instead of running them manually.
You can also add further tasks and processes to the process chain or link task
chains to it to run full end-to-end workflows between your BW system and your SAP
Business Data Cloud landscape.
