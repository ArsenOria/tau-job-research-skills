# Tau Skills search positioning — November 13, 2026

The primary search hypothesis is **“linkedin job search skill for claude”**, supported by a useful [Claude Code setup guide](claude-linkedin-job-search.md). **“codex job search skill”** is a secondary host-specific guide. These are opportunities to test, not measured low-difficulty keywords or ranking promises. The README heading “LinkedIn Job Search Skills” describes the product; the narrower query's competition findings do not establish the competition for that broader heading.

## What was checked

- Actual Google desktop results for the queries below, with `hl=en`, `gl=us`, `pws=0`, on November 13, 2026. This is a dated first-page sample, not a complete ranking census or a guarantee of depersonalization. Search results can vary by location, device, time and query rewriting.
- Public Google Autocomplete, requesting English without account cookies. Country was not pinned. Suggestions are a qualitative query-pattern proxy, not monthly volume. Google's [explanation of predictions](https://support.google.com/websearch/answer/7368877?hl=en) includes both searches and web language patterns among its signals.
- Public GitHub repository/API snapshots for popularity and adjacent intent. Stars help identify visible adjacent projects; they are not Google's ranking metric or a keyword-difficulty score. Listings in a directory can bring a large repository into competition even when the GitHub URL is absent.
- A public Trends request returned HTTP 429; no usable series was collected and no restriction was bypassed. **Monthly search volume, Trends growth and numeric keyword difficulty remain unknown.** No paid keyword-tool or advertising account was accessed.

## Actual Google observations

| Exact query checked | Observed first-page competition | Decision |
|---|---|---|
| [linkedin job search skill for claude](https://www.google.com/search?q=linkedin+job+search+skill+for+claude&hl=en&gl=us&pws=0) | MCPMarket's LinkedIn job-search skill; LinkedIn posts; Reddit discussion; GetClaudeSkills' BrowserAct skill; a Substack article and YouTube video. No directly surfaced GitHub repository above 10k stars was observed in this sample. The BrowserAct source repository has **6,348 stars**, so competition is material. | Primary narrow guide to test. Medium/uncertain competition, not an empty market. Claude Code end-to-end validation is explicitly pending. |
| [codex job search skill](https://www.google.com/search?q=codex+job+search+skill&hl=en&gl=us&pws=0) | SongMarco/codex-job-finder first among observed GitHub results, plus ItsBlurf/codex-job-search-assistant. Also career-ops.org, Reddit, videos, official docs, Composio and a directory listing for the much larger ai-job-search project; career-ops appeared in the AI overview. | Secondary guide matching the host actually exercised here. Large adjacent competitors remain present. |
| [job search skills claude github](https://www.google.com/search?q=job+search+skills+claude+github&hl=en&gl=us&pws=0) | ai-job-search-dev/ai-job-search (~71k stars), proficientlyjobs/proficiently-claude-skills and career-ops-hq/career-ops (~82k) among the leading organic results. | Reject as the primary acquisition target: popular repositories address closely related job-search intent. |
| [job research skills for ai chat](https://www.google.com/search?q=job+research+skills+for+ai+chat&hl=en&gl=us&pws=0) | General AI research libraries, including orchestra-research/AI-research-SKILLs, and broader research/career content. | Retire the old primary phrase: weak alignment with job-search installation intent, with no Autocomplete suggestions observed. |

The narrow Claude query also produced questions about using Claude for LinkedIn job search and whether Claude has a LinkedIn skill. These are useful content ideas, not search-volume estimates. The links above rerun live queries; they are not archived SERP evidence.

## Demand proxies and rejected alternatives

The public [Autocomplete endpoint](https://suggestqueries.google.com/complete/search?client=firefox&hl=en&q=codex%20job%20search) returned `codex job search skill` for the prefix `codex job search`. `claude code job search` produced variants including `skill`, `agent`, `github`, `reddit` and `plugin`. `job search skills claude` produced the base phrase and `claude code job search skills`. The exact narrow LinkedIn/Claude query returned a singleton matching the query; that is a weaker signal than multiple related suggestions and cannot establish substantial demand.

| Candidate family | Evidence and intent | Use |
|---|---|---|
| LinkedIn job search skill for Claude | Exact singleton suggestion; dated Google sample has directories/discussions and a material 6k-star source competitor, without the 70k–80k-star repositories directly visible. | Useful local Claude Code setup guide with validation limits. |
| Codex job search skill | Generated from the shorter `codex job search` prefix; actual Google still includes career-ops and a large-project directory listing. | Secondary Codex guide and README link. |
| Claude code job search / Claude job search skills | Multiple suggestions, but broad nearby intent faces the large incumbents seen above. The exact shorter variants were not separately validated as low-competition Google queries. | Natural context only; no low-competition claim. |
| Company research skill | Suggestions include business research, resume and example intents; a general web-search engine also surfaced the 8,007-star Product-Manager-Skills collection. That engine's results were not treated as Google ranks. | Feature description, not the primary target. |
| Claude resume analysis | Suggestions lean toward prompts and summaries, rather than installing research skills. | Do not target as the main product promise. |
| Job fit analysis skill / CV job matching Claude | No suggestions observed; no Google competition conclusion established. Absence of suggestions does not prove zero searches. | Do not promote as demand-validated keywords. |

## Adjacent repository snapshots

Stars below are dated November 13, 2026; counts change. Compare actual capabilities before treating a project as equivalent.

| Repository | Stars | Relevance |
|---|---:|---|
| [browser-act/skills](https://github.com/browser-act/skills) | 6,348 | Source of the BrowserAct skill directory result; material LinkedIn/browser-automation adjacency. |
| [proficientlyjobs/proficiently-claude-skills](https://github.com/proficientlyjobs/proficiently-claude-skills) | 459 | Job-search skills appearing in the broad actual Google sample. |
| [sameergdogg/job-search-skills](https://github.com/sameergdogg/job-search-skills) | 21 | Adjacent analyzer/crawler/application workflow found through a separate web-search engine. |
| [SongMarco/codex-job-finder](https://github.com/SongMarco/codex-job-finder) | 1 | Small direct Codex job-search result in the observed Google sample. |
| [ItsBlurf/codex-job-search-assistant](https://github.com/ItsBlurf/codex-job-search-assistant) | 7 | Another direct Codex result in the observed Google sample. |
| [rubenviolinha/linkedin-job-search-skill](https://github.com/rubenviolinha/linkedin-job-search-skill) | 0 | Small direct Claude/LinkedIn skill found through a separate web-search engine; absence from the observed Google sample is not proof of no competition. |

The large [ai-job-search](https://github.com/ai-job-search-dev/ai-job-search) and [career-ops](https://github.com/career-ops-hq/career-ops) repositories are why broad Claude job-search positioning was rejected. Their presence through directories, homepages or AI overviews also matters.

## Content and product boundaries

Use relevant language in the title, opening explanation, banner accessibility text, installation guide and helpful chat examples. Do not repeat the exact query throughout unrelated files or change skill behavior to insert keywords. Keep existing repository URLs stable and link the two companion modules clearly.

The guide answers a specific installation and workflow question. It does not claim Claude validation that has not happened, support for every chat client, or official LinkedIn authorization. Tau Skills reasons over evidence; Scout optionally obtains listings with the user's Apify account. Neither applies, sends outreach or logs in to LinkedIn.

After publication, evaluate actual indexing and qualified usage when data is available. No Search Console ownership, measured impressions, clicks, monthly search volume or ranking improvement was established in this research.
