# codex-subculture

AIW Codex Subculture keeps Sol in charge of architecture and quality while routing bounded
implementation work to Luna Max in separate, user-visible Codex tasks. It is a Sol-mediated
mixed-model workflow, not a native subagent loop.

The protocol activates only when the user gives the exact standalone instruction `SUBCULTURE`.
Mentioning, reviewing, or translating the word does not activate it.

## Why AIW uses it

AIW prefers Sol for architecture, ambiguous decomposition, integration, and final acceptance. In
our experience, Luna is not reliable enough to own those decisions without strict mediation. This
protocol compensates by having Sol inspect the project, lock the plan, write complete worker
contracts, resolve blockers, and verify every terminal handoff. Luna Max receives only bounded
implementation work.

The intended token shift looks like this:

| Workflow | Illustrative token allocation |
| --- | ---: |
| Sol-only baseline | approximately 100 million Sol tokens |
| Subculture target | approximately 50 million Sol tokens and 80 million Luna tokens |

These figures are a planning scenario, not a measured benchmark, fixed ratio, or guarantee. The
goal is to reduce Sol execution while retaining Sol control over quality-critical decisions.

That control costs time. Complete contracts, separate task handoffs, code inspection, and stricter
verification can make delivery substantially slower than direct single-agent execution.

AIW also rejects the native Codex subagent lifecycle for this workflow. Subculture requires
first-class Codex tasks with their own `threadId`, visible history, and direct curator handoff. It
never substitutes workers that exist only inside a `Subagents` panel.

## Requirements

- A Codex app environment that exposes app-level task creation through `create_thread`.
- Support for creating tasks in the current saved project with the local environment.
- Sol for the main orchestrator and curator role.
- Luna with Max thinking for the default bounded implementation role.

The protocol does not support CLI-only environments that cannot create user-visible tasks. It
never falls back to internal `spawn_agent`, agent-team, or subagent mechanisms.

## Install from a local checkout

Copy `skills/subculture` into your Codex skills directory.

PowerShell:

```powershell
Copy-Item -Recurse .\skills\subculture "$HOME\.codex\skills\subculture"
```

macOS or Linux:

```bash
cp -R skills/subculture "${CODEX_HOME:-$HOME/.codex}/skills/subculture"
```

These commands assume that the destination does not already exist. For development, you may link
the destination to this checkout so edits take effect without another copy.

## Protocol

1. The Sol main task inspects the project and owns the architecture and implementation plan.
2. It creates only the minimum independent frontier of separate, user-visible Luna Max tasks.
3. Before creating each task, it reads the bundled implementation-brief contract and writes one
   self-contained first message.
4. Workers stay silent during normal progress. They contact the curator only for a real blocker or
   a terminal handoff.
5. Every terminal report must reach the main task. A report left only in a worker task is a protocol
   violation and does not transfer ownership.
6. The curator inspects the implementation, integrates accepted work, and performs the final
   evidence-based risk check.

## Repository layout

```text
skills/subculture/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    └── implementation-brief.md
```

`SKILL.md` contains the orchestration protocol. The bundled reference contains the complete
implementation-contract authoring rules and terminal report format. It is not a second skill and
cannot drift to a different installed version.

## Validate

```bash
python scripts/validate_skill.py
```

The validator checks the skill metadata, bundled links, mandatory protocol markers, and absence of
the retired standalone brief dependency.

## Compatibility notes

- Worker creation must return a distinct `threadId` and produce a separate task in the Codex task
  list. An entry that appears only under a `Subagents` panel is not compliant.
- Luna Max is the default implementation worker. Terra and other profiles remain optional, but
  architecture and final acceptance stay with Sol.
- The exact activation word is `SUBCULTURE`.

## Access and license

This is an AIW private project. No external reuse or redistribution license has been granted.
