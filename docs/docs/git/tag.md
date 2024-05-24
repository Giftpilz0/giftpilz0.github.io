---
title: Git Tags
---

______________________________________________________________________

## Introduction

Tags in Git are used to mark significant milestones in a repository's history, often representing stable releases of software. For example, you can create a tag like "v1.0" to mark the release of version 1.0 of your software.

______________________________________________________________________

## Creating a New Tag

To create a new tag and link it to a precise commit:

```
git tag 1.0.0 <commit-ID>
```

## Deleting a Tag

If you need to remove a tag:

```
git tag -d <tag-name>
```
