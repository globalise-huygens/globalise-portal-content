---
title: "Data model & ontologies"
subtitle: ""
summary: "How Globalise data is structured: identifiers, standards, the Globalise ontology and the event ontology."
type: "page"
slug: "data-model-and-ontologies"
status: "draft"

authors: []
datePublished: ""
dateUpdated: "2026-11-16"

featured: false

hero:
  src: ""
  alt: ""
  caption: ""
  credit: ""
  source: ""
  licence: ""

related: ["globalise-data", "event-ontology", "accessing-the-data", "technical-documentation", "reference-data"]
---

# Data model & ontologies

<!-- Sources: live data for inventory 1056 and scan NL-HaNA_1.04.02_1056_0125 (IIIF collection, manifest, annotation pages, inventory and document records), JSON-LD context https://objectstore.surf.nl/87435b768620494e8e911c83d1997f24:globalise-data/contexts/globalise.json, all retrieved 2026-10-01; README of https://github.com/globalise-huygens/ontology (private repository); event ontology wiki https://github.com/globalise-huygens/nlp-event-detection/wiki (version 3, last updated 12 August 2026). -->

This page is for readers who want to know how Globalise data is structured, for instance to reuse it in their own research or software. It describes the identifiers, the international standards the data follows, and the two ontologies that give the data its meaning: the Globalise ontology and the event ontology.

An **ontology** is a formal description of the kinds of things a dataset talks about (such as people, places, documents and events) and the relationships between them. Using an ontology makes it possible to combine and query information consistently, and to connect it with data from other projects.

## Identifiers

Every inventory, document, page and annotation page in Globalise has a persistent identifier, based on the Handle system (prefix `20.500.14722`). These identifiers resolve to the data via `https://data.globalise.huygens.knaw.nl/`. For example:

| Resource | Identifier |
| --- | --- |
| The collection | [`hdl:20.500.14722/inventory:collection`](https://data.globalise.huygens.knaw.nl/hdl:20.500.14722/inventory:collection) |
| An inventory (IIIF manifest) | [`hdl:20.500.14722/inventory:1056.manifest`](https://data.globalise.huygens.knaw.nl/hdl:20.500.14722/inventory:1056.manifest) |
| An inventory (description) | [`hdl:20.500.14722/inventory:1056`](https://data.globalise.huygens.knaw.nl/hdl:20.500.14722/inventory:1056) |
| A document (description) | [`hdl:20.500.14722/document:NL-HaNA_1.04.02_1056_0011-0013`](https://data.globalise.huygens.knaw.nl/hdl:20.500.14722/document:NL-HaNA_1.04.02_1056_0011-0013) |
| A page (IIIF canvas) | `hdl:20.500.14722/canvas:NL-HaNA_1.04.02_1056_0125` |
| Transcription of a page | [`hdl:20.500.14722/annotations:transcriptions:NL-HaNA_1.04.02_1056_0125`](https://data.globalise.huygens.knaw.nl/hdl:20.500.14722/annotations:transcriptions:NL-HaNA_1.04.02_1056_0125) |
| Entities on a page | [`hdl:20.500.14722/annotations:entities:NL-HaNA_1.04.02_1056_0125`](https://data.globalise.huygens.knaw.nl/hdl:20.500.14722/annotations:entities:NL-HaNA_1.04.02_1056_0125) |
| Events on a page | [`hdl:20.500.14722/annotations:events:NL-HaNA_1.04.02_1056_0125`](https://data.globalise.huygens.knaw.nl/hdl:20.500.14722/annotations:events:NL-HaNA_1.04.02_1056_0125) |

Pages are identified by the file name of the Nationaal Archief scan: `NL-HaNA_1.04.02_1056_0125` is scan 0125 of inventory number 1056 in archive 1.04.02 of the Nationaal Archief (NL-HaNA). Documents are identified by their first and last scan.

<!-- TODO: confirm that the hdl: identifiers are registered as persistent Handles (and how they resolve via hdl.handle.net), and how long they are guaranteed to remain resolvable (handover to Huygens Data & Collections). -->

## Standards

Globalise data follows established international standards, so that it can be used with existing tools.

* **IIIF** (International Image Interoperability Framework). The collection, the inventories and the documents are published as [IIIF Presentation](https://iiif.io/api/presentation/3.0/) resources. The collection lists all inventories. Each inventory is a *manifest*, in which every scan is a *canvas*, and the documents within an inventory are *ranges* that group canvases into a table of contents. The images themselves are served by the Nationaal Archief through the [IIIF Image API](https://iiif.io/api/image/).
* **Web Annotation.** Transcriptions, entities and events are published as [W3C Web Annotations](https://www.w3.org/TR/annotation-model/), grouped in one annotation page per scan and per type. Annotations on the transcription point to areas of the image (as polygons). Entity and event annotations point to words in the normalised page text, and also to the corresponding words in the diplomatic transcription and to the area of the image where they appear.
* **Linked Art and CIDOC CRM.** Descriptions of inventories, documents and entities use [Linked Art](https://linked.art/), a JSON-LD profile of the [CIDOC Conceptual Reference Model](https://www.cidoc-crm.org/), an ontology widely used for cultural heritage. Some general terms, such as types of identifiers and units, come from the Getty [Art & Architecture Thesaurus](https://www.getty.edu/research/tools/vocabularies/aat/).

## The Globalise ontology (GLOBo)

Standard ontologies do not cover everything that the VOC archives talk about. The Globalise ontology, GLOBo, extends [CIDOC CRM](https://www.cidoc-crm.org) and the related [PWRo](https://ontology.swissartresearch.net/pwro/) and [AAAo](https://ontology.swissartresearch.net/aaao/) ontologies to represent historical information that these cannot express on their own. It includes, for example, classes for commodities, financial exchanges, payments and purchases, units and values of exchange, internal states and changes, and attestations.

GLOBo was developed by the Globalise project together with Takin.solutions, using the OntoME tool. Its namespace is `https://w3id.org/globalise/ontology/` (prefix `globo`). Version 1.0 is the current stable release.

<!-- TODO: link to the GLOBo specification and RDF files. The ontology repository (https://github.com/globalise-huygens/ontology) is private; make it public or publish the release elsewhere, and check that the namespace URI resolves. -->

### How GLOBo is used

Content to be developed.

<!-- TODO: explain the function of GLOBo in the portal: which data is modelled with it (entity and event annotations, reference data), how it relates to the event ontology, and what users can do with it (e.g. combined queries on entities and events). -->

## The event ontology

Events are classified according to the Globalise event ontology. It builds on the Circumstantial Event Ontology (CEO). The definitions of all event classes, grouped into the seven categories used on the portal, are on the [Event ontology](/pages/research-responsibly/data/event-ontology.md) page. The [event ontology wiki](https://github.com/globalise-huygens/nlp-event-detection/wiki) contains the guidelines for annotators.

The ontology distinguishes between:

* **static events**: situations that hold for some time, such as [*being at a place*](/pages/research-responsibly/data/event-ontology.md#BeingAtAPlace), [*having in possession*](/pages/research-responsibly/data/event-ontology.md#HavingInPossession), [*being in a relationship*](/pages/research-responsibly/data/event-ontology.md#BeingInARelationship), [*being leader*](/pages/research-responsibly/data/event-ontology.md#BeingLeader), [*being employed*](/pages/research-responsibly/data/event-ontology.md#BeingEmployed), [*being in conflict*](/pages/research-responsibly/data/event-ontology.md#BeingInConflict), [*being dead*](/pages/research-responsibly/data/event-ontology.md#BeingDead) or [*having a medical condition*](/pages/research-responsibly/data/event-ontology.md#HavingAMedicalCondition);
* **dynamic events**: events that change such a situation. For example, [*Leaving*](/pages/research-responsibly/data/event-ontology.md#Leaving), [*Arriving*](/pages/research-responsibly/data/event-ontology.md#Arriving), [*Voyage*](/pages/research-responsibly/data/event-ontology.md#Voyage) and [*Transportation*](/pages/research-responsibly/data/event-ontology.md#Transportation) are kinds of [*Translocation*](/pages/research-responsibly/data/event-ontology.md#Translocation), which changes where someone or something is; [*Buying*](/pages/research-responsibly/data/event-ontology.md#Buying), [*Selling*](/pages/research-responsibly/data/event-ontology.md#Selling) and [*Trade*](/pages/research-responsibly/data/event-ontology.md#Trade) change who possesses something.

Each event type has **arguments**: the roles that people, things and places play in it. A *Translocation*, for example, has a *Patient* (the person or object that moves), an *Agent* (who carries out the movement, such as a ship's captain) and an *Instrument* (such as a ship), and may mention a *Source*, a *Target* and a *Path*.

On the portal, every event annotation is classified with an event type from this ontology. In the data, the type currently links to its definition in the wiki.

<!-- TODO: once the w3id URIs for event classes (e.g. https://w3id.org/globalise/BeingAtAPlace) redirect to the Event ontology page, update this sentence and the event annotations to use them. -->

<!-- TODO: check whether event arguments (participants, places, times) are included in the event annotations on the portal; currently the annotations only contain the event type and the word(s) that evoke the event. -->

<!-- TODO: the event ontology is documented in a GitHub wiki, which is not versioned as a release. Consider publishing a citable, versioned version. -->

## Thesauri and vocabularies

The data also uses Globalise's own controlled vocabularies, for instance for the types of text regions on a page, the categories of named entities and the types of documents. These are published in the [Globalise thesaurus](https://thesaurus.globalise.huygens.knaw.nl/), which also defines the concepts of the reference data, such as commodities, units of measure, occupations and place types. For an overview of its vocabularies, see [The Globalise thesaurus](/pages/research-responsibly/data/reference-data.md#the-globalise-thesaurus) on the Reference data page.

<!-- TODO: thesaurus URIs used in the data (e.g. https://data.globalise.huygens.knaw.nl/hdl:20.500.14722/thesaurus:page-number) currently lead to an error page in the thesaurus browser. Fix or explain. -->

## Provenance

Each annotation page records how it was created: the type of process (for example, the creation of Web Annotations from the output of the Globalise HTR or NER model), the date and time, and a link to the version of the software used. Inventory and document descriptions include references to their sources, such as links to the Nationaal Archief's inventory and identifiers in the TANAP index.
