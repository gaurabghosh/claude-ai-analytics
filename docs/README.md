# AI Analytics System

An agentic analytics system built with Claude Code. Drop in a dataset, ask a question, get a full analysis deck in ~30 minutes. No SQL. No Python required. The system is markdown files that Claude Code reads and follows.

## Quick Start

1. Install Claude Code: `npm install -g @anthropic-ai/claude-code`
2. Install Marp (for slide rendering): `npm install -g @marp-team/marp-cli`
3. Open this repo in your terminal or Google Antigravity IDE
4. Launch Claude Code and select `claude-opus-4-6` as the model
5. Drop your dataset into `/data/`
6. Prompt: `Analyze the data in /data and produce a full deck`

## Repo Structure

```
CLAUDE.md                    ← Master orchestration file — start here
agents/                      ← 15 analytical agents (one task each)
.claude/skills/              ← 12 always-active skills (how things get done)
helpers/                     ← Python chart utilities and style guide
themes/                      ← Marp CSS themes (dark + light)
data/                        ← Drop your CSVs/Excel files here
outputs/                     ← Final deck PDFs and charts land here
working/                     ← Intermediate files during analysis (auto-managed)
docs/                        ← Additional documentation
fallbacks/                   ← Fallback instructions for edge cases
```

## The Pipeline

```
Frame → Explore → Validate → Story → Charts → Deliver
```

6 phases, 4 checkpoints, 15 agents, 12 skills. See `CLAUDE.md` for details.

## The Key Distinction

**Skills** define HOW things get done (always active, like a style guide).  
**Agents** define WHAT gets done (invoked on demand for specific tasks).

Change a skill → all agents that touch that concern change automatically.  
Invoke an agent → it runs a structured multi-step workflow.

## Improving the System

The system improves every time you use it. When you give feedback:
- Claude Code updates the relevant agent or skill file permanently
- The improvement applies to all future analyses automatically
- You're building institutional memory, not just fixing one output

## Themes

| Theme | Best for |
|---|---|
| `analytics-dark` | Executive decks, external audiences |
| `analytics-light` | Internal reviews, printed output |

Specify in your prompt: "Use the light theme" or "Use the dark theme"
