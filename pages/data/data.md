---
title: "Globalise data: what you see on the portal"
subtitle: ""
summary: "What the scans, transcriptions, entities, events and documents on the portal are, and where they come from."
type: "page"
slug: "globalise-data"
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

related: ["how-the-data-was-produced", "data-model-and-ontologies", "accessing-the-data", "reference-data"]
---

# Globalise data: what you see on the portal

<!-- Sources: live data for inventory 1056 and scan NL-HaNA_1.04.02_1056_0125 (IIIF manifest https://data.globalise.huygens.knaw.nl/hdl:20.500.14722/inventory:1056.manifest, annotation pages for transcriptions, entities and events), retrieved 2026-10-01; README of https://github.com/globalise-huygens/documents. -->

<!-- TODO: check this page against the final portal interface (dependency "Final data model" in CONTENT.md), in particular the names of interface elements such as "right panel". -->

When you open a page on the Globalise portal, you see several kinds of information side by side: an image of the original page, a transcription of its text, and highlighted words that have been recognised as people, places, commodities or events. These come from different sources and were produced in different ways. This page explains what each of them is.

As an example, we use one page from the archive: scan [NL-HaNA_1.04.02_1056_0125](https://data.globalise.huygens.knaw.nl/hdl:20.500.14722/canvas:NL-HaNA_1.04.02_1056_0125), a page from inventory number 1056 of the VOC archive, which the archive's inventory dates to 1614.

## The scan

The image of the page is a scan made by the Nationaal Archief (Dutch National Archives) in The Hague, which holds the original documents. The portal displays them directly from the Nationaal Archief's image server, using the [IIIF](https://iiif.io/) standard for sharing images online. This is why you can zoom in to see the page in full detail.

The scan is the closest you can get to the original document on this portal. When in doubt about anything else on the page, check the scan.

## The transcription

Next to the scan, the portal shows a transcription of the text on the page. This transcription was produced automatically by handwritten text recognition (HTR) software, not typed by a person. It will contain errors. See [How the data was produced](/pages/data/production.md).

The transcription comes in more than one form:

* a **diplomatic** version: the text as recognised by the software, line by line, in the order in which the lines were found on the page;
* a **normalised** version of the page text, on which the entity and event annotations are based.

<!-- TODO: explain in plain language what "normalised" means here (e.g. reading order, joining of lines and hyphenated words), and which version the portal shows by default. -->

Every line and every word of the transcription is linked to its exact position on the scan, so the portal can show where on the page a piece of text was found. The software also divided the page into **text regions** and labelled them, for instance as a header, a paragraph, a marginal note, a page number or a catchword (a word at the foot of a page repeating the first word of the next page).

## Entities

Words and phrases in the transcription that refer to people, places, commodities, ships, organisations, dates and documents are highlighted as **entities**. They were recognised by a language model trained by the project, a method called named entity recognition (NER).

Each entity is labelled with a category, such as *Name of Person*, *Name of Location*, *Profession, title*, *Name of Commodity* or *Quantity*. The labels describe the form of the word in the text: a place name is labelled as a location, even if in context it refers to a state or ruler. The [technical documentation](/pages/data/technical-documentation.md#named-entity-recognition) lists all categories.

Entity annotations are model output. They will include errors: words that were missed, words that were labelled wrongly, and words that are not entities at all.

## Events

Some words are highlighted as **events**: actions and situations, such as a ship arriving, goods being traded, a letter being written, or someone being killed. These were also recognised by a language model. Each event is classified according to the Globalise event ontology, a structured list of event types, such as *Arriving*, *Trade*, *Communication* or *Attacking*. See [Data model & ontologies](/pages/data/data-model.md).

Event detection is one of the most difficult tasks in the project, because events can be described in many different ways, and many are only implied. Treat event annotations with particular care.

## Links to reference data

Content to be developed.

<!-- TODO: describe how entity annotations are linked to records in the reference data (people, places, polities, commodities, ships, ...), what users see of these links in the portal, and how reliable they are. See /pages/data/reference-data.md (section "Entity linking"). -->

## Documents, inventories and the collection

Pages do not stand alone. The portal organises them in three levels:

* **Collection.** All pages that Globalise works with belong to one collection: the *Overgekomen Brieven en Papieren* (OBP) in series 1.04.02 of the VOC archive at the Nationaal Archief, comprising about 6,900 inventory numbers.
* **Inventory.** An inventory number usually refers to one bound volume of documents, from a handful to over a thousand pages. Inventory 1056, for example, contains 550 scans of documents concerning VOC settlements such as Bantam, Ambon, Ternate and Coromandel, and is dated 1614.
* **Document.** Within an inventory, pages are grouped into documents: letters, reports, journals, lists and other items. A volume was not originally divided into documents in a way a computer can read, so Globalise had to identify where documents begin and end. Different methods were used for this, and their results do not always agree: a page may be assigned to more than one document, or to none. See [How the data was produced](/pages/data/production.md#3-identifying-documents).

Information about inventories, such as their dates, titles and the settlements they concern, comes from the Nationaal Archief's inventory of the VOC archive. Titles and types of documents come from historical tables of contents and finding aids, including the [index compiled by the TANAP project](https://docs.globalise.huygens.knaw.nl/tanap/tanap-index-establishment-reconstructions/), which Globalise digitised and extended. See also [TANAP](/pages/resources/related-projects.md#tanap-towards-a-new-age-of-partnership) under Resources.

<!-- TODO: confirm which document identification methods are used in the final portal, and how overlapping or missing assignments are shown to users. -->

## What the data is based on

| What you see | Source | How it was made |
| --- | --- | --- |
| Scan | Nationaal Archief | Digitised by the Nationaal Archief, displayed via its IIIF image server |
| Transcription | Globalise | Automatic text recognition (Laypa and Loghi) |
| Text regions | Globalise | Automatic layout analysis (Laypa) |
| Entities | Globalise | Named entity recognition model, trained on manually annotated documents |
| Events | Globalise | Event detection model, trained on manually annotated documents |
| Documents | Globalise, based on historical finding aids | Combination of finding aids and automatic methods |
| Inventory information | Nationaal Archief | Inventory of the VOC archive (1.04.02) |
| Reference data | Globalise | Compiled by historians from sources and literature |

Every annotation file records how and when it was created, and with which software. See [Data model & ontologies](/pages/data/data-model.md) and [Accessing the data](/pages/data/access.md).
