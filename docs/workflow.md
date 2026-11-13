# Job research skills for AI chat: the Tau workflow

Tau's job research skills for AI chat guide the conversation from a CV and preferences to an evidence-based job shortlist. The host assistant supplies the chat, attachment reader and reasoning. Tau Scout supplies the local LinkedIn job research MCP tools; Apify is an optional external vacancy source. No second LLM API key or Tau account is needed.

| Step | Assistant's job | Scout tool, if connected |
|---|---|---|
| Understand | Read the CV, distinguish preferences from inferred role suggestions, ask only missing material questions | None |
| Plan | Show roles, locations, source and caps; keep CV/contacts out of provider search fields | `prepare_search` |
| Discover | Start the requested search; keep its identity through follow-up calls | `search_jobs` |
| Read | Poll the same run once per call and describe pending, failed or incomplete states honestly | `get_search_status`, `get_saved_results` |
| Compare | Use heuristic ordering as an aid, then compare actual requirements with CV evidence | `rank_jobs` |
| Refine | Reuse saved data for supported filters; explain when a new paid search is needed | `refine_shortlist` |
| Investigate | Research companies with public-web tools; separate findings from unavailable evidence | None in Scout |

Scout's successful output includes `ok: true` and `contract_version: "0.3"`. A response with `ok: false` is an error, not zero jobs. Each tool's discovered schema is authoritative for arguments. See the [bundled tool reference](../skills/job-research/references/scout-tools.md) for the v0.3 snapshot, including student-program eligibility, publication provenance and employer identity.

`start_uncertain` means the provider may have started a paid run but Scout did not receive its identity. Stop automatic paid retries and explain how the user can inspect the run in Apify Console. `results_unavailable` means the same run's results could not be read; polling it again may retry reading without starting a new run. Do not prepare a new plan to sidestep either state silently.

Most refinements should not cost anything. Removing titles or companies from the saved set is local. Changing to a new geography may need a new search; disclose that before using another plan. Scout cannot enforce company headcount or agency classification as structured filters. The assistant may review available evidence manually and label unknowns.

Every shortlist distinguishes the source and observation time from a vacancy's posted date and independent verification time. A received Actor row is an observed listing. A successfully fetched page is evidence at the time checked, not a guarantee the role will remain open.

The user opens vacancies and sends applications themselves. No skill or Scout tool applies, messages, connects to a LinkedIn account or schedules background work.
