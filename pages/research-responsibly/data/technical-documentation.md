---
title: "Technical documentation"
subtitle: ""
summary: "Detailed documentation of models, tools, pipelines and technical decisions."
type: "page"
slug: "technical-documentation"
status: "draft"

authors: []
datePublished: ""
dateUpdated: "2026-11-23"

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

<!-- Sources: README of https://github.com/globalise-huygens/language-identification-data (data last regenerated 4 July 2025); README, Makefile and lexicons of the langdetect pipeline and scripts/gt_classify_language.py in https://github.com/knaw-huc/globalise-tools (retrieved 2026-11-12); counts computed from pages.lang.tsv, non-latin.scripts.tsv and corrections.lang.tsv on 2026-11-12; Arno Bosse, "The Languages of GLOBALISE" (archived blog post). -->

| Component | Description | Link |
| --- | --- | --- |
| Language identification data | Language(s) per page, lists of pages with a non-Dutch or unknown language (with their text), pages in non-Latin scripts, and manual corrections | <https://github.com/globalise-huygens/language-identification-data> |
| langdetect pipeline | Pipeline that produced the automatic identifications, part of globalise-tools | <https://github.com/knaw-huc/globalise-tools/tree/main/pipelines/langdetect> |
| lingua-cli | Command-line wrapper around [lingua-rs](https://github.com/pemistahl/lingua-rs), language detection with character n-gram models | <https://github.com/proycon/lingua-cli> |
| lexmatch | Language detection by lexicon lookup | <https://github.com/proycon/lexmatch> |

The language of each page was identified from its transcription, line by line. Only lines in **paragraph** regions were used. Text in other regions, such as marginal notes, headers, signatures, catchwords and page numbers, was set aside, because on most pages the paragraphs hold nearly all of the text.

**Two classifications per line.** Each line was classified in two ways, restricted to ten languages known to occur in the corpus: Dutch, English, French, German, Latin, Italian, Portuguese, Spanish, Danish and Malay in Latin script.

* **lingua** recognises a language from typical combinations of characters. It returns the most likely language and a confidence score. Its models were trained on modern texts; Malay was detected with its model for Indonesian.
* **lexmatch** looks up each word of at least three characters in a word list per language, and returns the share of the line's words found in each list. Dutch has two lists: one of historical Dutch derived from [ground truth transcriptions of VOC documents](https://zenodo.org/record/6414086), and one of modern Dutch. The Latin list contains the most common Latin words; the other lists contain the 10,000 most frequent words in that language in the OpenSubtitles 2018 corpus (via [FrequencyWords](https://github.com/hermitdave/FrequencyWords)). The [lexicons](https://github.com/knaw-huc/globalise-tools/tree/main/pipelines/langdetect/lexicons) are published with the pipeline.

**Reconciling the two.** The two results were combined with a fixed set of rules ([gt_classify_language.py](https://github.com/knaw-huc/globalise-tools/blob/main/scripts/gt_classify_language.py)), applied in this order:

1. A line with six letters or fewer is too short to classify and counts as unknown.
2. If the character model's language is among the best lexicon matches and its confidence is at least 0.5, the models agree and that language is assigned.
3. If the best lexicon match is Dutch with a score of at least 0.5, the line is Dutch, whatever the character model says. This keeps Dutch lines with many French or Latin loan words from being classified as French or Latin.
4. If the character model says Dutch and the lexicon score is at most 0.5, the line is Dutch.
5. A line consisting of a single word that is not Dutch counts as unknown, so that a name or a single foreign word does not make a line non-Dutch.
6. If the character model's confidence is at least 0.9 and higher than the lexicon score, its language is assigned.
7. If the lexicon score is at least 0.5 and at least as high as the character model's confidence, the best lexicon match is assigned.
8. Otherwise the line counts as unknown.

**From lines to pages.** For each paragraph region, a language was assigned if it accounts for at least a quarter of the region's lines, with lines classified as unknown included in the count. A language other than Dutch must in addition occur on at least three lines. The first rule allows a region to be assigned two languages, for example when it has Dutch and French in parallel columns. The second keeps short phrases from counting. A page receives every language assigned to any of its paragraph regions, and *unknown* if none was assigned. Languages are recorded as [ISO 639-3](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) codes.

**Non-Latin scripts and manual corrections.** The automatic method cannot identify languages in non-Latin scripts, because Loghi cannot read them. On such pages, Loghi produces Latin characters that look similar, such as digits, and otherwise falls back on rare letters and symbols, such as ꝝ, ȼ or ꝕ. The project searched the transcriptions for unusual combinations of such characters and leafed through volumes whose inventory descriptions mention documents in other languages. The pages found this way are listed in `non-latin.scripts.tsv` (186 pages, including 8 in cipher). A separate list, `corrections.lang.tsv`, contains 884 manual corrections and additions to the automatic identifications. Both are merged into the published `pages.lang.tsv`.

**Results.** `pages.lang.tsv` covers 4,498,686 pages in 6,914 inventory numbers.

| Language(s) of a page | Pages | Share |
| --- | ---: | ---: |
| Dutch only | 4,349,193 | 96.7% |
| Unknown | 136,427 | 3.0% |
| At least one language other than Dutch | 13,066 | 0.3% |

Pages with each language, alone or together with others: French 5,604; English 3,600; Latin 2,202; Portuguese 583; Malay (Latin and Arabic script) 507; Spanish 273; German 139; Sinhala 113; Danish 31; Chinese 20; Italian 18; Persian 8; Tamil 8; cipher 8; Japanese 6; Bengali 3; Gujarati 2; Buginese 2; Church Slavonic 2; Hebrew 1; Ancient Greek 1.

**Reliability.** The identifications have only been tested qualitatively; there is no quantitative evaluation. Arno Bosse checked a sample of scans by hand, and reviewed every scan listed in `non-latin.scripts.tsv` and `corrections.lang.tsv`. According to these checks, precision is very high: Dutch pages are rarely classified as non-Dutch, and non-Dutch pages are almost always assigned the right language. Recall is lower: some pages in other languages are classified as Dutch or unknown, for instance individual pages within a French document. Most unknown pages contain too little text, such as blank pages between documents; others are tables with mostly numbers, or pages bound upside down or sideways. The list of non-Latin-script pages is not exhaustive. Because any threshold for mixed-language pages is a choice, `nondutch-pages.lang.tsv` and `unknown-pages.lang.tsv` include the text of the paragraph regions and a link to each page, so that researchers can apply their own criteria.

**Credits.** Bram Buitendijk, Maarten van Gompel and Arno Bosse (KNAW Humanities Cluster).

<!-- TODO: the identifications were made on the PageXML of the earlier transcriptions (last regenerated 4 July 2025, "after receiving new pagexml data"). Check whether they match the transcriptions on the portal (annotation pages generated September 2026), and whether the pipeline will be run again. Also explain why pages.lang.tsv covers 4,498,686 pages while the corpus has about 4.8 million scans. -->

<!-- TODO: state whether and how the portal shows the language of a page and allows filtering by language, and whether the language data will be deposited on DataverseNL. -->

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

## Machine translation

<!-- Sources: README, prompt (prompts/translate_collection.md), scripts (translate_collection.py, page_filters.py, pagexml_text.py, running_headers.py, term_matcher.py, place_matcher.py, page_shift.py) and run reports of https://github.com/globalise-huygens/globalise-translation-experiments (retrieved 2026-11-23); curated-translations/matches.csv in the same repository. -->

<!-- TODO: the translation-experiments repository may not remain available. Replace the links to it with a permanent location for the translations, the code, the prompt and the glossary files (e.g. DataverseNL or Zenodo), and add the dataset to the table below. -->

<!-- TODO: add the figures for the final run (date, scans translated, skipped, retried, overlaid by redo runs) and confirm the settings used for it (effort, thinking). -->

| Component | Description | Link |
| --- | --- | --- |
| Claude Haiku 5.5 | Large language model (Anthropic) used for the translation; thinking off, effort `high`, requests sent through the Message Batches API | <https://www.anthropic.com/claude> |
| Translation pipeline | Scripts that prepare the text, glossary and requests, and check and collect the results | <https://github.com/globalise-huygens/globalise-translation-experiments> |
| Translation prompt | The instructions given to the model | [`prompts/translate_collection.md`](https://github.com/globalise-huygens/globalise-translation-experiments/blob/main/prompts/translate_collection.md) |

**Units of translation.** Each inventory was translated as one continuous sequence of scans, in requests of up to 40,000 characters (about 20 scans). A request is closed where a document begins once it is half full, so the model sees whole letters and resolutions where possible. Each request carries the end of the previous page as context (not translated), marks where documents begin (with their titles, from the [document segmentation](#document-identification)) and the language of scans that are not (only) Dutch (from the [language identification](#language-identification)). The model returns one translation per scan.

**Page text.** The text was rebuilt from the PageXML rather than taken from the normalised page text, in which the lines of a marginal note are often sorted into the paragraph next to it, so that notes end up in the middle of a sentence. Per page, lines that share a left and right edge form columns; the column with the most text is the main block, and lines beside it form margin notes, which are sent after the main text of the scan. Double scans are split at the gutter. Page numbers, catchwords and signature marks are left out, and words hyphenated over a line break are joined. This was checked on two random samples of 300 inventories (1,500 scans each): margin notes on prose pages come out right; complex layouts, such as two-column registers and accounts, are the weak spot.

**Running headers.** Copy books repeat the source and date of a letter at the top of every page ("Van Siam onder den 8=e Januarij 1704:"). Such headers were removed before translation: a short line counts as a header when a nearly identical line (allowing for transcription errors) occurs on one of the three scans before or after it. In a sample of 400 inventories (275,000 scans), 25–30% of the scans had one. In the test set described below, about 94% of the copy-book headers were removed.

**Page filters.** Only pages without usable text were skipped: blank pages (fewer than 20 characters) and pages of garbled text (of the words, fewer than 25% have four or more letters, and fewer than 10 such words in all). In two test inventories, 37 of 385 (VOC 3773) and 127 of 1,112 scans (VOC 3598) were skipped, nearly all blank. Pages that the model could only render as *[illegible]* were marked as skipped too. Tables, accounts and lists were translated: headings, labels and entries are translated, bare columns of figures are not.

**Glossary.** In each request, words whose meaning in the VOC and Asian context may not be obvious are marked, and explained in a glossary with their Dutch and English label and a short definition. The terms come from:

* the [Globalise thesaurus](/pages/research-responsibly/data/reference-data.md), matched against the page text with fuzzy matching that allows for spelling variants, inflection and transcription errors: all ethnic, religious and caste categories, and the unfamiliar terms among commodities, ship types, occupations, units of measure and financial terms;
* the entity annotations that link a word to the thesaurus, which add spellings the matcher misses (47.0 million linked annotations in 6,913 inventories, 41.9 million of them to 1,709 distinct concepts; export of 16 November 2026);
* lists reviewed by the project: which concepts to explain, corrections of English labels and definitions, links that are often wrong, and terms the thesaurus lacks.

Place names are matched against the [Globalise places dataset](/pages/research-responsibly/data/reference-data.md). A capitalised spelling variant of a known place is glossed with its standard name: the spelling the VOC corpus uses most, not the modern name. Forts, buildings, Dutch town names (in the corpus mostly ship names) and names shared by different places are not used. Person names are never normalised.

**Output and checks.** For each scan, the model returns the first five words of the scan's transcription (`begins`) and the English (`english`). The pipeline checks that every scan is present and that the `begins` anchor fits this page rather than another page in the request. A second check compares the words that survive translation unchanged (numbers, names, terms kept in the source's spelling) with the transcription of the scan and of the two pages on either side, to find English that belongs to a neighbouring page (a "shift") or that runs on into the next page (an "overlap"). Scans that fail a check are translated again, if necessary on their own, with the English of the neighbouring pages given for orientation only.

The output is one English text per scan, with the model and the time of translation.

### Evaluation of the translations

There are no quantitative measures of translation quality. The project compared the translations with published translations made by historians, from two volumes in the *Harta Karun* series of the Arsip Nasional Republik Indonesia (ANRI) and the Corts Foundation, which give the Dutch text and an English translation of letters from Asian rulers to the High Government in Batavia:

* Hendrik E. Niemeijer et al., *The Diplomatic Correspondence between Asian Rulers and Batavia Castle during the 17th and 18th centuries: The Digital Reconstruction of a Lost Treasure* (Arsip Nasional Republik Indonesia (ANRI) & The Corts Foundation, 2015): three letters, from the Susuhunan of Mataram, the Sultan of Maguindanao and the King of Bone (1697–1700);
* Hendrik E. Niemeijer et al., *The Diplomatic Correspondence between The Kingdom of Siam and The Castle of Batavia during the 17th and 18th centuries* (Arsip Nasional Republik Indonesia (ANRI) & The Corts Foundation, 2016): eight letters from the kings of Siam and their Phrakhlang (1668–1769).

Copies of these eleven letters were found in fourteen places in the Globalise collection, together 195 scans. Several of the Siam letters are given in modernised spelling in the publication, which makes a word-by-word comparison with the transcription harder.

<!-- TODO: add links to the two Harta Karun volumes. -->

The machine translations are somewhat weaker than the published ones. The model fails on some difficult syntax, and it lacks the context the historians had, so some names of places and people are wrong; this is mostly a consequence of errors in the transcription. On the other hand, the machine translation is more literal and follows the original closely, which makes it easier to compare with the scan.

The check for English under the wrong page flagged between 2.4% and 10.0% of the scans in the test runs, and between 2.4% and 5.1% in the runs on the diplomatic letters. Of 30 flagged scans checked by hand, about nine in ten were real shifts or overlaps. Flagged scans were translated again, but the check does not find every case.

## Publishing annotations

The transcriptions, entities and events are converted into W3C Web Annotations with scripts in the [globalise-tools](https://github.com/knaw-huc/globalise-tools) repository of the KNAW Humanities Cluster. The annotation pages on the portal record the exact version of the script used. See [Data model & ontologies](/pages/research-responsibly/data/data-model.md).

<!-- TODO: describe how the translations are published (e.g. as Web Annotations per scan, like the transcriptions) and with which script, once this is decided. -->

## Query expansion

<!-- Sources: Kweepeer README, PLAN.md and man pages kweepeer(1) and kweepeer(5) (https://github.com/knaw-huc/kweepeer, retrieved 2026-11-13); issue globalise-huygens/glob-portal-infomodel#97; module list and responses of https://kweepeer.globalise.nl, retrieved 2026-11-13. -->

| Component | Description | Link |
| --- | --- | --- |
| Kweepeer | Interactive query expansion service (KNAW Humanities Cluster), written in Rust; licence AGPL-3.0 | <https://github.com/knaw-huc/kweepeer> |
| Kweepeer service for Globalise | The instance used by the portal | <https://kweepeer.globalise.nl> |
| INT Historisch Lexicon | Historical spellings and word forms of Dutch words (Instituut voor de Nederlandse Taal) | <https://ivdnt.org/> |
| Globalise word embeddings | Word embeddings trained on the transcriptions of the VOC archives | <!-- TODO: add link --> |

<!-- TODO: confirm which embeddings model the service uses (possibly derived from the GLOBALISE Word2vec Experiment, https://doi.org/10.5281/zenodo.15038313), how it was trained and on which version of the transcriptions, and add a link. -->

To help researchers deal with the spelling variation in the archive, the portal expands the words in a search with other spellings and word forms. The suggestions come from **Kweepeer** (from *kweepeer*, Dutch for quince), a query expansion service developed for Globalise by Maarten van Gompel at the KNAW Humanities Cluster. How users work with the expansions is described under [Searching](/pages/learn-get-started/searching-browsing/searching.md#spelling-variants-and-query-expansion).

**How it works.** The portal sends the words of a search to Kweepeer as a query in Lucene syntax. Kweepeer parses the query, looks up each word in its expansion modules, and returns the suggestions per word and per module, together with a template of the query in which each word can be replaced by its expansions. Kweepeer does not search the index itself. The portal shows the suggestions to the user, builds the final query from the original words and the expansions the user keeps, and sends it to the search index. Each word is replaced by a disjunction of the word and its expansions (an *OR* query), so that the structure of the original query, such as *AND* between words, is kept. Words that refer to entities from the reference data, chosen from the suggestions while typing, are not sent to Kweepeer.

**Modules.** Kweepeer can combine several kinds of expansion: lookup in lists of variants, spelling variants within a given edit distance, anagram hashing with [analiticcl](https://github.com/proycon/analiticcl), and semantic similarity with word embeddings. Several of these were tested during development. The project chose the two modules that gave the most relevant results for the VOC archives, and only these are enabled in the service the portal uses:

* **INT Historisch Lexicon** (`inthislex`, a lookup module). A list of Dutch words with the historical spellings and inflected forms in which they occur, compiled by the Instituut voor de Nederlandse Taal. The module returns every form listed for a word, which can be more than twenty (for example 21 for *nagel*), and nothing for words that are not in the lexicon. It was used earlier in Nederlab and Golden Agents; INT gave permission for its use in Globalise.
* **Globalise word embeddings** (`embeddings`, a finalfusion module). A model of word vectors trained on the transcriptions of the VOC archives. For each word, the module returns the ten words whose vectors are closest to it, with their similarity scores. The number is a setting of the service (`k = 10`, the default). Because the model was trained on the automatic transcriptions, its nearest neighbours include spelling variants that occur in the archive, transcription errors, case variants and words with punctuation attached, but also words that occur in similar contexts without meaning the same, such as *buskruidt* (gunpowder) for *kruidnagel* (clove).

<!-- TODO: add the credit for the INT Historisch Lexicon in the wording agreed with INT, and its exact name, version and link. -->

**Control by the user.** Because both modules can suggest unwanted forms, the expansions are not applied silently. The user can switch expansion on and off for each word, for each module, and for each expanded form.

**Credits.** Maarten van Gompel (Digital Infrastructure department, KNAW Humanities Cluster) and Robert Goené (Clean Code).

<!-- TODO: add the people who integrated Kweepeer into the portal. -->

## The portal

| Component | Description | Link |
| --- | --- | --- |
| Globalise research portal | Source code of the portal | <https://github.com/globalise-huygens/globalise-research-portal> |
| Kweepeer | Query expansion service. See [Query expansion](#query-expansion) | <https://github.com/knaw-huc/kweepeer> |
| Globalise MCP server | Model Context Protocol server that gives AI assistants read-only access to the search indices and persistent data | <https://github.com/globalise-huygens/globalise-mcp> |

The MCP server is designed to run as a separate service next to the portal, so that heavy use by AI assistants does not slow down the portal itself. It queries the same search indices. To limit the load on them, it caches responses for 15 minutes, limits the number of simultaneous requests, applies timeouts and caps the size of result sets, and limits each client to 60 requests per minute. See [Accessing the data](/pages/research-responsibly/data/access.md#mcp-server).

<!-- TODO: add a short description of the portal's technical architecture (search index, hosting) once final. -->
