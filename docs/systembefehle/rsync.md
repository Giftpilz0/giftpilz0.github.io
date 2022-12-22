---
layout: default
title: Rsync
parent: Systembefehle
---

# {{ page.title }}

______________________________________________________________________

Synchronize /home to /backup

`rsync -aPX /home /backup`

Synchronize files/directories between the local and remote system with compression enabled

`rsync -avz /home server:/backups/`

um verschiedene Ordner gleich zu halten

`rsync -rltpDug --modify-window=1 --progress --delete /home /backup`
