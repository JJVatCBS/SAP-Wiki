---
guide: Data Product Generator for SAP Business Data Cloud
product: SAP BW/4HANA
title: "Configuring the Data Product Generator"
page: 8586340e2bf647d783e4cf506559c25a.html
url: https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/8586340e2bf647d783e4cf506559c25a.html?locale=en-US
source_type: SAP Help
---

# Configuring the Data Product Generator

*Data Product Generator for SAP Business Data Cloud · [auf help.sap.com öffnen](https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/8586340e2bf647d783e4cf506559c25a.html?locale=en-US)*

Configuring the Data Product Generator
-
## Configuring the Data Product Generator
Configure the Data Product Generator for SAP Business Data Cloud to connect your
on-premise SAP BW or SAP BW/4HANA system with your SAP BDC system to enable reuse of
existing data in BW InfoProviders for scenarios across the SAP BDC landscape.

### Preparing your SAP BW or SAP BW/4HANA System

#### Ensuring Minimum Systems Requirements

Before you can use the Data Product Generator, ensure you're on a supported SAP BW or SAP
BW/4HANA system which has been lifted into the private cloud component of SAP
Business Data Cloud. In addition, you need to have an SAP Business Data Cloud
cockpit tenant with an SAP Datasphere system in the formation.

The Data Product Generator for SAP Business Data Cloud is available for SAP BW 7.5 SP24 or
higher, SAP BW/4HANA 2021 SP04 or higher, and SAP BW/4HANA 2023 SP00 or higher.
Caution

For SAP BW/4HANA 2023, technical availability of the Data Product
Generator starts from SP00. However, productive usage is only supported
and recommended from SP04 or higher. Using the Data Product Generator on
SAP BW/4HANA 2023 SP00–SP03 is intended for prototyping or functional
testing only. There will be no further deliveries of new functionality
or performance improvements for SAP BW/4HANA 2023 SP00–SP03. For
productive usage, upgrade to SAP BW/4HANA 2023 SP04 or higher. For more
information, see SAP Note [3593519](https://me.sap.com/notes/3593519).
Note

The Data Product Generator is not available
for embedded SAP BW systems, such as in SAP S/4HANA. For more information,
see SAP Note [3584640](https://me.sap.com/notes/3584640).
Note

Some features of the
Data Product Generator are only available on higher support packages than
the minimum systems requirements for the Data Product Generator itself. For
more information, see [What's New (Release Information)](207bd08e56a8487e88173373fd2f46b8.html).
Your SAP BW or SAP BW/4HANA system needs to be in a private cloud
environment in SAP Business Data Cloud, also referred to as SAP Business
Warehouse, private cloud edition for SAP NetWeaver, or SAP BW/4HANA, private
cloud edition. If your SAP BW or SAP BW/4HANA system isn't in a private cloud
environment yet, please get in touch with SAP's sales representatives to assist
you with lifting your BW environment into the private cloud component of SAP
BDC.

You also need to have an SAP Business Data Cloud cockpit tenant with an SAP
Datasphere system in the formation. For further use cases, such as sharing to
SAP Databricks, you would require further components of SAP Business Data Cloud,
such as the SAP Databricks capability.Tip

It is possible to rewire
your existing standalone SAP Datasphere tenant into an SAP Business Data
Cloud system. For more information, see [Updating Your SAP Datasphere and SAP Analytics Cloud
Subscriptions to SAP Business Data
Cloud.](https://help.sap.com/docs/business-data-cloud/administering-sap-business-data-cloud/rewiring-of-standalone-sap-datasphere-and-sap-analytics-cloud-subscriptions-to-sap-business-data-cloud)

### Configuring the Data Product Generator

#### Enabling Object Store for SAP Datasphere

The object store needs to be enabled and configured in your SAP Datasphere
tenant.

To configure the object store in SAP Datasphere, go to Configuration    Tenant Configuration  Object Store. Here you can make the necessary settings for
Storage (storage size of object store in TB),
Compute (computing power in block-hours), and
Requests (number of API calls needed per month). For
more information, see [Configure the Size of Your SAP Datasphere
Tenant](https://help.sap.com/docs/SAP_DATASPHERE/9f804b8efa8043539289f42f372c4862/33f8ef4ec359409fb75925a68c23ebc3.html).

#### Configuration of the Data Product Generator

To configure the Data Product Generator, follow the steps provided in SAP Note
[3590400](https://me.sap.com/notes/3590400).

You need to conduct the configurations for the first-time setup of the Data Product
Generator manually.

To get started with the process, open a support case on component BDC-BW.Note

This is needed
to authorize you to use the Data Product Generator and register your BW system
on the SAP Business Data Cloud cockpit tenant with the SAP Datasphere system in
the formation. However, you still need to configure the Data Product Generator
manually by yourself.
If your systems and existing licenses fulfill the
requirements, the necessary instructions and tooling for the configuration will be
provided to you.

For the manual configurations, refer to the Configuring the Data Product
Generator guide which you can find here: [Configuring the Data Product Generator for
SAP Business Data Cloud](https://www.sap.com/documents/2026/06/a289a708-597f-0010-bca6-c68f7e60039b.html).
