---
layout: default
title: Rsync
parent: Systemcommands
---

______________________________________________________________________

Synchronize /home to /backup

`rsync -aPX /home /backup`

Synchronize files/directories between the local and remote system with compression enabled

`rsync -avz /home server:/backups/`

To keep different directories in sync

`rsync -rltpDug --modify-window=1 --progress --delete /home /backup`
