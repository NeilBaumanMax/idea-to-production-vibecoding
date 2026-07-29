# Construction Documents Reference

## AGENTS.md

Keep it short.

```md
# Project Agent Instructions

## Project Identity
- Project:
- Owner:
- Brand:
- Repository:

## Instruction Priority
1. Latest user instruction
2. Master requirements
3. Product requirements
4. Other construction documents
5. Existing code

## Required Reading
1.
2.
3.

## Start Rules
- Inspect repository and Git.
- Write a start plan.
- Create and push a backup branch.
- Do not overwrite unknown changes.

## Finish Rules
- Run tests.
- Record failures and fixes.
- Correct documentation drift.
- Update handoff.
- Commit and push.

## Current Phase
-

## Prohibitions
- No force push.
- No destructive cleanup.
- No fabricated test results.
- No secrets in the repository.
```

## PRODUCT_REQUIREMENTS.md

Required sections:

```md
# Product Requirements

## Identity
## Product One-Liner
## Problem
## Primary User
## Core Product Object
## Supporting Content
## Main User Journey
## First-Release Scope
## Explicit Non-Goals
## Permissions
## Taxonomy
## Delivery or Download Model
## Future Extension Points
## Success Criteria
## Decision Log
## Assumption Register
```

## ARCHITECTURE.md

Required sections:

```md
# Architecture

## Architectural Goal
## Current Stack
## Deployment Shape
## Layer Overview
## Data Flow
## File and Storage Flow
## Authentication Boundary
## Integration Boundary
## Testing Strategy
## Future Extension Points
```

## CONSTRUCTION_PLAN.md

Each phase must define:

```md
## Phase N: Name

### Goal
### Included
### Excluded
### Dependencies
### Planned Deliverables
### Tests
### Acceptance Criteria
### Rollback Point
```

## DEV_PROGRESS.md

Append-only entries:

```md
## YYYY-MM-DD HH:mm / Phase / Start Plan

### Objective
### Affected Layers
### Repository State
### Planned Files
### Tests
### Git Baseline
### Backup Branch
### Rollback Plan
### Acceptance Criteria
### Explicit Exclusions
```

## LOG.md

Append-only entries:

```md
## YYYY-MM-DD HH:mm / Phase / Work Log

### Plan Replay
### Actual Changes
### Files Changed
### Test Log
### Failures
### Fixes
### Retests
### Documentation Drift
### Git Status
### Rollback Judgment
### Risks
### Next Step
```

## HANDOFF.md

Append or keep a clear latest-state section:

```md
# Handoff

## Current State
## Completed
## Incomplete
## Next Tasks
## Required Reading
## Important Files
## Test Baseline
## Git State
## Backup Branch
## Latest Commit
## Push Status
## Working Tree
## Risks
```
