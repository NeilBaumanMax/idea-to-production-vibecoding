# Testing and Handoff Reference

## Minimum Checks

Use the project's real scripts.

Common examples:

```bash
npm run lint
npm run typecheck
npm run build
git diff --check
```

Run unit, integration, and end-to-end tests when established and relevant.

## Failure Record

```md
### Test Attempt 1
Command:
Result: Failed
Summary:

### Fix
Files:
Reason:

### Retest
Command:
Result:
```

Never remove the first failure merely because the retest passes.

## Phase Acceptance

A phase is accepted only when:

- included work exists;
- excluded work was not accidentally implemented;
- relevant tests pass;
- docs match reality;
- handoff is current;
- Git status is understood;
- commit and push status are recorded.

## Drift Checklist

- Product behavior matches requirements.
- New folders appear in architecture docs.
- Dependencies obey layer contracts.
- Scripts match test documentation.
- Current work matches the active phase.
- Owner, brand, repository, and remote are current.
- No hidden future-phase implementation exists.
- No secrets were committed.

## Handoff Quality Test

Ask:

> Could a fresh agent continue the next task safely without reading the chat?

If not, the handoff is incomplete.
