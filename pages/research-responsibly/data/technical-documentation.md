---
title: "Technical documentation"
subtitle: ""
summary: "Detailed documentation of models, tools, pipelines and technical decisions."
type: "page"
slug: "technical-documentation"
status: "draft"

authors: []
datePublished: ""
dateUpdated: "2026-11-06"

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
| GLOBALISE – Document Segmentation of the VOC Archives | The resulting documents, the evaluation, the method, and the code and inputs needed to reproduce them (5.7 GB) | <https://doi.org/10.34894/P826UY> |
| GLOBALISE – Digitized Indexes of the Dutch East India Company OBP (1602-1799) | Document-level index entries from the TANAP and Nationaal Archief finding aids (version 4.0 used) | <https://doi.org/10.34894/OP20NM> |
| Early Modern Dutch Colonial Court Records (Resilient Diversity project) | Court cases of the Councils of Justice of Batavia and the Cape, used as documents in volumes without an index (version 3.0 used) | <https://doi.org/10.34894/S1BIHJ> |
| Overzicht van Generale Missiven in het archief van de VOC | The *Generale Missiven* identified by hand (version 5.0 used, with corrected first and last scans of 3 missives) | <https://doi.org/10.34894/SRDMFU> |
| GLOBALISE – VOC Document Segmentation Dataset | Dataset for training and evaluating document segmentation (version 3.0 used) | <https://doi.org/10.34894/XAJ12C> |
| SKOS Thesauri for VOC Archival Document Classification | Document types: the TANAP classification and the Globalise classification (version 1.0 used) | <https://doi.org/10.34894/B2WBZZ> |

Publication: Schnober et al. (2024), *Page Embeddings: Extracting and Classifying Historical Documents with Generic Vector Representations* (`Schnober2024` in the bibliography).

### The segmentation model

The documents were identified with a single segmentation model, applied to all 6,914 inventory numbers and stored as the method *Segmentation model* (final run and import: 30 October 2026). A plain-language summary and the counts per kind of document are on [How the data was produced](/pages/research-responsibly/data/production.md#3-identifying-documents).

**Inputs.**

* The index entries of the *Digitized Indexes* (TANAP index and Nationaal Archief typescripts), combined with the corrected TANAP list in the physical order of the volumes. The *Digitized Indexes* list some documents more than once, once for each settlement the indexers filed them under (in inventory 3558, OBP 95419 under *Batavia* and 95420 under *Japan* describe the same report). Entries in the same inventory with the same description, folios and dates were merged into one document, linked to all of their settlements and index identifiers (991 entries in 943 groups).
* The 933 [*Generale Missiven*](https://doi.org/10.34894/SRDMFU) identified by hand, which override the model (start, extent, title and dates).
* The court cases of the [*Early Modern Dutch Colonial Court Records*](https://doi.org/10.34894/S1BIHJ) (Resilient Diversity project), used for *Raad van Justitie* volumes without an index. A case with a start and end scan is a fixed document, and the ranges of the individual accused are its parts.
* The HTR text and the PageXML layout of [*VOC transcriptions v2*](https://doi.org/10.34894/50ZYWS) (version 1.0), the page metadata of every scan (folio numbers, headers, signatures, blank pages), and GloBERTise page embeddings. The embeddings cover 95% of the scans; nearly all scans without one are blank.
* As ground truth, the 22 inventories segmented by hand, published as the [*GLOBALISE – VOC Document Segmentation Dataset*](https://doi.org/10.34894/XAJ12C): documents, parts, documents sharing a scan, and the types of non-document pages.

**Method.**

1. **Scan features.** Predictors describe every scan:
   * opening and closing formulas in the text, and a closing followed by a new opening on the same page;
   * how well the text matches an index entry's description;
   * blank pages, text length, and text that recurs on nearby scans (such as a small sheet scanned on top of a larger page);
   * position in the inventory and signature marks;
   * page and folio numbers, cleaned of misreadings, stamps and restarts of the numbering;
   * running headers and header dates, language changes and marginalia;
   * page layout from the PageXML: where text starts and stops, gaps, headings and catch-words;
   * GloBERTise page embeddings: kNN start scores, similarity with the neighbouring scans, and linear probes for first, last and non-document pages.
2. **Scan models.** Four logistic regressions turn the features into scores per scan. Each answers one question:
   * **start:** does a document, or a part of one, begin on this scan?
   * **end:** does a document end on this scan?
   * **same scan:** given that a document starts here, does the previous one end on this same scan? This is typical of copy-books, in which one letter ends halfway down a page and the next copy begins below it.
   * **non-document:** is the scan a cover, blank page, table of contents, title page or other page outside the documents?

   Each regression combines 72 features of the scan itself with the same features of its neighbours, because a boundary is often recognised by what lies next to it. For example, a start is likely after a scan that ends with a closing formula, or is followed by a blank page. The weights were fitted on the 22 hand-segmented inventories. A missing feature, such as the layout of a scan without PageXML, counts as neutral.

   The result is a score per scan for each question, expressed as log-odds: 0 means a 50% chance, +2 about 88%, and −2 about 12%. Among the strongest signals are:
   * for a start: text beginning at the very top of the page, and text that differs from that of the previous scan (measured with the embeddings);
   * for an end: the page numbering starting again on the next scan;
   * for both: being near the start or end of the inventory, where covers and indexes are bound.

   On their own, these scores treat each scan separately. A **length prior** adds how plausible a document of a given length is, learned from the documents in the hand-segmented inventories (most are short: half have three scans or fewer). It discourages, for example, splitting a long letter into many short pieces on weak evidence.
3. **Index alignment.** The index lists the documents of a volume in the order in which they are bound, so their start scans must follow that order: the alignment is *monotone*. It works in two steps.

   First, for every entry, the model lists up to 20 candidate start scans, each with a score:
   * **exact:** a scan whose page or folio number equals the entry's start folio, with a correction for entries starting on the verso of a leaf;
   * **interpolated:** scans near the position estimated from the nearest numbered pages, scoring less the further they are from it (the number of scans per folio is estimated per volume, as it differs between paginated and foliated volumes and between single and double scans);
   * **text:** scans whose opening words match the entry's description;
   * **register:** for registers of papers, pages recognised by the entries they list.

   Each candidate's score also includes the scan's start score from the scan models, and whether the date in the running header agrees with the entry's date.

   Second, the model chooses one candidate for each entry so that the entries never go backwards in the volume and the total score is highest. Choosing each entry's best candidate on its own would let a single misread folio number pull an entry far out of place. Instead, the total also scores each pair of consecutive entries:
   * **span:** how well the number of scans between them fits the number of folios that the index gives the first one;
   * **shared scan:** a cost when both start on the same scan (a letter and its enclosures can, but this costs more the further apart their folios are in the index, and is ruled out after an entry that covers more than one folio);
   * **skipped entry:** a cost for every entry left without a place, so that entries are only skipped when no candidate fits.

   Trying all combinations would be impossible for volumes with hundreds of entries. A *dynamic programme* finds the best one efficiently: it works through the entries in order and keeps, for every candidate of the current entry, only the best placement of the entries before it.

   Entries without a usable candidate are then placed between their placed neighbours, on the strongest start evidence, drawn towards the position their own folio implies. Titles that announce a number of documents (*Vier brieven van Ternaten ...*; 6.6% of the index titles) make the model look for that many parts: it finds 71% of the starts inside such entries, against 57% without this.
4. **Segmentation.** A second dynamic programme divides the whole volume into documents and stretches of non-document scans. Of all possible divisions, it chooses the one with the highest total score. The total adds up:
   * for every document, the start score of its first scan, the end score of its last scan and the length prior;
   * for every boundary, the same-scan score: the next document starts on the same scan, on the next scan, or after non-document scans;
   * for every scan outside the documents, the non-document score.

   The placed index entries are fixed starts, a document never starts on a blank scan, and only blank scans (or scans that mostly repeat text from nearby scans) may lie outside documents.

   Because the whole division is scored at once, a single strong signal is not always enough for a boundary. In one case, a scan had a start probability of 79% (+1.32), but the previous scan had an end probability of only 54% (+0.17). Splitting the 32-scan document there into documents of 12 and 20 scans cost 1.91 in the length prior, so the split lost by 0.42 and was not made.

   Documents are then labelled as index entries, court cases, unindexed documents, or parts. A part is a document that falls within the page range of the preceding index entry, such as an enclosure or appendix. Index entries are never parts of each other. Title pages lie outside documents, as in the hand-segmented inventories.

**Evaluation.** The model was cross-validated on the 22 hand-segmented inventories, which hold 2,532 document starts: each inventory was scored with a model fitted on the other 21, including the embedding probes. The *Generale Missiven* (920 letters in 545 inventories) were used for evaluation only, and scored by the model fitted on all 22 inventories. With an exact scan match (±1 scan in brackets):

| | With index | Without index |
| --- | --- | --- |
| Top-level starts, F1 | 80.6 (91.3) | 53.0 (66.0) |
| All starts, including parts, F1 | 69.2 (78.2) | 53.4 (64.0) |
| All ends, F1 | 63.6 (77.1) | 52.2 (63.8) |
| End correct, given a correct start | 66.8% (80.6%) | 58.3% (70.6%) |
| Same-scan boundaries, F1 | 89.3 | 90.0 |
| Non-document scans, F1 | 69.2 | 67.9 |
| *Generale Missiven*: starts found | 88.9% (94.0%) | 64.9% (70.4%) |
| *Generale Missiven*: false starts per 100 scans | 0.14 | 0.15 |

* **Index entries placed on the right scan.** 79.4% in the hand-segmented inventories (91.2% within one scan), and 76.3% in the *Generale Missiven* (81.9%).
* **Baseline.** For comparison, a baseline that splits on blank pages and signatures finds 71.7% of the starts of the *Generale Missiven*, with 0.35 false starts per 100 scans.
* **Parts without an index.** In the hand-segmented inventories, some documents are parts of others, such as enclosures. Without an index, the model has no way to tell this, so when it correctly finds where an enclosure begins, it reports that as the start of an ordinary document. Strictly, the top-level score would count such a start as a false start, although the start itself is right. These starts (373) are therefore not counted in the top-level score without an index. Counted as errors, the F1 score would be 47.0 instead of 53.0.
* **Title pages.** The model still starts a document on its title page in about one in five cases.
* **Choice of test set.** The *Generale Missiven* are much longer than most documents (median 49 scans, against a median of 3 in the hand-segmented inventories and in the archive as a whole), so they mainly test long documents. Models were therefore chosen on the hand-segmented inventories.

**Titles, dates and types.**

* **Who made the title.** Every document records the source of its title (`title_source`): `VOC` (an index entry, or a *Generale Missive* identified by hand), `Resilient Diversity` (court cases) or `inferred`. Titles not given by the VOC are stored in square brackets.
* **Inferred titles** take the form *type, place, date*.
  * The type comes from a classifier on the opening of the first page and the end of the last page, trained on documents with an index entry. Cross-validated, it is right for 84% of the documents, and assigns a type to 78% of them at a confidence threshold of 0.5.
  * Place and date come from the closing formula on the last page or the page before, read with the Globalise entity annotations; failing that, from the last full date on the last page or the date in the running header.
  * Places are first matched to the **VOC gazetteer**: the Globalise dataset on the [organisational structure of the VOC](https://doi.org/10.34894/2VNEUG). It lists the Company's offices and establishments (247 in all, such as the *comptoir* of Surat or the government of Ambon), with their names and spelling variants, their place in the hierarchy of the Company and, by period, the place where they were located (as a GLOB identifier of the places dataset). The closing formula of a letter usually names such an office (*Gamron*, *Cochin*). A place is matched to an exact label of the gazetteer, then to an exact name or variant in the [Globalise places dataset](https://doi.org/10.34894/UFFFNO) (version 3.0), and finally to the closest gazetteer label, to allow for misreadings. It is shown as written, with the preferred label of the places dataset in brackets: *Batavia (Jakarta)*.

  <!-- TODO: the organisational structure dataset (https://doi.org/10.34894/2VNEUG) has not yet been published on DataverseNL; check the link once it has. -->
* **Dates of index entries.** Where the enriched index has no date, dates were parsed from the entry's description. On entries whose dates were known, the parser agreed with them for 97% of begin and end dates. Missing years of dates such as *dato 14 September* were inferred from the typescript's year and the neighbouring entries; with years hidden as a test, this was right in 99.3% of cases with a receipt date and 92.1% without.
* **Checks of dates after the segmentation.** Dates that lay more than two years outside the years of the inventory or typescript (1,499) were checked against evidence independent of the entry's description: the document's own text, the previous entry for *Dito* entries, and the years of the typescript and inventory. Of these, 1,194 were kept (mostly periods covered, or older acts the description names), 217 were corrected, 1 was cleared, and 87 were flagged and left alone. This changed the dates of 218 documents and of the index entries they took them from.
* **Cleaning of titles after the segmentation.** The titles from the typescripts were read by OCR. Their spacing and hyphenation were corrected (*Brie fje* → *Briefje*, *No-vember* → *November*) in 919 documents and the index entries they took them from; their wording was not changed. The segmentation itself read the uncorrected dates and titles, so its boundaries are not affected.
* **Identifiers.** Each document is linked to its Globalise document type (and, for index entries, the TANAP type), to its index identifiers (OBP, TANAP, typescript, and OBP NT, the Nationaal Archief's new detailed finding aid), and to the place as a GLOB identifier of the Globalise places dataset (`place_glob_id`). A few places of inferred titles are missing from the places dataset and have no GLOB identifier.
* **Evidence.** How the model found each document is stored with it as JSON evidence. This covers the index placement, the page numbers and dates read, the start and end probabilities, and their main reasons.

**Data, code and reproducibility.** Everything is in the deposit [*GLOBALISE – Document Segmentation of the VOC Archives*](https://doi.org/10.34894/P826UY):

* the results, with a codebook: the documents, their scans, the direct output of the segmentation, the inferred titles, and the records of the date and title corrections;
* the Digitized Indexes with each entry's start and end scan;
* the full evaluation output and its definitions;
* a description of the method, including the approaches that were tried and dropped;
* the code and the fitted model, the part of the documents database that the method reads, the transcriptions, the page layout, and the page embeddings or the features computed from them.

Run from the deposit and two published datasets on 6 November 2026, the code reproduced all 636,542 segments with identical boundaries, and the inferred titles and the evaluation exactly. Embeddings computed again from the sources differ slightly, so a segmentation from the sources is close to these results, but not identical.

**Credits.** The segmentation was made in the Globalise project by Lodewijk Petram, with Renate Smit (the ground truth of the hand-segmented inventories and the Globalise document classification), Kay Pepping (the digitisation of the typescripts, the ground truth of the *Generale Missiven*, and segmentation scripts), Leon van Wissen (segmentation scripts and the documents database), Brecht Nijman (segmentation scripts) and Marijn Koolen (the embedding pipeline).

<!-- TODO: the globalise-huygens/documents repository, linked in the table above, will not be kept. The scripts that export the IIIF collection and manifests are not in the deposit: decide where they will be kept, and update the link. -->

<!-- TODO: check where on the portal a user can find the source of a title (title_source) and the evidence of a document, and refer to it here. -->

<!-- Sources: README, METHODS and METRICS of the deposit (https://doi.org/10.34894/P826UY, draft of 6 November 2026), README of the documents repository (branch llm-definitive-doc), cross-validated evaluation of the final model (evaluate-20261105b.log, 5 November 2026), and its database, queried 2026-11-06. -->

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
