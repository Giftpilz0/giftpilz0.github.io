---
title: Rsync
---

rsync copies only what differs between source and target, so repeated runs are fast. It works locally and over SSH
(`host:path`).

## The trailing slash

The most common mistake: a trailing slash on the **source** means "the contents of", without it the directory itself is
copied.

| Command                    | Result                 |
| -------------------------- | ---------------------- |
| `rsync -a photos /backup`  | `/backup/photos/1.jpg` |
| `rsync -a photos/ /backup` | `/backup/1.jpg`        |

A slash on the target makes no difference.

## Examples

| Command                                         | Effect                                                                            |
| ----------------------------------------------- | --------------------------------------------------------------------------------- |
| `rsync -aP /home /backup`                       | Copies `/home` to `/backup/home` with progress, resumable.                        |
| `rsync -avz /home/ server:/backups/home/`       | Copies to a server over SSH, compressed.                                          |
| `rsync -av --delete src/ dst/`                  | Makes `dst` an exact mirror, deleting files missing in `src`.                     |
| `rsync -av --exclude '.cache' src/ dst/`        | Skips matching files and directories.                                             |
| `rsync -avn --delete src/ dst/`                 | Dry run: lists what would happen.                                                 |
| `rsync -aHAX src/ dst/`                         | Additionally keeps hard links, ACLs and extended attributes.                      |
| `rsync -rltDv --modify-window=1 src/ /mnt/usb/` | For FAT/exFAT targets, which have no owners or permissions and coarse timestamps. |

| Option | Meaning                                                                                        |
| ------ | ---------------------------------------------------------------------------------------------- |
| `-a`   | Archive: recursive, keeps symlinks, permissions, times, owner, group and devices (`-rlptgoD`). |
| `-v`   | Lists the transferred files.                                                                   |
| `-z`   | Compresses during the transfer; only useful over a network.                                    |
| `-P`   | Shows progress and keeps partially transferred files, so a restart continues.                  |
| `-n`   | Dry run.                                                                                       |

:::danger
`--delete` together with a wrong trailing slash or a swapped source and target deletes data in the target. Run the
command with `-n` first.
:::
