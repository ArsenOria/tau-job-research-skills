# Contributing to Tau job research skills

Improve Tau's job research skills for AI chat while keeping each skill independently useful and all daily interaction conversational. Prefer a demonstrated improvement to a long rule catalog.

1. Explain the user request or research failure your change addresses.
2. Keep required references inside that skill's folder. Do not depend on the checkout, a sibling skill, private Tau code or a host-specific absolute path.
3. Use synthetic examples only. Never commit credentials, CVs, account information or scraped personal information.
4. Validate the package with `python checks/validate.py` after installing `requirements-dev.txt` in an isolated environment.
5. Exercise a relevant scenario in `checks/scenarios.md`. Report tools available, observations, limitations and any external calls. Structural validation alone is not behavioral evidence.

Coordinate changes to MCP names or arguments with Scout's versioned tool contract. Do not add a Tau account requirement, separate search CLI or a request to paste secrets into conversation. Any live Apify evaluation must use an explicitly chosen account and spending limit; normal checks stay offline.
