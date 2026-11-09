---
title: "Reference data & entity linking"
subtitle: ""
summary: "How Globalise reference datasets were selected and constructed, and how annotations were linked to them."
type: "page"
slug: "reference-data"
status: "draft"

authors: []
datePublished: ""
dateUpdated: "2026-10-30"

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

<!-- Sources: Globalise datasets on DataverseNL (https://dataverse.nl/dataverse/globalise): descriptions, data envelopes and documentation, downloaded 2026-10-01; README of https://github.com/globalise-huygens/reference-data-pipeline; inventory record https://data.globalise.huygens.knaw.nl/hdl:20.500.14722/inventory:1056; "Mission, Research Themes and Guiding Questions" v1.0; Globalise Ethics Policy v2.0 (ethics report on the Places Dataset); export of the Globalise thesaurus from PoolParty (concepts.trig in the documents repository, file dated 2026-10-27, last concept scheme modified 2026-10-20). -->

<!-- TODO: this page depends on the final datasets (dependency "Final datasets" in CONTENT.md). -->

The VOC archives mention thousands of people, places, states and rulers, and ships, as well as goods, units of measure, occupations and groups of people. A keyword search can find a name, but it cannot tell you who someone was, where a place lay, or that *Bantam*, *Banten* and *Bantamm* are the same place. The Globalise project therefore compiled **reference data**: structured, curated information about the entities and concepts that appear in the archive. **Entity linking** connects the entities and concepts recognised in the text to this reference data.

## What reference data is

Reference data was compiled by historians in the project from source publications, secondary literature and the archive itself, and from existing datasets created by others. It is of two kinds: records about **entities**, and definitions of **concepts**.

### Entities and concepts

**Entities** are individual things that existed: one particular place, person, state or ship. Each entity has its own record in a reference dataset, for example a place with its coordinates and name variants, or a polity with its rulers and the period of their rule. The town of Cochin, the kingdom of Kandy and a particular ship called *Amsterdam* are entities. Because different people, places and ships often had the same name, an important part of the work is telling them apart.

Globalise has reference data on the following types of entities:

* places
* polities and rulers
* persons
* organisations
* ships

**Concepts** are kinds of things: categories and terms rather than individuals. *Pepper* is a concept (a kind of goods), and so are the *pikol* (a unit of weight of about 60 kilograms), the rank of *opperkoopman* (chief merchant), the place type *fortification*, and ethnic, religious and caste categories such as those the VOC used to describe people. Concepts are defined in the [Globalise thesaurus](#the-globalise-thesaurus). Among them are:

* commodities
* units of weight, measure and currency
* ethnic, religious and caste categories
* occupations, ranks and titles
* types of places, organisations, ships and documents

The two kinds work together. Entity records use concepts to describe entities: a place has a place type, a person can be described by an occupation, rank or status, a ship by its ship type, and a document by its document type. In the text, the named entity recognition model marks both kinds of words: names of persons, places and ships, which are linked to entity records, and words for commodities, professions, ship types, organisation types or ethnic and religious groups, which are linked to concepts in the thesaurus (see [How the data was produced](/pages/research-responsibly/data/production.md#4-recognising-entities)).

Reference data is curated, but it is not neutral. It reflects the sources it was built from and the choices of the people who made it. Because much of it depends on colonial sources, it tends to record colonial names, categories and perspectives more fully than local ones. See [Bias & limitations](/pages/research-responsibly/ethics/bias-and-limitations.md#reference-data) and [Colonial context](/pages/research-responsibly/ethics/colonial-context.md#place-names).

### The Globalise thesaurus

The Globalise thesaurus is a set of controlled vocabularies, each covering one domain, compiled by historians in the Globalise project. Each concept has a preferred label in Dutch, often also in English and other languages, and alternative labels for spelling variants and synonyms. Most concepts have a definition with a reference to its source, and concepts are arranged in hierarchies of broader and narrower terms: *pepper* falls under *spices* and, several levels up, under *food and live animals*.

In October 2026 the thesaurus contained about 8,700 concepts in the following vocabularies. A concept can belong to more than one vocabulary: more than 100 occupations, for example, also appear in the South Asia glossary.

| Vocabulary | Concepts | What it contains |
| --- | --- | --- |
| Commodities | 3,901 | Goods traded by the VOC, arranged in the categories of the Standard International Trade Classification (SITC), such as food and live animals, crude materials, and manufactured goods. 1,651 concepts are not yet classified. A separate category covers people who appear on VOC lists of goods. |
| Occupations | 2,278 | Occupations grouped by field of activity (such as administration and government, law, maritime and military occupations), occupations with a VOC-specific meaning, and 965 ranks and titles |
| Ethnic, religious and caste categories | 577 | Ethnicities, demonyms (names for the inhabitants of a place), castes, religious groups and social strata |
| Person-related concepts | 546 | Forms of address, legal and social statuses (such as *enslaved* or *banneling*, exile), family and other relationships, and kinds of names (such as a ruler's regnal name) |
| Units of measure | 427 | Units of weight, volume, length and area, and currencies |
| Place types | 351 | Kinds of places in the built environment (buildings, settlements, trading posts, plantations), in the natural landscape (bodies of water, landforms), political and administrative divisions, and regions |
| Organisation-related concepts | 269 | Types of organisations by field (government, commerce, military and others), and relationships between organisations, such as *suborganisation of* or *successor to* |
| Ship types | 135 | European and Asian kinds of watercraft |
| Globalise document types | 115 | Types of documents by function (such as letters, reports, orders and daily journals), form, production and provenance, and types of documents from other traditions (such as a *fatwa* or a *cartaz*, a Portuguese shipping licence) |
| TANAP document classification | 149 | The categories that the TANAP project used to describe documents (in Dutch) |
| Calendrical systems | 70 | Islamic, Javanese Islamic, Malayalam, Sinhala and Tamil calendars and their months |
| Financial and monetary terms | 19 | Terms for payments such as wages, interest and tolls |
| South Asia glossary and Japan glossary | 278 and 237 | Terms from these regions across domains: forms of address, ranks, commodities, coins, measures, documents and others |
| Necessary Reunions places | 251 | Place types used in the Necessary Reunions gazetteer for Kerala |
| Not classified | 2,171 | Terms collected from glossaries and other sources that are being placed in a domain vocabulary; all but about 300 already appear in one |
| Miscellaneous | 73 | Technical terms used in the data, such as the categories of the named entity recognition model, the types of text regions on a page, the two versions of the transcription, the classes of entities, and identifier types |

* **Languages.** Labels are given in more than 90 languages. Nearly 2,900 concepts have a label in a language other than Dutch or English, most often Japanese, Chinese, Indonesian, Vietnamese, Malay, Persian, Javanese, Korean, Arabic and Sinhala. Definitions are mostly in English and Dutch; where the project translated a definition, this is marked.
* **Sources.** Most definitions cite their source, with a reference to the project's Zotero library.
* **Links to other vocabularies.** Many concepts are linked to matching concepts in the Getty *Art & Architecture Thesaurus*, the *Cultuurhistorische Thesaurus* of the Rijksdienst voor het Cultureel Erfgoed, Wikidata and, for commodities, the SITC.
* **Offensive and contested terms.** Terms are recorded as they appear in the sources, including terms that are now offensive. Labels of 79 concepts are marked *[PROBLEMATIC TERM]*. Gendered concepts, such as titles and statuses specific to women, are grouped in collections so that they can be found together. See [Colonial context](/pages/research-responsibly/ethics/colonial-context.md#colonial-terminology-and-categories).

The thesaurus can be browsed in the [Globalise thesaurus browser](https://thesaurus.globalise.huygens.knaw.nl/). Versions of some vocabularies have been published as datasets: commodities, ethnic, religious and caste categories, and document types (see below). See also [Data model & ontologies](/pages/research-responsibly/data/data-model.md#thesauri-and-vocabularies).

<!-- TODO: update the figures for the final version of the thesaurus, and add where the complete thesaurus can be downloaded (version, date, licence). The thesaurus browser showed an error page on 2026-10-01; see the TODO on the data model page. -->

### Which name is shown: preferred labels

Every entity and concept has one **preferred label** per language, the name under which it is shown, and any number of **alternative labels**: other names, spellings and translations. The archive, the scholarly literature and present-day usage often name the same thing differently, so choosing the preferred label is an editorial decision. The Globalise project made it differently for places and for concepts. Alternative labels are kept in both cases, so a search for a name that is not the preferred label still finds the entity or concept.

**Places: the modern name.** The preferred label of a place is the name by which it is known today, so that users can find it on present-day maps and in current literature. *Batavia* is therefore listed as *Jakarta*, *Ceylon* as *Sri Lanka*, *Formosa* as *Taiwan* and *Bantam* as *Banten*. The names the VOC used, and other historical and local names, are alternative labels. Following the project's ethics policy, the preferred label was chosen for findability, clarity and ethical considerations.

* **Sources.** Most preferred labels (about two thirds) were taken from GeoNames, a widely used online gazetteer. Others come from Wikidata, the Getty *Thesaurus of Geographic Names*, the World Historical Gazetteer or the scholarly literature.
* **No modern name.** For places that no longer exist, or for which no modern name was found, the preferred label is taken from historical sources, such as the VOC archive or eighteenth-century Dutch maps. A remark in the dataset says so.
* **Places with the same name.** A short addition distinguishes them, such as a country, a type of place, or the years in which a fort existed: *Madura (Indonesia)*, as distinct from Madurai in India.
* **Limitations.** GeoNames is edited by its users, and it is not always clear where its information comes from or how far it reflects a Western view. To include other perspectives, researchers from India, Indonesia and Taiwan reviewed and added to the places data.

**Concepts: the term in the sources.** Every concept in the thesaurus has a preferred label in Dutch. This is usually the term as the VOC sources use it, in one standardised spelling: *fluit* (a type of ship), *vrijman* (a freed person, or an Asian Christian citizen), *opperkoopman*. The spellings found in the sources are alternative labels (*fluijtschip*, *fluitschip*).

* **English.** About 40% of the concepts also have an English preferred label. This is either a translation (*huurling*, *mercenary*) or the form usual in English-language scholarship (*fluit*, *fluyt*).
* **Terms from other languages.** Where a term comes from another language, such as Japanese, Tamil, Sinhala, Malay or Persian, it also has a preferred label in that language, in Latin script (*tsūshin*, *Valankai*), often with the original script as an alternative label. The Dutch and English labels are then usually the same term.
* **Terms with more than one meaning.** An addition in brackets distinguishes them. Square brackets give the domain (*mendelika [status]* and *mendelika [beroepen]*, occupations), round brackets the place or context to which a unit or office belongs (*fanam (Sacaram)*, *fiscal (Formosa)*).
* **Offensive terms.** The preferred label keeps the term from the sources, marked *[PROBLEMATIC TERM]* where it is offensive (see above).

<!-- Sources for this section: places, Labels Detail sheet of "GLOBALISE - Places in the Dutch East India Company Archives (1602-1799)" v3.0 (label_type, label_source and label_remarks of the 2,372 PREF labels; 1,601 from GeoNames); Globalise Ethics Policy v2.0, ethics report on the Places Dataset; concepts, thesaurus export of October 2026 (concepts.trig): one prefLabel per language for every concept, Dutch for all, English for 3,449 of about 8,700; 65 concepts record the source of their preferred label in a scope note. -->

<!-- TODO: add how preferred labels were chosen for polities and rulers, persons, ships and organisations. State which language's label the portal shows (e.g. English where available, otherwise Dutch). The ethics policy refers to a "workflow for standard name selection (see 3.C)", which is not part of the policy text; add or link it if it is available. -->

## The final reference datasets

> **To be added:** a description of the final reference datasets as used on the portal: per type of reference data, what a record contains, the number of records, the version and date, how the dataset was compiled from the datasets listed below, and where it can be downloaded.

| Reference data                           | Kind     | Final dataset                                                     | Number of records        | Version and date         | Download                                       |
| ---------------------------------------- | -------- | ----------------------------------------------------------------- | ------------------------ | ------------------------ | ---------------------------------------------- |
| Places                                   | Entities | *To be added*                                                     | *To be added*            | *To be added*            | *To be added*                                  |
| Polities and rulers                      | Entities | *To be added*                                                     | *To be added*            | *To be added*            | *To be added*                                  |
| Persons                                  | Entities | *To be added*                                                     | *To be added*            | *To be added*            | *To be added*                                  |
| Ships                                    | Entities | *To be added*                                                     | *To be added*            | *To be added*            | *To be added*                                  |
| Organisations                            | Entities | GLOBALISE - Organisations in the Dutch East India Company Archive | 270 organisational units | Version 1, November 2026 | [DataverseNL](https://doi.org/10.34894/2VNEUG) |
| Ethnicities, religious groups and castes | Concepts | *To be added*                                                     | *To be added*            | *To be added*            | *To be added*                                  |
| Commodities                              | Concepts | *To be added*                                                     | *To be added*            | *To be added*            | *To be added*                                  |
| Weights, measures and currencies         | Concepts | *To be added*                                                     | *To be added*            | *To be added*            | *To be added*                                  |
| Thesaurus (all vocabularies)             | Concepts | *To be added*                                                     | *To be added*            | *To be added*            | *To be added*                                  |

<!-- TODO: fill in this table and the "Final reference data" notes in the sections below. The datasets are converted into RDF knowledge graphs and JSON-LD with the reference-data-pipeline (https://github.com/globalise-huygens/reference-data-pipeline), which has pipelines for places, persons, organisations, polities, ships, measurements and the thesaurus. Remove the "To be added" placeholders before publication. -->

## The datasets they are based on

The final reference data is built from datasets that the Globalise project and its collaborators published while the project was under way. Each of these is available on [DataverseNL](https://dataverse.nl/dataverse/globalise) with detailed documentation: a description of the sources and methods, and a *data envelope* that sets out the dataset's scope, known biases and sensitive content. This page summarises what each type of reference data is based on and what you can expect from it. For details, consult the documentation of the individual datasets.

<!-- Source for this section: descriptions, data envelopes and documentation of the datasets on DataverseNL, downloaded 2026-10-01. -->

<!-- TODO: confirm that every dataset listed below feeds into the final reference data. -->

### What all reference datasets have in common

The documentation of the datasets points to a number of limitations that apply to almost all of them:

* **They reflect the VOC's view.** Most of the information comes from the VOC archives, from published selections of those archives such as the *Generale Missiven*, and from other sources concerned with the VOC. People, places and groups therefore appear mainly as far as they mattered to the company, and descriptions (of place types, occupations, ethnic or religious groups) often reflect how company personnel saw them, not how people saw themselves.
* **They are not complete.** None of the datasets lists all people, places, polities or commodities mentioned in the archive, let alone all those that existed in the regions where the VOC was active.
* **They rely on European-language sources.** Almost all sources used are in Dutch or English, and the creators preferred sources that were easily accessible.
* **They contain sensitive and offensive content.** Names, place names and categories can be contested, and some labels and descriptions taken from the sources are offensive.

### Entities

#### Places

> **Final reference data — to be added:** a description of the final places reference data, the number of records, and how it was compiled from the datasets listed below.

Place records give the names by which a place was and is known, its coordinates, and its type (such as a town, fort, river or island), taken from the place types in the thesaurus.

**Based on:** the place names in the indexes of the published *Generale Missiven*, supplemented with information from the VOC archives, the online gazetteers GeoNames and the Atlas of Mutual Heritage, other datasets (such as the Exploring Slave Trade in Asia database), early modern maps and secondary literature. For Kerala, a gazetteer created in the Necessary Reunions project adds information from fifteen VOC maps.

**What to expect:** mainly places in Asia and Africa where the VOC was active, and a few in Europe, the Americas and Oceania. Places that had little contact with the company, or were of little interest to it, are likely to be missing. Place types often reflect a place's function for the VOC: a *residentie*, for instance, is a place where the company had a trading office. Some coordinates were filled in semi-automatically and have not all been checked by hand.

* GLOBALISE – Places in the Dutch East India Company Archives (1602-1799). <https://doi.org/10.34894/UFFFNO>
* GLOBALISE Geographical Indices of the RGP General Missives. <https://doi.org/10.34894/PAHO7Q>
* Necessary Reunions: Gazetteer of Place Names in Kerala (India) from Dutch Maps and Textual Archives of the Seventeenth and Eighteenth Centuries. <https://doi.org/10.34894/FN1DBL>

#### Polities and rulers

> **Final reference data — to be added:** a description of the final polities and rulers reference data, the number of records, and how it was compiled from the datasets listed below.

Polity records describe states and other political entities that existed between 1600 and 1815, with their rulerships and rulers, and the dates and locations associated with them.

**Based on:** existing datasets and secondary literature, not on original research. The principal basis is Hans Hägerdal's *Kerajaan2 Indonesia*, a set of genealogies of more than 200 former princely states in present-day Indonesia, which he compiled from archival research and literature since the 1990s.

**What to expect:** some polities are well documented, but for most of them even the specialist literature gives no complete list of rulers or precise dates. The dates when polities, rulerships and rulers began and ended can be uncertain or contested, and are often given as ranges. The genealogies in Kerajaan2 Indonesia are simplified and not always complete.

* GLOBALISE – Early Modern Polities in the Dutch East India Company Archives (1600-1815). <https://doi.org/10.34894/SIAUPO>
* Kerajaan2 Indonesia (Hans Hägerdal). <https://doi.org/10.34894/CBO80N>

<!-- TODO: check whether coverage of polities differs strongly by region (e.g. because Kerajaan2 Indonesia is the principal basis), and if so, say so here. -->

#### Persons

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

Occupations, ranks, statuses and forms of address of persons are concepts in the thesaurus.

**What to expect:** the persons data is uneven. Some groups, such as higher-ranking VOC officials, are covered systematically; others appear only where a specific source happened to record them. In the sources used, enslaved people, women and people of lower status are often absent or recorded without a name.

#### Ships

> **Final reference data — to be added:** a description of the final ships reference data, the number of records, and how it was compiled from the datasets listed below.

**Based on:** the Dutch-Asiatic Shipping (DAS) database, which records the voyages of VOC ships (and those of its predecessors) between the Netherlands and Asia from 1595 to 1795: 4,722 outbound and 3,359 homebound voyages. The Globalise project published an enriched version in which individual ships are identified.

**What to expect:** ships that sailed between the Netherlands and Asia. Ships that only sailed within Asia are not covered by this source. Uncertain dates and gaps in the original database are inherited. Kinds of ships are concepts in the thesaurus (*Ship types*).

* Dutch-Asiatic Shipping (DAS) – Enriched Dataset. <https://doi.org/10.34894/RJ7UEA>

<!-- TODO: confirm that the DAS dataset is the basis of the ship reference data, and whether ships sailing within Asia are covered by other sources. -->

#### Organisations

The project aimed to describe organisations and organisational units that structured the archive of the Dutch East India Company (VOC). Where relevant to the Person reconstructions, the data also includes other organisations that appear in its archives. They include VOC settlements, administrative areas and governing bodies, as well as organisations such as the English East India Company in Bengal and the States-General.

**Based on:** the organisation of records in the VOC archives, the [GLOBALISE Namebooks dataset](https://doi.org/10.34894/MD59SC), the [GLOBALISE places dataset](https://doi.org/10.34894/UFFFNO), the [Atlas of Mutual Heritage](https://www.atlasofmutualheritage.nl/), and historical studies of the VOC and its administrative institutions. The latter includes _De Archieven van de Verenigde Oostindische Compagnie, 1602–1795_ (Meilink-Roelofsz et al., 1992) and Niemeijer's introduction to _The Central Administration of the VOC Government and the Local Institutions of Batavia (1619–1811)_. Classifications, locations and relationships are documented using historical and archival sources.

**What to expect:** the dataset contains 270 organisational units. The level of detail varies: some units refer to individual settlements, while others cover broader geographical areas. The dataset includes names and some name variants, classifications, locations, relationships between organisations and references to external databases. Some information, particularly for organisations outside the VOC, is less comprehensive. For more name variants, it is recommended to make use of the connections to the GLOBALISE places dataset, WikiData and the Atlas of Mutual heritage. All these sources contain additional labels and information for the organisations.

- Pepping, Kay; Joseph, Lija; Kuruppath, Manjusha; Nijman, Brecht (2026). _GLOBALISE - Organisations in the Dutch East India Company Archive_. [https://doi.org/10.34894/2VNEUG](https://doi.org/10.34894/2VNEUG)
### Concepts

#### Ethnicities, religious groups and castes

> **Final reference data — to be added:** a description of the final ethnicities, religious groups and castes reference data, the number of records, and how it was compiled from the datasets listed below.

These concepts define and contextualise the ethnic, religious and caste categories that appear in the VOC archives. In the thesaurus they form the vocabulary *Ethnic, religious and caste categories* (577 concepts in October 2026).

**Based on:** labels from the VOC archives, from other datasets based on these archives and from indexes of source publications; definitions mostly from the glossaries of secondary works on the Indian Ocean world in the seventeenth and eighteenth centuries.

**What to expect:** most categories were assigned to people by the VOC, and rarely correspond to how people identified themselves. Many are linked to histories of colonial violence, enslavement and racism, and some are derogatory. The dataset is meant to help users understand these categories in the archive; its creators advise against using it for other purposes. See also [Colonial context](/pages/research-responsibly/ethics/colonial-context.md#people-and-groups).

* GLOBALISE – Ethnicities, Religious Groups and Castes in the Archives of the Dutch East India Company (1602-1799). <https://doi.org/10.34894/RI0KGV>

#### Commodities

> **Final reference data — to be added:** a description of the final commodities reference data, the number of records, and how it was compiled from the datasets listed below.

The commodities thesaurus defines goods traded by the VOC and arranges them in a hierarchy of broader and narrower categories, based on the Standard International Trade Classification (SITC).

**Based on:** all physical items in the shipping lists of the Bookkeeper-General in Batavia and the Monsoon Traders database, with definitions from secondary literature and broader categories from existing classifications.

**What to expect:** the thesaurus is mainly based on eighteenth-century shipping lists, so goods that were rarely shipped, or mainly traded in the seventeenth century, may be missing. The first published version contained 3,787 concepts, of which 2,294 were not yet classified; in October 2026 the thesaurus contained 3,901, of which 1,651 were not yet classified. Some definitions in the sources use outdated or offensive language; where possible, these were not adopted or were edited. Because the VOC also recorded people on its lists of goods, in some cases with a monetary value, the vocabulary has a separate category for them.

* GLOBALISE Thesaurus – Commodities. <https://doi.org/10.34894/5PZPPK>

<!-- TODO: update the number of concepts and unclassified concepts for the final version. -->

#### Weights, measures and currencies

> **Final reference data — to be added:** a description of the final weights, measures and currencies reference data, the number of records, and how it was compiled from the datasets listed below.

These concepts define units of weight, measure and currency used in VOC settlements in Asia, and how they converted into each other. In the thesaurus they form the vocabulary *Units of measure* (427 concepts in October 2026, among them 171 units of weight and 133 currencies).

**Based on:** the *Memoriën van Munten, Maaten, en Gewigten*, an eighteenth-century VOC compilation (1764–1771) on the units in use in Batavia and other settlements, supplemented with the VOC Glossarium.

**What to expect:** units as the VOC defined and understood them, in the eighteenth century, for the places covered by the source. The names are Dutch renderings of local terms, and for many lesser-known units the local name is unknown. The list is not exhaustive, and the conversions in the source may contain errors.

* GLOBALISE – Weights and Measures in the 18th-Century Indian Ocean World. <https://doi.org/10.34894/GDEPNF>

### Documents

Document descriptions and document types (see [How the data was produced](/pages/research-responsibly/data/production.md#3-identifying-documents)) are based on the following datasets. Individual documents are described in the indexes; document types are concepts in the thesaurus (*Globalise document types* and *TANAP document classification*).

* GLOBALISE – Digitized Indexes of the Dutch East India Company OBP (1602-1799): document-level index entries from the [TANAP index](https://docs.globalise.huygens.knaw.nl/tanap/tanap-index-establishment-reconstructions/) and from typescript indexes in the Nationaal Archief. The indexes do not cover all inventory numbers. <https://doi.org/10.34894/OP20NM>
* SKOS Thesauri for VOC Archival Document Classification: the TANAP document classification and a simplified Globalise classification. <https://doi.org/10.34894/B2WBZZ>
* Overzicht van Generale Missiven in het archief van de VOC, 1.04.02: the *Generale Missiven* identified in the archive, 1618–1793. <https://doi.org/10.34894/SRDMFU>
* GLOBALISE – VOC Document Segmentation Dataset: manually segmented inventories, for training and evaluating document segmentation. <https://doi.org/10.34894/XAJ12C>
* Early Modern Dutch Colonial Court Records (Resilient Diversity project): court cases of the Councils of Justice of Batavia and the Cape of Good Hope, used as documents, with their titles, in volumes without an index.

<!-- TODO: add the DOI or URL of the Early Modern Dutch Colonial Court Records dataset. -->

## How reference data appears on the portal

Reference data is already used to describe the archive itself. The description of each inventory, for instance, links the settlements it concerns to records in the places dataset: inventory 1056 is linked to Bantam, Siam, Timor, Japan, Ambon and other places.

Content to be developed.

<!-- TODO: describe how users encounter reference data on the portal (entity pages, search filters, maps, timelines), once the interface is final. -->

## Entity linking

The named entity recognition model labels words in the text as, for example, a person's name or a location, but it does not know *which* person or place is meant. Entity linking is the step that connects such a mention to a record in the reference data: deciding, for example, that *Bantam* in a letter from 1614 refers to the polity or port of Banten on Java. Mentions of concepts are linked in the same way: a word such as *peper* or *opperkoopman* in the text is linked to the corresponding concept in the thesaurus.

This is difficult. Names are spelled in many different ways, transcriptions contain errors, the same name can refer to different people or places, and many entities that appear in the archive are not in the reference data at all.

### Method

Content to be developed.

<!-- TODO: describe the entity linking method(s) used (which entity types, which features, how candidates are selected and ranked, any manual checking). Relevant private repositories: nlp-entity-linking, entity-linking-reference-data. Include how mentions of concepts (e.g. commodities, occupations, ship types) are linked to the thesaurus. -->

### Evaluation

Content to be developed.

<!-- TODO: add plain-language evaluation metrics for entity linking (e.g. precision and recall per entity type), and explain how users can tell how reliable a link is. -->
