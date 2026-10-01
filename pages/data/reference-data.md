---
title: "Reference data & entity linking"
subtitle: ""
summary: "How Globalise reference datasets were selected and constructed, and how annotations were linked to them."
type: "page"
slug: "reference-data"
status: "draft"

authors: []
datePublished: ""
dateUpdated: "2026-10-01"

featured: false

hero:
  src: ""
  alt: ""
  caption: ""
  credit: ""
  source: ""
  licence: ""

related: ["globalise-data", "how-the-data-was-produced", "data-model-and-ontologies", "bias-and-limitations", "colonial-context"]
---

# Reference data & entity linking

<!-- Sources: Globalise datasets on DataverseNL (https://dataverse.nl/dataverse/globalise), listed via the DataCite API and the outputs page of the project website, retrieved 2026-10-01; README of https://github.com/globalise-huygens/reference-data-pipeline; inventory record https://data.globalise.huygens.knaw.nl/hdl:20.500.14722/inventory:1056; "Mission, Research Themes and Guiding Questions" v1.0; Globalise Ethics Policy v2.0 (ethics report on the Places Dataset). -->

<!-- TODO: this page depends on the final datasets (dependency "Final datasets" in CONTENT.md). -->

The VOC archives mention thousands of people, places, states and rulers, ships and commodities. A keyword search can find a name, but it cannot tell you who someone was, where a place lay, or that *Bantam*, *Banten* and *Bantamm* are the same place. Globalise therefore compiled **reference data**: structured, curated information about the entities that appear in the archive. **Entity linking** connects the entities recognised in the text to this reference data.

## What reference data is

Reference data consists of records about individual entities, for example a place with its coordinates and name variants, or a polity with its rulers and the period of their rule. It was compiled by historians in the project from source publications, secondary literature and the archive itself, and from existing datasets created by others.

The reference data covers the following types of entities:

* places
* polities and rulers
* persons
* organisations
* ships
* commodities
* weights, measures and currencies

Alongside the reference data, Globalise developed **thesauri**: controlled vocabularies with definitions of concepts found in the archive, such as commodities, and types of documents.

Reference data is curated, but it is not neutral. It reflects the sources it was built from and the choices of the people who made it. Because much of it depends on colonial sources, it tends to record colonial names and perspectives more fully than local ones. See [Bias & limitations](/pages/ethics/bias-and-limitations.md#reference-data) and [Colonial context](/pages/ethics/colonial-context.md#place-names).

## The final reference datasets

Content to be developed.

<!-- TODO: describe the final reference datasets as used on the portal: per entity type, what a record contains, how many records there are, how the datasets were combined from their constituent datasets, and where they can be downloaded. The datasets are converted into RDF knowledge graphs and JSON-LD with the reference-data-pipeline (https://github.com/globalise-huygens/reference-data-pipeline), which has pipelines for places, persons, organisations, polities, ships, measurements and the thesaurus. -->

## The datasets they are based on

The final reference data is built from datasets that Globalise published while the project was under way. These are available on [DataverseNL](https://dataverse.nl/dataverse/globalise), each with its own documentation, version history and licence.

<!-- TODO: confirm that this list is complete and that every dataset listed here feeds into the final reference data. Datasets on organisations and ships are not (yet) on DataverseNL. -->

### Places

* GLOBALISE – Places in the Dutch East India Company Archives (1602-1799). <https://doi.org/10.34894/UFFFNO>
* GLOBALISE Geographical Indices of the RGP General Missives. <https://doi.org/10.34894/PAHO7Q>

### Polities and rulers

* GLOBALISE – Early Modern Polities in the Dutch East India Company Archives (1600-1815). <https://doi.org/10.34894/SIAUPO>
* Kerajaan2 Indonesia (Hans Hägerdal). <https://doi.org/10.34894/CBO80N>

### Persons and groups

* GLOBALISE – Namebooks of the Dutch East India Company (1730-1794). <https://doi.org/10.34894/MD59SC>
* GLOBALISE – Non-Western people described in the General Missive footnotes. <https://doi.org/10.34894/CGQ4J1>
* Japanese Individuals relevant to the Dutch East India Company Archives. <https://doi.org/10.34894/PPUJZB>
* Overview of People in the TEPC Inventories (1673-1844). <https://doi.org/10.34894/K5BYMN>
* GLOBALISE – Ministers in Ambon, Ternate & Banda, 1605-1791. <https://doi.org/10.34894/TKHSH2>
* GLOBALISE – VOC Census Records of Cochin (1700-1775). <https://doi.org/10.34894/O12KME>
* GLOBALISE – VOC Census Records of Banda (1683-1742). <https://doi.org/10.34894/NQILHT>
* GLOBALISE – Ethnicities, Religious Groups and Castes in the Archives of the Dutch East India Company (1602-1799). <https://doi.org/10.34894/RI0KGV>

### Commodities

* GLOBALISE Thesaurus – Commodities. <https://doi.org/10.34894/5PZPPK>

### Weights, measures and currencies

* GLOBALISE – Weights and Measures in the 18th-Century Indian Ocean World. <https://doi.org/10.34894/GDEPNF>

### Documents

* GLOBALISE – Digitized Indexes of the Dutch East India Company OBP (1602-1799). <https://doi.org/10.34894/OP20NM>
* GLOBALISE – VOC Document Segmentation Dataset. <https://doi.org/10.34894/XAJ12C>
* SKOS Thesauri for VOC Archival Document Classification. <https://doi.org/10.34894/B2WBZZ>

## How reference data appears on the portal

Reference data is already used to describe the archive itself. The description of each inventory, for instance, links the settlements it concerns to records in the places dataset: inventory 1056 is linked to Bantam, Siam, Timor, Japan, Ambon and other places.

Content to be developed.

<!-- TODO: describe how users encounter reference data on the portal (entity pages, search filters, maps, timelines), once the interface is final. -->

## Entity linking

The named entity recognition model labels words in the text as, for example, a person's name or a location, but it does not know *which* person or place is meant. Entity linking is the step that connects such a mention to a record in the reference data: deciding, for example, that *Bantam* in a letter from 1614 refers to the polity or port of Banten on Java.

This is difficult. Names are spelled in many different ways, transcriptions contain errors, the same name can refer to different people or places, and many entities that appear in the archive are not in the reference data at all.

### Method

Content to be developed.

<!-- TODO: describe the entity linking method(s) used (which entity types, which features, how candidates are selected and ranked, any manual checking). Relevant private repositories: nlp-entity-linking, entity-linking-reference-data. -->

### Evaluation

Content to be developed.

<!-- TODO: add plain-language evaluation metrics for entity linking (e.g. precision and recall per entity type), and explain how users can tell how reliable a link is. -->
