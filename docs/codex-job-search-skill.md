# Codex job search skill: from CV to shortlist in chat

Tau Skills is a set of six independent skills for researching a job search in Codex. Use the same chat to turn a CV into a search brief, plan LinkedIn queries, compare vacancies and refine a shortlist. Optional [Tau Scout](https://github.com/ArsenOria/tau-linkedin-job-research-mcp) tools fetch listings through your own Apify account.

Codex is the host used in the repository's recorded [native output review](OUTPUT_QUALITY.md). Those dated exercises demonstrate a particular setup and outputs; they do not verify today's openings or guarantee equivalent results in every host version.

## Connect once

Follow [Connect to Codex desktop](../README.md#connect-to-codex-desktop) for the complete setup: copy the individual skill folders to `~/.agents/skills/`, install Scout separately and configure its local stdio MCP connection. Put your own Apify token in the connection's protected environment configuration; never send it in chat. You can use the skills without Scout to analyze supplied vacancies and plan searches.

Start with the free [manual checkpoints](installation.md#manual-checkpoints). Skill discovery, MCP discovery and a successful paid request are separate checks. The daily search workflow uses chat after this one-time setup.

## A conversation to try

> Use job-search-brief. Here is my CV. I am looking for product analyst roles in Berlin or remote within Germany. I can work in Germany without sponsorship. Help me choose target titles, and keep missing facts unknown.

> Use linkedin-search-plan. Turn that brief into focused queries. Do not run a paid search yet.

> Check Scout's connection without showing my token. Then demonstrate the search with synthetic data only, without contacting Apify.

When you want current listings, give a small explicit limit:

> Find up to five roles using my Apify account with a maximum run charge of $0.10. Show the source, search filters and caps before starting. Explain publication-date uncertainty and remote-country eligibility in the shortlist.

Then refine the same results:

> Use fit-review and shortlist-review. Compare the first two vacancies against my CV. Separate confirmed conflicts from unknowns, identify the actual employer where established, and keep recruitment agencies separate. Do not start another search.

The assistant presents original links, source and observation times, stated posting dates when known, fit evidence and unanswered questions. Missing salary or sponsorship stays unknown. A lexical match score is not an interview probability. An Apify result is an observed listing until its current posting is checked independently.

## What the modules do

Skills supply research instructions; Scout supplies local search and saved-result tools. They do not log in to LinkedIn, submit applications, send outreach or monitor in the background. No Tau account or Tau backend is required. See the [full workflow](workflow.md), [Scout connection guide](https://github.com/ArsenOria/tau-linkedin-job-research-mcp#first-connection) and [access boundaries](../README.md#access-and-evidence).
