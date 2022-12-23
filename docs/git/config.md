---
layout: default
title: Configuration
parent: Git
---

# {{ page.title }}

______________________________________________________________________

{: .note }

> Git config files are used to set global settings related to the editor,
> Set colors, default branch and more.

______________________________________________________________________

```ini
[user]
    email = 86166667+Giftpilz0@users.noreply.github.com
    name = Moritz Schmidt
    username = Giftpilz0

[init]
    defaultBranch = main

[core]
    editor = nano
    whitespace = fix,-indent-with-non-tab,trailing-space,cr-at-eol

[color]
    ui = auto

[color "branch"]
    current = yellow bold
    local = green bold
    remote = cyan bold

[color "diff"]
    meta = yellow bold
    frag = magenta bold
    old = red bold
    new = green bold
    whitespace = red reverse

[color "status"]
    added = green bold
    changed = yellow bold
    untracked = red bold
```
