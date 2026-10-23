---
title: "Bias & limitations"
subtitle: ""
summary: "An explanation of archival, computational and interpretive biases and limitations in Globalise."
type: "page"
slug: "bias-and-limitations"
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

related: ["colonial-context", "responsible-use", "methods", "voc-archives-guide"]
---

# Bias & limitations

<!-- Sources: pages/research-responsibly/voc-archives-guide.md; "Mission, Research Themes and Guiding Questions" v1.0 (pages/about/project/archive/mission-research-themes.md); Globalise Ethics Policy v2.0 and its ethics reports on Primary Sources and the Places Dataset (pages/research-responsibly/ethics/policy.md); Arno Bosse, "The Languages of GLOBALISE" (pages/about/project/archive/blog/the-languages-of-globalise.md). -->

<!-- TODO: this page depends on the final models and data (dependency "Final models" in CONTENT.md). Check all statements against the final state of the portal before publication. -->

Everything on this portal is shaped by choices and limitations: those of the people who created the archive centuries ago, those of the archivists who organised it, and those of the Globalise project, which selected, transcribed, annotated and linked it. This page explains the most important ones, so that you can take them into account when you use the portal.

Neutrality is not attainable. The aim of this page is not to excuse these limitations, but to make them visible.

## The archive

### A VOC perspective

The documents on this portal were written by the Dutch East India Company (VOC) and its personnel. They record events, people and societies as the company saw them, and what it considered worth writing down. People who were not part of the company appear mainly when they mattered to it, and their words usually reach us translated and selected by company officials. See [Colonial context](/pages/research-responsibly/ethics/colonial-context.md).

### What survived

The VOC archives that survive today are spread over archives in Indonesia, Sri Lanka, India, South Africa, Malaysia, the United Kingdom and the Netherlands. Much has been lost. Each VOC factory and outpost kept its own archive, but most of these local archives have not survived.

### Written sources and accessible sources

History writing has traditionally privileged written sources over other ways of recording and remembering the past, such as oral history, material culture and art. Not every society recorded its history in writing, and not all written sources have been digitised or transcribed.

Making the VOC archives easier to search also carries a risk: that research relies on them more than on other sources from the Indian Ocean world simply because they are more accessible. Prioritising digitised and transcribed collections affects how the history of this period is understood.

## What Globalise covers

### Part of the VOC archives

Globalise does not cover all VOC archives, nor even all of the VOC archive at the Nationaal Archief (Dutch National Archives). It works with the *Overgekomen Brieven en Papieren* (OBP) in series 1.04.02: inventory numbers 1053–4454 and 7527–11024, roughly 6,900 inventory numbers and about 4.8 million pages. The material dates roughly from 1605 to 1794.

Not covered are, for instance, the resolutions of the company's directors, the correspondence sent from the Dutch Republic to Asia, and the archives of the Delft, Rotterdam, Hoorn and Enkhuizen chambers. Nor does the portal include VOC archives held elsewhere in the world. The [guide to the VOC archives](/pages/research-responsibly/voc-archives-guide.md) lists what is and is not included.

### Languages and scripts

Almost 97% of the pages in the Globalise corpus (about 4.3 million pages) are written in Dutch. The remainder includes pages in other European languages, such as French, English, Latin and Portuguese, and in Asian languages, such as Malay, Persian, Sinhala and Chinese.

The text recognition software used by Globalise cannot read non-Latin scripts. Pages written in, for example, Chinese, Persian or Sinhala are turned into strings of seemingly random characters and cannot be searched for their content. For about 3% of pages, no language could be identified automatically, and pages with too little continuous text, such as tables and blank pages, were left out of the automatic identification. See [The Languages of GLOBALISE](/pages/about/project/archive/blog/the-languages-of-globalise.md) for details.

## Computational processing

### Text recognition

All transcriptions on the portal were produced automatically using handwritten text recognition. They contain errors. A word that was misread cannot be found by searching for its correct spelling, and errors carry through to every later step.

### Evaluation of text recognition

Content to be developed.

<!-- TODO: add plain-language results of the HTR evaluation (e.g. character error rate), including any known differences in quality between periods, regions, hands or document types. See also the related TODO on pages/about/methods.md. -->

### Entities and events

Given the size of the archive, Globalise relies on machine learning to recognise entities (such as people, places and polities) and events in the text. Only part of these annotations could be checked by hand. Annotations on the portal are therefore model output: they can be wrong, incomplete or inconsistent, and they should not be treated as established facts.

### Evaluation of entity and event recognition

Content to be developed.

<!-- TODO: add plain-language results of the evaluation of the entity and event recognition models, and describe what kinds of errors are most common. -->

### Bias in models

The project's [ethics policy](/pages/research-responsibly/ethics/policy.md) commits to checking its models for discriminatory or biased results, through careful selection of training and test data by people with relevant historical expertise, and through qualitative and quantitative analysis of model output.

Content to be developed.

<!-- TODO: report what bias analyses were carried out on the models and what they found. -->

## Reference data

Reference data and thesauri, such as the datasets on polities, places, people and commodities, were compiled and checked by historians. They are curated, but they are not neutral. They reflect the knowledge, perspectives and expertise of the project team and contributors, and the sources and literature they were built from.

The places dataset is an example. Because the project depends largely on colonial sources in Dutch and English, names used by colonial powers are more likely to be included than local names. GeoNames, the main source for preferred place names, is open and widely used, but it is not always clear where its information comes from or to what extent it reflects a Western view of the world. Experts from India, Indonesia and Taiwan have since reviewed and added to the data to counter this imbalance.

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

## Known issues

Content to be developed.

<!-- TODO: list known gaps and errors in the data and the portal (e.g. missing or problematic inventories, layout types that are poorly recognised), or link to where these are tracked. -->

## Reporting errors

Content to be developed.

<!-- TODO: explain how users can report errors, biased or harmful content, and what happens with their reports. Link to /pages/footer/contact.md. -->
