---
title: "Methods"
subtitle: ""
summary: "A high-level overview of the methods used to transform archival material into Globalise data."
type: "page"
slug: "methods"
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

related: ["what-is-globalise", "outputs", "bias-and-limitations"]
---

# Methods

<!-- Sources: https://globalise.huygens.knaw.nl/project_overview/ ; https://docs.globalise.huygens.knaw.nl/mission/mission_researchthemes/ ; dataset and model list on https://globalise.huygens.knaw.nl/output/ (consulted 2026-10-01). -->

<!-- TODO: check against the final pipeline (dependency in CONTENT.md) before publication, in particular the steps described under "Bringing it together" and anything on the MCP server. -->

This page gives a high-level overview of how almost 5 million scanned pages of handwritten documents became the material you can search and explore on this portal. Each step involves both computational methods and the work of historians, and each step introduces its own uncertainties. For detailed technical documentation, see [How the data was produced](/pages/research-responsibly/data/production.md) and [Technical documentation](/pages/research-responsibly/data/technical-documentation.md).

## 1. From scans to text

The starting point is the set of high-quality scans of the *Overgekomen Brieven en Papieren* (OBP; in English the Copied Letters series) made by the Nationaal Archief (Dutch National Archives).

These scans were transcribed automatically using **handwritten text recognition (HTR)**: software that recognises handwriting on an image and turns it into machine-readable text. The Globalise project used Loghi, open-source HTR software developed by the Digital Infrastructure department of the KNAW Humanities Cluster. Loghi first analyses the layout of each page, detecting text regions and the lines of text within them, and then transcribes each line.

To train the HTR models, members of the project team and others created **ground truth**: a set of pages transcribed and checked by hand, from which the software learns what the handwriting looks like. The ground truth and the trained models have been published openly (see [Outputs](/pages/about/outputs.md)).

Automatic transcriptions are not perfect. The software also cannot read non-Latin scripts, such as Chinese, Persian or Sinhala (see [Bias & limitations](/pages/research-responsibly/ethics/bias-and-limitations.md)). When you read a transcription on this portal, always compare it with the scan if the exact wording matters.

<!-- TODO: add a short, plain-language statement of HTR accuracy (e.g. character error rate) and link to evaluation details. -->

## 2. From pages to documents

The OBP was bound into volumes, and a single volume can contain hundreds of separate letters, reports, journals and lists. The Globalise project identified where these documents begin and end with a segmentation model. For every page, the model weighed the signs of a new document, such as opening and closing formulas, signatures, page numbers, blank pages and the layout of the page. Where a volume has a historical index, the model placed each index entry on the page where its document begins, and then looked for documents that the index does not list. The result was about 508,000 documents in all 6,914 volumes. Documents with an index entry keep the title the VOC gave them; the project inferred titles for the others from their text, and a classifier predicted their type. See [How the data was produced](/pages/research-responsibly/data/production.md#3-identifying-documents).

<!-- TODO: the segmentation has not yet been integrated into the portal (issue #24). -->

## 3. Recognising entities and events

Next, the project identified **entities** (persons, places, polities, ships, commodities and other things mentioned in the text) and **events** (actions and occurrences, such as attacks, treaties, purchases, voyages or deaths).

Historians and computational linguists in the team first annotated a sample of documents by hand, using the annotation tool INCEpTION. These manual annotations were then used to train and evaluate language models that recognise entities and events across the whole corpus. Among them is GloBERTise, a language model developed by the project for early modern Dutch VOC texts. Recognising events is especially difficult, because the same event can be described in many ways, and much of what happened is only implied in the text.

<!-- TODO: check description of GloBERTise with Stella Verkijk. -->

Given the size of the archive, the entity and event annotations across the corpus were produced by these models and could only partly be checked by hand. Treat them as suggestions made by a model, not as established facts: they will contain errors and omissions.

## 4. Reference data and thesauri

Alongside this computational work, historians in the team built **reference data**: structured datasets compiled from source publications, secondary literature and the archive itself. These datasets include polities and their rulers, places, people, ethnic and religious groups, and weights and measures in the Indian Ocean world. Each records name variants and spellings, dates and relationships. For example, the polities dataset records that Banten also appears as Bantam or Bantamm, who ruled it and when.

The project also developed **thesauri**: controlled vocabularies with definitions of concepts found in the archive, such as hundreds of types of traded textiles and other commodities. This work was done together with colleagues from around the world.

Reference data is curated and checked by people, but it is not neutral. It reflects choices about what to include and how to classify, and it is shaped by the sources and literature it was built from.

## 5. Bringing it together

Finally, entities and events recognised in the text are **linked** to the reference data, so that a mention of a ruler in a document can be connected to what is known about that ruler. An **ontology**, a formal model of the kinds of entities and events and the relationships between them, structures this information so that it can be queried in combination: for example, all conflicts involving a particular polity in a given period.

On the portal, you can see whether a piece of information comes from the transcription, from a model, or from curated reference data. See [Understanding results](/pages/learn-get-started/searching-browsing/results.md) for how to read this.

<!-- TODO: confirm that provenance (manual / model / user) is indeed visible in the portal interface, and adjust the paragraph above if needed. -->

## Limitations

Every step above can introduce errors, and errors in earlier steps carry through to later ones: a misread name cannot be correctly linked. The archive itself is also incomplete and one-sided. It records what VOC officials saw, heard and thought worth reporting. The section on [Bias & limitations](/pages/research-responsibly/ethics/bias-and-limitations.md) discusses these issues in detail.
