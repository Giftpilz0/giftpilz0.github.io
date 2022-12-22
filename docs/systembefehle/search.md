---
layout: default
title: Dateisuche
parent: Systembefehle
---

# {{ page.title }}

______________________________________________________________________

Search for pattern in file

`grep pattern file`

Search recursively for pattern in files

`grep -r pattern directory`

Find files in /home/ that start with "pattern"

`find /home/ -name 'pattern'`

Find files larger than 100MB in /home

`find /home/ -size +100M`

List installed software

`dpkg --get-selections`
`dnf list installed`

Dateipfad von Anwendung herausfinden

`which {{ app }}`
