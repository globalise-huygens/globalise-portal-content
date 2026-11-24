---
title: "Using Globalise with an AI assistant"
subtitle: ""
summary: "How to connect an AI assistant to the Globalise MCP server, what you can ask it, and how to check its answers."
type: "tutorial"
slug: "ai-assistant"
status: "draft"

authors: []
datePublished: ""
dateUpdated: "2026-11-23"

featured: false

hero:
  src: ""
  alt: ""
  caption: ""
  credit: ""
  source: ""
  licence: ""

related: ["accessing-the-data", "bias-and-limitations", "citation-guide"]
---

# Using Globalise with an AI assistant

<!-- Sources: README and source code of https://github.com/globalise-huygens/globalise-mcp (version 0.1.0, retrieved 2026-11-12), in particular src/knowledge.ts (the documentation the server gives the assistant), src/server.ts and the tool definitions; test queries against the development server, 2026-11-12. Technical details such as the transport and rate limits are on the Accessing the data page; this page is for users without a technical background. -->

<!-- TODO: the MCP server is a prototype (version 0.1.0) and runs against work-in-progress search indices. Check this page against the server as it is at launch. -->

You can ask an AI assistant, such as Claude or ChatGPT, to search the Globalise data for you. You ask a question in your own words; the assistant searches the transcriptions and reference data, reads the documents and checks the scans, and reports what it found, with links to the pages it used.

This can save time, especially when you are exploring a subject or need to try many spellings. But an AI assistant adds its own layer of interpretation, and it makes mistakes. Treat its answers as leads to check, not as findings.

## What you will learn

* what the Globalise MCP server is and what it gives your assistant access to;
* how to connect your assistant to it;
* what kinds of questions work well;
* how to check the answers, and how to cite what you found.

## What the MCP server is

An AI assistant does not know the VOC archives. Without help, it answers from what it picked up during training, which may be incomplete, outdated or wrong. The **Globalise MCP server** lets it look things up in the Globalise data instead. MCP (Model Context Protocol) is an open standard for connecting AI assistants to external sources of information.

Once connected, the assistant can:

* search the transcriptions, by words and spelling variants, but also by tagged people, places and events, by date, place of writing, inventory number and document type;
* read a whole document, with the entities and events recognised in it;
* look at a single scan: its transcription, its annotations and the image itself, including a close-up of a quoted passage;
* look up people, places, ships, organisations, polities and concepts in the reference data;
* count documents and mentions, and compare them with the size of the corpus in each decade, settlement or document type.

This is the same data that you see on the portal, with the same limitations: transcriptions and annotations made by computer models, and an archive written from the perspective of the VOC. The server only reads data; it cannot change anything. You do not need an account.

Before it starts searching, the assistant receives background information from the server on how the data is organised, how to search it and what its limitations are, with links to the pages on this website that explain them. Whether and how well the assistant uses that information depends on the assistant.

## Connecting an AI assistant

Your assistant must support adding an MCP server, often called a *custom connector*, *remote MCP server* or *integration*. To connect it:

1. Open the settings of your assistant and find the option to add a connector or MCP server.
2. Enter the address of the Globalise MCP server: `https://globalise.nl/mcp`
3. Give it a name, such as *Globalise*, and save. No login is needed.
4. Start a new conversation and check that the Globalise tools are switched on.

<!-- TODO: https://globalise.nl/mcp does not work yet. Check that the address works once the server is hosted, and whether it is http or https. -->

<!-- TODO: check which AI assistants (e.g. Claude, ChatGPT, Le Chat, Copilot, Cursor, VS Code) work with the server, on which plans, and add short step-by-step instructions, with screenshots, for the ones we support. -->

If your assistant offers prompts, choose **Research a question in the VOC archives**. It asks for your question and instructs the assistant to work step by step: check the evidence on the scans, cite every claim, and end with the limitations that apply.

Developers who want to run the server on their own computer can find instructions under [Accessing the data](/pages/research-responsibly/data/access.md#mcp-server).

## What you can ask

You can ask in English or another language. The archive is written in early modern Dutch, with many spellings for the same word; a good assistant translates your terms into period spellings and tries several variants. Ask it to show which searches it used.

Questions that work well:

* **Finding documents.** *Find letters written from Ceylon in the 1650s that mention cinnamon.* *Which documents in inventory 1056 were written in Japan?*
* **Looking something up.** *Which places are called Coromandel in the Globalise place data?* *What does the reference data say about the ship Wapen van Hoorn?* (There are several ships of that name; a good answer says so.)
* **Reading a document.** *Summarise document NL-HaNA_1.04.02_1056_0251-0253 and list the people mentioned.*
* **Patterns over time.** *How often are enslaved people mentioned in documents from the Cape per decade, relative to the number of documents from the Cape?*
* **Checking a passage.** *Show me the passage on the scan where this letter mentions pepper prices.*

<!-- TODO: the example document id comes from the search index of 5 November 2026, which does not yet contain the final document segmentation (issue #24). Check the examples once it does. -->

What it cannot do well:

* answer questions about anything outside the Globalise corpus. If the assistant goes beyond what it found, for instance with background from its own training, ask it to say so;
* prove that something is *not* in the archive. A search that finds nothing may have missed spellings or misread text;
* read pages in non-Latin scripts, such as Chinese or Persian, which the text recognition could not read;
* give reliable translations. The assistant translates and summarises on its own; these translations have not been checked. They are not the same as the machine translations shown in the Globalise viewer, which have not been checked either (see [Bias & limitations](/pages/research-responsibly/ethics/bias-and-limitations.md#translation)).

<!-- TODO: check whether the MCP server returns the viewer's translations (e.g. in get_scan); if so, say here that the assistant can use them, and add them to the tool table on pages/research-responsibly/data/access.md. -->

## Checking the answers

AI assistants make mistakes. They can misread or misquote a transcription, mix up documents, count the wrong thing, overstate what the sources say, and occasionally invent quotations or sources. On top of that, everything they find carries the limitations of the Globalise data itself. See [Bias & limitations](/pages/research-responsibly/ethics/bias-and-limitations.md).

To check an answer:

* **Follow the links.** Every document and scan the server returns comes with an identifier and a link to the portal. Ask for them if the assistant leaves them out, and be wary of any claim that has none.
* **Check the scan.** Transcriptions contain errors, and the assistant's reading of them may too. Open the scan and check quotations, names, numbers and dates yourself.
* **Read the context.** A search result is a small piece of a larger document. Open the document and read the surrounding pages before drawing conclusions. See [Responsible use](/pages/research-responsibly/ethics/responsible-use.md).
* **Ask how it searched.** Ask for the exact searches it used. Results depend on the spellings tried, and you may want to try others.
* **Check what was counted.** Did the assistant count documents or mentions? Raw numbers mostly reflect how much of the archive survives for a period or place; ask for figures relative to the size of the corpus. A single long register or list can dominate a count of mentions.
* **Separate source from interpretation.** Ask the assistant to keep what the documents say apart from its own conclusions. Entities and events are recognised by computer models; do not treat a label such as *Attack* or *Name of Person* as an established fact.

## Citing what you found

Cite the documents and scans, not the conversation. Each answer from the server includes the identifiers of documents and scans and the version of the search index it used; note these down, because the index is updated from time to time. If an AI assistant played a substantial part in your research, say so, and describe how you used it. See the [Citation guide](/pages/learn-get-started/citation.md).

## Privacy

Your questions and the assistant's answers are processed by the company that provides your AI assistant, under its own terms and privacy policy. The Globalise MCP server receives only the requests the assistant sends to it, such as search terms and identifiers, not your conversation.

<!-- TODO: check with the developers and hosting whether requests to the MCP server are logged (the server itself only logs errors; the proxy in front of it may keep access logs), and align with the Privacy page. -->

## Further information

* [Accessing the data](/pages/research-responsibly/data/access.md#mcp-server): technical details of the MCP server
* [Bias & limitations](/pages/research-responsibly/ethics/bias-and-limitations.md)
* [How the data was produced](/pages/research-responsibly/data/production.md)
* [Model Context Protocol](https://modelcontextprotocol.io)
