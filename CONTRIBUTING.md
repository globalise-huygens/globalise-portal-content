# Contributing to the Globalise Research Portal

This repository contains the editorial source content for the Globalise research portal.

Contributions are managed through GitHub Issues and Pull Requests so that drafts and reviews remain traceable.

## 1. Before you start

Check:

* [SITEMAP.md](SITEMAP.md) to see where a page sits in the site structure;
* [CONTENT.md](CONTENT.md) to see what is expected for a website specific section / page;
* [STYLEGUIDE.md](STYLEGUIDE.md) for editorial conventions;
* the relevant template in [`templates/`](templates/) if you are creating a new page.

If the task is not already represented by a GitHub Issue, create one before starting substantial work.

## 2. Creating or updating a page

For a new page:

1. Identify the appropriate website section and filename.
2. Copy the relevant template.
3. Add the required YAML front matter.
4. Write the content in Markdown.
5. Check links, headings, images and citations.
6. Update the page status.
7. Open a Pull Request referencing the relevant Issue.

For a small correction to an existing page, you may edit the page directly and open a Pull Request.

## 3. GitHub Issues

Issues should be used for:

* requesting a new page;
* asking a colleague for input;
* requesting historical or technical review;
* identifying missing information;
* recording questions that need a project decision;
* reporting content problems;
* tracking dependencies on the portal or data infrastructure.

### Suggested Issue types

**New page**

Describe the purpose, audience, key questions, suggested length and intended owner.

**Request input**

Use when a page exists but needs information or text from a particular colleague.

**Review**

Use when content is ready for subject-matter, editorial, technical or ethical review.

**Decision**

Use for questions that affect multiple pages or the overall content structure.

**Technical dependency**

Use when content depends on an API, identifier, screenshot or other technical component.

## 4. Pull Requests

A Pull Request should:

* describe what has changed;
* link to the relevant Issue;
* identify any unresolved questions;
* request appropriate reviewers.

Keep Pull Requests reasonably focused. A Pull Request containing one coherent page or small group of related pages is easier to review than a large collection of unrelated changes.

## 5. Review

Different types of content may require different reviewers.

### Editorial review

Check:

* clarity;
* structure;
* consistency;
* terminology;
* accessibility;
* links;
* spelling and grammar.

### Historical / subject-matter review

Check:

* archival context;
* terminology;
* references.

### Technical review

Check:

* descriptions of data;
* descriptions of models;
* descriptions of search functionality;
* descriptions of APIs;
* file formats;
* technical limitations.

### Ethics review

Check:

* colonial terminology;
* content warnings;
* descriptions of bias;
* responsible-use guidance;
* potentially harmful or misleading formulations.

### Institutional / legal review

Required where appropriate for:

* privacy;
* cookies;
* accessibility statements;
* licences;
* disclaimers;
* institutional credits.

## 6. Page status

Use the following values in front matter:

| Status      | Meaning                         |
| ----------- | ------------------------------- |
| `planned`   | Page identified, no draft yet   |
| `draft`     | Initial draft exists            |
| `review`    | Ready for review                |
| `approved`  | Approved for publication        |
| `published` | Published on the portal         |
| `later`     | Not required for initial launch |

A page should normally move through:

```text
planned → draft → review → approved → published
```

## 7. Metadata

Every page must contain YAML front matter.

At minimum:

```yaml
---
title: "Page title"
summary: "Short description."
type: "page"
slug: "page-title"
status: "draft"

authors: []
datePublished: ""
dateUpdated: ""

featured: false

hero:
  src: ""
  alt: ""
  caption: ""
  credit: ""
  source: ""
  licence: ""

related: []
tags: []
---
```

See [CONTENT-METADATA.md](CONTENT-METADATA.md) for the full explanation.

## 8. Images

Do not add images without recording their provenance.

For each image, establish:

* creator;
* source;
* licence or rights status;
* meaningful alt text.

The page front matter should contain the information for the hero image. Additional images can be referenced in the Markdown text:

`![alt text](/path/to/image.jpg)`
`*caption*`

Include full metadata for additional images in [`image-metadata.yml`](/assets/images/image-metadata.yml), following the guidelines in [`content-metadata.md`](/CONTENT-METADATA.md).

Provide images in JPEG format in a reasonable size and resolution, and store them in a subfolder in `/assets/images/`. Ideal image dimensions depend on where and how the image is used, but generally: 1600 by 900 px (portrait or landscape)

## 9. External links

Prefer stable sources; avoid links to temporary search results or pages that are likely to disappear.

If an external resource is central to the page, describe what users will find there rather than simply providing a bare link.

## 10. Citations

Follow the citation conventions in the [style guide](STYLEGUIDE.md#16-citations). In practice:

1. **Check whether the work is already in [`/assets/references/references.bib`](/assets/references/references.bib).** If it is, use its key.
2. **If not, add a BibTeX entry** to `references.bib`. Export it from Zotero or another reference manager, or copy it from the publisher, Crossref or the ACL Anthology, and then:
   * give it a key following the `AuthorYear` convention (for example `Gaastra2003`), and make sure the key is unique;
   * include at least author or editor, title, year and publisher or journal, and a DOI where one exists;
   * remove fields that are only used by your reference manager, such as `abstract`, `keywords`, `file` and `urldate`;
   * for works not in English, add the language, for example `langid = {dutch}`, so that titles keep their own capitalisation;
   * for reprints, give the original edition and mention the reprint in a `note`.
3. **Cite the work in your text** with its key, for example `[@Gaastra2003, 45]`. Do not type the formatted reference.

The [bibliography page](pages/learn-get-started/resources/bibliography.md) is generated from `references.bib`. Each entry on that page ends with its key in an HTML comment (`<!-- Gaastra2003 -->`). To add a work to the bibliography, add an entry anywhere in the right section with only its key, for example `* <!-- Boxer1965 -->`, and run:

```bash
python3 scripts/render_bibliography.py pandoc pages/learn-get-started/resources/bibliography.md assets/references/references.bib
```

This re-renders every list on the page from `references.bib` (Chicago author-date style). It requires [Pandoc](https://pandoc.org/) version 3 or later.

The [Citation guide](pages/learn-get-started/citation.md) is a page for portal users about how to cite Globalise data and documents. It is not a guide for citations in content pages.

## 11. Accessibility

Write with accessibility in mind:

* use logical heading levels;
* use descriptive link text;
* provide meaningful alt text;
* keep paragraphs reasonably short;
* avoid unnecessary jargon;
* provide text alternatives for important visual information.

## 12. Research guides

Research guides will often be written by external contributors. They are stored in `pages/explore/research-guides/`.

Use the relevant template: `collection.md` for a guide to a category of material (such as persons, places or commodities), `theme.md` for a guide to a historical theme:

* [`templates/collection.md`](templates/collection.md)
* [`templates/theme.md`](templates/theme.md)

Contributors should receive the relevant page brief from the Globalise team before drafting.

## 13. Keeping content and implementation separate

Markdown should contain the editorial content, not the implementation of the website. Avoid specific markup and/or HTML and Javascript.

If a page genuinely requires special functionality, discuss the requirement in a GitHub Issue first.

## 14. Changes affecting multiple pages

If a change affects terminology, navigation, metadata, citations, ethics guidance or another cross-cutting issue, create a GitHub Issue before making widespread edits.

For example, changing the preferred terminology for an entity category should be recorded as a project decision rather than silently changed in individual pages.

## 15. External contributors

External contributors do not need to become experts in the repository structure.

The Globalise team should provide:

* a clear brief;
* the relevant template;
* suggested length;
* required examples.
