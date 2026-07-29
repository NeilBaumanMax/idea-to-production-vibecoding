#!/usr/bin/env python3
"""Create a safe construction-document scaffold without overwriting existing files."""

from __future__ import annotations

import argparse
from pathlib import Path
from datetime import datetime


FILES = {
    "AGENTS.md": """# Project Agent Instructions

## Project Identity
- Project: {project_name}
- Owner: {owner}
- Brand: {brand}

## Instruction Priority
1. Latest explicit user instruction
2. `docs/construction/CODEX_MASTER_REQUIREMENTS.md`
3. `docs/product/PRODUCT_REQUIREMENTS.md`
4. Other construction documents
5. Existing code

## Required Reading
1. `AGENTS.md`
2. `docs/construction/CODEX_MASTER_REQUIREMENTS.md`
3. `docs/product/PRODUCT_REQUIREMENTS.md`
4. `docs/construction/DEV_PROGRESS.md`
5. `docs/construction/LOG.md`
6. Current phase file
7. `docs/construction/HANDOFF.md`

## Start Rules
- Inspect repository and Git state.
- Preserve unknown user changes.
- Write a start plan before real code changes.
- Create and push a remote backup branch before meaningful construction.

## Finish Rules
- Run relevant tests.
- Record failures, fixes, and retests.
- Correct documentation drift.
- Update progress and handoff.
- Commit and push only when stable.

## Current Phase
- Phase 0: Foundation

## Prohibitions
- No force push.
- No destructive cleanup.
- No fabricated test results.
- No secrets in the repository.
""",
    "docs/product/PRODUCT_REQUIREMENTS.md": """# Product Requirements

## Identity
- Product: {project_name}
- Owner: {owner}
- Brand: {brand}

## Product One-Liner
TBD

## Problem
TBD

## Primary User
TBD

## Core Product Object
TBD

## Supporting Content
TBD

## Main User Journey
TBD

## First-Release Scope
TBD

## Explicit Non-Goals
TBD

## Permissions
TBD

## Taxonomy
TBD

## Delivery or Download Model
TBD

## Future Extension Points
TBD

## Success Criteria
TBD

## Decision Log
TBD

## Assumption Register
TBD
""",
    "docs/construction/CODEX_START_HERE.md": """# Start Here

Read `AGENTS.md` first, then follow its required reading order.
""",
    "docs/construction/CODEX_MASTER_REQUIREMENTS.md": """# Master Construction Requirements

## Highest Priority
The latest explicit instruction from {owner} is the source of truth.

## Mandatory Loop
Understand → plan → back up → build → test → correct drift → hand off → commit → push.

## Safety
- Preserve unknown work.
- Do not fabricate status.
- Do not expose secrets.
- Do not exceed the current phase.
""",
    "docs/construction/ARCHITECTURE.md": """# Architecture

## Architectural Goal
TBD

## Current Stack
TBD

## Deployment Shape
TBD

## Layer Overview
TBD

## Data Flow
TBD

## Storage Flow
TBD

## Authentication Boundary
TBD

## Integration Boundary
TBD

## Testing Strategy
TBD

## Future Extension Points
TBD
""",
    "docs/construction/CONSTRUCTION_PLAN.md": """# Construction Plan

## Phase 0: Foundation

### Goal
Establish product truth, construction documents, Git safety, and the minimal project baseline.

### Included
- Documentation
- Repository baseline
- Minimal scaffold
- Lint, typecheck, build

### Excluded
- Full product features
- Production integrations

### Acceptance Criteria
TBD
""",
    "docs/construction/DEV_PROGRESS.md": """# Development Progress

## {timestamp} / Phase 0 / Start Plan

### Objective
Establish the project foundation.

### Affected Layers
- Foundation

### Repository State
TBD after inspection.

### Planned Files
- Construction documents

### Tests
TBD

### Git Baseline
TBD

### Backup Branch
TBD

### Rollback Plan
Prefer `git revert`.

### Acceptance Criteria
TBD

### Explicit Exclusions
No feature overbuild.
""",
    "docs/construction/LOG.md": """# Construction Log

## {timestamp} / Phase 0 / Initialization

Construction-document scaffold created. Real repository inspection, backup, implementation, testing, and closeout remain to be performed by the active agent.
""",
    "docs/construction/HANDOFF.md": """# Handoff

## Current State
Construction-document scaffold created.

## Completed
- Initial document structure

## Incomplete
- Repository inspection
- Product clarification
- Git backup
- Implementation
- Tests

## Next Tasks
1. Read all construction documents.
2. Inspect repository and Git.
3. Complete product discovery.

## Required Reading
- `AGENTS.md`
- `docs/product/PRODUCT_REQUIREMENTS.md`
- `docs/construction/CODEX_MASTER_REQUIREMENTS.md`

## Important Files
TBD

## Test Baseline
Not established.

## Git State
TBD

## Risks
Product truth is not yet complete.
""",
    "docs/construction/WORKFLOW.md": """# Workflow

Read → inspect → plan → remote backup → build one increment → test → log → correct drift → hand off → commit → push.
""",
    "docs/construction/GITHUB_ROLLBACK.md": """# GitHub and Rollback

## Backup
Create and push `backup/pre-<phase>-<topic>-<timestamp>` before meaningful construction.

## Recovery
Prefer `git revert`.

## Prohibited by Default
- `git reset --hard`
- `git clean -fd`
- force push
""",
    "docs/construction/TEST_METRICS.md": """# Test Metrics

## Required Baseline
- lint
- typecheck
- build
- `git diff --check`

Missing tests must be recorded as `Not established`, never `Passed`.
""",
    "docs/construction/LAYER_CONTRACT.md": """# Layer Contract

Define each layer's responsibilities, allowed dependencies, and forbidden dependencies before implementing cross-layer behavior.
""",
    "docs/construction/TOOL_POLICY.md": """# Tool Policy

- Use the repository's existing package manager.
- Do not expose secrets.
- Do not perform destructive Git operations without explicit approval.
- Verify external CLI behavior before hard-coding commands.
""",
}

LAYER_FILES = [
    "00-foundation.md",
    "01-public-web.md",
    "02-domain.md",
    "03-delivery.md",
    "04-admin.md",
    "05-integrations.md",
    "06-discovery.md",
    "07-deployment.md",
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-name", required=True)
    parser.add_argument("--owner", required=True)
    parser.add_argument("--brand", required=True)
    parser.add_argument("--root", default=".")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing scaffold files. Use only after reviewing changes.",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()
    timestamp = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M %Z")
    values = {
        "project_name": args.project_name,
        "owner": args.owner,
        "brand": args.brand,
        "timestamp": timestamp,
    }

    created: list[Path] = []
    skipped: list[Path] = []

    for relative, template in FILES.items():
        target = root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists() and not args.force:
            skipped.append(target)
            continue
        target.write_text(template.format(**values), encoding="utf-8")
        created.append(target)

    layers_root = root / "docs/construction/progress/layers"
    layers_root.mkdir(parents=True, exist_ok=True)
    for filename in LAYER_FILES:
        target = layers_root / filename
        if target.exists() and not args.force:
            skipped.append(target)
            continue
        title = filename.removesuffix(".md").replace("-", " ").title()
        target.write_text(
            f"# {title}\n\n## Status\nNot started.\n\n## Progress Log\n",
            encoding="utf-8",
        )
        created.append(target)

    print(f"Root: {root}")
    print(f"Created: {len(created)}")
    for path in created:
        print(f"  + {path.relative_to(root)}")
    print(f"Skipped: {len(skipped)}")
    for path in skipped:
        print(f"  = {path.relative_to(root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
