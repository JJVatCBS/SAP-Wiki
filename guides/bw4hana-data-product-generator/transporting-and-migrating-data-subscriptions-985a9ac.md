---
guide: Data Product Generator for SAP Business Data Cloud
product: SAP BW/4HANA
title: "Transporting and Migrating Data Subscriptions"
page: 985a9ac9f61047e39639ba0440465ed4.html
url: https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/985a9ac9f61047e39639ba0440465ed4.html?locale=en-US
source_type: SAP Help
---

# Transporting and Migrating Data Subscriptions

*Maintaining Data Subscriptions · [auf help.sap.com öffnen](https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/985a9ac9f61047e39639ba0440465ed4.html?locale=en-US)*

Transporting and Migrating Data Subscriptions
-
## Transporting and Migrating Data Subscriptions
You can transport data subscriptions between different BW systems (e.g. production,
development, quality) if they are in the DSUB format (TLOGO type for the data
subscriptions). To migrate the data subscriptions from the SUBS to the DSUB format, you can
use a dedicated ABAP report in the SAP GUI.

### Transporting Data Subscriptions

To make the data subscriptions transportable, a new data subscriptions type (DSUB) has
been introduced. The DSUBs follow the TLOGO framework for all BW objects with DSUB
denoting the TLOGO type.Note

The TLOGO framework (TLOGO = Transportable Logical
Object) is the unified transport architecture behind all BW objects, letting you
group, identify, and transport BW objects through the system
landscape.
Transportable BW objects have a TLOGO type, such as ELEM for BW
Queries, or DSUB for the data subscriptions. The TLOGO type defines what
kind of object you want to transport, how it is stored in the database, how
it behaves during the transport, and which sub-objects belong to it. This
allows the BW system to treat complex BW objects as single units during
transport.

Local data subscriptions (which are not transportable) remain in the old data subscriptions
type (SUBS). You can migrate data subscriptions from SUBS to DSUB format by using
the ABAP report RSDDS_DSUB_MIGRATION. In addition, all new data subscriptions are
now automatically created as DSUBs. For more information on the data subscriptions
types, see [Data Subscription (DSUB and SUBS)](5ad3c27c5f8640b39ba26a838cd93c1b.html).

To be able to transport a data subscription, it needs to fulfill the following
prerequisites:

- Be of the type DSUB (TLOGO type) and not SUBS. If you want to transport a data subscription
of type SUBS, you first need to migrate it to the DSUB type via
RSDDS_DSUB_MIGRATION. (For more information, see section "Migrating Data
Subscriptions".)

- Be assigned to a transport request and package. This happens during initial creation of the
data subscription ([Creating Data Subscriptions](f2e950ed4e8c475b8571478d6c2004c0.html)) or
during migration to DSUB format.
Note

A transport request is a container in
the Change and Transport System (CTS) that collects the changes in the
BW object you want to move between different systems.
The package is
the ABAP container the BW object is assigned to in the repository.
It determines whether the object is transportable, as well as its
transport layer. The package $TMP is for holding local objects which
cannot be transported. It is the default package assigned if you
create a new data subscription. If you want to transport the data
subscription, ensure to assign it to a different package than
$TMP.
If no package is given for the data subscription, it
will be automatically assigned to $TMP.

- Be in A (Active) state, which means the data subscription must have been
activated. (For more information, see section "Activating and Deactivating
Data Subscriptions".)

### Activating and Deactivating Data Subscriptions

The TLOGO object for the data subscriptions (DSUB) supports an A (Active) and an M
(Modified) version:

- A (Active): This version of the data subscription is
validated and executable. All changes have been checked in and runtime
artifacts have been generated or regenerated. Data subscriptions in A state
can be run or transported to production and quality systems.

- M (Modified): This version of the data subscription has
been changed and is still marked as a work in progress. Before you can run
or transport it, you need to activate it to convert it to A state and check
in the changes.

Activating the data subscription turns it from an M (Modified) to an A (Active) state.
Deactivating the data subscription sets it in a state that cannot be run.

There are different ways to activate or deactivate a data subscription:

- Data Subscriptions app (SAP BW/4HANA Cockpit):

- Select a data subscription in the list and choose Toggle
Status in the top bar to switch between active and
inactive version.

- Click on a data subscription to open the Maintain Subscription
screen and there choose Activate or
Deactivate in the bottom bar.
Note

In the
field Active Version in the data
subscription details header, you can view the current state of
the object:

- Executable, Equal to Revised
Version: Data subscription has been
activated and A (Active) version equals M (Modified)
version. It can be run or transported.

- Executable, Not Equal to Revised
Version: Data subscription has been
activated, but changed afterwards, so A (Active)
version is different than M (Modified) version. It
can be run in the A version, but if you want to
consider changes, you first need to activate
again.

- Not Executable, Not Equal to Revised
Version: Data subscription has been
deactivated and changed afterwards, so A (Active)
version is different than M (Modified) version.

- Not Executable, Equal to Revised
Version: Data subscription has been
deactivated, but no changes have been made yet, so A
(Active) version equals M (Modified) version.

- Does not Exist: Data
subscription only exists in M (Modified) version and
has never been activated before. This is typically
the case after first time creation of the
object.

- RSDPS transaction (SAP GUI):

- Select a data subscription in the list and select Edit () to
open the edit screen. Here choose Activate Data
Subscription () to activate the
data subscription.
Note

In the field Active
Version in the edit screen, you can view the
current state of the object:

- Not exists: Data subscription has
never been activated before. This is typically the case
after first time creation of the object.

- Executable: Data subscription has
been activated and can be run or transported.

- Not executable: Data subscription
has been deactivated and cannot be run or
transported.

The status of the data subscription can also be viewed
in the columns State and
Revision in the data
subscriptions list. For a full overview, see [RSDPS Transaction in SAP GUI](67d73d2e2086409c8bc06ff79b116476.html).

### Migrating Data Subscriptions from SUBS to DSUB

You can use the RSDDS_DSUB_MIGRATION report in the SAP GUI to convert existing local
data subscriptions (SUBS) into transportable data subscriptions (DSUB).

Note

All newly created data subscriptions are automatically DSUBs. You can only
transport data subscriptions if they are DSUBs and not SUBSs, so performing the
migration is a necessary prerequisite for the transporting operation.

To migrate the data subscriptions, perform the following procedure:

- Call transaction SE38 and enter the program name RSDDS_DSUB_MIGRATION, then select
Execute () in the top bar.
As a
result, the report TLOGO Migration for Data
Subscriptions will open.

- Select the data subscriptions you want to migrate from SUBS to DSUB format.
You can select one data subscription or multiple at once.

- In the field Transport Request, enter the number of the transport
request for the DSUBs.
Note

If you do not already have created a transport
request, you can do so via SE09/SE10. Make sure to assign the correct
package to the request so the transport layer knows the system
path.

- In the field Package, choose the package the objects will belong to.
If you click on , a pop-up will open in
which you can specify the package, as well as its transport layer (system
path for objects in the package), and the maximum number of hits (how many
objects can be assigned to the package).

- (Optional) Select Enable Simulation if you want to preview the
simulated results of the migration operation without performing any actual
changes on your objects.

As a result, all selected data subscriptions in the SUBS format will be migrated to be TLOGOs
in the DSUB format.

They can now be transported between different systems, as well as activated to switch
between M (Modified) and A (Active) version.
