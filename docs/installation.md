# Install LinkedIn job search skills for AI chat

Install Tau's six LinkedIn job search skills for AI chat, then optionally connect Tau Scout's LinkedIn job search MCP server for bounded vacancy discovery with your own Apify token.

## What is supported

The skills are folders containing `SKILL.md`; the AI host must support importing these instructions and reading any bundled references. Installation locations and UI differ by host. Import a whole folder or its packaged ZIP through your host's skill mechanism, rather than copying only `SKILL.md` when a `references/` directory exists. This repository does not install into or alter your AI host automatically.

Start with `job-search-brief` and `job-research`, or install all six. Each works without the others. A host can use the plain instructions without skill discovery, but automatic selection is then the host's responsibility. We do not claim a completed behavioral integration with every client.

## Codex desktop

Use the [README's Codex walkthrough](../README.md#connect-to-codex-desktop). The user-level directory is `~/.agents/skills/`; each of the six skill directories belongs directly inside it. Preserve the `job-research/references/` directory. Codex's MCP connection is configured separately in settings or `~/.codex/config.toml` using the Scout repository's example.

This repository contains instructions, not an installed MCP connection. Scout's executable must come from an installed `tau-job-scout` package. The initial manual exercise should verify both skill discovery and MCP tool discovery rather than silently substituting an operator test harness.

## Claude Code

See the [LinkedIn job search skill for Claude setup guide](claude-linkedin-job-search.md). It covers local skill folders and an optional Scout stdio connection using your own Apify token. **This route is documented from Anthropic's setup references; Tau has not completed end-to-end chat validation in Claude Code.** The recorded native manual exercises use Codex. This is not an installation claim for Claude web chat, Cowork or every Claude Desktop session.

## Scout is optional

Without Scout, the assistant can work with pasted vacancies and its own available public-web tools. If it has neither live search nor readable listings, it prepares searches and explains that it has not found or verified current roles. It does not invent a shortlist.

For automated LinkedIn vacancy discovery, connect the separately installed Tau Job Scout in a host that can launch local stdio MCP servers. A remote-only web chat connector is insufficient for this transport. Use the Scout repository's installation instructions for the package and launch command; the executable is `tau-job-scout`.

Initial package installation and MCP configuration are setup steps. The daily job-search workflow is entirely conversational. The first version is not a universal one-click installer.

## Your Apify token

1. Create or use your own account at [Apify](https://console.apify.com/) and obtain an API token from the account settings.
2. Configure `APIFY_TOKEN` for the Scout MCP process using your host's secret facility where supported, or a local process environment setting. Configuration values may be stored in plaintext by some hosts; protect that configuration and do not commit it.
3. Never send the value as a chat message or MCP tool argument. The assistant checks only the boolean token-presence result from `get_scout_status`.
4. Use demo mode to check the conversation before a live search. The demo does not need a token or balance.

No Tau backend participates. You pay Apify directly. The assistant states the source, maximum results and run-charge cap before a paid search; a prepared plan makes no paid request. Adding a token does not give permission for unbounded repeated searches.

## Check the connection in chat

> Check whether Scout is connected. Then demonstrate a product analyst search with synthetic data, without using Apify.

The assistant should discover Scout's tools, call `get_scout_status`, prepare a `demo` plan, start it and show a labeled synthetic shortlist. Tool identifiers and polling mechanics can stay out of the ordinary chat response.

If Scout is absent or the token is missing, the assistant explains the setup issue and offers demo mode or research using the material already in the chat. It never asks you to move reports between applications as the normal workflow.

## Manual checkpoints

Work through these one at a time with the assistant:

1. **Skills visible:** ask it to use `job-search-brief`. It should work from your supplied experience/preferences, asking only for missing details. No token is needed.
2. **MCP visible:** ask it to check Scout's connection without searching. It should call `get_scout_status`; token presence is a boolean only. If no tool is discovered, finish setup rather than counting a shell harness as a connected chat.
3. **Free demo:** ask for synthetic results only. Expect clearly labeled fictional data, then ask to refine the same saved results. No Apify account call is needed.
4. **Live search:** specify role, geography, freshness and caps; for example up to five jobs and $0.10. The assistant discloses the plan, starts it once and checks the same run. This is a paid operation on your account, even if it returns no useful results.
5. **Follow-up:** refine the saved shortlist and request a description-based fit review. The assistant should reuse it without another Actor start unless you ask to expand the search.

Do not send a token, a screenshot containing a token, or a token-bearing configuration file into the conversation. Share only a non-secret error message if a checkpoint fails.
