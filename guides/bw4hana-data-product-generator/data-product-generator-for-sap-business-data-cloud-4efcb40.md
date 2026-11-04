---
guide: Data Product Generator for SAP Business Data Cloud
product: SAP BW/4HANA
title: "Data Product Generator for SAP Business Data Cloud"
page: 4efcb40d03334381a6111fd9d270b7f0.html
url: https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/4efcb40d03334381a6111fd9d270b7f0.html?locale=en-US
source_type: SAP Help
---

# Data Product Generator for SAP Business Data Cloud

*Data Product Generator for SAP Business Data Cloud · [auf help.sap.com öffnen](https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/4efcb40d03334381a6111fd9d270b7f0.html?locale=en-US)*

Data Product Generator for SAP Business Data Cloud
-
## Data Product Generator for SAP Business Data Cloud
The Data Product Generator for SAP Business Data Cloud is a dedicated toolset available
for SAP BW and SAP BW/4HANA allowing you to extract data from your existing BW
InfoProviders into local tables (file) in the object store of SAP Datasphere in
SAP Business Data Cloud.
To support the Data Product Generator, the data subscriptions have been introduced as a new
object type in BW. You can create, maintain, and run the data
subscriptions in a dedicated Data Subscriptions app in the SAP
BW/4HANA Cockpit, in the RSDPS transaction in the SAP GUI, or in dedicated Eclipse
views in the BW Modeling Tools.
By creating a data subscription, you can replicate data from a specific BW InfoProvider into a local table (file). The local table (file) with the BW data will be generated into a dedicated BW file space which has been created during the initial configuration of the Data Product Generator. The local tables (file) in this space are read-only, but it's possible to perform data management tasks such as previewing, exporting, or deleting the data. To use the data in modeling scenarios, you can share it to other spaces where it can be consumed in views and analytic models.
To enable further use cases for SAP Business Data Cloud, you can create a data product out of
the local table (file) in the Data Sharing Cockpit. The created data
product can be accessed from the catalog in the SAP Business Data
Cloud cockpit, where it can be delta shared to SAP Databricks for
advanced AI/ML workflows on top of your BW data.
