# Example Implementation Brief: Backend Stale Greeting-Translation Lifecycle

**Dispatch:** Sol sends this contract to a new Luna Max implementation thread.

## Mission and outcome

Implement the backend persistence lifecycle that prevents a translated character greeting from
remaining active after its source message changes.

For users of AIWORLDING Character Editor, an unchanged translation remains active. Editing the
current greeting atomically marks its old translation as stale. A later translation uses the
current edited message as its new source and replaces the stale record.

## Original request

The user reported that the editor could treat a previously translated greeting as active after the
underlying message had changed.

The approved behavior is:

- an unchanged translation remains active;
- changing the current message makes the previous translation stale;
- stale translation data must not override the current message;
- retranslation uses the current message as its source;
- a successful retranslation replaces the stale per-slot record.

## Repository grounding and baseline

- Repository root: `<REPOSITORY_ROOT>`.
- Main curator thread: `<CURATOR_THREAD_ID>`.
- Dispatch baseline: `<BASELINE_COMMIT>`.
- Workspace model: shared local working tree, no worktree.
- Preserve the curator's existing change in `<PRODUCT_SPEC_PATH>`.
- Read these sources before implementation:
  1. `<PROJECT_AGENT_RULES>`
  2. `<PRODUCT_ARCHITECTURE_GUIDE>`
  3. `<CHARACTER_EDITOR_SPEC>`
  4. `<TRANSLATION_STATE_MODULE>`
  5. `<TRANSLATION_TEST_MODULE>`
  6. `<GREETING_SYNC_MODULE>`
  7. `<TRANSLATION_COMMAND_MODULE>`
  8. `<CHARACTER_UPDATE_MODULE>`
  9. `<CHARACTER_REPOSITORY_MODULE>`
  10. `<PORTABLE_EXPORT_MODULE>`
- Run backend commands through `<PROJECT_BACKEND_WRAPPER>`.
- Do not create alternate cache directories or clean shared project caches.

## Exact scope

Implement this complete backend slice:

1. Add an explicit `Stale` value to the existing translation-entry status enum.
2. Define one central active-translation rule:
   - the entry status is `Translated`;
   - the slot identity matches;
   - the current persisted text equals the recorded translated value.
3. Before a general character update is persisted, reconcile translation metadata against incoming
   greeting values:
   - changed active entries become stale;
   - unchanged active entries remain translated;
   - failed, conflicting, and stale entries remain non-active;
   - unrelated character edits do not affect greeting translations;
   - translation commands do not immediately stale their own matching metadata;
   - deleted, moved, or replaced alternate greetings do not inherit an unrelated active record.
4. Preserve unrelated extension data and persist text plus metadata through the existing atomic
   character-update boundary.
5. Restoring an active translation may return the original text, but it must make the old
   translation record stale in the same persisted mutation.
6. Retranslation of stale or mismatched content must use the current message as its new source.
7. Portable export may use a stored original only for an active translation.
8. Malformed translation metadata must fail closed without discarding user text or unrelated data.
9. Do not expand the task into frontend behavior, storage migrations, multi-locale history,
   background migration, provider prompts, or unrelated performance work.

## Responsibility and workspace boundary

Primary responsibility:

- backend translation-state reconciliation;
- character-update integration;
- restore and retranslation behavior;
- portable export behavior;
- focused backend tests.

Owned paths:

- `<TRANSLATION_STATE_MODULE>`
- `<TRANSLATION_TEST_MODULE>`
- `<GREETING_SYNC_MODULE>`
- `<TRANSLATION_COMMAND_MODULE>`
- `<CHARACTER_UPDATE_TEST_MODULE>`

Coordination boundaries:

- another worker owns the frontend character-model projection;
- another worker owns the translation UI and localization;
- the curator owns product specifications, generated contracts, integration, and final acceptance;
- do not edit generated files, manifests, lockfiles, frontend paths, or another worker's files;
- contact the curator before introducing a public schema change beyond the approved additive status.

Do not commit. The shared working tree is the integration surface.

## Inputs and locked decisions

- Serialized stale status: `"stale"`.
- Changed current text becomes the new translation source.
- A successful retranslation replaces the previous per-slot record.
- Translation metadata remains under `<TRANSLATION_METADATA_EXTENSION_KEY>`.
- Do not add a database migration or translation-history collection.
- Preserve existing public command names and request/response shapes.
- The curator owns all material architectural decisions.

## Dependencies and integration contract

- This task may run in parallel with the frontend source-projection and UI workers.
- Do not enter another worker's owned paths.
- This task blocks generated-contract synchronization and final integration.
- Preserve the existing translation-entry shape apart from the additive status value.
- Produce the canonical backend meaning of `"stale"` for downstream consumers.

## Implementation requirements

1. Inspect the named code and confirm how extension patches are merged at the canonical update
   boundary.
2. Add focused failing tests before implementation.
3. Implement the smallest central reconciliation helper.
4. Integrate reconciliation into the existing atomic update path.
5. Update restore and retranslation source selection.
6. Add structured diagnostics without logging greeting bodies.
7. Run focused tests through `<PROJECT_BACKEND_WRAPPER>`.
8. Run the project-level backend check after focused tests pass.
9. Inspect the final diff for scope drift and concurrent-worker conflicts.

## Deliverables

- Explicit stale translation state.
- Atomic update reconciliation.
- Restore and retranslation lifecycle changes.
- Portable export protection.
- Focused regression tests.
- No frontend, documentation, migration, manifest, generated-file, or lockfile changes.
- One terminal report delivered directly to `<CURATOR_THREAD_ID>`.

## Acceptance criteria and evidence

### AC-1: Changing an active translated greeting makes it stale atomically

Scenario:

- the current greeting equals the recorded translated value;
- the entry status is `Translated`.

Action:

- a general character update submits different greeting text.

Expected:

- the new text is persisted;
- the existing translation entry becomes `Stale`;
- both changes appear in the same returned character;
- unrelated extension data remains intact.

Evidence:

- focused backend test through the canonical update boundary.

### AC-2: Unrelated character edits preserve active translations

Action:

- update a non-greeting field.

Expected:

- greeting text and active translation metadata remain unchanged.

Evidence:

- focused backend regression test.

### AC-3: A translation commit does not invalidate itself

Action:

- submit new translated text and matching active metadata through the canonical mutation.

Expected:

- the new text and metadata remain active.

Must not:

- immediately convert the newly committed translation to `Stale`.

Evidence:

- focused test on the translation commit path.

### AC-4: Restore and retranslation follow the approved lifecycle

Scenario:

- an active translation is restored and later translated again.

Expected:

- restore returns the original text and makes the old record stale;
- retranslation uses the current restored or edited text;
- successful retranslation replaces the stale record.

Evidence:

- source-resolution tests and a focused persistence test.

### AC-5: Alternate greeting changes cannot misattach translations

Scenario:

- active alternate greetings are removed, reordered, or changed.

Expected:

- missing or mismatched slots become stale;
- unchanged correctly matched slots may remain active;
- an old translated record never remains active against different current content.

Evidence:

- focused alternate-slot reconciliation tests.

### AC-6: Stale records export current content

Scenario:

- a stale record retains its previous source and translated evidence while the current greeting has
  changed.

Expected:

- portable export uses the current greeting;
- it does not export the previous original or translated body.

Evidence:

- focused portable-export test.

### AC-7: Verification respects project cache and scope

Expected:

- focused tests and the backend check pass, or the worker reports a precise blocker;
- the diff contains only owned or explicitly justified backend files;
- shared caches and another worker's files remain untouched.

Evidence:

- exact commands and results in the terminal report;
- curator inspection of the final diff.

## Stop and escalation conditions

Stop and contact the curator only when:

- the behavior requires an unapproved public schema change;
- another worker creates a real conflict in an owned path;
- malformed metadata requires a missing product decision;
- repository behavior contradicts a locked decision;
- a required test cannot run because of a concrete environment failure.

Do not lower correctness, add a second non-atomic write, or silently reset malformed metadata.

## Communication protocol

- Do not send acknowledgements, progress updates, or phase summaries.
- Work silently while the task remains within scope and unblocked.
- Do not create, fork, or delegate to another thread or agent.
- Contact `<CURATOR_THREAD_ID>` only for a concrete blocker or the terminal handoff.
- Deliver the terminal report to the curator thread, not only inside the worker thread.
- Do not claim project-wide acceptance, integration, merge, or ship readiness.

## Terminal report format

For a blocker:

```text
STATUS: BLOCKED | NEEDS_CONTEXT | NEEDS_DECISION
QUESTION/BLOCKER: <precise statement>
EVIDENCE CHECKED: <paths and commands>
IMPACT: <what cannot proceed>
OPTIONS: <known options and trade-offs>
DECISION NEEDED FROM: curator in <CURATOR_THREAD_ID>
```

For a terminal handoff:

```text
STATUS: READY_FOR_CURATOR_VERIFICATION | READY_WITH_CONCERNS
OUTCOME: <implemented behavior>
CHANGED: <files and purpose>
ACCEPTANCE EVIDENCE: <criterion to exact evidence>
CHECKS RUN: <exact commands and results>
SCOPE/RESPONSIBILITY: <boundary confirmation and justified adjacent changes>
UNRESOLVED: <none or precise risks>
CURATOR ACTION: Independently verify in <CURATOR_THREAD_ID>
```

## Curator verification

Sol inspects the actual implementation and call paths, maps every required acceptance criterion to
evidence, performs any missing focused checks, resolves integration issues, and issues the only
acceptance verdict.
