---
title: "Technical documentation"
subtitle: ""
summary: "Detailed documentation of models, tools, pipelines and technical decisions."
type: "page"
slug: "technical-documentation"
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

related: ["how-the-data-was-produced", "data-model-and-ontologies", "accessing-the-data", "outputs"]
---

# Technical documentation

<!-- Sources: DataverseNL dataset records (via DataCite, retrieved 2026-10-01); GitHub repositories of globalise-huygens and knaw-huc; Hugging Face model cards of the globalise organisation; NER guidelines (https://github.com/globalise-huygens/finegrained-hist-ner/blob/main/docs/ner-guidelines.md); provenance metadata in the annotation pages; publications listed in /assets/references/references.bib. -->

<!-- TODO: this page depends on the final documentation (dependency "Documentation" in CONTENT.md). Confirm for each component which version was used to produce the data on the portal. -->

This page brings together the technical details of each step described in [How the data was produced](/pages/research-responsibly/data/production.md): the software, models, training data, code and publications. It is intended for researchers and developers who want to evaluate, reproduce or reuse the work.

## Layout analysis and text recognition

| Component | Description | Link |
| --- | --- | --- |
| Laypa | Layout analysis software (KNAW Humanities Cluster) | <https://github.com/knaw-huc/laypa> |
| Loghi | Handwritten text recognition software (KNAW Humanities Cluster) | <https://github.com/knaw-huc/loghi> |
| GLOBALISE Laypa Baseline Model – August 2023 | Model for detecting text lines | <https://doi.org/10.34894/JPS8TB> |
| GLOBALISE Laypa Region Model – August 2023 | Model for detecting and classifying text regions | <https://doi.org/10.34894/E4CGBF> |
| GLOBALISE Loghi Handwritten Text Recognition Model – August 2023 | Model for recognising handwriting | <https://doi.org/10.34894/HHM4TE> |
| GLOBALISE Ground Truth for Handwritten Text and Layout Recognition | Training and evaluation data | <https://doi.org/10.34894/IQ0YMT> |
| VOC transcriptions v2 – GLOBALISE | Earlier published version of the transcriptions (2024) | <https://doi.org/10.34894/50ZYWS> |

<!-- TODO: state which model versions produced the transcriptions on the portal, and whether the transcriptions on the portal will be published as a new dataset version. -->

### Evaluation of text recognition

Content to be developed.

<!-- TODO: add HTR evaluation results (e.g. character error rate on a held-out test set), with a short explanation. See also issue #3. -->

### Language identification

The languages of all pages in Latin script were identified automatically; pages in other scripts were identified separately. The method and results are documented in the [language-identification-data](https://github.com/globalise-huygens/language-identification-data) repository and in the blog post [The Languages of GLOBALISE](/pages/about/project/archive/blog/the-languages-of-globalise.md).

## Document identification

| Component | Description | Link |
| --- | --- | --- |
| Globalise documents | Database and scripts for identifying documents, and for exporting the IIIF collection and manifests | <https://github.com/globalise-huygens/documents> |
| TANAP index and establishment reconstructions | Introduction to the TANAP index, its coverage, and document lists per VOC establishment (Renate Smit, 2025) | <https://docs.globalise.huygens.knaw.nl/tanap/tanap-index-establishment-reconstructions/> |
| Document segmentation model | Code, method and evaluation of the segmentation (`segmentation/`), branch `llm-definitive-doc` | <https://github.com/globalise-huygens/documents/blob/llm-definitive-doc/README.md#document-segmentation-segmentation> |
| GLOBALISE – Digitized Indexes of the Dutch East India Company OBP (1602-1799) | Document-level index entries from the TANAP and Nationaal Archief finding aids | <https://doi.org/10.34894/OP20NM> |
| Early Modern Dutch Colonial Court Records (Resilient Diversity project) | Court cases of the Councils of Justice of Batavia and the Cape, used as documents in volumes without an index | *To be added* |
| GLOBALISE – VOC Document Segmentation Dataset | Dataset for training and evaluating document segmentation | <https://doi.org/10.34894/XAJ12C> |
| SKOS Thesauri for VOC Archival Document Classification | Document types: the TANAP classification and the Globalise classification | <https://doi.org/10.34894/B2WBZZ> |

Publication: Schnober et al. (2024), *Page Embeddings: Extracting and Classifying Historical Documents with Generic Vector Representations* (`Schnober2024` in the bibliography).

### The segmentation model

The documents were identified with a single segmentation model, applied to all 6,914 inventory numbers. A plain-language summary and the counts per kind of document are on [How the data was produced](/pages/research-responsibly/data/production.md#3-identifying-documents).

1. **Scan features.** Predictors describe every scan: opening and closing formulas in the text, blank pages and text length, text that recurs on nearby scans, position in the inventory, signature marks, page and folio numbers (cleaned of misreadings and restarts), running headers and header dates, language changes, marginalia, page layout from the PageXML (where text starts and stops, gaps, headings, catch-words), and GloBERTise page embeddings with kNN start scores (Schnober et al. 2024).
2. **Scan models.** Logistic regressions on each scan's features and those of its neighbours give the log-odds that a document starts on the scan, ends on it, starts on the same scan where the previous one ends, or that the scan is not part of a document. They were fitted on the 22 hand-segmented inventories, with a prior on document length.
3. **Table-of-contents alignment.** A monotone dynamic programme places the index entries, in index order, on their start scans: on page and folio numbers found on the scans (exact or interpolated), on text matching the entry's description, and on registers of papers recognised by the entries they list. Titles that announce a number of documents (*Vier brieven van Ternaten ...*) make the model look for that many parts. Entries that cannot be placed this way go to the strongest start evidence between their placed neighbours.
4. **Segmentation.** A second dynamic programme over all scans, with the placed entries fixed, decides every document's start and end and the type of each boundary (next document on the same scan, the next scan, or after non-document scans). Documents are labelled as index entries, parts of a preceding entry (such as enclosures), unindexed documents, or court cases.

**Evaluation** (cross-validated on the hand-segmented inventories, exact scan):

| | With index | Without index |
| --- | --- | --- |
| Start F1 | 65.1 | 50.6 |
| End F1 | 61.2 | 49.5 |
| *Generale Missiven*: starts found | 87.6% | 59.6% |

Index entries placed on the right scan: 78.3% in the hand-segmented inventories (91.4% within one scan), 73.7% in the *Generale Missiven*.

**Titles and types.** Documents without a VOC title get an inferred title (*type, place, date*). The type comes from a classifier on the opening of the first page and the end of the last page, trained on documents with an index entry (cross-validated: 84% right for the 78% of documents to which it assigns a type, at a confidence threshold of 0.5); place and date come from the closing formula, read with the Globalise entity annotations. Dates of index entries missing from the enriched index were parsed from the descriptions (97% agreement with the enriched dates where both exist).

**Versions.** Scans holding the same text in two inventories are linked (word 3-gram containment of at least 0.3 between inventories within two years of each other), in about 168,000 links.

<!-- TODO: link the README on main once the llm-definitive-doc branch has been merged. Add the DOI of the Early Modern Dutch Colonial Court Records dataset. -->

<!-- Sources: README of the documents repository (branch llm-definitive-doc) and its database, queried 2026-10-30. -->

## GloBERTise

GloBERTise is an encoder language model with a RoBERTa architecture, pre-trained from scratch on transcriptions of the VOC archives, and therefore specialised in early modern Dutch as used in the archive. It is the basis for the entity and event recognition models.

| Component | Link |
| --- | --- |
| Model | <https://huggingface.co/globalise/GloBERTise> |
| Pre-training code | <https://github.com/globalise-huygens/GloBERTise> |
| Evaluation code | <https://github.com/globalise-huygens/GloBERTise-eval> |

Publications: Verkijk, Vossen & Sommerauer (2025), *Language Models Lack Temporal Generalization and Bigger is Not Better* (`Verkijk2025`); Verkijk & Vossen (2026), *Out-Of-Tune rather than Fine-Tuned* (`Verkijk2026`).

## Named entity recognition

The NER model labels tokens in the normalised page text with one of 15 categories:

| Label | Description | Example |
| --- | --- | --- |
| PER_NAME | Name of person | Tilling |
| PRF | Profession, title | Conincx |
| STATUS | (Civic) status | veduwe, slaaf |
| PER_ATTR | Other person attributes | manspersoon |
| LOC_NAME | Name of location | Sumatra |
| LOC_ADJ | Adjective derived from a location name | Ternaats |
| ETH_REL | Ethno-religious designation, not derived from a location name | Moor, alfoerees |
| CMTY_NAME | Name of commodity | peper |
| CMTY_QUAL | Commodity qualifier, such as colour or processing | gemeen gebleekt |
| CMTY_QUANT | Quantity | 840 pikol |
| SHIP | Ship name | Abigail |
| SHIP_TYPE | Ship type | jacht |
| ORG | Name of organisation | Compagnie, Comptoir |
| DATE | Date | 14e, ultimo Februari |
| DOC | Document | Jongste, brief |

The labels and examples are taken from the annotation guidelines. Some labels (STATUS, ETH_REL) capture categories used in the sources themselves, including colonial designations of status and ethnicity; see [Colonial context](/pages/research-responsibly/ethics/colonial-context.md#colonial-terminology-and-categories).

| Component | Link |
| --- | --- |
| Annotation guidelines | <https://github.com/globalise-huygens/finegrained-hist-ner/blob/main/docs/ner-guidelines.md> |
| Annotations, training and inference code | <https://github.com/globalise-huygens/finegrained-hist-ner> |
| Inference model used on the corpus | <https://huggingface.co/globalise/globalise-NER> |
| Training dataset (train A+B) | <https://huggingface.co/datasets/globalise/globalise_NER_token_classification_dataset> |

Publication: Arnoult, Nijman & Van Wissen (2025), *Fine-grained Named-Entity Recognition for the East-India Company domain* (`Arnoult2025`).

### Evaluation of the NER model

Content to be developed.

<!-- TODO: add evaluation results for the inference model globalise/globalise-NER (its Hugging Face model card is currently empty apart from the licence). -->

## Event detection

Event detection is done in two steps, both with models fine-tuned from GloBERTise: a detection model marks the words that refer to an event, and a classification model assigns an event type from the [event ontology](/pages/research-responsibly/data/data-model.md#the-event-ontology).

| Component | Link |
| --- | --- |
| Event ontology and annotation guidelines | <https://github.com/globalise-huygens/nlp-event-detection/wiki> |
| Event detection model | <https://huggingface.co/globalise/GloBERTise-event-detector-general> |
| Event classification model | <https://huggingface.co/globalise/GloBERTise-event-classifier-general> |
| Pilot code | <https://github.com/globalise-huygens/nlp-event-detection> |
| Lexical approach to event detection | <https://github.com/globalise-huygens/nlp-event-lexical-approach> |
| Evaluation of event classifiers | <https://github.com/globalise-huygens/nlp-event-classifier-evaluation> |
| Validation of model output by external historians | <https://github.com/globalise-huygens/nlp-event-external-machine-output-validation> |

Publications: Verkijk & Vossen (2023), *Sunken Ships Shan't Sail: Ontology Design for Reconstructing Events in the Dutch East India Company Archives* (`Verkijk2023a`); Verkijk, Sommerauer & Vossen (2024), *Studying Language Variation Considering the Re-Usability of Modern Theories, Tools and Resources for Annotating Explicit and Implicit Events in Centuries Old Text* (`Verkijk2024`).

### Methodology and evaluation

Content to be developed.

<!-- TODO: document the full event detection methodology (annotation, training data, models used for the portal data, inference, evaluation). Confirm which models produced the event annotations on the portal. -->

## Entity linking

Content to be developed.

<!-- TODO: document the entity linking method, code and evaluation. Relevant repositories are currently private (nlp-entity-linking, entity-linking-reference-data). -->

## Reference data

| Component | Description | Link |
| --- | --- | --- |
| Reference data pipeline | Converts dataset workbooks into RDF knowledge graphs and JSON-LD | <https://github.com/globalise-huygens/reference-data-pipeline> |
| Source datasets | Datasets on DataverseNL | See [Reference data & entity linking](/pages/research-responsibly/data/reference-data.md) |

## Publishing annotations

The transcriptions, entities and events are converted into W3C Web Annotations with scripts in the [globalise-tools](https://github.com/knaw-huc/globalise-tools) repository of the KNAW Humanities Cluster. The annotation pages on the portal record the exact version of the script used. See [Data model & ontologies](/pages/research-responsibly/data/data-model.md).

## The portal

The source code of the research portal is available at <https://github.com/globalise-huygens/globalise-research-portal>.

<!-- TODO: add a short description of the portal's technical architecture (search index, MCP server, hosting) once final. -->
