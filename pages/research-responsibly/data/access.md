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

<!-- TODO: this page depends on the final infrastructure (dependency for DATA-07 in CONTENT.md). Check all endpoints before publication. -->

Everything you see on the portal is also available as open data. This page explains where to find it. For an explanation of the structure and formats, see [Data model & ontologies](/pages/research-responsibly/data/data-model.md). For the conditions for reuse, see [Licences & reuse](/pages/learn-get-started/licences.md).

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

## MCP server

<!-- Sources: README and source code of https://github.com/globalise-huygens/globalise-mcp (version 0.1.0, retrieved 2026-11-12). -->

The Globalise MCP server lets AI assistants and other clients that support the [Model Context Protocol](https://modelcontextprotocol.io) search and read the Globalise data. Instructions for users without a technical background, and advice on checking an assistant's answers, are on [Using Globalise with an AI assistant](/pages/learn-get-started/ai-assistant.md).

| | |
| --- | --- |
| Address | `https://mcp.globalise.nl/mcp` |
| Transport | Streamable HTTP; stateless |
| Access | Read-only; no authentication |
| Rate limit | 60 requests per minute per client |
| Source code | <https://github.com/globalise-huygens/globalise-mcp> |
| Status | Prototype (version 0.1.0) |

<!-- Address checked 2026-11-26: https://mcp.globalise.nl/mcp answers MCP requests over https; http redirects to https. TODO: update the status and version at launch (the hosted server still reported version 0.1.0 on 2026-11-26). -->

<!-- TODO: check which clients work with the server (e.g. Claude, ChatGPT, Le Chat, Copilot, Cursor, VS Code), and list them here or on the AI assistant page. -->

**Tools.** The server offers eight tools:

| Tool | What it does |
| --- | --- |
| `search_documents` | Full-text and structured search in the documents: words, phrases, wildcards, fuzzy matching, proximity, and fields for tagged entities (by id), roles, annotation types, dates, place of writing, inventory and document type. Returns documents with highlighted snippets and viewer links. |
| `analyze_distribution` | How a result set is spread over decades, places of writing, document types, professions and archive series, compared with the whole corpus |
| `count_mentions` | The number of occurrences of the search terms (not documents), with the spellings matched, mentions per decade relative to the size of the corpus, and the documents with most mentions. Exact up to a set number of documents, otherwise estimated from a sample with a 95% interval. |
| `search_reference_data` | Persons, places, ships, organisations, polities and thesaurus concepts by any spelling, with the number of documents that mention them |
| `get_record` | Any record by identifier or URI, summarised: names, classifications, dates, sources and linked records |
| `get_document` | A document's metadata, text (plain or with inline entity tags), tagged entities and scans; can find which scan contains a quoted passage |
| `get_scan` | One scan: the normalised and diplomatic transcription, annotations, IIIF image and viewer link, and the image itself, either the whole page or a crop around a quoted passage |
| `globalise_about` | Background for the assistant: the data model, limitations, query syntax and a research workflow, with links to the pages on this website |

The same background texts are also available as MCP resources (`globalise://docs/…`), and the prompt `research_question` starts a research session that follows the recommended workflow.

**Provenance.** Every response includes a `provenance` block with the services queried, the dated version of the search index (for example `annotated-documents.2026.11.05`) and the caveats that apply to that query, such as "names matched by spelling, not by id". Search responses also show how names in the query were resolved to identifiers. Cite the index version together with document and scan identifiers: the search indices are rebuilt from time to time, and results can change.

**Data.** The server reads the same search indices as the portal and the persistent data at `data.globalise.huygens.knaw.nl`. The images come from the Nationaal Archief's IIIF image server. All limitations of the data apply; see [Bias & limitations](/pages/research-responsibly/ethics/bias-and-limitations.md). An AI assistant adds its own errors and interpretation, so check every claim against the scans and transcriptions.

**Running it yourself.** The server can also run locally over stdio, for example in Claude Desktop, Claude Code, Cursor or VS Code. It needs Node 26. See the [README](https://github.com/globalise-huygens/globalise-mcp#readme) for instructions.

<!-- TODO: once the package is published on npm, replace the local instructions with `npx -y @globalise/mcp`. -->

## Bulk downloads

Content to be developed.

<!-- TODO: describe how to download the complete data (transcriptions, annotations, documents, reference data) in bulk, and in which formats and versions. -->

Earlier versions of the transcriptions, and the datasets on which the reference data is based, are available on [DataverseNL](https://dataverse.nl/dataverse/globalise). See [Reference data & entity linking](/pages/research-responsibly/data/reference-data.md) for a list.

The documents identified by the Globalise project are available in the deposit [*GLOBALISE – Document Segmentation of the VOC Archives*](https://doi.org/10.34894/P826UY) on DataverseNL, as compressed CSV files with a codebook:

| File | Contents |
| --- | --- |
| `results/documents.csv.gz` | All 508,448 documents, with their first and last scan, title and source of the title, dates, place, types and index identifiers |
| `results/document_scans.csv.gz` | The scans of each document |
| `results/… - with scans.csv.gz` | The *Digitized Indexes* with each entry's start and end scan |

## Models and code

* The code and the fitted model of the document segmentation are in the [deposit](https://doi.org/10.34894/P826UY) described under *Bulk downloads*.
* Models (text recognition, named entity recognition, event detection) are available on [DataverseNL](https://dataverse.nl/dataverse/globalise) and [Hugging Face](https://huggingface.co/globalise).
* Code is available on GitHub, in the [globalise-huygens](https://github.com/globalise-huygens) organisation and, for text recognition and annotation conversion, the [knaw-huc](https://github.com/knaw-huc) organisation.

See [Technical documentation](/pages/research-responsibly/data/technical-documentation.md) for an overview per component.

## Long-term availability

Content to be developed.

<!-- TODO: explain who maintains the data after the end of the project (handover to Huygens Data & Collections), how long the identifiers and endpoints will remain available, and where archived copies are deposited. -->

## Questions and support

Content to be developed.

<!-- TODO: explain where technical users can ask questions or report problems with the data (e.g. contact page, GitHub issues). -->
