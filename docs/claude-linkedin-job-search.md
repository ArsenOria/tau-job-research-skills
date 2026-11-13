# LinkedIn job search skill for Claude: Claude Code setup

Tau Skills turns a CV and search constraints into a brief, LinkedIn search plan and evidence-based shortlist. The six skills work as instructions in your AI conversation; the optional [Tau Scout MCP server](https://github.com/ArsenOria/tau-linkedin-job-research-mcp) supplies vacancy discovery through your own Apify account.

**Validation status:** this is a setup guide based on Anthropic's documentation, checked on November 13, 2026. Tau's recorded native chat exercises were performed in Codex. **We have not yet completed an end-to-end Tau Skills + Scout exercise in Claude Code.** Follow the free checkpoints before using a paid search. This guide covers local Claude Code sessions, not a universal Claude web, Cowork or Desktop installation.

## Install the skill folders

Download this repository and copy the six individual folders inside `skills/` to `~/.claude/skills/`. Preserve each folder's `SKILL.md` and any `references/` subdirectory; for example, `~/.claude/skills/job-research/SKILL.md`. Review an existing same-named skill before replacing it. A project-local `.claude/skills/` is another option.

In Claude Code, start a local conversation and ask to use `job-search-brief`. You can also invoke `/job-search-brief`. These locations and invocation rules follow the [official Claude Code skills documentation](https://code.claude.com/docs/en/skills). If the skill is not visible, resolve discovery before proceeding; do not treat a separate script run as a successful chat integration.

## Add Scout for LinkedIn vacancy discovery

Skills can review vacancies supplied in chat without Scout or an Apify token. To fetch listings, first install the companion [Scout package](https://github.com/ArsenOria/tau-linkedin-job-research-mcp#first-connection) and locate its absolute `tau-job-scout` executable path.

For a project-local connection, merge this non-secret example into `.mcp.json` in the directory where you start Claude Code. Preserve other server entries and replace only the executable path:

```json
{
  "mcpServers": {
    "tau-job-scout": {
      "type": "stdio",
      "command": "/ABSOLUTE/PATH/TO/tau-linkedin-job-research-mcp/.venv/bin/tau-job-scout",
      "env": {
        "APIFY_TOKEN": "${APIFY_TOKEN}"
      }
    }
  }
}
```

Set your own `APIFY_TOKEN` in the environment that launches Claude Code, using a protected local secret facility where available. Obtain it from [Apify Console → Settings → API & Integrations](https://console.apify.com/settings/integrations). The JSON reference above is a placeholder expansion, not the token. Do not paste the token into chat, commit it, or send it as a tool argument. Scout does not read a repository `.env` automatically.

Claude Code supports local stdio servers and environment references in `.mcp.json`; project servers require its workspace approval. See the [official MCP setup reference](https://code.claude.com/docs/en/mcp). Check the connection with `/mcp`, then use the chat check below. Saving configuration alone does not prove that the server started.

## Check the workflow in chat

> Use job-research. Check Scout's connection and whether APIFY_TOKEN is configured, without displaying its value. Do not start a search or contact Apify.

Expected: the assistant calls Scout's `get_scout_status`. Token presence is only a boolean; it does not validate the token or balance. If tools are absent, finish MCP discovery first.

> Use Scout's synthetic demo to show a product analyst shortlist. Label it synthetic. Do not make paid requests. Then explain which roles fit a candidate with SQL experience who can work remotely only within Germany.

Expected: fictional demo results and evidence limits, followed by refinement of the same saved results. An unavailable tool is a setup issue, not an empty job market.

Once these checks pass, a real request can stay entirely in chat:

> Here is my CV. Find up to five product analyst jobs in Germany, including remote roles that explicitly allow working from Germany. Use my Apify account with a maximum run charge of $0.10. Show the search plan before starting, and separate unknown remote eligibility from confirmed matches.

The assistant discloses the source, filters, maximum results and spending cap before a paid search. Follow-ups reuse the saved shortlist. Apify charges your account; receiving a listing does not independently establish that the opening is current. The AI host handles your CV; Scout receives only minimal local matching facts and sends search parameters to Apify.

Tau Skills and Scout do not log in to LinkedIn, apply, send messages or automate the user's browser. The Actor is a third-party source, not official LinkedIn authorization. See [access and evidence](../README.md#access-and-evidence) and the [installation checkpoints](installation.md#manual-checkpoints).
