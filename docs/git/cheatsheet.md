---
layout: default
title: Cheat Sheet
parent: Git
---

# {{ page.title }}

Änderungen zu einem Commit anzeigen

`git show`

Lokale Änderungen verwerfen (noch kein add)

`git checkout Dateiname`

Lokale Änderungen verwerfen (nach add)

```
git reset HEAD Dateiname # hiernach ist alles wie bevor "add"
git checkout Dateiname
```

Änderungen rückgängig machen

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
