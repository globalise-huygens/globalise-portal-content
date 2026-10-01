# Globalise Portal Content Plan

This document is the editorial  plan for the Globalise research portal.

It records the pages that need to be produced, their purpose, intended audience, suggested content, responsibility and dependencies.

Collections and Themes are included in the structure, but their substantive content will primarily be commissioned from external contributors.

## Status vocabulary

| Status      | Meaning                                          |
| ----------- | ------------------------------------------------ |
| `planned`   | Page identified but drafting has not started     |
| `draft`     | Initial content exists                           |
| `review`    | Ready for editorial and/or subject-matter review |
| `approved`  | Approved for publication                         |
| `published` | Live on the portal                               |
| `later`     | Useful, but not required for launch              |

## 1. Home

| ID      | Page                 | File                       | Purpose / key questions                                                                               | Suggested length      | Owner / source                         | Priority  | Status  | Dependencies         |
| ------- | -------------------- | -------------------------- | ----------------------------------------------------------------------------------------------------- | --------------------- | -------------------------------------- | --------- | ------- | -------------------- |
| HOME-01 | Home                 | `pages/home.md`            | What is Globalise? What can I search? Where should I start?                                           | 200 words + cards | Editorial team                         | Essential | planned | Final UI             |
| HOME-02 | What can I search?   | Component on Home          | What archival material, metadata, entities and other data can users search? What are the limitations? | 150 words         | Project team                      | Essential | planned | Final data model & search index     |
| HOME-03 | Content warning      | Component + link to Ethics | What kind of colonial material might users encounter?                                                 | 50 words          | Manjusha                  | Essential | planned | none          |
| HOME-04 | Featured Collections | Component                  | Provide visual entry points into Collections                                                          | —                     | External contributors + editorial team | Essential | planned | Collection selection |
| HOME-05 | Featured Themes      | Component                  | Demonstrate research applications                                                                     | —                     | External contributors   + editorial team                | Essential | planned | Theme selection      |

## 2. Collections

| ID      | Page                   | File                          | Purpose / key questions                                                 | Suggested length         | Owner / source        | Priority  | Status  | Dependencies         |
| ------- | ---------------------- | ----------------------------- | ----------------------------------------------------------------------- | ------------------------ | --------------------- | --------- | ------- | -------------------- |
| COLL-01 | Collections overview   | `pages/collections/README.md` | Explain what Collections are and how they support discovery             | 300–500 words            | Editorial team        | Essential | planned | Collection selection |
| COLL-02 | Individual Collections | `pages/collections/...`       | What is this collection? What can I find? How can I search it?          | 100–150 words + examples | External contributors | Essential | planned | Commissioning        |


### Planned Collection categories

* TBA (Melinda)

Collections should be treated as a content type rather than merely as static pages.

## 3. Themes

| ID       | Page               | File                                 | Purpose / key questions                                         | Suggested length | Owner / source        | Priority  | Status  | Dependencies         |
| -------- | ------------------ | ------------------------------------ | --------------------------------------------------------------- | ---------------- | --------------------- | --------- | ------- | -------------------- |
| THEME-01 | Themes overview    | `pages/themes/README.md`             | Explain what Themes are and how they support research           | 300–500 words    | Editorial team        | Essential | planned | Theme selection      |
| THEME-02 | Individual Themes  | `pages/themes/...`                   | How can Globalise be used to investigate this historical theme? | ~1,000 words     | External contributors | Essential | planned | Commissioning        |


### Possible themes

* Animal studies
* Cultural history
* Commodity history
* Diplomatic history
* Environmental history
* Food history
* Genealogical history
* Gender history
* Slavery history
* Social history
* History of science
* Medicine and health
* Technology
* Visual and material culture

The list is non-exhaustive.

## 4. Learn & Get Started

| ID       | Page                          | File                               | Purpose / key questions                                                         | Suggested length | Owner / source    | Priority    | Status  | Dependencies   |
| -------- | ----------------------------- | ---------------------------------- | ------------------------------------------------------------------------------- | ---------------- | ----------------- | ----------- | ------- | -------------- |
| LEARN-01 | Getting started               | `pages/learn/getting-started.md`   | Where does a new user begin?                                                    | 500–700 words    | Editorial team        | Essential   | planned | Final UI       |
| LEARN-02 | Searching                     | `pages/learn/searching.md`         | How does full-text and structured search work?                                  | 800–1,200        | Editorial team + developers       | Essential   | planned | Final search   |
| LEARN-03 | Filters & facets              | `pages/learn/facets.md`            | How do search and facets work together?                                         | 500–800          | Editorial team + developers    | Essential   | planned | Final facets   |
| LEARN-04 | Semantic / AI-assisted search | `pages/learn/semantic-search.md`   | What does semantic search do? When should it be used? What are its limitations? | 600–900          | Editorial team + developers    | Essential   | planned | Final feature  |
| LEARN-05 | Browsing                      | `pages/learn/browsing.md`          | How do users explore documents, entities, maps and other entry points?          | 600–900          | Editorial team + developers        | Essential   | planned | Final UI       |
| LEARN-06 | Understanding results         | `pages/learn/results.md`           | What do result fields, highlights and rankings mean?                            | 600–900          | Project team + developers    | Essential   | planned | Final UI       |
| LEARN-07 | Working with documents        | `pages/learn/documents.md`         | How do users inspect scans, transcriptions, metadata and annotations?           | 600–900          | Project team + developers        | Essential   | planned | Final viewer   |
| LEARN-08 | Research workflow             | `pages/learn/research-workflow.md` | How can a user move from a research question to archival evidence?              | 700–1,000        | Project team    | Recommended | planned | Examples       |
| LEARN-09 | Citation guide                | `pages/learn/citation.md`          | How should documents, entities, datasets and portal output be cited?            | 200        | Project team | Essential   | planned | Persistent IDs |

## 5. About Globalise

| ID       | Page                | File                       | Purpose / key questions                                                               | Suggested length | Owner / source       | Priority    | Status  | Dependencies      |
| -------- | ------------------- | -------------------------- | ------------------------------------------------------------------------------------- | ---------------- | -------------------- | ----------- | ------- | ----------------- |
| ABOUT-01 | About Globalise     | `pages/about/index.md`     | Orient users to the project and its supporting pages                                  | 300–500          | Editorial team         | Essential   | draft   | —                 |
| ABOUT-02 | What is Globalise?  | `pages/about/project.md`   | What problem does Globalise address? What are its aims?                                | ~500             | Project team         | Essential   | draft   | —                 |
| ABOUT-03 | Project & ambitions | `pages/about/ambitions.md` | Why Globalise? What are its ambitions around access and research?                     | 500–700          | Project team         | Recommended | draft   | —                 |
| ABOUT-04 | Methods             | `pages/about/methods.md`   | Give a high-level account of the transformation from archive to digital research data | 500–800          | Project team & developers    | Essential   | draft   | Final pipeline    |
| ABOUT-05 | Outputs             | `pages/about/outputs.md`   | Publications, presentations, reports, datasets, software and other outputs            | Variable         | Project team         | Essential   | draft   | Final output list |
| ABOUT-06 | Team & partners     | `pages/about/team.md`      | Who made Globalise and who collaborated?                                              | 300–500          | Editorial team   | Essential   | draft   | Final team list   |
| ABOUT-07 | Archive             | `pages/about/archive/index.md` | Preserve project documents and blog posts that record how Globalise developed | 300–500 + list | Editorial team | Recommended | draft   | Archived pages (5.1) |

### 5.1 Archive

Archived pages are reproduced verbatim from the former project website (blog posts) and documentation website (project documents). Editorial work is limited to front matter, an archive notice, a one-sentence author bio, image metadata and checking image rights. See the archive landing page for details.

| ID      | Page | File | Purpose / key questions | Suggested length | Owner / source | Priority | Status | Dependencies |
| ------- | ---- | ---- | ----------------------- | ---------------- | -------------- | -------- | ------ | ------------ |
| ARCH-01 | Mission, Research Themes and Guiding Questions | `pages/about/archive/mission-research-themes.md` | Full project statement (v1.0, 2024), reproduced verbatim from docs.globalise.huygens.knaw.nl | Existing text | Matthias van Rossum, Manjusha Kuruppath | Recommended | draft | Licence: CC BY-SA 4.0 |
| ARCH-02 | Looking back on a successful kickoff meeting (2022-05-23) | `pages/about/archive/blog/looking-back-on-a-successful-kickoff-meeting.md` | Archived blog post, reproduced verbatim | Existing text | Merve Tosun | Recommended | draft | Image rights check |
| ARCH-03 | Rediscovering Early Modern Polities: First Thoughts on Dataset Creation (2022-06-30) | `pages/about/archive/blog/rediscovering-early-modern-polities-first-thoughts-on-dataset-creation.md` | Archived blog post, reproduced verbatim | Existing text | Manjusha Kuruppath | Recommended | draft | Image rights check |
| ARCH-04 | Automatic Event Detection in Early Modern Dutch (VOC) documents: the Annotation Phase (2022-10-04) | `pages/about/archive/blog/automatic-event-detection-in-early-modern-dutch-voc-documents-the-annotation-phase.md` | Archived blog post, reproduced verbatim | Existing text | Stella Verkijk | Recommended | draft | Image rights check |
| ARCH-05 | The (Ground) Truth is out there: an introduction to GLOBALISE’s use of Handwritten Text Recognition (2022-12-13) | `pages/about/archive/blog/the-ground-truth-is-out-there-an-introduction-to-globalises-use-of-handwritten-text-recognition.md` | Archived blog post, reproduced verbatim | Existing text | Maartje Hids and Kay Pepping | Recommended | draft | Image rights check |
| ARCH-06 | Aligning GLOBALISE with Researchers’ Needs (2023-03-01) | `pages/about/archive/blog/aligning-globalise-with-researchers-needs.md` | Archived blog post, reproduced verbatim | Existing text | Merve Tosun | Recommended | draft | Image rights check |
| ARCH-07 | Textile Taxonomies – GLOBALISE’s efforts in defining traded textiles in the Indian Ocean Region (2023-04-05) | `pages/about/archive/blog/textile-taxonomies-globalises-efforts-in-defining-traded-textiles-in-the-indian-ocean-region.md` | Archived blog post, reproduced verbatim | Existing text | Henrike Vellinga | Recommended | draft | Image rights check |
| ARCH-08 | Old Maps, New Discoveries: A Datasprint’s Digital Exploration (2023-11-06) | `pages/about/archive/blog/old-maps-new-discoveries-a-datasprints-digital-exploration.md` | Archived blog post, reproduced verbatim | Existing text | Leon van Wissen | Recommended | draft | Image rights check |
| ARCH-09 | An interactive design collaboration with the University of Utrecht (2024-01-29) | `pages/about/archive/blog/an-interactive-design-collaboration-with-the-university-of-utrecht.md` | Archived blog post, reproduced verbatim | Existing text | Arno Bosse | Recommended | draft | Image rights check |
| ARCH-10 | Thesaurus Treasures: Why We’re Creating a Hierarchical Lexicon of Commodities (2024-02-15) | `pages/about/archive/blog/thesaurus-treasures-why-were-creating-a-hierarchical-lexicon-of-commodities.md` | Archived blog post, reproduced verbatim | Existing text | Kay Pepping | Recommended | draft | Image rights check |
| ARCH-11 | Unearthing Insights at the GLOBALISE Commodity Data Sprint (2024-04-02) | `pages/about/archive/blog/unearthing-insights-at-the-globalise-commodity-data-sprint.md` | Archived blog post, reproduced verbatim | Existing text | Kay Pepping | Recommended | draft | Image rights check |
| ARCH-12 | From ABC to VOC Volume: Utilizing Traditional Finding Aids for the GLOBALISE Infrastructure (2024-06-20) | `pages/about/archive/blog/from-abc-to-voc-volume-utilizing-traditional-finding-aids-for-the-globalise-infrastructure.md` | Archived blog post, reproduced verbatim | Existing text | Renate Smit | Recommended | draft | Image rights check |
| ARCH-13 | Closeness at a Distance? The Port Town Paradox (2024-10-25) | `pages/about/archive/blog/closeness-at-a-distance-the-port-town-paradox.md` | Archived blog post, reproduced verbatim | Existing text | Marc Widmer | Recommended | draft | Image rights check |
| ARCH-14 | The Languages of GLOBALISE (2024-12-11) | `pages/about/archive/blog/the-languages-of-globalise.md` | Archived blog post, reproduced verbatim | Existing text | Arno Bosse | Recommended | draft | Image rights check |
| ARCH-15 | Towards Creating Meaningful Infrastructures for Colonial Archives (2025-03-04) | `pages/about/archive/blog/towards-creating-meaningful-infrastructures-for-colonial-archives.md` | Archived blog post, reproduced verbatim | Existing text | Renate Smit | Recommended | draft | Image rights check |
| ARCH-16 | Yes okay – but what were they doing? (2025-04-07) | `pages/about/archive/blog/yes-okay-but-what-were-they-doing.md` | Archived blog post, reproduced verbatim | Existing text | Stella Verkijk | Recommended | draft | Image rights check |
| ARCH-17 | Incognito Royalty on the Princes Roijael (2025-05-29) | `pages/about/archive/blog/incognito-royalty-on-the-princes-roijael.md` | Archived blog post, reproduced verbatim | Existing text | Ann Heylen | Recommended | draft | Image rights check |
| ARCH-18 | Transcriptions Viewer How-to Guide (2025-07-03) | `pages/about/archive/blog/transcriptions-viewer-how-to-guide.md` | Archived blog post, reproduced verbatim | Existing text | Melinda Susanto | Recommended | draft | Image rights check |
| ARCH-19 | A Gazetteer for the Dutch East India Company Archives: The GLOBALISE Places Dataset (2025-08-01) | `pages/about/archive/blog/a-gazetteer-for-the-dutch-east-india-company-archives-the-globalise-places-dataset.md` | Archived blog post, reproduced verbatim | Existing text | Dung Pham | Recommended | draft | Image rights check |
| ARCH-20 | When Archives Break Hearts (2025-08-08) | `pages/about/archive/blog/when-archives-break-hearts.md` | Archived blog post, reproduced verbatim | Existing text | Asawari Luthra | Recommended | draft | Image rights check |
| ARCH-21 | Guide to finding places in the GLOBALISE corpus of VOC documents (2025-11-05) | `pages/about/archive/blog/guide-to-finding-places-in-the-globalise-corpus-of-voc-documents.md` | Archived blog post, reproduced verbatim | Existing text | Nikhil Bellarykar | Recommended | draft | Image rights check |
| ARCH-22 | Echoes of genocidal erasure: a reflection on historical ‘voices’ and digital infrastructure for colonial archives (2025-12-19) | `pages/about/archive/blog/echoes-of-genocidal-erasure-a-reflection-on-historical-voices-and-digital-infrastructure-for-colonial-archives.md` | Archived blog post, reproduced verbatim | Existing text | Matthias van Rossum | Recommended | draft | Image rights check |
| ARCH-23 | Looking Back and Ahead: Access and Research in a Changing Archive (2025-12-30) | `pages/about/archive/blog/looking-back-and-ahead-access-and-research-in-a-changing-archive.md` | Archived blog post, reproduced verbatim | Existing text | Tara Huveneers | Recommended | draft | Image rights check |
| ARCH-24 | Digging deeper in the VOC archives, without the right keywords (2026-02-04) | `pages/about/archive/blog/digging-deeper-in-the-voc-archives-without-the-right-keywords.md` | Archived blog post, reproduced verbatim | Existing text | Arlette Verdonk | Recommended | draft | Image rights check |
| ARCH-25 | Cataplasma and Lienteria: Medical Terms in the VOC Archives (2026-03-27) | `pages/about/archive/blog/cataplasma-and-lienteria-medical-terms-in-the-voc-archives.md` | Archived blog post, reproduced verbatim | Existing text | Linda Robertus | Recommended | draft | Image rights check |
| ARCH-26 | Building Bridges: Archives as Spaces of Reconnection (2026-04-09) | `pages/about/archive/blog/building-bridges-archives-as-spaces-of-reconnection.md` | Archived blog post, reproduced verbatim | Existing text | Tara Huveneers | Recommended | draft | Image rights check |
| ARCH-27 | From acts of resistance and feminist theory to tortoiseshell trade and 17th-century currency – (not) everything I learnt at the GLOBALISE conference (2026-04-16) | `pages/about/archive/blog/from-acts-of-resistance-and-feminist-theory-to-tortoiseshell-trade-and-17th-century-currency-not-everything-i-learnt-at-the-globalise-conference.md` | Archived blog post, reproduced verbatim | Existing text | Lina de Swaaf | Recommended | draft | Image rights check |
| ARCH-28 | Documenting the Indonesian princely states (2026-04-21) | `pages/about/archive/blog/documenting-the-indonesian-princely-states.md` | Archived blog post, reproduced verbatim | Existing text | Hans Hägerdal | Recommended | draft | Image rights check |

## 6. Ethics & Colonial Context

| ID        | Page                      | File                                   | Purpose / key questions                                                               | Suggested length          | Owner / source         | Priority    | Status  | Dependencies          |
| --------- | ------------------------- | -------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------- | ---------------------- | ----------- | ------- | --------------------- |
| ETHICS-01 | Ethics & Colonial Context | `pages/ethics/index.md`                | Explain why critical interpretation is essential                                      | 300–500                   | Manjusha / editorial team | Essential   | planned | —           |
| ETHICS-02 | Ethics policy             | `pages/ethics/ethics-policy.md`        | What ethical principles guided Globalise?                                             | Existing policy + summary | Manjusha / editorial team               | Essential   | planned | Existing ethics text on https://docs.globalise.huygens.knaw.nl/ethics/policy/  |
| ETHICS-03 | Colonial context          | `pages/ethics/colonial-context.md`     | How should users understand colonial terminology, categories and archival structures? | 800–1,200                 | Manjusha / Matthias  | Essential   | planned | Ethics review         |
| ETHICS-04 | Bias & limitations        | `pages/ethics/bias-and-limitations.md` | What is missing, distorted or uncertain in the archive and computational processing?  | 1,000–1,500               | Project team   | Essential   | planned | Final models          |
| ETHICS-05 | Responsible use           | `pages/ethics/responsible-use.md`      | How should users interpret and reuse Globalise material?                              | 500–800                   | Project team           | Recommended | planned | Ethics review         |

## 7. Data & Documentation

| ID      | Page                      | File                                    | Purpose / key questions                                        | Suggested length | Owner / source          | Priority    | Status  | Dependencies         |
| ------- | ------------------------- | --------------------------------------- | -------------------------------------------------------------- | ---------------- | ----------------------- | ----------- | ------- | -------------------- |
| DATA-01 | Data & Documentation      | `pages/data/index.md`                   | Orient users to the documentation section                      | 300–500          | Editorial team team               | Essential   | planned | —                    |
| DATA-02 | Globalise data            | `pages/data/data.md`                    | What data products does Globalise provide?                     | 700–1,000        | Editorial team               | Essential   | planned | Final data model     |
| DATA-03 | Accessing the data        | `pages/data/access.md`                  | How can users access API and bulk data?                        | 600–900          | Leon          | Essential   | planned | Final infrastructure |
| DATA-04 | Licences & reuse          | `pages/data/licences.md`                | What can users reuse and under what conditions?                | 500–800          | Editorial team   | Essential   | planned | Licence decisions    |
| DATA-05 | How the data was produced | `pages/data/production.md`              | How does archival material become Globalise data?              | 1,000–1,500      | Leon / project team | Essential   | planned | Final pipeline       |
| DATA-06 | Technical documentation   | `pages/data/technical-documentation.md` | Detailed models, tools, pipelines and technical specifications | Variable         | Project team          | Essential   | planned | Documentation        |
| DATA-07 | Reference data            | `pages/data/reference-data.md`          | How were reference datasets selected and constructed?          | 700–1,200        | Contextualisation team               | Recommended | planned | Final datasets       |
| DATA-08 | Changelog                 | `pages/data/changelog.md`               | What changed in data, models and platform?                     | Ongoing          | Editorial team          | Recommended | planned | Release process      |

## 8. Resources

| ID     | Page                         | File                                  | Purpose / key questions                                          | Suggested length | Owner / source     | Priority    | Status  | Dependencies         |
| ------ | ---------------------------- | ------------------------------------- | ---------------------------------------------------------------- | ---------------- | ------------------ | ----------- | ------- | -------------------- |
| RES-01 | Resources                    | `pages/resources/index.md`            | Introduce the wider resource collection                          | 300–500          | Editorial team     | Recommended | planned | —                    |
| RES-02 | VOC guide                    | `pages/resources/voc-guide.md`        | Provide historical orientation for users unfamiliar with the VOC and its archives | 500–1,000        | Manjusha           | Essential   | planned | Existing guide       |
| RES-03 | Bibliography                 | `pages/resources/bibliography.md`     | Provide a curated reading list                                   | Variable         | Editorial team     | Recommended | planned | Bibliography         |
| RES-04 | Related projects & databases | `pages/resources/related-projects.md` | Point users towards complementary resources                      | Variable         | Editorial team     | Recommended | planned | Curated list         |
| RES-05 | Podcasts                     | `pages/resources/podcasts.md`         | Relevant existing podcasts and audio resources                   | Variable         | Editorial team     | Recommended | planned | External links       |
| RES-06 | Videos                       | `pages/resources/videos.md`           | Short videos introducing the VOC and Globalise                   | Variable         | Manjusha / Melinda | Recommended | planned | Video production     |
| RES-07 | Interviews                   | `pages/resources/interviews.md`       | Researcher and community perspectives                            | Variable         | Community partners | Later       | planned | Community discussion |

## 9. Contact & feedback

| ID         | Page               | File                | Purpose / key questions                                 | Suggested length | Owner / source     | Priority  | Status  | Dependencies              |
| ---------- | ------------------ | ------------------- | ------------------------------------------------------- | ---------------- | ------------------ | --------- | ------- | ------------------------- |
| CONTACT-01 | Contact & feedback | `pages/contact.md`  | Who can users contact and how can they report problems? | 300–500          | Editorial team | Essential | planned | Post-project arrangements |


## 10. Legal & footer

| ID       | Page                    | File                     | Purpose / key questions                                               | Owner                    | Priority  | Status  | Dependencies           |
| -------- | ----------------------- | ------------------------ | --------------------------------------------------------------------- | ------------------------ | --------- | ------- | ---------------------- |
| LEGAL-01 | Privacy                 | `legal/privacy.md`       | Explain applicable processing of personal data                        | Huygens/KNAW             | Essential | planned | Institutional guidance |
| LEGAL-02 | Cookies                 | `legal/cookies.md`       | Explain cookies and analytics                                         | Huygens/KNAW             | Essential | planned | Analytics decision     |
| LEGAL-03 | Accessibility statement | `legal/accessibility.md` | Explain accessibility commitments, limitations and reporting route    | Huygens/KNAW + Globalise | Essential | planned | Accessibility audit    |
| LEGAL-04 | Disclaimer              | `legal/disclaimer.md`    | Explain responsibility and limitations                                | Huygens/KNAW             | Essential | planned | Legal review           |
| LEGAL-05 | Colophon                | `legal/colophon.md`      | Credit people, institutions, software, datasets, licences and funding | Project team             | Essential | planned | Final credits          |

## Cross-cutting content

Some information should not live on only one page.

### Content warning

A concise warning should appear prominently on Home (the landing page) and where users encounter potentially sensitive archival material. It should link to the fuller explanation under Ethics & Colonial Context.

### Citation

Citation guidance should be available from the Learn section and linked from document, entity and data views where relevant.

### Bias and limitations (optional)

Relevant limitations could be linked contextually from search results, document/entity views and data documentation rather than being confined to the Ethics section.

### Licensing

Licence information should be visible wherever downloads or reusable data are offered.

### Related content

The `related` metadata field should be used to connect Collections, Themes, Resources and supporting documentation.

## Editorial architecture

The portal should make three different user needs visible:

### Learning to use Globalise

**Learn & Get Started**

“How do I operate the tool?”

### Understanding Globalise

**About + Ethics & Colonial Context + Data & Documentation**

“What is this data, how was it produced, and what does it mean?”

### Researching with Globalise

**Collections + Themes**

“How can I use this material to investigate historical questions?”

## Future additions

The following may be added later rather than being treated as launch-critical:

* Teaching resources
* Interviews
* Additional videos
* More Collections
* More Themes
* Advanced technical documentation
* Additional research workflows
* Community-contributed content
