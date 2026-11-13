# Offline demonstration conversation

This is an illustrative transcript, not a record of a live search or a claim that every AI host has been tested. Use Scout's actual packaged demo to obtain results. Companies and vacancies in demo mode are synthetic; never present their links as opportunities to apply.

**User:** Here is my CV. I use SQL and Python and have designed A/B tests. Find product analyst roles in Berlin or remote from Germany. Use demo data only; do not spend anything.

**Assistant:** I will use synthetic Scout demo data, with no Apify call. I will compare the postings with your stated experience and keep unknown salary and eligibility conditions visible.

Internal tool sequence (not instructions for the user):

1. Discover Scout's schemas; `get_scout_status()`.
2. `prepare_search(brief={"target_titles":["Product Analyst"],"locations":["Berlin, Germany"],"workplace":"any","posted_within":"week","easy_apply_only":false,"max_results":25,"max_charge_usd":0.5}, source="demo")`.
3. `search_jobs(plan_id=<returned plan_id>)`.
4. `get_saved_results(search_id=<returned search_id>)`.
5. `rank_jobs(search_id=<same search_id>, candidate={"skills":["SQL","Python","A/B testing"],"target_titles":["Product Analyst"],"locations":["Germany"],"workplace":"remote","requires_sponsorship":null})`.

**Assistant:** Here is the synthetic shortlist from Scout. The ordering is a keyword/title relevance aid; I will explain the actual requirements separately. A remote label alone does not establish whether employment from Germany is allowed. Salary or sponsorship not stated in a demo row remains unknown.

The actual table uses the jobs returned by the tool, their original links and the relevant description evidence. Do not insert invented result counts, scores, employers or availability labels into a real response.

**User:** Prioritize SQL and remove recruitment agencies.

The assistant reuses the saved search. `refine_shortlist` can include the term `SQL`. Agency classification is not a structured v0.1 filter, so the assistant reviews the descriptions and explains which rows explicitly identify an agency; unknown employers remain in a separate group. It does not silently equate an unfamiliar company name with an agency or run another provider search.

**User:** Research the first company and its funding.

**Assistant:** These are fictional demo employers, so there is no real company funding to verify. We can practice the questions to investigate, or switch to a separately requested live search using your configured Apify account and a disclosed cap.

For a live search, select `source="apify"`; the user must have configured their own token outside chat. That change is a different action from the explicitly free demo, so ask before making it. No token or CV text belongs in `brief`.
