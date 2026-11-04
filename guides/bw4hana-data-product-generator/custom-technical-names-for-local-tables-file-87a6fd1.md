---
guide: Data Product Generator for SAP Business Data Cloud
product: SAP BW/4HANA
title: "Custom Technical Names for Local Tables (File)"
page: 87a6fd1da8cd44509e77c232f39c8449.html
url: https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/87a6fd1da8cd44509e77c232f39c8449.html?locale=en-US
source_type: SAP Help
---

# Custom Technical Names for Local Tables (File)

*Working with Local Tables (File) · [auf help.sap.com öffnen](https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/87a6fd1da8cd44509e77c232f39c8449.html?locale=en-US)*

Custom Technical Names for Local Tables (File)
-
## Custom Technical Names for Local Tables (File)
When creating a data subscription, you can define a custom technical name for the local
table (file) that SAP Datasphere in SAP Business Data Cloud generates, instead of relying on
a system-generated name.

### Technical Names of Local Tables (File)

Each data subscription generates one or multiple local tables (file) in SAP Datasphere in SAP
Business Data Cloud. The technical name of the local table (file) is a unique
internal identifier for that object. By default, the system derives the technical
name automatically from the selected source object (InfoProvider). By setting a
custom technical name, you can change the default behavior and enter a meaningful
identifier of your choice when creating the data subscription.

This is particularly useful if you manage a large number of data subscriptions across multiple BW
systems and need the associated local tables (file) to follow a consistent naming
convention — for example, one that reflects the source system, functional area, or
data domain. Descriptive technical names make local tables (file) immediately
recognizable in SAP Datasphere in SAP Business Data Cloud without having to trace
them back to their originating data subscription.

The following rules apply to technical names of local tables (file):

- If you do not enter a custom technical name, the system derives a default
name from the source object name and applies it when you save the data
subscription.

- If the derived name already exists in the target SAP Datasphere tenant in SAP Business Data
Cloud, the system appends a numeric counter suffix to ensure uniqueness (for
example, SALES_DATA_1 ).

- The technical name of the local table (file) is independent from the
technical name of the data subscription itself. The system generates the
data subscription's own technical name automatically and you cannot change
it.

- The system performs a collision check whenever you save, activate, or transport a data
subscription. If the technical name already exists in the target system, the
operation fails and the system displays an error message. You must provide a
unique technical name for the local table (file) before you can proceed.

### Setting Custom Technical Name for Local Table (File)

You can set a custom technical name for the local table (file) via the Base
Name field when you create the data subscription.

If you create a hierarchy data subscription, the custom technical name you set will
be used as a base name in combination with the suffixes for the individual local
tables (file) that are generated for each hierarchy data subscription. These
technical names can be viewed under the Base Name field if
you create or edit the data subscription.

After first time creation it is still possible to change the custom technical name if you edit
the data subscription as long as you have not activated it yet. Once you activate
the data subscription, the system creates and deploys the local table (file). The
technical name then becomes read-only and you can no longer change it.

### Migration Report for Existing Data Subscriptions

For existing data subscriptions created before the upgrade for custom technical names was
available, the technical name field of the local table (file) will be empty until
you enable it.

To migrate your existing data subscriptions and enable the technical name field, run the ABAP
report RSDDS_LTF_TECH_NAME_POP in the SAP GUI. The report populates
the technical name field for data subscriptions that already existed in your system
before the upgrade. Following the migration, you will be able to edit that field and
set a custom technical name for those of these data subscriptions that haven't been
activated yet. If you create new data subscriptions after the upgrade you can
directly set and edit a custom technical name for their local tables (file).

Note

Run this report in all your system environments, including development, test,
and production. Changes made to data subscriptions by this report are not
transported automatically between systems.

Caution

Before running RSDDS_LTF_TECH_NAME_POP, ensure that you have migrated all
selected data subscriptions to the TLOGO type (DSUB). It is not possible to
enable the technical name field for data subscriptions of type SUBS. For more
information, see [Transporting and Migrating Data Subscriptions](https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/985a9ac9f61047e39639ba0440465ed4.html?state=DRAFT).

- Open your BW system in the SAP GUI and call transaction SE38.

- Enter the program name RSDDS_LTF_TECH_NAME_POP and select
Execute.

- Under Select Data Subscriptions for Update select the data subscriptions
for which you want to enable the technical name field of the local table
(file).

- (Optional) Choose Adjust "Last Changed By" Field to let the report
update the Last Changed By field of the selected data
subscriptions as well.

- (Optional) Choose Enable Simulation to preview the results of the
migration without making any actual changes to the selected data subscriptions.
If you select this option, no data subscriptions will be updated - it is for
previewing the potential outcome and making adjustments if there are still any
error messages.

- Run the report. The report log displays the results of the migration, including how many data
subscriptions have been selected and updated or if there have been any errors.
Use the error messages to resolve any issues accordingly.
