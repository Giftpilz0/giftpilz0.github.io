---
title: Disk Usage
---

| Command                          | Shows                                                                           |
| -------------------------------- | ------------------------------------------------------------------------------- |
| `df -h`                          | Free and used space per mounted filesystem.                                     |
| `df -i`                          | Free and used inodes. A full inode table blocks new files even with free space. |
| `lsblk -f`                       | Disks, partitions, filesystems and mount points as a tree.                      |
| `fdisk -l`                       | Partition tables of all disks (needs root).                                     |
| `du -sh dir`                     | Total size of a directory.                                                      |
| `du -h --max-depth=1 \| sort -h` | Size of each subdirectory, largest last.                                        |
| `ncdu /`                         | Interactive browser for disk usage; can delete with <kbd>d</kbd>.               |

:::tip[df and du disagree]
If `df` reports a full disk but `du` can't find the files, a process still holds deleted files open. The space is only
freed when it closes them. `lsof +L1` lists such files; restart the process that owns them.
:::
