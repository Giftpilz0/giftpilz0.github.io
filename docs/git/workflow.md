---
layout: default
title: Workflow
parent: Git
---

# {{ page.title }}

______________________________________________________________________

Your local repository consists of three instances managed by git.
The first is your working copy, which contains the real files.
The second is the index, which acts as an intermediate stage and the HEAD,
pointing to your last commit.

![](../../assets/images/git_workflow.png)

You can add changes to the index with

`git add`

You confirm your changes with

`git commit -m "commit message"`

To upload the changes

`git push origin main`

General process

```
git checkout -b FeatureBranch
git add .
git commit -m 'Changelog message'
git rebase -i # if needed
git checkout main
git merge FeatureBranch
git branch -d FeatureBranch
```
