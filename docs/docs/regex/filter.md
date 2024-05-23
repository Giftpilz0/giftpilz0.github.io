---
layout: default
title: Useful Filters
parent: Regex
---

______________________________________________________________________

trim whitespaces at end of line

`sed 's/\s*$//g'`

wrap long strings after 40 symbols

`sed -E 's/.{1,40}( |$)/&\n/g' Notiz.md`
