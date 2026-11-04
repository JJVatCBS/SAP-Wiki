---
guide: Data Product Generator for SAP Business Data Cloud
product: SAP BW/4HANA
title: "Creating Data Products (Data Sharing Cockpit)"
page: b13c0b5d25eb4b658d5b76f60281e91c.html
url: https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/b13c0b5d25eb4b658d5b76f60281e91c.html?locale=en-US
source_type: SAP Help
---

# Creating Data Products (Data Sharing Cockpit)

*Creating and Sharing Data Products · [auf help.sap.com öffnen](https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/b13c0b5d25eb4b658d5b76f60281e91c.html?locale=en-US)*

Creating Data Products (Data Sharing Cockpit)
-
## Creating Data Products (Data Sharing Cockpit)
You can create BW data products out of the local tables (file) in the BW file space by
utilizing the Data Sharing Cockpit in SAP Datasphere. The data products will be listed in
the catalog in SAP Datasphere and the SAP Business Data Cloud cockpit. From here, they are
available for further use cases, such as sharing them to SAP Databricks via Delta
Sharing.

### Prerequisites

- The BW administrator has set up and configured the Data Product Generator for SAP Business
Data Cloud. During the configuration, the BW administrator has created a
space to receive data pushed by the Data Product Generator (BW file space)
and performed all necessary connection setup tasks. (For more information,
see [Configuring the Data Product Generator](https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/8586340e2bf647d783e4cf506559c25a.html?locale=en-US&state=DRAFT&version=1.0).)

- The BW administrator has created and run a data subscription to replicate data from a BW
InfoProvider into a local table (file) in the BW file space in SAP Datasphere.
(For more information, see [Creating Data Subscriptions](f2e950ed4e8c475b8571478d6c2004c0.html).)

- The BDC administrator has created a formations profile in the Data Sharing Cockpit in SAP
Datasphere. This is a specialized data provider profile that enables the
creation and consumption of data products exclusively within a specific SAP
system formation (e.g. an SAP Business Data Cloud formation). To configure the
formations profile you need to go to Data Sharing Cockpit  My Data Provider Profile  Create Data Provider Profile, fill in the profile, and select the visibility option
Formations. (For more information, see [Creating Custom Delta Share Data Products - Creating
Formations Profile (SAP Datasphere)](https://help.sap.com/docs/SAP_DATASPHERE/e4059f908d16406492956e5dbcf142dc/b07e95d07a1e4569b87d9bb57b732bcf.html).)

### Context

To create a data product out of BW data pushed by the Data Product Generator, you need to
utilize the Data Sharing Cockpit. This is a dedicated app available in your SAP
Datasphere tenant to create and publish data products into the catalog. (For more
information, see [Creating Custom Delta Share Data Products (SAP
Datasphere)](https://help.sap.com/docs/SAP_DATASPHERE/e4059f908d16406492956e5dbcf142dc/b07e95d07a1e4569b87d9bb57b732bcf.html).Note

The created BW data product will be a custom data
product on a Delta Share runtime (also called custom Delta Share data product or
Delta Share data product). This means it is optimized for sharing to other SAP
systems or supported third-party systems such as SAP Databricks via the Delta
Sharing protocol.
There are other types of data products that can be created
through the Data Sharing Cockpit, which are called marketplace data
products. These are proprietary to SAP and published to the catalog in the
Data Products (Marketplace) collection in SAP Datasphere. The BW data
products however are not marketplace data products.

### Procedure

-
In your SAP Datasphere tenant, open the sidebar navigation, and go to Data Sharing Cockpit  My Data Products.
Here, you can view a list of all your data products, as well as the
space they belong to, their status, their visibility, and their number of
installations.

-
To create a new data product, go to the top bar and select Create
Product.
A new screen will open where you can fill in the details of the data
product.

-
Enter a Business Name for your data product (e.g. Sales
Orders). The Technical Name will be automatically filled
in (e.g. SALES_ORDERS).

-
In the section Overview, enter a description for your
data product (e.g. BW DataStore object (advanced) containing Sales
Orders).

-
In the section Product Details, select a Data
Category (e.g. Company Data).
The field Contexts is automatically set to
Formations since you create the data product as a
formations provider. The field Data Shipments is also
automatically set to Integrated Delivery and the field
Delivery Mode to Delta Share.
Under Pricing, the Contract Type
is automatically set to Free. It is not possible to
adjust any of these default values.

-
In the section Product Artifacts, select your BW file
space as the Product Artifact Space.
The selected space contains the local tables (file) with your BW data.
The Storage Type will be automatically set to
SAP HANA Cloud, data lake Files as this is the
technology used under the BW file space to store the data.

-
Select the plus icon beside the space name to open a new screen for adding the
local table (file) with your BW data. Here, search for and tick off the checkbox
for your local table (file). Then, choose Select to
continue.

-
Select Save Changes to confirm your settings and create
the data product.

-
In the results screen, select Switch Status and choose
List to list the data product.
In the results screen the details of the data product will now be filled
in and the Lifecycle Status will change to
Listing.If you go back to My Data
Products you can now also see the new data product you just
created.

### Results

Some time after the data product has been listed, it will be accessible from the catalog
in SAP Datasphere and in the SAP Business Data Cloud cockpit under the Data
Products collection.Note

It might take a while until the data product
appeared in the catalog because the systems need to synchronize first. If you want
that it appears immediately, contact your catalog administrator to run a manual
synchronization.
