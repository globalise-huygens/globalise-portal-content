---
title: "Bias & limitations"
subtitle: ""
summary: "An explanation of archival, computational and interpretive biases and limitations in Globalise."
type: "page"
slug: "bias-and-limitations"
status: "draft"

authors: []
datePublished: ""
dateUpdated: "2026-11-12"

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

<!-- Sources: pages/research-responsibly/voc-archives-guide.md; "Mission, Research Themes and Guiding Questions" v1.0 (pages/about/project/archive/mission-research-themes.md); Globalise Ethics Policy v2.0 and its ethics reports on Primary Sources and the Places Dataset (pages/research-responsibly/ethics/policy.md); Arno Bosse, "The Languages of GLOBALISE" (pages/about/project/archive/blog/the-languages-of-globalise.md). Limitations of the VOC archives themselves are covered in the VOC archives guide; this page links to it rather than repeating it. -->

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

The lists of pages with a non-Dutch or unknown language, including their text, are published, so that you can apply your own criteria. See the [Technical documentation](/pages/research-responsibly/data/technical-documentation.md#language-identification) and [The Languages of GLOBALISE](/pages/about/project/archive/blog/the-languages-of-globalise.md).

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

### Bias in models

The project's [ethics policy](/pages/research-responsibly/ethics/policy.md) committed it to checking its models for discriminatory or biased results, through careful selection of training and test data by people with relevant historical expertise, and through qualitative and quantitative analysis of model output.

Content to be developed.

<!-- TODO: report what bias analyses were carried out on the models and what they found. -->

## Reference data

Reference data and thesauri, such as the datasets on polities, places, people and commodities, were compiled and checked by historians. They are curated, but they are not neutral. They reflect the knowledge, perspectives and expertise of the project team and contributors, and the sources and literature they were built from. Because these are mostly colonial sources in Dutch and English, colonial names and categories are recorded more fully than local ones. The limitations of each dataset are summarised on the [Reference data](/pages/research-responsibly/data/reference-data.md#what-all-reference-datasets-have-in-common) page, and the choice of place names under [Which name is shown](/pages/research-responsibly/data/reference-data.md#which-name-is-shown-preferred-labels).

Even when a dataset is well documented, it can be hard for users to see why a particular value was chosen for a particular entry.

### Thematic choices

The project could not create reference data for every subject in the archive. It prioritised political and economic subjects, which appear most often in the sources, while drawing attention to lesser-known Asian polities and to the activities of non-European actors. In 2024, the social domain was next in line, after which the project planned to explore the environmental and cultural domains. Any such selection is subjective. See [Mission, Research Themes and Guiding Questions](/pages/about/project/archive/mission-research-themes.md).

<!-- TODO: update with the final coverage of reference data per domain. The 2024 mission statement says datasets existed or were in preparation for polities, commodities, units of measurement, locations and persons, with the social domain next. -->

## Searching and interpreting

### The infrastructure shapes what you find

An infrastructure that makes an archive easier to search also influences what people search for, what they find, which histories are written and which topics enter public debate.

### Results are snippets

Advanced search makes it possible to extract small pieces of information from millions of pages. These are representations of historical realities, shaped by the context of the document they come from: its type, its author and its purpose. The archive does not offer unfiltered historical truths, but fragmented observations and interpretations.

Searches on the portal can tell you what was recorded, where and when. Explaining how and why things happened remains the task of the researcher. See [Responsible use](/pages/research-responsibly/ethics/responsible-use.md).

### Searching with an AI assistant

An AI assistant connected to the [Globalise MCP server](/pages/learn-get-started/ai-assistant.md) works with the same data and inherits all the limitations described on this page. It adds limitations of its own. It decides which searches to run and which results to read, and it may stop before it has found everything. It can misread or misquote a transcription, overstate what the sources say, fill gaps with knowledge from its training, and occasionally invent quotations or sources, all in fluent and confident language. Its translations and summaries have not been checked. The server gives the assistant background on the limitations of the data, with links to this page, but whether the assistant passes them on to you depends on the assistant.

## Known issues

Content to be developed.

<!-- TODO: list known gaps and errors in the data and the portal (e.g. missing or problematic inventories, layout types that are poorly recognised), or link to where these are tracked. -->

## Reporting errors

Content to be developed.

<!-- TODO: explain how users can report errors, biased or harmful content, and what happens with their reports. Link to /pages/footer/contact.md. -->
