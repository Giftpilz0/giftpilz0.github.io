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

Lokalen Änderungen komplett entfernen und den letzten Stand vom entfernten Repository holen

```
git fetch origin
git reset --hard origin/main
```

Lokale Commits verwerfen

`git reset --hard reponame/branch`

Vergleich von zwei Branches

```
git diff quell_branch ziel_branch
git diff --name-status quell_branch ziel_branch
```

Vergleiche generell

`git diff --staged`

Branch löschen

```
git branch -d branch # Vorher merge in anderen Branch nötig
git branch -D branch # Löscht auch ohne Merge
```

Mache FeatureBranch zu main

```
git checkout main
git reset --hard FeatureBranch
```
