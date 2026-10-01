# Content Metadata

## Pages

The page front matter uses YAML. The schema has been slightly expanded from the initial proposal to make it useful for a static-site build and editorial workflow.

### Fields

| Field | Required | Purpose |
|---|---|---|
| `title` | Yes | Human-readable page title |
| `subtitle` | No | Optional subtitle shown near the title |
| `summary` | Yes | Short description for cards, search results and metadata |
| `type` | Yes | Content type, e.g. `page`, `collection`, `theme`, `tutorial`, `resource-list`, `legal`, `archived-post` |
| `slug` | Yes | Stable URL/content identifier (NOTE: what kind of URL structure?) |
| `status` | Yes | Editorial/publishing status |
| `authors` | Yes | List of contributor IDs; keep IDs stable |
| `datePublished` | No | Publication date; leave empty until published; use ISO 8601 dates: `YYYY-MM-DD` |
| `dateUpdated` | No | Date of most recent substantive update; Use ISO 8601 dates: `YYYY-MM-DD` |
| `featured` | Yes | Whether the page is eligible for featured placement |
| `hero` | Yes | Structured hero image metadata. Fill in `src`, `alt`, `caption`, `credit`, `source` and `licence` |
| `related` | No | List of related content slugs |
| `originalPublication` | For `archived-post` | Where and when an archived text was first published: `url` and `date` (`YYYY-MM-DD`) |

## Images

For images other than the hero image (whose metadata is included in the page metadata – see above), provide metadata in `/assets/images/image-metadata.yml`. On the content page, only include the image path, alt text and (where appropriate) caption.

### Fields

| Field | Required? | Description | Example |
|---|---|---|---|
| `id` | Yes | Unique identifier for the image. | `"padtbrugge-1677-01"` |
| `file` | Yes | Path to the image file within the repository. | `"/images/collections/voyages/padtbrugge-1677-01.jpg"` |
| `title` | Recommended | Short descriptive title for the image. | `"Journal of Robertus Padtbrugge, 1677"` |
| `credit` | Yes | Person, institution or collection to be credited for the image. | `"Nationaal Archief"` |
| `source` | Recommended | URL or other source from which the image was obtained. | `"https://www.nationaalarchief.nl/..."` |
| `licence` | Yes | Copyright or reuse licence, or statement of rights status. | `"Public Domain"` |
| `creator` | If known | Creator, photographer, artist or author of the original image/document. | `"Robertus Padtbrugge"` |
| `date` | If known | Date or date range associated with the original image/document. | `"1677–1679"` |
| `archival_reference` | If applicable | Reference to the archival source represented by the image. | `"NL-HaNA, VOC, 1.04.02, inv. 1234"` |
| `rights_note` | If needed | Additional information about copyright, permissions or restrictions. | `"Reproduction permitted for non-commercial research."` |
| `notes` | Optional | Other relevant provenance or editorial information. | `"Detail cropped from the original scan."` |