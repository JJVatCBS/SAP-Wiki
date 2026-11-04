---
guide: Data Product Generator for SAP Business Data Cloud
product: SAP BW/4HANA
title: "Creating Data Subscriptions from Template"
page: c2c90f4fce964121a50d8f6794ea5dad.html
url: https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/c2c90f4fce964121a50d8f6794ea5dad.html?locale=en-US
source_type: SAP Help
---

# Creating Data Subscriptions from Template

*Maintaining Data Subscriptions · [auf help.sap.com öffnen](https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/c2c90f4fce964121a50d8f6794ea5dad.html?locale=en-US)*

Creating Data Subscriptions from Template
-
## Creating Data Subscriptions from Template
You can create a data subscription based on a template from an existing data
subscription. This allows you to take over settings, enabling you to create data subscriptions
faster and replicate existing extraction operations to more InfoProviders.

### Creating Data Subscriptions from Template in the SAP BW/4HANA Cockpit

In the SAP BW/4HANA Cockpit you can create data subscriptions in the Data Subscriptions
app.

- In the SAP BW/4HANA Cockpit, go to the section Data Product Generator for SAP
Business Data Cloud and open the app Data Subscriptions.

- Select one of the data subscriptions in the list. This will be the data subscription
you use as a template to create another data subscription.

- Select Create from Template amongst the buttons in the top
bar.
The details and settings of the new data subscription will be filled in based
on the information in the selected data subscription.Note

The new data subscription
will be a 1:1 copy of the old data subscription. However, it is possible to adjust a
select amount of properties in the copied data subscription.

- (Optional) In the field Source Name, select a different BW
InfoProvider to extract data from with the same settings.

- (Optional) In the field Target Name, select a different target
to extract data into with the same settings.

- Select Save to save the new data subscription.

- Select the Package the data subscription will belong to for
transport requests.
Note

Even if you create a new data subscription based on a template
from a data subscription of type SUBS, the new data subscription still will be of type
DSUB and therefore will be automatically transportable.

- (Optional) After you have saved the data subscription, you can adjust further settings
you don't want to take over from the template. It's possible to change the description
(Description), the extraction mode (Settings  Extraction Mode), the selection (Settings  Selections), the process chain (Settings  Process Chain Variant), and the projection (Projections).

- (Optional) Select Save to save the data subscription with the
adjusted properties.

### Creating Data Subscriptions from Template in the SAP GUI

In the SAP GUI you can create data subscriptions in the RSDPS transaction.

- Open your BW system in the SAP GUI and call transaction RSDPS.

- Select one of the data subscriptions in the list. This will be the data subscription
you use as a template to create another data subscription.

- Select Create from Template () amongst the icons in the top
bar.
The details and settings of the new data subscription will be filled in based
on the information in the selected data subscription.Note

The new data subscription
will be a 1:1 copy of the old data subscription. However, it is possible to adjust a
select amount of properties in the copied data subscription.

- (Optional) Adjust properties of the new data subscription you don't want to take over
from the template. It's possible to change the selected BW InfoProvider
(Source Name), the selected target (Target
Name), the extraction mode (Extraction Mode), and
the scheduling settings (Scheduling).

- Select Save () in the top bar to save the new data
subscription based on the template.

- Select the Package the data subscription will belong to for
transport requests.
Note

Even if you create a new data subscription based on a template
from a data subscription of type SUBS, the new data subscription still will be of type
DSUB and therefore automatically transportable.

- (Optional) After you have saved the data subscription, you can adjust further
settings. It's now possible to change the description
(Description), the selection (Edit
Selection), and the projection (Edit Projection).
In addition, you can now also still adjust the extraction mode (Extraction
Mode) and scheduling settings (Scheduling).

- (Optional) Select Save () in the top bar to save the data
subscription with the adjusted properties.
