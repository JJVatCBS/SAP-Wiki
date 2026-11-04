---
guide: Data Product Generator for SAP Business Data Cloud
product: SAP BW/4HANA
title: "Sharing Data Products to SAP Databricks"
page: 8e18183c402c49808463f19e68adda91.html
url: https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/8e18183c402c49808463f19e68adda91.html?locale=en-US
source_type: SAP Help
---

# Sharing Data Products to SAP Databricks

*Creating and Sharing Data Products · [auf help.sap.com öffnen](https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/8e18183c402c49808463f19e68adda91.html?locale=en-US)*

Sharing Data Products to SAP Databricks
-
## Sharing Data Products to SAP Databricks
You can share the BW data products you have created in the Data Sharing Cockpit via
Delta Sharing to SAP Databricks in case you have a SAP Databricks capability enabled in your
SAP Business Data Cloud formation.

### Prerequisites

- The BW administrator has used the Data Sharing Cockpit to create a custom data product on a
Delta Share runtime out of the BW data in the local table (file). The data
product with the BW data has been successfully listed and appears in the
catalog. (For more information, see [Creating Data Products (Data Sharing Cockpit)](b13c0b5d25eb4b658d5b76f60281e91c.html).)

- The BDC administrator has enabled SAP Databricks in their SAP Business Data
Cloud formation ([Provisioning SAP Databricks](https://help.sap.com/docs/business-data-cloud/administering-sap-business-data-cloud/provisioning-sap-databricks)) or
connected their existing Databricks instance as an external system via SAP
Business Data Cloud Connect ([Provisioning SAP Business Data Cloud
Connect](https://help.sap.com/docs/business-data-cloud/administering-sap-business-data-cloud/provision-sap-business-data-cloud-connector-for-supported-external-systems)).

### Context

Sharing the BW data products created in the Data Sharing Cockpit is possible through the
catalog entry point in the SAP Business Data Cloud cockpit.

You can share the data products to SAP Databricks in your SAP Business Data Cloud formation,
but also to a Databricks instance that is connected to your SAP Business Data Cloud
system as an external system through SAP Business Data Cloud Connect.

The share process works through the Delta Sharing protocol, an open protocol used by
Databricks for secure data sharing. Delta Sharing allows to share live data across
platforms, clouds, and regions without copying or moving it (zero-copy sharing).

### Procedure

-
Open the SAP Business Data Cloud Cockpit and go to Catalog & Marketplace  Search.

-
In the catalog, search for the data product you have just created out of the BW
data and open its details page.

-
Here, select Share to open the Manage
Access dialog.

-
In the Manage Access dialog, you can configure further
settings for sharing.

-
Go to Target System and select the SAP
Databricks system you want to share to.

-
Enter a Share Name for the data product.
This is the name the data product will have in the SAP Databricks catalog. You will not
be able to change it after sharing.Note

Only lowercase letters are
allowed for the Share Name.

-
Select a Workspace in SAP Databricks to share
to.
You can select one or multiple workspaces. If there is only one
workspace available, it will be automatically selected.Note

A workspace
is an environment in SAP Databricks to access all SAP Databricks
assets (such as notebooks, tables, views, SQL queries) for your team
or your department in one place. An organization can have multiple
workspaces or just one.

-
Once you're finished, select Share.

-
A message will appear to let you know the share process has started. Once the
process has been completed, the Manage Access dialog will
refresh and you can choose Open to directly open the data
product in SAP Databricks for further consumption or enrichment.
For detailed information on the process, see [Sharing Data Products to SAP Systems - Sharing Data
Products to SAP Databricks](https://help.sap.com/docs/business-data-cloud/governing-and-publishing-data-in-catalog/sharing-data-products-to-other-sap-systems#sharing-data-products-to-sap-databricks).Tip

You can also share the
data product through SAP Business Data Cloud Connect to an externally
connected Databricks system. For more information, see [Working with Data Products in SAP Business Data Cloud
Connect](https://help.sap.com/docs/business-data-cloud/sap-bdc-connector-for-existing-databricks-ab6ecce2c57f48cca8fb0dd9ab0488a2/introducing).

### Results

After the data product has been shared to SAP Databricks, the BW data can be used in
advanced AI (artificial intelligence) and ML (machine learning) workflows.

- In SAP Databricks, the data product is accessible as a Delta table in the
Unity Catalog. The schema and the Delta table can be found in the folder
Delta Share Received.

- You can act on the data by creating a notebook for tasks like data
preparation, data training, data forecasting, and writing the forecast
results into a Delta table.

- The Delta table can be shared back again to SAP Business Data Cloud. You can
also publish the share as a data product back into the catalog in the SAP
Business Data Cloud cockpit.

For more information, see [SAP Databricks
Documentation](https://docs.databricks.com/sap/en/).
