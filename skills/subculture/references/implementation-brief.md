# Implementation Brief Contract

Read this file completely before creating each implementation thread. Use it to write exactly one
ready-to-send first-message contract that lets a fresh worker begin without reconstructing the
parent conversation. Keep normal execution silent and make the terminal result independently
verifiable.

This reference defines the contract only. It does not grant permission to create a thread, perform
the implementation, or accept the result. The orchestrator must already have authorization under
the main `subculture` protocol before dispatch.

## Contents

- [Authoring rules](#authoring-rules)
- [Required contract](#required-contract)
- [Mission and outcome](#mission-and-outcome)
- [Original request](#original-request)
- [Repository grounding and baseline](#repository-grounding-and-baseline)
- [Exact scope](#exact-scope)
- [Responsibility and workspace boundary](#responsibility-and-workspace-boundary)
- [Inputs and locked decisions](#inputs-and-locked-decisions)
- [Dependencies and integration contract](#dependencies-and-integration-contract)
- [Implementation requirements](#implementation-requirements)
- [Deliverables](#deliverables)
- [Acceptance criteria and evidence](#acceptance-criteria-and-evidence)
- [Stop and escalation conditions](#stop-and-escalation-conditions)
- [Communication protocol](#communication-protocol)
- [Terminal report format](#terminal-report-format)
- [Curator verification](#curator-verification)
- [Output discipline](#output-discipline)

## Authoring rules

1. Inspect the repository and applicable instructions before filling in technical details. Use
   exact paths, symbols, commands, interfaces, and current behavior when they are known.
2. Preserve the user's requested outcome. Separate verified facts, user requirements, fixed
   decisions, preferred patterns, assumptions, open decisions, and non-goals. Label repository
   facts as verified and never present an assumption as an observed fact.
3. Do not invent product behavior, architecture, file ownership, numeric targets, commands, or
   APIs. If a missing decision can change correctness or scope, mark it as a blocking question
   for the curator before dispatch.
4. Make the contract concrete enough that two implementers would produce materially equivalent
   results. Replace vague terms such as “robust”, “clean”, “polished”, “handle errors”, or “as
   needed” with observable behavior, bounds, or an explicit human-review decision.
5. Prefer one bounded vertical implementation slice over a broad checklist. Include only
   acceptance evidence relevant to the promised behavior.
6. Put all required context in this first message. Do not plan to send missing context through
   routine progress updates.

## Required contract

Return one Markdown block with these sections. Omit a section only when it is genuinely not
applicable and state the reason briefly.

```text
# Implementation Brief: <short task name>

## Mission and outcome
## Original request
## Repository grounding and baseline
## Exact scope
## Responsibility and workspace boundary
## Inputs and locked decisions
## Dependencies and integration contract
## Implementation requirements
## Deliverables
## Acceptance criteria and evidence
## Stop and escalation conditions
## Communication protocol
## Terminal report format
## Curator verification
```

### Mission and outcome

State the single user- or system-visible result this task must create. Name the intended consumer
and why the result matters. Do not describe a solution before stating the outcome.

### Original request

Quote or faithfully preserve the relevant user request. Clearly label any interpretation added by
the curator. Do not silently narrow or expand the requested result.

### Repository grounding and baseline

Give the fresh agent the minimum verified context it needs:

- project/repository root and applicable `AGENTS.md` or local instructions;
- relevant existing files, symbols, interfaces, schemas, tests, and analogous patterns;
- runtime or environment entry points;
- exact commands for focused checks and, when justified, broader checks;
- baseline revision or working-tree assumption when diff identity matters.

Tell the agent what to read first. Link or name large source artifacts instead of pasting
irrelevant bodies into the prompt.

### Exact scope

Define:

- the behavior and surfaces to implement;
- explicit non-goals and adjacent work that must not be touched;
- edge cases, failure/recovery behavior, invariants, and compatibility rules;
- fixed, preferred, and open implementation choices;
- any quantitative limits or performance/security/accessibility obligations.

Use a task boundary, not a list of departments. If the task is not ready to implement, stop the
brief and surface the blocking decision instead of disguising discovery as implementation.

### Responsibility and workspace boundary

State the following explicitly:

- **Primary responsibility area:** the modules, behavior, and likely files or artifacts the agent
  owns for the outcome. Use paths and symbols for orientation, not as a rigid per-file allowlist.
- **Shared and coordination boundaries:** known files, contracts, schemas, migrations, registries,
  generated outputs, lockfiles, manifests, production state, or external systems that may overlap
  with other work or require curator coordination.
- **Safe implementation discretion:** the agent may change adjacent files when that change is
  necessary for the requested behavior, stays within the task's purpose, and does not conflict with
  another active owner's work. It must name such changes in the terminal report.
- **Integration owner:** who owns shared changes, cross-cutting decisions, final integration, and
  conflict resolution.

If another task owns an overlapping surface, mark the dependency and do not authorize concurrent
edits there. The agent must contact the curator before changing another active owner's area, a
shared public contract, schema, migration, lockfile, manifest, production state, external system,
or making a destructive or irreversible change. Same-project execution does not remove write
conflicts. Do not authorize opportunistic refactors, repository-wide formatting, unrelated cleanup,
or commits unless the contract explicitly assigns them.

### Inputs and locked decisions

List the exact input artifacts and their revision/version, upstream outputs already accepted,
interfaces that are frozen, dependencies that must be complete first, and decisions the agent
must not re-decide. Identify any allowed implementation latitude.

Include the actual main/curator thread destination:

```text
Main/curator thread: <filled absolute thread link or thread identifier>
```

The orchestrator must replace the placeholder with the actual main-thread link or identifier
before dispatch. The child must use that thread for every blocker question and its one terminal
report. Do not put model selection or reasoning settings in the implementation contract; the
orchestrator applies them when creating the thread.

### Dependencies and integration contract

Describe what this task consumes and what later work will consume from it. For each dependency,
state `blocked by`, `can run in parallel with`, or `blocks`. Define interfaces, schemas, event
shapes, filenames, exported symbols, or other handoff forms that must remain stable.

If the task produces a reusable artifact, name its owner, location, identity/version, and how the
curator will integrate it.

### Implementation requirements

Give an ordered internal route with enough detail to execute:

1. inspect the named context and confirm the task is ready;
2. implement the smallest complete slice within the primary responsibility area, using the allowed
   adjacent-change discretion when necessary;
3. add or update focused tests/checks required by the acceptance criteria;
4. run the exact verification commands and capture their real output;
5. inspect the final diff for scope drift, unjustified adjacent changes, coordination violations,
   and unfinished work.

These are execution steps, not progress-report checkpoints. The agent should not message the
curator after each step.

### Deliverables

List concrete outputs, including changed files or artifact paths, tests, migrations or generated
outputs when applicable, documentation that must stay synchronized, and the expected final state.
Do not count a plan, placeholder, screenshot of a command, or unintegrated generated file as a
finished implementation unless the task explicitly asks for it.

### Acceptance criteria and evidence

Write independent, observable criteria. For each criterion use:

```text
AC-<n>: <observable result>
- Scenario: <starting state and relevant inputs>
- Action: <single trigger or operation>
- Expected: <observable result>
- Must not: <important prohibited side effect, if any>
- Evidence: <exact test, command, runtime observation, diff, or artifact>
- Priority: Required | Important | Optional
```

Map every Required criterion to evidence. Prefer real runtime or public-boundary evidence over
implementation claims. Include negative, error, boundary, persistence, compatibility, or
accessibility checks only when the task makes them relevant.

The worker may self-check, but its self-report is not final acceptance. The curator performs the
independent final verification after the worker reports completion.

### Stop and escalation conditions

The agent must stop and contact the curator only when:

- a required input, authority, dependency, or acceptance decision is missing;
- the task would require taking over another active owner's responsibility area or changing a
  shared contract;
- repository behavior contradicts a locked decision or the requested outcome;
- a security, data-loss, migration, public-API, destructive, or irreversible choice is unresolved;
- verification cannot establish a Required criterion;
- the implementation is blocked by a capability or environment failure it cannot safely resolve.

The escalation message must state the exact question/blocker, evidence already checked, options if
known, and the decision needed. Do not send a vague “I am stuck” message.

### Communication protocol

This is a terminal-communication contract:

- Do **not** send progress updates, phase summaries, acknowledgements, or “still working” notes
  to the main thread.
- Continue working silently while the task is within scope and unblocked.
- Do not create, fork, or delegate to another thread or agent. If additional delegation appears
  necessary, request explicit user authorization through the main/curator thread.
- Message the curator/main thread only when a decision or answer is required, or when the terminal
  result is ready.
- Use the supplied curator thread link for both cases. Do not report completion only in a child
  thread, a local log, or an unrelated channel.
- Delivering the terminal report to the supplied main/curator thread is mandatory. Finishing the
  implementation without sending it there is a protocol violation and does not constitute a valid
  handoff to the curator.
- Do not declare the work accepted, merged, complete for the whole project, or safe to ship. The
  curator owns those judgments.

### Terminal report format

When blocked, report:

```text
STATUS: BLOCKED | NEEDS_CONTEXT | NEEDS_DECISION
QUESTION/BLOCKER: <precise statement>
EVIDENCE CHECKED: <paths, commands, or observations>
IMPACT: <what cannot proceed or may be wrong>
OPTIONS: <known options and trade-offs, if any>
DECISION NEEDED FROM: curator in <main-thread link>
```

When the implementation is ready, send this report once to the supplied main/curator thread. Merely
printing it in the child thread does not satisfy the contract:

```text
STATUS: READY_FOR_CURATOR_VERIFICATION | READY_WITH_CONCERNS
OUTCOME: <what was implemented>
CHANGED: <files/artifacts and concise purpose>
ACCEPTANCE EVIDENCE: <AC -> command/result or runtime/artifact evidence>
CHECKS RUN: <exact commands and results>
SCOPE/RESPONSIBILITY: <confirm boundaries and explain necessary adjacent changes or deviations>
UNRESOLVED: <none, or precise risks/gaps>
CURATOR ACTION: Independently verify and accept, request focused rework, or escalate in <main-thread link>
```

### Curator verification

The curator must perform the final verification after receiving a terminal report:

1. Inspect the implementation code, actual diff, changed artifacts, call paths, and responsibility
   boundaries.
2. Compare every Required acceptance criterion with the code and the worker's exact evidence.
3. Run only lightweight, focused checks or a narrow runtime probe when code review and existing
   evidence do not establish a criterion. Do not repeat an expensive full suite or long end-to-end
   run already completed by the worker unless its evidence is missing, stale, contradictory, the
   code changed afterward, or a material risk cannot be resolved otherwise.
4. Check for scope drift, hidden placeholders, broken contracts, and unreported risks.
5. After all accepted work is integrated, perform one final adversarial pass and create one
   combined list of up to three material checks. Select candidates from both: (a) contract
   obligations the implementation may have missed or failed to satisfy, and (b) concrete
   product-logic risks the implementation may have introduced or left unresolved.
6. Ground each candidate in a specific contract clause, changed path, state transition, error
   path, integration boundary, or other concrete signal from the task. Rank candidates by credible
   likelihood and user/product impact. Do not pad the list with speculative or negligible risks,
   including 0.1–0.5% edge cases with no material product consequence. A simple task may produce
   zero or one check. For every selected item, record its category, hypothesis, concrete reason it
   is credible, direct code inspection or lightweight targeted verification, evidence, result
   (`PASS`, `FAIL`, or `BLOCKED`), and required rework. Do not rerun a heavy suite merely to fill
   this check when the worker already supplied exact results. `BLOCKED` or `UNVERIFIED` is not a
   pass. This is one combined cap of three items, not three per category.
7. Issue one verdict: `ACCEPTED`, `FOCUSED_REWORK`, `REJECTED`, or `BLOCKED`; repeat the relevant
   checks after any rework.

The curator may send a focused rework brief containing only the failed criteria and evidence. The
worker's test results are reusable evidence, while final acceptance still requires the curator to
inspect the implementation code and its product logic.

## Output discipline

Return the briefing prompt only, ready to paste into the first message of the implementation
thread. Do not append a second planning essay, a generic orchestration guide, or a progress plan.
