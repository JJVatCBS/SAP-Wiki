---
guide: Data Product Generator for SAP Business Data Cloud
product: SAP BW/4HANA
title: "Using Scenario Generator"
page: 7f1a099f66a54e67b4d7a71aa6e954c5.html
url: https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/7f1a099f66a54e67b4d7a71aa6e954c5.html?locale=en-US
source_type: SAP Help
---

# Using Scenario Generator

*Data Product Generator for SAP Business Data Cloud · [auf help.sap.com öffnen](https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/7f1a099f66a54e67b4d7a71aa6e954c5.html?locale=en-US)*

Using Scenario Generator
-
## Using Scenario Generator
The Scenario Generator is an Eclipse view in the BW Modeling Tools (BWMT) that is part
of the BW Data Product Generator perspective. It lets you reconstruct existing BW models as
local tables (file) in SAP Datasphere by generating the required data subscriptions through
the creation of a scenario.

### Important Concepts

A scenario is a list of references between data subscriptions which
are required to reconstruct a specific BW model (such as a DataStore object
(advanced) (aDSO) or a CompositeProvider (HCPR)). For example, if you have a
CompositeProvider, you would not only need a data subscription to represent the
top-level object, but also further data subscriptions for the InfoObjects it
contains and other dependencies.

The scenario tree saves these dependencies between the objects
in the BW model, as well as the equivalent data subscriptions and their
dependencies. It also considers existing data subscriptions for dependent objects to
avoid the creation of duplicate data subscriptions and local tables (file).

The Scenario Generator lets you not only create scenarios out of your BW
models, but also mass generate the associated data subscriptions out of the scenario
tree. Through this you can replicate an entire BW model into local tables (file) in
your SAP Datasphere tenant in SAP Business Data Cloud. There, the extracted data and
associated semantics are stored in table format and become available for further use
cases, such as creating data products or sharing to SAP Databricks.

### Key Workflow

There are two steps needed to convert the BW model into equivalent local tables (file):

- [Creating Scenarios](27e24efbd818463b834a1000bbaf3854.html): Create a scenario by selecting any
existing BW objects from your system and collecting its dependent objects
and existing data subscriptions.

- [Generating Data Subscriptions](304de2d15cc049578aaafbba420c27d2.html): Use the scenario to generate all
required data subscriptions for the BW object and its dependency tree.
Afterwards, the data subscriptions need to be run to extract the data and
semantics into local tables (file).

For a detailed reference of the Eclipse view, see [BW Data Product Generator Perspective in BW Modeling Tools (BWMT)](21393d96c2f94fdebc20ee3941b4eb02.html).
