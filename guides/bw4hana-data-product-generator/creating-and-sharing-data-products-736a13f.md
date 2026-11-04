---
guide: Data Product Generator for SAP Business Data Cloud
product: SAP BW/4HANA
title: "Creating and Sharing Data Products"
page: 736a13f2fec24c6d8839a41546188a4c.html
url: https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/736a13f2fec24c6d8839a41546188a4c.html?locale=en-US
source_type: SAP Help
---

# Creating and Sharing Data Products

*Data Product Generator for SAP Business Data Cloud · [auf help.sap.com öffnen](https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/736a13f2fec24c6d8839a41546188a4c.html?locale=en-US)*

Creating and Sharing Data Products
-
## Creating and Sharing Data Products
Data products are an object type in SAP Datasphere and SAP Business Data Cloud that has
been introduced to enable automated data sharing, governance, and consumption across
different applications and domains.

You can create data products out of your BW data through the Data Sharing Cockpit in SAP
Datasphere:

- [Creating Data Products (Data Sharing Cockpit)](b13c0b5d25eb4b658d5b76f60281e91c.html)

The BW data products will be listed in the catalog in SAP Datasphere and the SAP Business
Data Cloud cockpit and are from there available for further use cases:

- [Sharing Data Products to SAP Databricks](8e18183c402c49808463f19e68adda91.html)

Note

A data product is a ready to use, curated data set that is delivered for analytics, AI/ML,
and operational use cases and provides insights related to a specific business topic
or challenge. It consists of a refined data set, metadata describing the data set,
and an access port or Application Programming Interface (API), allowing to exchange
data with third-party applications.
The BW data product is created directly out of
the local table (files) in the BW file space which contains the data extracted
from the BW InfoProvider. This is how you can convert, for example, Sales Orders
from a DataStore object (advanced) (aDSO) into a BW data product delivering
insights about these Sales Orders.
The created BW data products are custom
data products (also called custom Delta Share data products or Delta Share data
products). This means they are maintained and governed by your own organization
and not by SAP.
