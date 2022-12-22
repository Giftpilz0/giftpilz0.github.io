---
layout: default
title: Tar
parent: Systembefehle
---

# {{ page.title }}

______________________________________________________________________

| Option | Funktion                          | Beispiel                           |
| ------ | --------------------------------- | ---------------------------------- |
| c      | erstellen                         | tar cf Archive.tar Data            |
| x      | extrahieren                       | tar xf Archive.tar                 |
| f      | datei                             |                                    |
| v      | ausführlich                       |                                    |
| I      | kompressionsprogram auswählen     | tar cI zst -f Archive.tar.zst Data |
| a      | automatisches kompressionsprogram | tar caf Archive.tar.zst Data       |

Create tar named archive.tar containing directory

`tar cf archive.tar directory`

Extract the contents from archive.tar

`tar xf archive.tar`

Create a gzip compressed tar file name archive.tar.gz

`tar czf archive.tar.gz directory`

Extract a gzip compressed tar file

`tar xzf archive.tar.gz`

Create a tar file with bzip2 compression

`tar cjf archive.tar.bz2 directory`

Extract a bzip2 compressed tar file

`tar xjf archive.tar.bz2`

System-Backup

```bash
sudo tar -cvpzf ./backup.tar.gz
  --exclude=./backup.tar.gz
  --exclude=/media/*
  --exclude=/mnt/*
  --exclude=/var/log/*
  --exclude=/home/.cache/
  --exclude=/tmp/*
  --exclude=/proc/*
  --exclude=/sys/*
  --exclude=/btrfs_pool/timeshift-btrfs/*
  --exclude=/run/timeshift/*
  --exclude=/home/*/.local/share/Trash/
```
