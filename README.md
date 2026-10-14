# SpaceX: an Agent Skill for weird ideas you can act on

A two-phase ideation skill for Claude. **Liftoff** thinks about a real problem the way a stoned person thinks about a doorknob: sincere, associative, every connection feeling cosmic. **Reentry** is mission control reading the flight recorder the next morning: it keeps only ideas that are both sound *and* absent from a sealed "sober baseline," then turns them into moves you can test this week.

The output is a mission report with at most three ideas, each with a concrete move and a cheapest test, plus telemetry on how many claims survived.

> Simulation only. The skill copies how associative thinking works; it never mentions or discusses substances.

## Install

### Claude Code (plugin marketplace)

```
/plugin marketplace add cumeadi/spacex-skill
/plugin install spacex@spacex-skill
```

### Claude Code (manual)

Copy `skills/spacex` into `~/.claude/skills/` (personal) or `.claude/skills/` in a project.

### Claude.ai / Claude desktop

Download `spacex.zip` from the [latest release](https://github.com/cumeadi/spacex-skill/releases/latest), then upload it under **Settings → Capabilities → Skills**.

### Claude API

Upload the `skills/spacex` folder through the Skills API. See [Anthropic's Skills docs](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview).

## Use

Say "SpaceX" or "get high on this problem" and give it something real:

```
SpaceX: meal-kit subscribers cancel after week six. Dose 2.
```

- **Dose** 1 (low orbit), 2 (orbit, default), 3 (deep space)
- **Register** giggly, cosmic (default), or paranoid-philosophical

## Layout

```
skills/spacex/
├── SKILL.md              # instructions and frontmatter
└── scripts/
    └── roll_moves.py     # rolls each trip's move order
```

## License

MIT. See [LICENSE](LICENSE).
