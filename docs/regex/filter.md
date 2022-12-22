---
layout: default
title: Nützliche Filter
parent: Regex
---

# {{ page.title }}

______________________________________________________________________

trim whitespaces at end of line

`sed 's/\s*$//g'`

wrap long strings after 40 symbols

`sed -E 's/(\b.{1,40})\s+|\n|$/\1\n/g'`
