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

<!-- Sources: Globalise datasets on DataverseNL (https://dataverse.nl/dataverse/globalise): descriptions, data envelopes and documentation, downloaded 2026-10-01; README of https://github.com/globalise-huygens/reference-data-pipeline; inventory record https://data.globalise.huygens.knaw.nl/hdl:20.500.14722/inventory:1056; "Mission, Research Themes and Guiding Questions" v1.0; Globalise Ethics Policy v2.0 (ethics report on the Places Dataset). -->

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

> **To be added:** a description of the final reference datasets as used on the portal: per entity type, what a record contains, the number of records, the version and date, how the dataset was compiled from the datasets listed below, and where it can be downloaded.

| Entity type | Final dataset | Number of records | Version and date | Download |
| --- | --- | --- | --- | --- |
| Places | *To be added* | *To be added* | *To be added* | *To be added* |
| Polities and rulers | *To be added* | *To be added* | *To be added* | *To be added* |
| Persons | *To be added* | *To be added* | *To be added* | *To be added* |
| Ethnicities, religious groups and castes | *To be added* | *To be added* | *To be added* | *To be added* |
| Commodities | *To be added* | *To be added* | *To be added* | *To be added* |
| Weights, measures and currencies | *To be added* | *To be added* | *To be added* | *To be added* |
| Ships | *To be added* | *To be added* | *To be added* | *To be added* |
| Organisations | *To be added* | *To be added* | *To be added* | *To be added* |

<!-- TODO: fill in this table and the "Final reference data" notes in the sections below. The datasets are converted into RDF knowledge graphs and JSON-LD with the reference-data-pipeline (https://github.com/globalise-huygens/reference-data-pipeline), which has pipelines for places, persons, organisations, polities, ships, measurements and the thesaurus. Remove the "To be added" placeholders before publication. -->

## The datasets they are based on

The final reference data is built from datasets that Globalise and its collaborators published while the project was under way. Each of these is available on [DataverseNL](https://dataverse.nl/dataverse/globalise) with detailed documentation: a description of the sources and methods, and a *data envelope* that sets out the dataset's scope, known biases and sensitive content. This page summarises what each type of reference data is based on and what you can expect from it. For details, consult the documentation of the individual datasets.

<!-- Source for this section: descriptions, data envelopes and documentation of the datasets on DataverseNL, downloaded 2026-10-01. -->

<!-- TODO: confirm that every dataset listed below feeds into the final reference data. -->

### What all reference datasets have in common

The documentation of the datasets points to a number of limitations that apply to almost all of them:

* **They reflect the VOC's view.** Most of the information comes from the VOC archives, from published selections of those archives such as the *Generale Missiven*, and from other sources concerned with the VOC. People, places and groups therefore appear mainly as far as they mattered to the company, and descriptions (of place types, occupations, ethnic or religious groups) often reflect how company personnel saw them, not how people saw themselves.
* **They are not complete.** None of the datasets lists all people, places, polities or commodities mentioned in the archive, let alone all those that existed in the regions where the VOC was active.
* **They rely on European-language sources.** Almost all sources used are in Dutch or English, and the creators preferred sources that were easily accessible.
* **They contain sensitive and offensive content.** Names, place names and categories can be contested, and some labels and descriptions taken from the sources are offensive.

### Places

> **Final reference data — to be added:** a description of the final places reference data, the number of records, and how it was compiled from the datasets listed below.

Place records give the names by which a place was and is known, its coordinates, and its type (such as a town, fort, river or island).

**Based on:** the place names in the indexes of the published *Generale Missiven*, supplemented with information from the VOC archives, the online gazetteers GeoNames and the Atlas of Mutual Heritage, other datasets (such as the Exploring Slave Trade in Asia database), early modern maps and secondary literature. For Kerala, a gazetteer created in the Necessary Reunions project adds information from fifteen VOC maps.

**What to expect:** mainly places in Asia and Africa where the VOC was active, and a few in Europe, the Americas and Oceania. Places that had little contact with the company, or were of little interest to it, are likely to be missing. Place types often reflect a place's function for the VOC: a *residentie*, for instance, is a place where the company had a trading office. Some coordinates were filled in semi-automatically and have not all been checked by hand.

* GLOBALISE – Places in the Dutch East India Company Archives (1602-1799). <https://doi.org/10.34894/UFFFNO>
* GLOBALISE Geographical Indices of the RGP General Missives. <https://doi.org/10.34894/PAHO7Q>
* Necessary Reunions: Gazetteer of Place Names in Kerala (India) from Dutch Maps and Textual Archives of the Seventeenth and Eighteenth Centuries. <https://doi.org/10.34894/FN1DBL>

### Polities and rulers

> **Final reference data — to be added:** a description of the final polities and rulers reference data, the number of records, and how it was compiled from the datasets listed below.

Polity records describe states and other political entities that existed between 1600 and 1815, with their rulerships and rulers, and the dates and locations associated with them.

**Based on:** existing datasets and secondary literature, not on original research. The principal basis is Hans Hägerdal's *Kerajaan2 Indonesia*, a set of genealogies of more than 200 former princely states in present-day Indonesia, which he compiled from archival research and literature since the 1990s.

**What to expect:** some polities are well documented, but for most of them even the specialist literature gives no complete list of rulers or precise dates. The dates when polities, rulerships and rulers began and ended can be uncertain or contested, and are often given as ranges. The genealogies in Kerajaan2 Indonesia are simplified and not always complete.

* GLOBALISE – Early Modern Polities in the Dutch East India Company Archives (1600-1815). <https://doi.org/10.34894/SIAUPO>
* Kerajaan2 Indonesia (Hans Hägerdal). <https://doi.org/10.34894/CBO80N>

<!-- TODO: check whether coverage of polities differs strongly by region (e.g. because Kerajaan2 Indonesia is the principal basis), and if so, say so here. -->

### Persons

> **Final reference data — to be added:** a description of the final persons reference data, the number of records, and how it was compiled from the datasets listed below.

The project's aim was a persons dataset that is consciously diverse, representing people from different ethnic, geographical, social, economic, religious and occupational backgrounds. In practice, it is built from a number of separate sources, each of which covers a specific group of people:

| Dataset | Who is included | Main limitations |
| --- | --- | --- |
| [Namebooks of the Dutch East India Company (1730-1794)](https://doi.org/10.34894/MD59SC) | Higher-ranking VOC employees, from six printed lists of personnel (1730, 1738, 1751, 1760, 1779, 1794) | Only higher ranks, so no soldiers, sailors or other lower-ranking staff, who were more often non-European; only men; no employees in Batavia; the printed lists contain errors |
| [Non-Western people described in the General Missive footnotes](https://doi.org/10.34894/CGQ4J1) | Non-European individuals described in the editorial footnotes of the published *Generale Missiven* | Mainly rulers and officeholders; depends on the editors' choices of whom to annotate |
| [Japanese Individuals relevant to the Dutch East India Company Archives](https://doi.org/10.34894/PPUJZB) | Japanese people of the Tokugawa period, from interpreters at Deshima to shoguns | Biographies are fragmentary |
| [Overview of People in the TEPC Inventories (1673-1844)](https://doi.org/10.34894/K5BYMN) | Deceased people, their partners and the people they enslaved, in estate inventories of the Orphan Chamber at the Cape of Good Hope | Enslaved people are often grouped together and unnamed; other people in the inventories are not included; some volumes are missing |
| [Ministers in Ambon, Ternate & Banda, 1605-1791](https://doi.org/10.34894/TKHSH2) | Ministers (*predikanten*) employed by the VOC in the Moluccas, from biographies in a published source edition | Structured with the help of an AI tool, then checked by hand |
| [VOC Census Records of Cochin (1700-1775)](https://doi.org/10.34894/O12KME) | Heads of household in ten census years | Only heads of household; a selection of the census records |
| [VOC Census Records of Banda (1683-1742)](https://doi.org/10.34894/NQILHT) | People in four census years | A selection of the census records; transcription errors may remain |

**What to expect:** the persons data is uneven. Some groups, such as higher-ranking VOC officials, are covered systematically; others appear only where a specific source happened to record them. In the sources used, enslaved people, women and people of lower status are often absent or recorded without a name.

### Ethnicities, religious groups and castes

> **Final reference data — to be added:** a description of the final ethnicities, religious groups and castes reference data, the number of records, and how it was compiled from the datasets listed below.

These records define and contextualise the ethnic, religious and caste categories that appear in the VOC archives.

**Based on:** labels from the VOC archives, from other datasets based on these archives and from indexes of source publications; definitions mostly from the glossaries of secondary works on the Indian Ocean world in the seventeenth and eighteenth centuries.

**What to expect:** most categories were assigned to people by the VOC, and rarely correspond to how people identified themselves. Many are linked to histories of colonial violence, enslavement and racism, and some are derogatory. The dataset is meant to help users understand these categories in the archive; its creators advise against using it for other purposes. See also [Colonial context](/pages/ethics/colonial-context.md#people-and-groups).

* GLOBALISE – Ethnicities, Religious Groups and Castes in the Archives of the Dutch East India Company (1602-1799). <https://doi.org/10.34894/RI0KGV>

### Commodities

> **Final reference data — to be added:** a description of the final commodities reference data, the number of records, and how it was compiled from the datasets listed below.

The commodities thesaurus defines goods traded by the VOC and arranges them in a hierarchy of broader and narrower categories.

**Based on:** all physical items in the shipping lists of the Bookkeeper-General in Batavia and the Monsoon Traders database, with definitions from secondary literature and broader categories from existing classifications.

**What to expect:** the thesaurus is mainly based on eighteenth-century shipping lists, so goods that were rarely shipped, or mainly traded in the seventeenth century, may be missing. The first version contained 3,787 concepts, of which 2,294 were not yet classified. Some definitions in the sources use outdated or offensive language; where possible, these were not adopted or were edited.

* GLOBALISE Thesaurus – Commodities. <https://doi.org/10.34894/5PZPPK>

<!-- TODO: update the number of concepts and unclassified concepts for the final version. -->

### Weights, measures and currencies

> **Final reference data — to be added:** a description of the final weights, measures and currencies reference data, the number of records, and how it was compiled from the datasets listed below.

These records define units of weight, measure and currency used in VOC settlements in Asia, and how they converted into each other.

**Based on:** the *Memoriën van Munten, Maaten, en Gewigten*, an eighteenth-century VOC compilation (1764–1771) on the units in use in Batavia and other settlements, supplemented with the VOC Glossarium.

**What to expect:** units as the VOC defined and understood them, in the eighteenth century, for the places covered by the source. The names are Dutch renderings of local terms, and for many lesser-known units the local name is unknown. The list is not exhaustive, and the conversions in the source may contain errors.

* GLOBALISE – Weights and Measures in the 18th-Century Indian Ocean World. <https://doi.org/10.34894/GDEPNF>

### Ships

> **Final reference data — to be added:** a description of the final ships reference data, the number of records, and how it was compiled from the datasets listed below.

**Based on:** the Dutch-Asiatic Shipping (DAS) database, which records the voyages of VOC ships (and those of its predecessors) between the Netherlands and Asia from 1595 to 1795: 4,722 outbound and 3,359 homebound voyages. Globalise published an enriched version in which individual ships are identified.

**What to expect:** ships that sailed between the Netherlands and Asia. Ships that only sailed within Asia are not covered by this source. Uncertain dates and gaps in the original database are inherited.

* Dutch-Asiatic Shipping (DAS) – Enriched Dataset. <https://doi.org/10.34894/RJ7UEA>

<!-- TODO: confirm that the DAS dataset is the basis of the ship reference data, and whether ships sailing within Asia are covered by other sources. -->

### Organisations

> **Final reference data — to be added:** a description of the final organisations reference data, the number of records, and the sources it is based on. No dataset on organisations has been published on DataverseNL.

<!-- TODO: describe the sources of the organisation reference data. No dataset on organisations has been published on DataverseNL. -->

### Documents

Document descriptions and document types (see [How the data was produced](/pages/data/production.md#3-identifying-documents)) are based on:

* GLOBALISE – Digitized Indexes of the Dutch East India Company OBP (1602-1799): document-level index entries from the TANAP project and from typescript indexes in the Nationaal Archief. The indexes do not cover all inventory numbers. <https://doi.org/10.34894/OP20NM>
* SKOS Thesauri for VOC Archival Document Classification: the TANAP document classification and a simplified Globalise classification. <https://doi.org/10.34894/B2WBZZ>
* Overzicht van Generale Missiven in het archief van de VOC, 1.04.02: the *Generale Missiven* identified in the archive, 1618–1793. <https://doi.org/10.34894/SRDMFU>
* GLOBALISE – VOC Document Segmentation Dataset: manually segmented inventories, for training and evaluating document segmentation. <https://doi.org/10.34894/XAJ12C>

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
