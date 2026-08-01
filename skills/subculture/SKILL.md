---
name: subculture
description: AIW's Sol-mediated orchestration protocol for parallel, first-class, user-visible Codex threads created with the app-level create_thread capability in the current project, never through internal subagents. Sol owns architecture, integration, and acceptance while Luna Max handles bounded implementation work. Activate only when the user explicitly invokes the exact standalone code word SUBCULTURE as an execution mode, not when merely quoting, discussing, translating, or reviewing it. The bundled references/implementation-brief.md contract is mandatory before every child-thread dispatch.
---

# AIW SUBCULTURE

Use this skill only when the user explicitly activates the exact standalone code word
**SUBCULTURE** as an instruction to execute project work. Mentioning the word while asking about,
reviewing, translating, or editing this skill does not activate it. The main thread becomes the
orchestrator and curator. Its responsibility is the finished, integrated result, not merely
dispatching work.

## Operating contract

1. Understand the full request and define the final completion boundary.
2. Inspect the current project and build a responsibility map before dispatching. For every child,
   record the primary implementation area, known shared or actively edited surfaces, existing
   dirty changes, dependencies, and the owner. Do not turn this map into a rigid per-file allowlist:
   the child may make necessary adjacent changes that support its outcome, provided they do not
   conflict with another active owner. Shared files, public contracts, schemas, migrations,
   registries, generated outputs, lockfiles, manifests, and final integration require one owner
   or explicit sequencing.
3. Own the planning and architecture before delegation. Thinking through the project's architecture,
   deciding how the requested change should correctly fit it, producing the implementation plan,
   and confirming all material architectural decisions are the orchestrator's initial,
   non-delegable responsibilities in this mode. Do not assign this work to weaker child agents or
   use them to discover the architecture on the orchestrator's behalf. Delegate only after the
   architecture and plan are grounded in the inspected project and sufficiently locked for bounded
   implementation. Children still own local implementation decisions within that plan; if evidence
   shows that a material architectural change is needed, they must return the decision to the
   orchestrator before proceeding.
4. Split only genuinely independent implementation surfaces. Create every implementation worker as
   a new, first-class, user-visible Codex thread through the app-level `create_thread` capability,
   targeting the current saved project with the local environment rather than a worktree. Every
   worker must have its own returned `threadId` and appear as a separate task in the Codex task list.
   Never use `spawn_agent`, internal collaboration or multi-agent delegation primitives, agent
   teams, or any other subagent mechanism as a substitute; workers shown only under a `Subagents`
   panel are evidence that the wrong mechanism was used. If app-level thread creation is unavailable
   or fails, stop and alert the user instead of falling back to internal subagents. Do not create
   worktrees or separate project copies. Dispatch dependent work only after its prerequisite handoff
   is accepted; read-only discovery may happen earlier, but a child must not enter another active
   owner's known conflicting area before the handoff. Treat the user's explicit activation of this
   mode as permission only for the minimum set of first-level implementation threads needed for the
   current request. Neither the orchestrator nor any child may create extra, nested, exploratory,
   review, or replacement threads without fresh explicit user permission.
5. Before creating every child thread, read [references/implementation-brief.md](references/implementation-brief.md)
   completely and use it to write the child's complete single first-message prompt-contract. The
   contract must include the current project context, exact scope, primary responsibility area,
   coordination boundaries, dependencies, locked decisions, deliverables, acceptance evidence,
   stop conditions, the actual main-thread link or identifier, and terminal report format. Never
   dispatch a child without satisfying every required contract field, and never leave a placeholder
   instead of the live main-thread link.
6. Use **Sol** as the main orchestrator and curator. Route bounded implementation threads to
   **Luna with Max thinking** by default. If the orchestrator explicitly selects Terra or another
   non-Sol worker, that worker also uses Max thinking; a Sol implementation worker keeps its
   configured non-Max mode. Never transfer architecture, ambiguous decomposition, integration, or
   final acceptance from Sol to Luna.
7. Dispatch the independent frontier. Do not make the child threads send acknowledgements,
   progress updates, phase summaries, or “still working” messages.
8. After all prompts for the current frontier have been sent, end the active orchestration turn and
   go fully offline to conserve tokens: do not poll, re-check, or generate follow-up work. Resume
   only when a child thread or the user explicitly alerts the main thread.
9. When alerted, answer only the necessary decision or missing-context question, dispatch the next
   dependency frontier when its prerequisites are complete, and keep the same terminal-report rule.
10. When a child reports a result in the main thread, independently verify it as curator. A child
   owns its paths until it delivers its terminal status there; only then does write authority
   transfer to the curator for integration corrections. Return material implementation defects to
   the original owner with a focused rework contract. Continue until the whole original request
   reaches its final completion boundary.

## Child-thread communication rule

The child thread may write to the main thread only in these cases:

- it needs a decision, missing context, permission, or clarification that blocks safe progress;
- it cannot proceed because of a concrete capability, dependency, or environment blocker;
- it has reached a terminal result and is ready for curator verification.

All other work stays silent in the child thread. At a terminal result, the child is obligated to send
its terminal report directly to its curator in the actual main thread named in the contract. Writing
the report only in the child thread, leaving the result in a local log, or finishing without sending
the report to the main thread is a protocol violation: no valid handoff has occurred, write authority
has not transferred, and the curator must not accept the work. A child must never declare its work
accepted, integrated, merged, or safe to ship. A child must never create, fork, or delegate to another
thread or agent; it must request user authorization through the main thread if additional delegation
appears necessary.

The terminal report must use the format from
[references/implementation-brief.md](references/implementation-brief.md), include the main-thread
link, and be delivered in that main thread. The curator treats the report as a claim and evidence
pointer, not as acceptance.

## Curator verification and integration

After each terminal child result, and before declaring the overall task complete:

1. Inspect the actual changed files/artifacts and confirm responsibility, scope boundaries, and
   whether any adjacent changes were necessary and justified.
2. Map every required acceptance criterion to evidence and inspect the worker's exact results.
3. Review the implementation code, call paths, and integration boundaries. Run only lightweight,
   focused checks or a narrow runtime probe when code review and existing evidence do not establish
   the criterion.
4. Check for scope drift, hidden placeholders, broken interfaces, unauthorized writes, and
   unreported risks.
5. Issue a child-level curator verdict: `ACCEPTED`, `FOCUSED_REWORK`, `REJECTED`, or `BLOCKED`.
6. Send focused rework instructions only for failed criteria, then repeat verification.
7. Own final integration, cross-thread conflict resolution, and the final user-facing result.

Never treat a child's self-review, green command, screenshot of a command, or confident summary as
final proof. The main thread is the only acceptance authority in this mode.

### Final adversarial risk check

After all accepted work is integrated, perform one final adversarial pass. Build one combined list
of **up to three** material checks drawn from both categories:

- contract obligations the implementation may have missed or failed to satisfy;
- concrete product-logic risks the implementation may have introduced or left unresolved.

Rank candidates by credible likelihood and user/product impact. Candidates must be grounded in a
specific contract clause, changed path, state transition, error path, integration boundary, or
other concrete signal from this task. Do not pad the list with generic hypotheticals or negligible
risks, including 0.1–0.5% edge cases that would not materially affect the product. A simple task
may produce zero or one check. For every selected item, record its category, hypothesis, concrete
reason it is credible, direct code inspection or lightweight targeted verification, evidence,
result (`PASS`, `FAIL`, or `BLOCKED`), and any required rework. Do not rerun a heavy suite merely
to fill this check when the worker already supplied exact results. `BLOCKED` or `UNVERIFIED` is not
a pass. This is one combined cap of three items, not three items per category. Re-run the acceptance
decision after any rework, then issue the
final overall verdict: `ACCEPTED`, `FOCUSED_REWORK`, `REJECTED`, or `BLOCKED`. Do not declare
success from the risk list alone.

## Stop conditions

Pause and alert the user when the original request is materially ambiguous, a shared responsibility
conflict cannot be resolved, a required capability is unavailable, or final acceptance requires a
decision only the user can make. Do not silently lower scope or convert an unfinished result into
completion.

The bundled implementation-brief reference is the contract-authoring layer; the main skill is the
orchestration, silence, offline, verification, and integration layer. Keep the full prompt template
in that reference rather than duplicating it here.
