# Git Safety Reference

## Required Preflight

```bash
pwd
git rev-parse --is-inside-work-tree
git branch --show-current
git status --short
git rev-parse HEAD
git remote -v
git config --get user.name
git config --get user.email
```

## Backup Branch

```bash
git switch -c backup/pre-<phase>-<topic>-<timestamp>
git push -u origin backup/pre-<phase>-<topic>-<timestamp>
git switch <development-branch>
```

Do not continue if the remote backup did not succeed.

## Default Prohibitions

Do not run without explicit user approval:

```bash
git reset --hard
git clean -fd
git clean -fx
git push --force
git push -f
git checkout -- <file>
git restore <file>
```

## Preferred Recovery

```bash
git revert <bad-commit>
```

For a range:

```bash
git revert <oldest-bad-commit>^..<newest-bad-commit>
```

## Unknown User Changes

When `git status --short` shows unknown work:

- identify files;
- do not overwrite;
- do not automatically stage;
- do not stash without approval;
- do not include them in a phase commit;
- work around them or stop if overlap is unavoidable.

## SSH Safety

You may verify:

```bash
ssh -T git@github.com
```

Do not read:

```bash
cat ~/.ssh/id_rsa
cat ~/.ssh/id_ed25519
```

Never copy keys into the repository.

## Final Inspection

```bash
git status --short
git diff --check
git diff --stat
git diff
```

Prefer explicit staging:

```bash
git add path/to/file1 path/to/file2
```

Avoid unreviewed:

```bash
git add .
```
