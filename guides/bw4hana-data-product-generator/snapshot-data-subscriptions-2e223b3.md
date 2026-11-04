---
guide: Data Product Generator for SAP Business Data Cloud
product: SAP BW/4HANA
title: "Snapshot Data Subscriptions"
page: 2e223b3c31614ab995ae45ee3187a016.html
url: https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/2e223b3c31614ab995ae45ee3187a016.html?locale=en-US
source_type: SAP Help
---

# Snapshot Data Subscriptions

*Data Subscriptions · [auf help.sap.com öffnen](https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/2e223b3c31614ab995ae45ee3187a016.html?locale=en-US)*

Snapshot Data Subscriptions
-
## Snapshot Data Subscriptions
When you create a data subscription with the Snapshot source type, the Data Product
Generator uses SQL services to extract BW characteristic data into local tables (file) in
your BW file space in SAP Datasphere in SAP Business Data Cloud.

The Snapshot source type supports three categories of BW data:

- Hierarchies — extracts the full hierarchy structure of a BW
characteristic hierarchy and generates a set of local tables (file) representing the
hierarchy directory, nodes, and associated texts. For details, see the section
Hierarchy Data Subscriptions below.

- Master data and texts — extracts BW characteristic attributes and texts
into local tables (file). A new combined local table (file) type is also available
for BW characteristics with language-independent texts. For details, see the section
Snapshot Data Subscriptions for Master Data and Texts
below.

- Transactional data - extracts fact data from DataStore objects
(advanced) into a single local table (file). For details, see the section
Snapshot Data Subscriptions for Transactional Data
below.

### Hierarchy Data Subscriptions

BW characteristic hierarchies have a more complex structure than flat InfoProviders such as
DataStore objects or CompositeProviders. A hierarchy in BW consists of named
hierarchies, their nodes arranged in a parent-child structure, and associated texts
for both the hierarchy itself and its individual nodes. To accurately represent this
structure in SAP Datasphere in SAP Business Data Cloud, a single hierarchy data
subscription generates multiple local tables (file) in your BW file space instead of
a single flat table.

Unlike standard data subscriptions, which use the Operational Data Provisioning (ODP)
framework to extract data, hierarchy data subscriptions rely on SQL services for
extraction, represented by the Snapshot source type.

When you create a hierarchy data subscription, the following local tables (file) are
automatically generated and deployed in your BW file space in SAP Datasphere in SAP
Business Data Cloud:

|
Local Table (File)
| Content
| --- |
|

|
Hierarchy Directory
| Contains the names of all hierarchies belonging to the characteristic InfoObject. Each row represents one hierarchy.
| --- |
|

|
Hierarchy Directory Texts
| Contains the descriptions for each hierarchy in the hierarchy directory, covering all available languages.
| --- |
|

|
Hierarchy (Nodes)
| Contains the main hierarchy structure with the individual nodes, their node IDs, and
| --- |
parent-child relationships, including the leaf-level nodes (nodes
that have no further children) and their mapping back to the
characteristic values they represent. This is the core table that
reflects the tree structure of the hierarchy as it exists in
BW.
|

|
Hierarchy Node Texts
| Contains the descriptions for each hierarchy node, covering all available languages.
| --- |
|

Together, these tables represent the complete hierarchy as it is available in BW, preserving the
semantic structure, parent-child node relationships, and all associated
descriptions.

Note

For each hierarchy data subscription, a separate set of local tables (file) is created. This is
different from standard data subscriptions, where one data subscription produces
one local table (file).

Creating a Hierarchy Data Subscription

You create a hierarchy data subscription in the same way as any other data subscription. When
selecting the source object, choose Snapshot as the source
type and select the characteristic InfoObject whose hierarchies you want to extract.

In the selection settings of the data subscription, you can filter by Hierarchy
Name (for version-independent hierarchies) or Hierarchy
Name and Hierarchy Version (for
version-dependent hierarchies) to define which hierarchies of the InfoObject to
include. If you do not apply a hierarchy name or version filter, all hierarchies
belonging to the InfoObject are extracted.

For the full procedure, see [Creating Data Subscriptions](https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/f2e950ed4e8c475b8571478d6c2004c0.html).

Restrictions for Hierarchy Data Subscriptions

The following restrictions apply to hierarchy data subscriptions:

- Full extraction only: Only full extraction is supported for hierarchy data subscriptions.
Delta extraction is not available. Each run of the data subscription
performs a complete snapshot of the hierarchy structure as it currently
exists in BW.

-
No projection:
It is not possible to limit the extraction to specific fields or columns via projection. All fields of all generated local tables (file) are always extracted.

- Selection by hierarchy name and hierarchy version only: The only available selection
filters are Hierarchy Name (for version-independent
hierarchies) or Hierarchy Name and
Hierarchy Version (for version-dependent
hierarchies). It is not possible to filter by other fields such as validity
date. Hierarchy Version is only available for
version-dependent hierarchies.

- Multiple local tables (file): Since a hierarchy data subscription produces a set of local
tables (file) rather than a single table, the Local Table
(File) column in the data subscriptions list and the
View Local Table (File) action are showing the
main hierarchy nodes table. The other tables of the set are accessible
directly in the BW file space in SAP Datasphere in SAP Business Data
Cloud.

Using Hierarchy Data in SAP Business Data Cloud

After the hierarchy tables have been extracted into the BW file space in SAP Datasphere in SAP
Business Data Cloud, you can share them to other spaces and use them in the
following ways:

- Analytic models in SAP Datasphere: Use the hierarchy node table to enable hierarchy-based
drill-down and hierarchy-aware filtering in analytic models. The
parent-child relationships in the nodes table allow SAP Datasphere in SAP
Business Data Cloud to navigate the hierarchy levels, for example to drill
from a region down to individual cost centers.

For more information on sharing local tables (file) and creating data products, see [Performing Data Management Tasks and Sharing
Local Table (File) to Other Spaces](https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/692538f27de745539c551ef7e08fff53.html).

### Snapshot Data Subscriptions for Master Data and Texts

When you create a master data or text snapshot subscription, the Data Product
Generator extracts the selected characteristic's attribute or text data into a
single local table (file) in your BW file space in SAP Datasphere in SAP Business
Data Cloud.

The source name combined with the suffix you enter when creating the data
subscription determines which data is extracted and which local table (file) type is
generated. The following suffixes are available:

|
Source Name Suffix
| Data Extracted
| --- |
| Local Table (File) Type
|

|
$P
| Time-independent attributes
| --- |
| Master Data (time-independent attributes)
|

|
$Q
| Time-dependent attributes
| --- |
| Master Data (time-dependent attributes)
|

|
$M
| Full master data (all attributes)
| --- |
| Master Data (full view)
|

|
$T
| Texts
| --- |
| Texts
|

|
$V
| Both master data and language-independent texts
| --- |
| Master Data & Language-Independent Texts
(combined)
|

Note

The following constraints apply for the combined local table (file) type
Master Data & Language-Independent Texts:

- The BW characteristic to extract from must not have language-dependent
texts.

- Time-dependency cannot apply to both attributes and texts
simultaneously. Either the attributes are time-dependent and the texts
are time-independent, or the texts are time-dependent and the attributes
are time-independent.

- The combined type cannot be used with the ODP source type. You must
select Snapshot as the source type and add the $V
suffix in the source name field of the source object.

Creating Master Data or Text Data Subscription

You create a master data or text data subscription in the same way as any other data
subscription. When selecting the source object, choose
Snapshot as the source type and enter the source name of
the characteristic InfoObject with the appropriate suffix to determine which data
should be extracted from the given object.

For the available source name suffixes and the local table (file) types they produce,
see the table in the section Master Data and Text Data
Subscriptions.

For the full procedure, see [Creating Data Subscriptions](https://help.sap.com/docs/SAP_BW4HANA/ed919380760a44388ab90e6bb3e7480a/f2e950ed4e8c475b8571478d6c2004c0.html).

### Snapshot Data Subscriptions for Transactional Data

Snapshot data subscriptions can also be created to extract transactional data from
DataStore objects (advanced) (aDSOs).

The procedure to setup the data subscription of type Snapshot
is the same as for master data and text data subscriptions.

Depending on the type of aDSO you want to extract data from, use the following
suffixes combined with the source name:

|
Source Name Suffix
| Data Extracted
| --- |
|

|
$E
| Transactional data from Standard DataStore objects (advanced)
| --- |
(aDSOs)
|

|
$F
| Transactional data from Write-Optimized Data Store objects
| --- |
(advanced) (aDSOs) and DataStore objects (advanced) (aDSOs) of
type data mart (Cube-Like aDSOs)
|
