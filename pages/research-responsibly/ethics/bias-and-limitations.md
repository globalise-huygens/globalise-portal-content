---
title: "Bias & limitations"
subtitle: ""
summary: "An explanation of archival, computational and interpretive biases and limitations in Globalise."
type: "page"
slug: "bias-and-limitations"
status: "draft"

authors: []
datePublished: ""
dateUpdated: "2026-11-24"

featured: false

hero:
  src: ""
  alt: ""
  caption: ""
  credit: ""
  source: ""
  licence: ""

related: ["colonial-context", "responsible-use", "methods", "voc-archives-guide"]
---

# Bias & limitations

<!-- Sources: pages/research-responsibly/voc-archives-guide.md; "Mission, Research Themes and Guiding Questions" v1.0 (pages/about/archive/mission-research-themes.md); Globalise Ethics Policy v2.0 and its ethics reports on Primary Sources and the Places Dataset (pages/research-responsibly/ethics/policy.md); Arno Bosse, "The Languages of GLOBALISE" (pages/about/archive/blog/the-languages-of-globalise.md). Limitations of the VOC archives themselves are covered in the VOC archives guide; this page links to it rather than repeating it. -->

<!-- TODO: this page depends on the final models and data (dependency "Final models" in CONTENT.md). Check all statements against the final state of the portal before publication. -->

Everything on this portal is shaped by choices and limitations: those of the people who created the archive centuries ago, those of the archivists who organised it, and those of the Globalise project, which selected, transcribed, annotated and linked it. This page explains the most important ones, so that you can take them into account when you use the portal.

Neutrality is not attainable. The aim of this page is not to excuse these limitations, but to make them visible.

## The archive

The limitations of the VOC archives themselves carry over to everything on this portal. The [guide to the VOC archives](/pages/research-responsibly/voc-archives-guide.md#what-do-you-need-to-be-aware-of-when-using-historical-archives-like-the-records-of-the-voc) explains them:

* the documents record events, people and societies as the Dutch East India Company (VOC) saw them, and people outside the company mostly appear when they mattered to it (see also [Colonial context](/pages/research-responsibly/ethics/colonial-context.md));
* most of the archives kept at the company's settlements have been lost (see [How was the Company's network of correspondence organized?](/pages/research-responsibly/voc-archives-guide.md#how-was-the-companys-network-of-correspondence-organized));
* written, digitised and transcribed sources such as these are easily given more weight than other ways of recording the past, and than other archives from the Indian Ocean world. By making the VOC archives easier to search, Globalise adds to this risk.

## What Globalise covers

### Part of the VOC archives

Globalise does not cover all VOC archives, nor even all of the VOC archive at the Nationaal Archief (Dutch National Archives). The Globalise project worked with the *Overgekomen Brieven en Papieren* (OBP; in English the Copied Letters series) in series 1.04.02: about 6,900 inventory numbers and about 4.8 million pages, dating roughly from 1605 to 1794. Among other things, the resolutions of the company's directors, the correspondence sent from the Dutch Republic to Asia, and VOC archives held elsewhere in the world are not included. The guide lists [what Globalise covers](/pages/research-responsibly/voc-archives-guide.md#how-much-of-the-10402-series-of-the-voc-archives-did-the-globalise-project-cover) and [what it does not](/pages/research-responsibly/voc-archives-guide.md#what-sections-in-the-10402-series-of-the-voc-archives-did-the-globalise-project-not-cover).

### Incomplete inventories

A few inventory numbers are not complete in Globalise, because not all of their scans are available online from the Nationaal Archief. Inventories 1212, 1286 and 1310 begin at scan 993: the first 992 scans of each are missing, and with them their transcriptions, annotations and translations. The Globalise project has reported this issue to the Nationaal Archief. The original volumes are held by the Nationaal Archief; for the missing pages, contact the Nationaal Archief.

### Languages and scripts

<!-- Sources for this section: README of https://github.com/globalise-huygens/language-identification-data and counts computed from its pages.lang.tsv (data of 4 July 2025, retrieved 2026-11-12); the langdetect pipeline in https://github.com/knaw-huc/globalise-tools. -->

Almost 97% of the pages in the Globalise corpus (about 4.35 million pages) are written in Dutch only. About 13,000 pages contain another language, often alongside Dutch. Most of these are in other European languages, especially French, English and Latin, and to a lesser extent Portuguese, Spanish and German. Several hundred contain an Asian language, mostly Malay and Sinhala, and a handful in, for example, Chinese, Persian, Tamil, Japanese, Bengali, Gujarati or Buginese. These numbers reflect what the archive kept and what the project could identify, not the languages actually spoken and written in the places where the VOC was active.

The text recognition software used by the Globalise project cannot read non-Latin scripts. Pages written in, for example, Chinese, Persian or Sinhala are turned into strings of seemingly random characters and cannot be searched for their content. These pages could only be found by hand, and the list of them is certainly incomplete.

The language of each page was identified automatically (see [How the data was produced](/pages/research-responsibly/data/production.md#identifying-languages)). Keep the following in mind:

* The tools used were designed for modern languages, and early modern spelling and text recognition errors make their task harder. Malay, for instance, was detected with a model for modern Indonesian.
* The method was set up to be cautious. A page in another language is more often classified as Dutch or unknown than a Dutch page as another language. The number of non-Dutch pages is therefore an underestimate.
* A language is recorded only if it occurs on a substantial share of a page's lines. A name, a phrase or a few lines in another language are not recorded, and neither are marginal notes. When a page mixes languages, deciding which of them it is "in" is always a choice.
* For about 3% of pages (some 136,000), no language could be identified. Most are blank pages, tables or pages bound upside down or sideways, but pages in languages the method does not cover can also end up here.
* Languages were identified per page, not per document.

The lists of pages with a non-Dutch or unknown language, including their text, are published, so that you can apply your own criteria. See the [Technical documentation](/pages/research-responsibly/data/technical-documentation.md#language-identification) and [The Languages of GLOBALISE](/pages/about/archive/blog/the-languages-of-globalise.md).

## Computational processing

### Text recognition

All transcriptions on the portal were produced automatically using handwritten text recognition. They contain errors. A word that was misread cannot be found by searching for its correct spelling, and errors carry through to every later step.

### Evaluation of text recognition

Content to be developed.

<!-- TODO: add plain-language results of the HTR evaluation (e.g. character error rate), including any known differences in quality between periods, regions, hands or document types. See also the related TODO on pages/about/methods.md. -->

### Documents and their titles

The archive's volumes were not originally divided into documents in a way a computer can read. The Globalise project reconstructed the documents with a segmentation model, guided by historical indexes where these exist. Where a document begins and ends, and the titles of documents not listed in an index, are therefore model output.

The model is markedly less reliable in volumes without an index. These are mostly volumes of the Zeeland Chamber (inventory numbers 9180–10405 and 10436–11024), which neither the TANAP project nor the Nationaal Archief's typescripts describe. In these volumes, enclosures appear as documents of their own.

Titles in square brackets were not given by the VOC. Those made by the project give no more than the type, place and date of a document.

Titles without brackets come from the existing indexes, which follow the VOC's own tables of contents. They are not neutral descriptions. They reflect the Company's perspective: what it considered a document to be about, whom it named and whom it left unnamed, and which papers it grouped together under one entry. A single entry can cover a letter together with the reports, lists, petitions or translations sent with it. By identifying such parts as documents of their own, the Globalise project aimed to make visible what the VOC grouped together, although parts carry only an inferred title.

Document metadata can contain errors. A document may begin or end on the wrong scan, two documents may have been merged into one or one split into two, and an inferred title or date may be wrong, for instance because the closing formula was misread or does not give the place where the document was written. Research that relies on document metadata, for example by counting documents per type, place or year, should therefore look critically at these aspects, and check the scans where the outcome depends on them. See [How the data was produced](/pages/research-responsibly/data/production.md#3-identifying-documents).

### Entities and events

Given the size of the archive, the Globalise project relied on machine learning to recognise entities (such as people, places and polities) and events in the text. Only part of these annotations could be checked by hand. Annotations on the portal are therefore model output: they can be wrong, incomplete or inconsistent, and they should not be treated as established facts.

### Evaluation of entity and event recognition

Content to be developed.

<!-- TODO: add plain-language results of the evaluation of the entity and event recognition models, and describe what kinds of errors are most common. -->

### Translation

The English translations on the portal were made by a large language model, Claude Haiku 5.5, and have not been checked by people. They are a help for reading and finding your way in the archive, not a substitute for the original.

**A translation reads more confidently than the original.** The transcription of a page is often noisy: misread letters, abbreviations, broken words, notes in the margin running through the text. The translation turns this into fluent, grammatical English. That fluency is not a sign of reliability. Where the model could not make sense of the transcription, it does not always say so: it may smooth over a passage, choose one reading of an ambiguous sentence, or produce a plausible sentence that is not what the document says. If you use a piece of information from a translation, check it against the scan. If you cannot read the original, look at least at whether the names, numbers and dates in the translation can be found in the transcription.

What to watch out for in particular:

* **Errors in the transcription carry through.** A misread word becomes a mistranslated word. Names of people and ships are kept as transcribed, misreadings included. Place names are standardised where the model was confident which place is meant, with the transcribed spelling in square brackets, but the identification can be wrong.
* **Difficult syntax.** Early modern Dutch letters and resolutions contain long sentences with chains of conditions, double negations and the verb at the very end. The model was instructed to keep this structure, but it sometimes misses it, and then who did what to whom can come out wrong.
* **Notes in the margin.** Margin notes were separated from the running text automatically before translation, and are given at the end of the page's translation. Notes that only repeat the running text were left out. The separation does not always succeed, especially on pages with tables, registers or several columns: a note can still end up in the middle of a sentence, or part of the main text can be treated as a note.
* **Page boundaries.** Each page has its own translation, but sentences and documents run on from one page to the next. Where a sentence crosses a page break, part of it can be translated on the wrong page, and occasionally the translation under a page belongs to the page before or after it. The project checked for this automatically and translated such pages again, but the check does not catch every case. If a translation does not seem to match its page, look at the pages around it.
* **What is left out.** Page numbers, catchwords and headers that are repeated on every page were removed, and so were margin notes that repeat the running text. Columns of figures are replaced by *[no translation available for table contents]*. Blank pages and pages whose transcription is unreadable were not translated, nor were pages in non-Latin scripts.
* **Words for people.** Categories of people, such as *Moor*, *inlander* or *heiden*, are translated literally, in their period meaning, without comment. Words for enslaved people are translated as "enslaved person" or "enslaved people". The model received a short explanation of such terms from the Globalise thesaurus, but it can still choose the wrong meaning. See [Colonial context](/pages/research-responsibly/ethics/colonial-context.md).
* **Context the model does not have.** The model translated about 20 pages at a time. It does not know what was written in other volumes, or what historians know about the people and events involved.

Unlike the models for entity and event recognition (see [Bias in models](#bias-in-models)), the translation model was not trained by the project. It is a general-purpose commercial model, trained on large amounts of text from the internet and other sources. Its biases cannot be traced back to the archive, and it may bring modern assumptions and phrasing into its translations.

<!-- TODO: once the translations are searchable on the portal (if they will be), add that a search in English finds only what the model translated, and that an English search term can miss a passage that was translated differently. -->

### Evaluation of translation

There are no quantitative measures of the quality of the translations. The project compared them with published translations by historians of eleven diplomatic letters from Asian rulers, among them the kings of Siam, to the VOC government in Batavia (1668–1769), from the *Harta Karun* series of the Arsip Nasional Republik Indonesia and the Corts Foundation. The machine translations were somewhat weaker: the model failed on some difficult syntax, and it lacked the context the historians had, so that some names of places and people came out wrong, mostly because of errors in the transcription. On the other hand, the machine translations are more literal and follow the original more closely, which makes them easier to check against the scan. See the [Technical documentation](/pages/research-responsibly/data/technical-documentation.md#evaluation-of-the-translations).

### Bias in models

Models learn from the examples they are trained on. Where some kinds of text, names or people are under-represented in those examples, the models tend to recognise them less well. The project's [ethics policy](/pages/research-responsibly/ethics/policy.md) therefore asked for careful selection of training and test data by people with relevant historical expertise, and for attention to discriminatory or biased output.

Even taking these biases into account during task design and manual labelling, the training datasets still contain a skewed representation of categories. For example, events related to violence are much less prevalent in the training data than events related to transport. Where possible, this imbalance has been mitigated by adopting methods that promote the automatic recognition of infrequent categories (see the project's documentation on event classification).

Apart from the (mitigated) bias in the data we labelled by hand, the archives themselves undeniably contain colonial biases that models pre-trained on the language contained within them will adopt. This is a bias that is not only hard to battle but also one that is informative, it being an accurate reflection of the culture of the VOC. We decided to use a completely self-trained Language Model as the basis for our event and entity recognition pipelines. Importantly, this means that we can trace back any biases present in the models caused by the data to the archives themselves. If we were to have used available open source foundational models as our basis, which are trained on text data from the internet's public domain, any bias present in our adapted versions of them would have been obscure, as there is no way to trace which bias comes from which parts of the training data. In other words, we do not deny the presence of bias in our models, more so, we encourage people to study it. 

Content to be developed.

<!-- TODO: add a plain-language description of where bias in the models is likely and what it may mean for users: for example which hands, periods, regions, languages and document types were under-represented in the training data of the text recognition, segmentation and entity and event recognition models, and whether names of non-Europeans, women or enslaved people are likely to be recognised less well. A quantitative analysis of bias is not feasible; this section describes possible bias, not measured bias. -->

## Reference data

Reference data and thesauri, such as the datasets on polities, places, people and commodities, were compiled and checked by historians. They are curated, but they are not neutral. They reflect the knowledge, perspectives and expertise of the project team and contributors, and the sources and literature they were built from. Because these are mostly colonial sources in Dutch and English, colonial names and categories are recorded more fully than local ones. The limitations of each dataset are summarised on the [Reference data](/pages/research-responsibly/data/reference-data.md#what-all-reference-datasets-have-in-common) page, and the choice of place names under [Which name is shown](/pages/research-responsibly/data/reference-data.md#which-name-is-shown-preferred-labels).

Even when a dataset is well documented, it can be hard for users to see why a particular value was chosen for a particular entry.

### Thematic choices

The project could not create reference data for every subject in the archive. It prioritised political and economic subjects, which appear most often in the sources, while drawing attention to lesser-known Asian polities and to the activities of non-European actors. In 2024, the social domain was next in line, after which the project planned to explore the environmental and cultural domains. Any such selection is subjective. See [Mission, Research Themes and Guiding Questions](/pages/about/archive/mission-research-themes.md).

<!-- TODO: update with the final coverage of reference data per domain. The 2024 mission statement says datasets existed or were in preparation for polities, commodities, units of measurement, locations and persons, with the social domain next. -->

## Searching and interpreting

### The infrastructure shapes what you find

An infrastructure that makes an archive easier to search also influences what people search for, what they find, which histories are written and which topics enter public debate.

### Results are snippets

Advanced search makes it possible to extract small pieces of information from millions of pages. These are representations of historical realities, shaped by the context of the document they come from: its type, its author and its purpose. The archive does not offer unfiltered historical truths, but fragmented observations and interpretations.

Searches on the portal can tell you what was recorded, where and when. Explaining how and why things happened remains the task of the researcher. See [Responsible use](/pages/research-responsibly/ethics/responsible-use.md).

### Query expansion

The portal expands the words in a search with other spellings and word forms (see [Searching](/pages/learn-get-started/searching-browsing/searching.md#spelling-variants-and-query-expansion)). This helps to find passages that use spellings you did not think of, but it has limits:

* The expansions from word embeddings include words that occur in similar contexts without meaning the same. A search for *kruidnagel* (clove) is expanded with *buskruidt* (gunpowder), for example. Such expansions add irrelevant results, and can inflate counts.
* The INT Historical Lexicon covers general historical Dutch. It has no forms for many words that are specific to the VOC archives, and none for words in other languages, including the many words from Asian languages that appear in the documents.
* Neither source finds every spelling or every misreading in the transcriptions. A search that finds nothing, even with expansion, does not prove that something is not in the archive.

Because results depend on which expansions are switched on, note them when you report search results or counts.

### Searching with an AI assistant

An AI assistant connected to the [Globalise MCP server](/pages/learn-get-started/ai-assistant.md) works with the same data and inherits all the limitations described on this page. It adds limitations of its own. It decides which searches to run and which results to read, and it may stop before it has found everything. It can misread or misquote a transcription, overstate what the sources say, fill gaps with knowledge from its training, and occasionally invent quotations or sources, all in fluent and confident language. The translations and summaries it makes itself have not been checked, and are not the same as the [translations](#translation) shown in the viewer. The server gives the assistant background on the limitations of the data, with links to this page, but whether the assistant passes them on to you depends on the assistant.

## Known issues

* Inventories 1212, 1286 and 1310 are incomplete: their first 992 scans are not available. See [Incomplete inventories](#incomplete-inventories).

<!-- TODO: list known gaps and errors in the data and the portal (e.g. missing or problematic inventories, layout types that are poorly recognised), or link to where these are tracked. -->

## Reporting errors

Content to be developed.

<!-- TODO: explain how users can report errors, biased or harmful content, and what happens with their reports. Link to /pages/footer/contact.md. -->
