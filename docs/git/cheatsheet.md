---
layout: default
title: Cheat Sheet
parent: Git
---

# {{ page.title }}

View changes of a commit

`git show`

Discard local changes (no add yet)

`git checkout filename`

Discard local changes (after add)

```
git reset HEAD filename # after this everything is as before "add"
git checkout filename
```

undo changes

`git checkout commit-ID`

Completely remove local changes and get the latest version from the remote repository

```
git fetch origin
git reset --hard origin/main
```

Discard local commits

`git reset --hard reponame/branch`

Comparison of two branches

```
git diff source_branch target_branch
git diff --name-status source_branch target_branch
```

Compare in general

`git diff --staged`

Delete branches

```
git branch -d branch # Need to merge in other branch first
git branch -D branch # Also deletes without merging
```

Make FeatureBranch main

```
git checkout main
git reset --hard FeatureBranch
```
