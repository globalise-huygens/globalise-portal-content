---
title: "Accessing the data"
subtitle: ""
summary: "How to access Globalise data through APIs, bulk downloads and repositories."
type: "page"
slug: "accessing-the-data"
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

related: ["data-model-and-ontologies", "licences-and-reuse", "technical-documentation", "globalise-data"]
---

# Accessing the data

<!-- Sources: live endpoints at https://data.globalise.huygens.knaw.nl/ (collection, manifests, annotation pages, inventory and document records), tested 2026-10-01; README of https://github.com/globalise-huygens/documents; Globalise datasets on DataverseNL; Hugging Face organisation https://huggingface.co/globalise. -->

<!-- TODO: this page depends on the final infrastructure (dependency for DATA-03 in CONTENT.md). Check all endpoints before publication. -->

Everything you see on the portal is also available as open data. This page explains where to find it. For an explanation of the structure and formats, see [Data model & ontologies](/pages/data/data-model.md). For the conditions for reuse, see [Licences & reuse](/pages/data/licences.md).

## Data per page, inventory and collection

All data on the portal is published as linked open data at `https://data.globalise.huygens.knaw.nl/`, using persistent identifiers. Every resource can be retrieved as JSON(-LD) with a simple web request, without registration.

| What | Format | Example |
| --- | --- | --- |
| The collection: a list of all inventories | IIIF Collection | <https://data.globalise.huygens.knaw.nl/hdl:20.500.14722/inventory:collection> |
| An inventory, with all its pages and documents | IIIF Manifest | <https://data.globalise.huygens.knaw.nl/hdl:20.500.14722/inventory:1056.manifest> |
| Description of an inventory | Linked Art (JSON-LD) | <https://data.globalise.huygens.knaw.nl/hdl:20.500.14722/inventory:1056> |
| Description of a document | Linked Art (JSON-LD) | <https://data.globalise.huygens.knaw.nl/hdl:20.500.14722/document:NL-HaNA_1.04.02_1056_0011-0013> |
| Transcription of a page | W3C Web Annotation page | <https://data.globalise.huygens.knaw.nl/hdl:20.500.14722/annotations:transcriptions:NL-HaNA_1.04.02_1056_0125> |
| Entities on a page | W3C Web Annotation page | <https://data.globalise.huygens.knaw.nl/hdl:20.500.14722/annotations:entities:NL-HaNA_1.04.02_1056_0125> |
| Events on a page | W3C Web Annotation page | <https://data.globalise.huygens.knaw.nl/hdl:20.500.14722/annotations:events:NL-HaNA_1.04.02_1056_0125> |

To find the data for another page, replace the scan name (`NL-HaNA_1.04.02_1056_0125`) or the inventory number (`1056`). The IIIF manifest of an inventory lists all its pages and links to their annotation pages, so you can start there and follow the links. Annotation pages also link to the previous and next page.

Because the collection and manifests follow the IIIF standard, you can open them in IIIF viewers such as [Mirador](https://projectmirador.org/) or [Universal Viewer](https://universalviewer.io/) to browse the scans of an inventory. Whether a viewer also shows the transcriptions and annotations depends on the viewer.

Responses are compressed (gzip). Web browsers and most programming libraries handle this automatically; with `curl`, use the `--compressed` option.

<!-- TODO: there are currently two manifests per inventory: https://data.globalise.huygens.knaw.nl/manifests/inventories/1056.json (without documents; rights statement Public Domain Mark) and https://data.globalise.huygens.knaw.nl/hdl:20.500.14722/inventory:1056.manifest (with documents as ranges; CC0). Decide which is canonical and document only that one. -->

<!-- TODO: each inventory also has a text file (e.g. hdl:20.500.14722/inventory:1056.txt), referenced from the manifest, which is currently served as text/plain but is a gzip archive. Fix, then document it here as a way to download all text of an inventory. -->

## The scans

The scans are not hosted by Globalise. They are served by the Nationaal Archief through its IIIF image server; the manifests contain the address of each image. The Nationaal Archief's own website also gives access to the scans, through the inventory of the [VOC archive (1.04.02)](https://www.nationaalarchief.nl/onderzoeken/archief/1.04.02).

## Search API

Content to be developed.

<!-- TODO: document any search API or query endpoint (e.g. full-text search, SPARQL endpoint for reference data and annotations) that will be offered, or state that there is none. -->

## Bulk downloads

Content to be developed.

<!-- TODO: describe how to download the complete data (transcriptions, annotations, documents, reference data) in bulk, and in which formats and versions. -->

Earlier versions of the transcriptions, and the datasets on which the reference data is based, are available on [DataverseNL](https://dataverse.nl/dataverse/globalise). See [Reference data & entity linking](/pages/data/reference-data.md) for a list.

## Models and code

* Models (text recognition, named entity recognition, event detection) are available on [DataverseNL](https://dataverse.nl/dataverse/globalise) and [Hugging Face](https://huggingface.co/globalise).
* Code is available on GitHub, in the [globalise-huygens](https://github.com/globalise-huygens) organisation and, for text recognition and annotation conversion, the [knaw-huc](https://github.com/knaw-huc) organisation.

See [Technical documentation](/pages/data/technical-documentation.md) for an overview per component.

## Long-term availability

Content to be developed.

<!-- TODO: explain who maintains the data after the end of the project (handover to Huygens Data & Collections), how long the identifiers and endpoints will remain available, and where archived copies are deposited. -->

## Questions and support

Content to be developed.

<!-- TODO: explain where technical users can ask questions or report problems with the data (e.g. contact page, GitHub issues). -->
