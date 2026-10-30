# Globalise Editorial Style Guide

This is the initial editorial style guide for the Globalise research portal. It should evolve as editorial decisions are made during content production.

## 1. Audience

Write primarily for researchers and students, but assume that many users will not be specialists in:

* Dutch early-modern history;
* VOC history;
* Dutch archival systems;
* digital humanities;
* computational methods.

A specialist should find the content precise; a non-specialist should be able to understand it without consulting another source.

## 2. Language

Since the project's name is Globali**s**e, the editorial language of the portal is UK English. Avoid unnecessary academic or technical jargon. When specialist terminology is necessary, explain it on first use.

## 3. Globalise

Always write:

> Globalise

not:

> GLOBALISE


**Globalise** is the name of both the website and the research project that built it. By the time the website goes live, the project will have ended, while the website remains online. Therefore:

* Call the project **the Globalise project** (or *the project*, once it is clear from the context), and write about it in the **past tense**: *The Globalise project transcribed almost 5 million pages.*
* Use **Globalise** on its own for the website and what it offers, in the **present tense**: *Globalise covers the Overgekomen Brieven en Papieren.* The same goes for outputs that remain available, such as the Globalise data, thesaurus and ontology.
* Do not change archived texts (blog posts, project documents) or documents reproduced verbatim, such as the full text of the ethics policy.

### The OBP

At first mention on a page, write:

> *Overgekomen Brieven en Papieren* (OBP; in English the Copied Letters series)

After that, use:

> OBP

Do not use other translations, such as "letters and papers received" or "Copied Letter Series". Names of datasets and inventory sections that contain a translation (for example *Letters and Papers received from the Indies*) are left as they are.

## 4. VOC

At first mention on a page, use:

> Dutch East India Company (VOC)


After that, use:

> VOC


## 5. Colonial terminology

Historical terminology should be treated carefully. Make clear where appropriate that a term is, for example, terminology used by colonial authorities. Where a historical term is offensive or outdated, provide contextualisation.

## 6. Distinguish source from interpretation

Users should be able to distinguish between:

1. the original archival source;
2. a digitised image of that source;
3. a transcription;
4. metadata;
5. a computational annotation;
6. an inferred or linked entity;
7. a search result.

Do not describe a model-generated annotation as though it were an undisputed historical fact.

## 7. Computational methods

When describing models or automated processes:

* explain what the process does;
* distinguish automated output from manually verified information;
* acknowledge uncertainty and incompleteness where relevant;
* link to technical documentation when useful.

## 8. Search

Be precise about what users are searching.

Distinguish, where relevant, between:

* full-text search;
* metadata search;
* entity search;
* faceted filtering;
* searching through an AI assistant connected to the Globalise MCP server.

## 9. Naming people and places

Follow project reference data where available for naming people and places.

## 10. Capitalisation

Use sentence case capitalisation for headings.

Prefer:

> Ethics and colonial context

over:

> Ethics And Colonial Context

## 11. Headings

Use headings hierarchically.

Start with:

```markdown
# Page title
```

Then:

```markdown
## Major section
```

and:

```markdown
### Subsection
```

Do not skip levels merely for visual appearance.

## 12. Paragraphs

Prefer short paragraphs, generally two to five sentences.

Break up long blocks of text with:

* headings;
* images;
* examples;
* quotations where appropriate.

## 13. Links

Use descriptive link text.

Prefer:

> Read the [Globalise data documentation](...)

over:

> [Click here](...)

Do not use bare URLs in normal prose unless the URL itself is important.

## 14. Images

Every meaningful image should have meaningful alt text.

Alt text should describe the information conveyed by the image, not merely repeat its caption.

For example:

> Map of the Cape of Good Hope showing VOC settlements and surrounding coastline.

is better than:

> Historical map.

Always record image provenance:

* creator;
* source;
* licence.

## 15. Captions

Captions should provide information that is useful to the reader.

Where relevant, include:

* what is shown;
* date;
* creator;
* source;
* licence.

Do not repeat the alt text unnecessarily.

## 16. Citations

Citations should make it possible for researchers to identify and, where possible, locate the source.

### Literature

All works cited on the portal are recorded once, in [`/assets/references/references.bib`](/assets/references/references.bib). In the text, refer to them by their citation key, using Pandoc citation syntax:

| You write | Meaning |
| --- | --- |
| `[@Gaastra2003]` | A citation in brackets |
| `[@Gaastra2003, 45]` or `[@Gaastra2003, 45–52]` | A citation with page numbers |
| `[see @Gaastra2003, 45; @Knaap2023]` | Several works, with a prefix |
| `@Gaastra2003 argues that …` | The author's name as part of the sentence |

Do not type out formatted references by hand. The formatted citation and the list of references are generated from `references.bib`, so that all pages use the same style.

Citation keys consist of the first author's (or editor's) family name, including particles, and the year of publication, without spaces or diacritics: `Gaastra2003`, `VanRossum2012`, `SJacob2000`. If the same author has more than one work in a year, add a letter: `Verkijk2023a`, `Verkijk2023b`. For reprints, use the year of the original edition.

### Footnotes

Use footnotes (`[^1]`) for comments and for references that need explanation. A footnote can contain a citation key.

### Archival documents

Refer to archival documents by archive, series, inventory number and, where relevant, scan or folio, for example `NL-HaNA, VOC, 1.04.02, inv. 1221, scan 0183`. Where the document is available on the portal, link to it.

<!-- TODO: confirm the format for archival references, and how links to documents on the portal should be formed. -->

### Citing the portal itself

How users should cite Globalise data and documents is explained in the [Citation guide](/pages/learn-get-started/citation.md). That page is about citing the portal, not about citations within it.

## 17. Licences and reuse

The rights status of material displayed on the Globalise research portal will vary. Where reuse conditions differ, explain the distinction clearly.

## 18. Content warnings

Content warnings should be:

* concise;
* placed before the potentially sensitive material;
* linked to fuller contextual information where appropriate.

## 19. Accessibility

All content should aim to meet the portal's accessibility requirements.

Writers should:

* provide meaningful alt text;
* avoid long unbroken passages;
* avoid colour-dependent explanations;
* use descriptive links;
* write in clear language;
* provide text alternatives for essential visual information.
