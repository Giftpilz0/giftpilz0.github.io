---
layout: default
title: Awk
parent: Systembefehle
---

# {{ page.title }}

______________________________________________________________________

Basic Syntax

`awk options 'selection-criteria {action}'`

Print the fifth column (a.k.a. field) in a space-separated file

`awk '{print $5}' filename`

Print the second column of the lines containing "foo" in a space-separated file

`awk '/foo/ {print $2}' filename`

Print the last column of each line in a file, using a comma (instead of space) as a field separator

`awk -F ',' '{print $NF}' filename`
