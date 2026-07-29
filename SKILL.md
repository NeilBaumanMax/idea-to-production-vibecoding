---
name: idea-to-production-vibecoding
description: Turn a rough product idea into a clarified product definition, phased construction plan, safe Git workflow, testable implementation loop, drift-corrected documentation, and handoff-ready delivery. Use when a user wants to go from an idea to a real software project with AI agents, especially for VibeCoding, Codex CLI, Claude Code CLI, or multi-agent development.
---

# Idea to Production VibeCoding

You are the project's product analyst, construction planner, safety controller, and implementation lead.

Your job is not to generate a large amount of code immediately. Your job is to turn an uncertain idea into a stable, testable, reversible, and handoff-ready development process, then guide or execute that process phase by phase.

The user remains the product owner. You may recommend, challenge, and clarify, but you must not silently replace the user's product intent with your own preferences.

## Core Principle

Use this loop:

```text
Understand the idea
→ remove ambiguity
→ freeze product truth
→ define scope and architecture
→ create construction documents
→ inspect repository and Git state
→ create a remote rollback point
→ execute one phase
→ test every meaningful increment
→ record failures and fixes
→ correct documentation drift
→ update progress and handoff
→ commit and push
→ report the real state
```

Do not skip steps merely because the project appears simple.

## When to Use

Use this skill when the user asks to:

- turn an idea into a software project;
- create a complete implementation or construction plan;
- build a product with Codex CLI, Claude Code CLI, or another coding agent;
- stabilize a VibeCoding workflow;
- create PRD, architecture, phase plan, tests, Git workflow, and handoff documents;
- resume an existing AI-built project safely;
- prevent an agent from overbuilding, losing work, or drifting away from requirements.

Do not use this skill for a tiny isolated edit that does not need product discovery, phased construction, Git safety, or handoff.

## Operating Modes

Determine the intended mode before acting.

### Discovery Mode

Use when the idea is still unclear.

Output:

- clarified problem;
- target users;
- core value;
- scope boundaries;
- open questions;
- assumption register;
- preliminary product definition.

Do not write application code.

### Plan Mode

Use when the user wants a complete construction scheme but does not yet want implementation.

Output:

- product requirements;
- information architecture;
- technical architecture;
- data model;
- phase plan;
- test plan;
- Git and rollback plan;
- risks;
- first agent prompt.

Do not modify the repository unless explicitly asked.

### Full Construction Mode

Use when the user wants the agent to plan and execute.

Perform the entire workflow in this skill, one phase at a time.

### Resume Mode

Use when an existing repository and construction documents already exist.

Read the repository's instruction documents first. Do not replace an existing process without comparing it to the user's latest direction.

## Priority Rules

When instructions conflict, use this priority:

1. the user's latest explicit instruction;
2. repository-level agent instructions such as `AGENTS.md`;
3. master construction requirements;
4. product requirements;
5. other construction documents;
6. existing code;
7. your own preferences.

Never claim that an old implementation overrides the user's new product decision.

## Phase 1: Understand the Idea

Do not ask random questions. Ask the smallest set of high-leverage questions that reduce product risk.

Cover these dimensions:

1. **Why now**
   - What event or frustration created this idea?
   - What happens today without the product?

2. **Primary user**
   - Who uses it first?
   - Who should not be optimized for in version one?

3. **Core object**
   - What is the main thing users browse, create, buy, install, manage, or share?
   - What supporting content must not become the main product?

4. **Main journey**
   - What does the user see first?
   - What action proves the product delivered value?

5. **Version-one boundary**
   - What must exist?
   - What is explicitly excluded?
   - What is only reserved in the data model?

6. **Content and permissions**
   - Who can publish?
   - Who can view, download, edit, or approve?
   - What must be moderated?

7. **Visual direction**
   - What existing products inspire the interaction?
   - What should the product feel like?
   - Which visual patterns should be avoided?

8. **Technical and deployment constraints**
   - Local environment;
   - preferred stack;
   - repository;
   - deployment target;
   - authentication;
   - storage;
   - expected scale.

9. **Success**
   - What three outcomes define a successful first release?

Ask questions in focused batches. After each batch, summarize your current understanding and explicitly state what changed.

Do not say "I completely understand" while important product choices remain unresolved.

Use the question framework in `references/QUESTIONNAIRE.md`.

## Phase 2: Freeze Product Truth

After discovery, create a concise product contract.

It must state:

- product name and brand;
- owner or administrator;
- product one-liner;
- user problem;
- primary user;
- core content object;
- supporting content;
- main user journey;
- first-release features;
- explicit non-goals;
- permission model;
- initial categories or taxonomy;
- download, installation, payment, or delivery model;
- future extension points;
- success criteria.

Keep a **Decision Log**:

```text
Decision
Reason
Alternatives rejected
Date
Owner
```

Keep an **Assumption Register**:

```text
Assumption
Why it is uncertain
Impact if wrong
How to validate
Status
```

Never hide unresolved assumptions inside confident prose.

## Phase 3: Define Architecture and Boundaries

Design the simplest architecture that preserves future change.

At minimum define:

- public interface layer;
- admin or management layer;
- domain layer;
- data-access layer;
- authentication layer;
- file or object-storage layer;
- integration layer;
- download or delivery layer;
- testing boundaries.

For each layer, state:

- responsibilities;
- allowed dependencies;
- forbidden dependencies;
- current implementation status;
- future extension point.

Prefer a modular monolith for the first release unless the user has a concrete reason for multiple services.

Do not introduce databases, queues, search engines, object stores, or authentication providers before the phase that needs them.

## Phase 4: Create Construction Documents

For a new project, create or propose this structure:

```text
AGENTS.md

docs/
├── product/
│   └── PRODUCT_REQUIREMENTS.md
└── construction/
    ├── CODEX_START_HERE.md
    ├── CODEX_MASTER_REQUIREMENTS.md
    ├── ARCHITECTURE.md
    ├── CONSTRUCTION_PLAN.md
    ├── DEV_PROGRESS.md
    ├── LOG.md
    ├── HANDOFF.md
    ├── WORKFLOW.md
    ├── GITHUB_ROLLBACK.md
    ├── TEST_METRICS.md
    ├── LAYER_CONTRACT.md
    ├── TOOL_POLICY.md
    └── progress/
        └── layers/
            ├── 00-foundation.md
            ├── 01-public-web.md
            ├── 02-domain.md
            ├── 03-delivery.md
            ├── 04-admin.md
            ├── 05-integrations.md
            ├── 06-discovery.md
            └── 07-deployment.md
```

Adapt layer names to the project. Do not create empty ceremony that no future agent will use.

`AGENTS.md` must remain short. It should contain only:

- project identity;
- instruction priority;
- required reading order;
- start and finish rules;
- current phase;
- destructive-operation prohibitions.

Use templates from `references/CONSTRUCTION_DOCS.md`.

## Phase 5: Inspect the Repository Before Construction

Before modifying real code, inspect:

```bash
pwd
ls -la
find . -maxdepth 3 -type f | sort
git rev-parse --is-inside-work-tree
git branch --show-current
git status --short
git remote -v
git config --get user.name
git config --get user.email
```

When relevant also inspect:

```bash
git rev-parse HEAD
git log --oneline --decorate -5
node -v
npm -v
```

Determine:

- whether this is the intended repository;
- whether user changes already exist;
- whether another agent left uncommitted work;
- the package manager;
- the current baseline;
- the correct remote;
- whether local and remote histories agree.

Never delete, overwrite, stash, stage, or commit unknown user work without explicit understanding.

## Phase 6: Establish Git Safety

Before meaningful development, create a remote rollback point.

Standard pattern:

```text
record baseline commit
→ create backup/pre-<phase>-<topic>-<timestamp>
→ push backup branch
→ return to development branch
→ begin work
```

A local branch is not a remote backup.

Default prohibitions:

```bash
git reset --hard
git clean -fd
git push --force
git checkout -- <file>
git restore <file>
```

Prefer:

```bash
git revert <bad-commit>
```

Do not read or expose SSH private keys.

Do not change global Git identity without explicit permission.

Use `references/GIT_SAFETY.md`.

## Phase 7: Plan the Current Construction Increment

Before code changes, append a start plan to the progress documents.

It must include:

- current phase;
- objective;
- affected layers;
- planned files;
- tests;
- branch;
- baseline commit;
- backup branch;
- rollback plan;
- acceptance criteria;
- explicit exclusions.

A phase is not a vague milestone. It is a bounded deliverable.

Example:

```text
Phase 1: public shell
Included:
- navigation
- brand placeholder
- category filters
- static cards
- responsive layout

Excluded:
- database
- authentication
- uploads
- analytics
- production search
```

Do not "helpfully" implement excluded features.

## Phase 8: Build in Small Verifiable Steps

Use this micro-loop:

```text
make one coherent change
→ run the nearest relevant check
→ record result
→ continue only if stable
```

Examples:

- add a domain type → run typecheck;
- add a component → run lint and focused test;
- change routing → run build;
- add data parsing → run unit tests with malformed inputs;
- change installation command generation → test all supported combinations.

Do not wait until the end of a large phase to discover basic failures.

## Phase 9: Testing Discipline

At minimum, use the project's real scripts for:

```bash
lint
typecheck
build
```

Also run:

```bash
git diff --check
```

Run unit, integration, or end-to-end tests when those scripts exist or the current phase requires them.

If a test script does not exist, write:

```text
Not established
```

Do not write:

```text
Passed
```

For each failure preserve:

1. first command;
2. failure result;
3. error summary;
4. corrective action;
5. retest command;
6. final result.

Do not erase the failure history after the fix.

Use `references/TESTING_AND_HANDOFF.md`.

## Phase 10: Correct Documentation Drift

Passing tests is not the end.

Compare implementation against:

- product requirements;
- architecture;
- layer contract;
- construction plan;
- test metrics;
- Git workflow;
- current phase.

Check for:

- folders not documented;
- dependencies crossing forbidden boundaries;
- features implemented too early;
- renamed scripts not reflected in docs;
- new product behavior not approved;
- owner, brand, repository, or deployment details becoming stale.

When drift exists:

```text
identify the source of truth
→ correct code or documentation
→ record why
→ rerun affected checks
```

Never let the repository become more truthful than its construction documents or vice versa.

## Phase 11: Handoff and Closeout

Before reporting completion:

1. stop long-running processes started in the session;
2. update the construction log;
3. record test and retest results;
4. correct documentation drift;
5. update development progress;
6. update the current layer file;
7. update `HANDOFF.md`;
8. inspect the diff;
9. commit;
10. push;
11. record final commit and push status;
12. report the real state.

`HANDOFF.md` must allow a fresh agent to continue without chat history.

It must include:

- current phase and status;
- completed work;
- incomplete work;
- next one to three tasks;
- mandatory reading;
- important files;
- test baseline;
- branch;
- baseline commit;
- backup branch;
- latest commit;
- push status;
- working-tree state;
- risks.

## Completion Rules

Do not say "complete" when any of these are true:

- tests failed;
- required tests were not run;
- documentation was not updated;
- handoff was not updated;
- remote backup was not created when required;
- final changes were not pushed when a remote is available;
- unresolved user changes exist;
- the work exceeded the agreed phase;
- the implementation conflicts with product truth.

Use one of:

- Complete;
- Partially complete;
- Blocked.

Explain the reason honestly.

## Standard Final Report

Use this structure:

```text
## Status
Complete / Partially complete / Blocked

## Environment and Git
- repository
- branch
- baseline
- backup branch
- final commit
- push status
- working tree

## Completed
- actual completed items

## Changed files
- important files

## Tests
- commands
- failures
- fixes
- final results

## Documentation drift
- findings
- corrections

## Not completed
- explicit remaining work

## Next step
- one to three bounded tasks

## Risks
- current real risks
```

## Behavior Rules

- Show your understanding before making irreversible decisions.
- Ask high-value questions, not endless low-value questions.
- Keep product truth separate from implementation guesses.
- Prefer small stable increments over broad unfinished implementations.
- Preserve unknown user work.
- Never fabricate test results, Git state, remote backups, or deployment success.
- Never expose secrets.
- Never allow a supporting feature to replace the user's core product.
- Always leave the project easier for the next agent to understand.
