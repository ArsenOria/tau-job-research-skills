# Skills with live Scout results — 2026-11-11

## Test boundary

The chat agent read and applied all six skill files to one real Scout/Apify query, using the repository's clearly synthetic candidate summary. This is a live integration exercise, not a test of the user's career preferences or automatic skill discovery in every host. The MCP client was a private operator harness. Setup and credential handling were outside the chat; no credentials or raw datasets are included in this repository.

The query was Product Analyst in Berlin, Germany, past week, up to five results, with a USD 0.10 run cap and Easy Apply optional. One Actor run completed in 23.71 seconds and reported `usageTotalUsd` of USD 0.0056. All five jobs were saved after correcting regional LinkedIn URL handling in Scout. The same plan was reused without starting another Actor run.

## Skills exercised

| Skill | Actual application |
|---|---|
| `job-search-brief` | Used the synthetic summary's SQL, Python, experiments and dashboard evidence. Kept its Germany/remote preference distinct from the real user's preferences. No personal CV was sent to Apify. |
| `linkedin-search-plan` | Prepared a bounded Berlin/past-week plan, disclosed caps before the start, and left Easy Apply optional. |
| `job-research` | Used real MCP discovery, source status, preparation, one Actor start, polls, saved results, explicit same-run refresh and repeat-plan reuse. Did not invent rows when the first mapping lost four results. |
| `fit-review` | Compared description requirements to the synthetic candidate and separated logistical conflicts and unproven domain experience from lexical scores. |
| `company-brief` | Identified Kaufland e-commerce from the role, read its official About page and inspected its Personio careers board. Kept inaccessible role-detail pages unverified. |
| `shortlist-review` | Used local SQL and workplace filters, then inspected source descriptions instead of presenting an empty structured remote filter as proof of no remote roles. |

## Evidence-based review beyond keyword scores

Scout ranked four of the observed roles at the same lexical relevance of 80 and the quantitative role at 50. Those scores did not settle the recommendation:

- **Kaufland e-commerce:** the saved role description supported SQL/Python, experimentation and remote work within Germany. For the synthetic candidate, mobile-app analytics and Adobe Analytics experience remained unproven. The employer's [Personio board](https://real-digital.jobs.personio.com/?language=en) listed the role during the check, but its linked detail page could not be retrieved successfully; present availability was not certified.
- **SumUp:** the observed description matched product analytics and experimentation but explicitly described an office-first Berlin arrangement. That conflicts with the synthetic candidate's remote preference despite a high lexical score.
- **Voodoo:** the observed description offered remote work in a CET ±3-hour range but requested gaming-domain experience that the synthetic summary did not establish. Time-zone compatibility alone did not prove country/employment eligibility.

These are bounded evaluations of saved source descriptions at the test date. They are not personalized recommendations for the real user, claims about missing abilities, or interview probabilities. Full copyrighted job descriptions are not republished here.

## Company research and source uncertainty

The [official Kaufland e-commerce About page](https://kaufland-ecommerce.com/en/about-us/) identified the marketplace technology business, its relationship to Schwarz Group, and its Germany-limited remote arrangement. The careers board listed Product Analyst — Mobile App. The old company-hosted role URL returned a retrieval error/404; the linked Personio detail page also could not be read successfully. The agent therefore kept the board listing, observed description and unreadable detail page as distinct evidence, rather than declaring a verified open vacancy or assuming closure from one failed page.

No funding safety, runway, salary or sponsorship policy was inferred from company marketing or absent fields.

## Changes and remaining limits

The bundled tool reference now documents `refresh_results` and regional URL canonicalization. The shortlist skill explicitly handles descriptions whose remote policy is missing from structured fields. The six package validators and independently installable ZIPs are rerun and regenerated after these changes.

No automatic LinkedIn login, application or outreach was attempted. This single query does not prove source completeness, continuous freshness, universal host compatibility or that structured Actor metadata is complete.
