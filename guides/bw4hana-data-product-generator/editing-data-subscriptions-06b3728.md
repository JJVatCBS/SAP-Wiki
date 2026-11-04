---
guide: Data Product Generator for SAP Business Data Cloud
product: SAP BW/4HANA
title: "Editing Data Subscriptions"
page: 06b37289aade411c8f289cac7095fc00.html
url: https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/06b37289aade411c8f289cac7095fc00.html?locale=en-US
source_type: SAP Help
---

# Editing Data Subscriptions

*Maintaining Data Subscriptions · [auf help.sap.com öffnen](https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/06b37289aade411c8f289cac7095fc00.html?locale=en-US)*

Editing Data Subscriptions
-
## Editing Data Subscriptions
You can edit existing data subscriptions after you have created them. This allows you to
still adjust the settings of a data subscription after initial creation.

### Editing Data Subscriptions in the SAP BW/4HANA Cockpit

In the SAP BW/4HANA Cockpit you can edit data subscriptions in the Data Subscriptions
app.

- In the SAP BW/4HANA Cockpit, go to the section Data Product Generator for SAP Business
Data Cloud and open the app Data Subscriptions.

- Click on the data subscription you want to edit in the list.
This opens the
Maintain Subscription screen where you can
view read-only properties of the data subscription, as well as adjust
the editable ones. In contrary to the SAP GUI, here you are
automatically in edit mode and don't need to switch to a dedicated edit
screen to perform changes.

- In the Maintain Subscription screen, adjust properties and settings
as needed.
Note

After you have created the data subscription and not run
yet, you can still edit the description
(Description), the process chain (Settings  Process Chain Variant), the extraction mode (Settings  Extraction Mode), the projection (Projections),
the selection (Settings  Selections) and the technical name of the local table (file) (General  Base Name).
Once you have run the data subscription and the local
table (file) has been created and deployed, you can only edit the
description (Description), and all other
fields (such as extraction mode, process chain, ...) become
read-only and cannot be adjusted anymore.
If you edit a
hierarchy data subscription (Source Type is
Snapshot), you cannot edit the extraction
mode since it is set to full by default and cannot be
changed.

- Select Save to save the changes.

- Select Activate to make the data subscription executable
again.
Note

In the Maintain Subscription screen you are viewing and
editing the M (Modified) version of the data subscription. If you do any
changes, you have to activate the data subscription again, so that the A
(Active) version equals the M (Modified) version. For more information
on the versions, see [Transporting and Migrating Data Subscriptions](985a9ac9f61047e39639ba0440465ed4.html).

### Editing Data Subscriptions in the SAP GUI

In the SAP GUI you can edit data subscriptions in the RSDPS transaction.

- Open your BW system in the SAP GUI and call transaction RSDPS.

- Select the data subscription you want to edit from the list.

- Choose Edit ()
among the icons in the top bar.
As a result, the edit screen will open,
providing an overview of the fields you can edit for the selected data
subscription.

- In the edit screen, adjust properties and settings as needed.
Note

Similarly to the Data
Subscriptions app, you can still edit the description
(Description), the scheduling settings
(Scheduling), the extraction mode
(Extraction Mode), the projection
(Edit Projection), the selection
(Edit Selection) and the technical name of
the local table (file) (Datasphere Local Table  Base Name) if you have not run the data subscription yet.
Once
you have run the data subscription and the local table (file) has
been created and deployed, you can only edit the description
(Description). All other fields (such as
extraction mode, scheduling settings, …) have now become read-only
and cannot be adjusted anymore.
If you edit a hierarchy data
subscription (Source Type is
Snapshot), you cannot edit the extraction
mode since it is set to full by default and cannot be
changed.
Tip

In the edit screen you can also
access the following options in the top bar:

- Display ↔ Change (): Switch
between displaying the properties of the data subscription
in view-only mode and in edit mode. This allows you to see
directly which properties you can still change (fields
displayed in white) and which not (fields greyed out).

- Check Data Subscription (): Check
the data subscription for any potential issues which could
impact the extraction of data. The results can be viewed in
a log screen, including any warnings or error messages
concerning the status of the source (InfoProvider), the
target, the connection to SAP Datasphere, and the local
table (file).

- Activate Data Subscription (): Make
the data subscription executable after it has been created
or changed. This changes the status of the data subscription
from Inactive to
Active.

- Data Preview ():
Preview the data set associated with the data subscription.
It's also possible to download this data set into a local
file or export it into other formats.

- Select Save () in
the top bar to save the changes.

- Select Activate Data Subscription () to make the data
subscription executable again.
Note

In the edit screen you are viewing and
editing the M (Modified) version of the data subscription. If you do any
changes, you have to activate the data subscription again, so that the A
(Active) version equals the M (Modified) version. For more information
on the versions, see [Transporting and Migrating Data Subscriptions](985a9ac9f61047e39639ba0440465ed4.html).
