---
title: "Searching"
subtitle: ""
summary: "How to search the Globalise portal using full text, metadata and entities."
type: "tutorial"
slug: "searching"
status: "draft"

authors: []
datePublished: ""
dateUpdated: "2026-11-13"

featured: false

hero:
  src: ""
  alt: ""
  caption: ""
  credit: ""
  source: ""
  licence: ""

related: []
---

# Searching

<!-- TODO: describe full-text search and search syntax, searching metadata, and searching by entities from the reference data. -->

## Spelling variants and query expansion

<!-- Sources: Kweepeer README and man pages (https://github.com/knaw-huc/kweepeer); issue globalise-huygens/glob-portal-infomodel#97; responses of the production service https://kweepeer.globalise.nl, retrieved 2026-11-13. -->

The VOC archives were written before Dutch spelling was standardised. The same word can appear as *kruidnagel*, *kruydnaghel* or *crujdnaeghelen*. The automatic transcription adds variants of its own: misread letters, or punctuation attached to a word. If you search for one spelling only, you miss passages that use another.

The portal therefore **expands** the words in your search with other spellings and word forms. It keeps the word you typed and adds the expansions as alternatives, so a passage is found if it contains any of them. The expansions come from two sources.

**Historical spellings from the INT Historical Lexicon.** This lexicon of the [Instituut voor de Nederlandse Taal](https://ivdnt.org/) lists how Dutch words were spelt and inflected in historical texts. For each word in your search, the portal adds all the forms the lexicon gives. These are reliable, but the lexicon covers general historical Dutch: it does not know every word used in the VOC archives.

**Spellings from the VOC archives, found with word embeddings.** The second source is a model trained on the transcriptions of the VOC archives themselves. It has learned which words occur in similar contexts, and for each word in your search it adds the ten words that are most similar. Because it learned from the transcriptions, it finds spellings that occur in this archive, including words that the automatic transcription misread. But words that occur in similar contexts are not always the same word: the model also suggests related words with a different meaning.

### Examples

| You search for | INT Historical Lexicon adds | Word embeddings add (a selection) |
| --- | --- | --- |
| *kruidnagel* (clove) | *crujdnaeghelen, kruidnagelen, kruydnaghel, kruyt-nagelen* | *kruidnagelen, kruidt, kruid, buskruidt, kruidtoren, kruidkamer* |
| *nagel* (nail, clove) | 21 forms, such as *naegel, naeghel, naghel, naghelen, nagle, negele* | *nagul, nagell, nagelbom, nagelBoomen* |
| *slaaf* (enslaved person) | *slaaven, slaef, slaeve, slave, slaven* | *slaaff, slaav, slaafe, slaef, Claaf* |
| *verongelukt* (wrecked, perished) | nothing | *verongeluckt, verongelukde, verongeluken, verongeluk* |

These examples show the strengths and weaknesses of each source:

* The lexicon gives genuine historical spellings, such as *kruydnaghel* and *slaeve*, but has nothing for *verongelukt*.
* The word embeddings find spellings the lexicon does not have, and misreadings of the automatic transcription, such as *Claaf* for *slaaf*.
* The word embeddings also suggest words that do not mean the same thing. For *kruidnagel* they suggest *buskruidt* (gunpowder) and *kruidtoren* (powder magazine), because these share part of the word. A search for cloves would then also find passages about gunpowder.

The expansions may change when the lexicon or the model is updated.

### Choosing which expansions to use

The portal shows which words in your search were expanded, and with which forms. You decide which expansions to use. You can switch expansion on or off:

* for each word in your search;
* for each source (the INT Historical Lexicon or the word embeddings);
* for each expanded form.

<!-- TODO: describe step by step how to view and switch off expansions in the search interface, with a screenshot, once the interface is final. -->

Switch expansions off when they bring in words with another meaning, as with *kruidnagel* above, or when you are interested in one particular spelling. Leave them on when you want to find as many passages as possible, for example when you explore a subject or count how often something is mentioned.

Only words you type are expanded. When you search for a person, place or other entity chosen from the reference data, the portal searches for that entity, not for its name as a word.

### Good to know

* Expansion does not find every variant. If you know other spellings, add them to your search yourself.
* Check the results. With expansions switched on, highlighted words in the results may be expansions rather than the word you typed.
* A search that finds nothing, even with expansion, does not prove that something is not in the archive. See [Bias & limitations](/pages/research-responsibly/ethics/bias-and-limitations.md#query-expansion).

The query expansion is done by Kweepeer, software developed for Globalise by the KNAW Humanities Cluster. See [Technical documentation](/pages/research-responsibly/data/technical-documentation.md#query-expansion) for how it works.
