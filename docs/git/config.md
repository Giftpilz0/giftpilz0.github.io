---
layout: default
title: Config
parent: Git
---

# {{ page.title }}

______________________________________________________________________

{: .note }

> Gitconfig Datein werden verwendet um global Einstelungen bezüglich Editor,
> Farben, Standard-Branch und mehr zu setzen.

______________________________________________________________________

```ini
[user]
    email = schmidtmoritz404@gmail.com
    name = Moritz Schmidt
    username = Giftpilz

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
