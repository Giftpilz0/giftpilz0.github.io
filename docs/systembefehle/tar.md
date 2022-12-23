---
layout: default
title: Tar
parent: Systemcommands
---

# {{ page.title }}

______________________________________________________________________

| Option | Function | Example |
| ------ | --------------------------------- | ---------------------------------- |
| c | create | tar cf Archive.tar Data |
| x | extract | tar xf Archive.tar |
| f | file | |
| v | verbose | |
| I | select compression program | tar cI zst -f Archive.tar.zst Data |
| a | automatic compression program | tar caf Archive.tar.zst Data |

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

System backup

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
