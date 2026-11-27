# Globalise Research Portal Content

This repository contains the editorial source content for the Globalise research portal.

The website content is maintained as Markdown files with YAML front matter and can (in the future...) be processed by the portal's static-site generator.

## Portal structure

The navigation bar has four sections. Each corresponds to a folder under `pages/`; Home sits outside them.

| Navigation | Folder | Contents | Priority |
| --- | --- | --- | --- |
| [Home](pages/home.md) | `pages/home.md` | Introduce Globalise and provide entry points into search, the data and research guides | Essential |
| [Explore](pages/explore/index.md) | `pages/explore/` | Entry points into the archive and the reference data, and [Research guides](pages/explore/research-guides/README.md) by researchers | Essential |
| [Learn & get started](pages/learn-get-started/index.md) | `pages/learn-get-started/` | How to use the portal (searching and browsing, using an AI assistant via the MCP server, research workflow, citation guide, licences and reuse), plus [Resources](pages/learn-get-started/resources/index.md): bibliography, related projects, and videos | Essential |
| [About GLOBALISE](pages/about/index.md) | `pages/about/` | What Globalise is, its ambitions and position, methods, outputs, team & partners, and an [Archive](pages/about/archive/index.md) of project documents and blog posts | Essential |
| [Research responsibly](pages/research-responsibly/index.md) | `pages/research-responsibly/` | [Ethics & colonial context](pages/research-responsibly/ethics/index.md), the [guide to the VOC archives](pages/research-responsibly/voc-archives-guide.md) and [Data & documentation](pages/research-responsibly/data/index.md) | Essential |
| Footer | `pages/footer/` | Contact, release notes, privacy, cookies, accessibility, disclaimer and colophon | Essential |

Folder names determine where a file lives, not necessarily the final URL. Navigation labels may change; keep URLs short and topic-based (e.g. `/ethics/policy`, `/data/overview`) so that renaming a navigation item does not break links.

See [CONTENT.md](CONTENT.md) for the detailed editorial production plan.

## Repository structure

```text
pages/
├── home.md
│
├── explore/
│   ├── index.md
│   └── research-guides/
│       ├── README.md
│       └── <one file per guide>.md
│
├── learn-get-started/
│   ├── index.md
│   ├── searching-browsing/
│   │   ├── index.md
│   │   ├── searching.md
│   │   ├── facets.md
│   │   ├── browsing.md
│   │   └── results.md
│   ├── ai-assistant.md
│   ├── research-workflow.md
│   ├── citation.md
│   ├── licences.md
│   └── resources/
│       ├── index.md
│       ├── bibliography.md
│       ├── related-projects.md
│       └── videos.md
│
├── about/
│   ├── index.md
│   ├── what-is-globalise.md
│   ├── ambitions.md
│   ├── position.md
│   ├── methods.md
│   ├── outputs.md
│   ├── team.md
│   └── archive/
│       ├── index.md
│       ├── mission-research-themes.md
│       ├── ethics-policy.md
│       └── blog/
│           └── <one file per archived blog post>.md
│
├── research-responsibly/
│   ├── index.md
│   ├── voc-archives-guide.md
│   ├── ethics/
│   │   ├── index.md
│   │   ├── policy.md
│   │   ├── colonial-context.md
│   │   ├── bias-and-limitations.md
│   │   └── responsible-use.md
│   └── data/
│       ├── index.md
│       ├── overview.md         (what's in the data)
│       ├── access.md
│       ├── production.md
│       ├── data-model.md
│       ├── event-ontology.md
│       ├── technical-documentation.md
│       └── reference-data.md
│
└── footer/
    ├── contact.md
    ├── release-notes.md
    ├── privacy.md
    ├── cookies.md
    ├── accessibility.md
    ├── disclaimer.md
    └── colophon.md

templates/
├── standard-page.md
├── collection.md
├── theme.md
└── tutorial.md

scripts/
└── render_bibliography.py   (renders the bibliography page from references.bib)

assets/
├── images/
│   ├── README.md
│   ├── image-metadata.yml
│   ├── about/archive/                 (images for the archived pages in pages/about/archive/)
│   └── resources/voc-archives-guide/  (images for pages/research-responsibly/voc-archives-guide.md)
├── references/
│   └── references.bib
└── videos/
    └── README.md
```

Image folders follow the original page locations and have not been moved with the pages; page links point to them directly.

See [SITEMAP.md](SITEMAP.md) for the site's navigation structure.

## Content workflow

The repository is both a content repository and an editorial workspace.

The basic workflow is:

1. Create a GitHub Issue describing the content task.
2. Assign the issue to the relevant contributor.
3. Draft or edit the relevant Markdown file.
4. Open a Pull Request referencing the issue.
5. Request editorial and/or subject-matter review.
6. Address review comments.
7. Merge the Pull Request when approved.
8. The static-site build processes the approved content.

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## Page metadata

Each page uses YAML front matter containing information such as:

* title and subtitle
* summary
* content type
* slug
* editorial status
* authors
* publication/update dates
* featured status
* hero image information
* related content

See [CONTENT-METADATA.md](CONTENT-METADATA.md) for the metadata schema.

## Editorial principles

The portal should:

* be accessible to users who are not specialists in Dutch early-modern history;
* distinguish clearly between archival sources and Globalise-generated data;
* make computational methods and their limitations transparent;
* contextualise colonial terminology and categories;
* avoid presenting computational classifications as neutral or objective historical facts;
* provide clear routes from discovery to the underlying archival source;
* support scholarly citation and responsible reuse.

## Content status

Content uses the following status values:

* `planned` — identified but not yet being drafted
* `draft` — initial content exists
* `review` — ready for editorial or subject-matter review
* `approved` — approved for publication
* `published` — live on the portal
* `later` — useful but not required for the initial launch

The detailed status of pages is maintained in [CONTENT.md](CONTENT.md).

## Related documentation

* [Sitemap](SITEMAP.md)
* [Content production plan](CONTENT.md)
* [Content metadata](CONTENT-METADATA.md)
* [Contribution guidelines](CONTRIBUTING.md)
* [Editorial style guide](STYLEGUIDE.md)
* [Page templates](templates/)
