---
layout: default
title: Git Cheat Sheet
parent: Git
---

# {{ page.title }}

______________________________________________________________________

## Introduction

This cheat sheet provides essential Git commands for common scenarios.

______________________________________________________________________

### View Changes of a Commit

To view the changes of a specific commit:

```shell
git show <commit-ID>
```

### Discard Local Changes (Before Add)

To discard local changes to a file before staging (adding) them:

```shell
git checkout <filename>
```

### Discard Local Changes (After Add)

To discard local changes to a file after staging but before committing:

```shell
git reset HEAD <filename> # Unstage the changes
git checkout <filename>   # Discard the changes
```

### Undo Changes

To undo changes and revert to a specific commit:

```shell
git checkout <commit-ID>
```

### Completely Remove Local Changes and Fetch Latest

To discard all local changes and get the latest version from the remote repository:

```shell
git fetch origin
git reset --hard origin/main # Replace 'main' with your desired branch
```

### Discard Local Commits

To discard local commits and reset to a remote branch:

```shell
git reset --hard <reponame/branch>
```

### Comparison of Two Branches

To compare changes between two branches:

```shell
git diff <source_branch> <target_branch>
```

To display only the names and statuses of changed files:

```shell
git diff --name-status <source_branch> <target_branch>
```

### Compare Staged Changes

To compare the changes that are currently staged (added) but not committed:

```shell
git diff --staged
```

### Delete Branches

To delete a local branch (note: you need to merge it into another branch first):

```shell
git branch -d <branch-name>
```

To forcefully delete a branch without merging:

```shell
git branch -D <branch-name>
```

### Make a Branch Main

To make a feature branch the new main branch:

```shell
git checkout main
git reset --hard <FeatureBranch>
```
