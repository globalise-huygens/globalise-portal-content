# Globalise Research Portal Content

This repository contains the editorial source content for the Globalise research portal.

The website content is maintained as Markdown files with YAML front matter and can (in the future...) be processed by the portal's static-site generator.

## Portal structure

| Section                                            | Purpose                                                                          | Priority    |
| -------------------------------------------------- | -------------------------------------------------------------------------------- | ----------- |
| [Home](pages/home.md)                              | Introduce Globalise and provide entry points into search, Collections and Themes | Essential   |
| [Collections](pages/collections/README.md)         | Provide structured entry points into selected categories of Globalise material   | Essential   |
| [Themes](pages/themes/README.md)                   | Demonstrate how Globalise can be used to investigate specific historical themes  | Essential   |
| [Learn & Get Started](pages/learn/index.md)        | Teach users how to use the portal effectively                                    | Essential   |
| [About Globalise](pages/about/index.md)            | Explain the project, archive, methods, outputs and team                          | Essential   |
| [Ethics & Colonial Context](pages/ethics/index.md) | Explain colonial context, ethics, bias and limitations                           | Essential   |
| [Data & Documentation](pages/data/index.md)        | Explain Globalise data, methods, models and access                               | Essential   |
| [Resources](pages/resources/index.md)              | Provide historical, research and media resources                                 | Recommended |
| Legal & footer pages                               | Provide institutional, legal, accessibility and attribution information          | Essential   |

See [CONTENT.md](CONTENT.md) for the detailed editorial production plan.

## Repository structure

```text
pages/
├── home.md
├── about/
│   ├── index.md
│   ├── project.md
│   ├── ambitions.md
│   ├── methods.md
│   ├── outputs.md
│   └── team.md
│
├── learn/
│   ├── index.md
│   ├── getting-started.md
│   ├── searching.md
│   ├── facets.md
│   ├── semantic-search.md
│   ├── browsing.md
│   ├── results.md
│   ├── documents.md
│   ├── research-workflow.md
│   └── citation.md
│
├── ethics/
│   ├── index.md
│   ├── ethics-policy.md
│   ├── colonial-context.md
│   ├── bias-and-limitations.md
│   └── responsible-use.md
│
├── data/
│   ├── index.md
│   ├── data.md
│   ├── access.md
│   ├── licences.md
│   ├── production.md
│   ├── technical-documentation.md
│   ├── reference-data.md
│   └── changelog.md
│
├── resources/
│   ├── index.md
│   ├── voc-archives-guide.md
│   ├── bibliography.md
│   ├── related-projects.md
│   ├── podcasts.md
│   ├── videos.md
│   └── interviews.md
│
├── collections/
│   └── README.md
│
└── themes/
    └── README.md

legal/
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

assets/
├── images/
└── videos/
```

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

* [Content production plan](CONTENT.md)
* [Content metadata](CONTENT-METADATA.md)
* [Contribution guidelines](CONTRIBUTING.md)
* [Editorial style guide](STYLEGUIDE.md)
* [Page templates](templates/)
