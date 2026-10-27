---
title: File Search
---

## grep

| Command                                  | Effect                                         |
| ---------------------------------------- | ---------------------------------------------- |
| `grep pattern file`                      | Prints matching lines.                         |
| `grep -rn pattern dir`                   | Searches recursively, with line numbers.       |
| `grep -ri pattern dir --include='*.yml'` | Case-insensitive, only in matching files.      |
| `grep -l pattern *`                      | Prints only the names of matching files.       |
| `grep -v pattern file`                   | Prints lines that don't match.                 |
| `grep -C 3 pattern file`                 | Adds three lines of context around each match. |
| `grep -E 'error\|warn' file`             | Extended regex, here either word.              |

[ripgrep](https://github.com/BurntSushi/ripgrep) (`rg pattern`) searches recursively by default, skips files from
`.gitignore` and is much faster on large trees.

## find

`find` walks a directory tree and applies tests to every entry; all tests must match.

| Command                                   | Finds                                                       |
| ----------------------------------------- | ----------------------------------------------------------- |
| `find /home -name '*.log'`                | Files by name (`-iname` ignores case).                      |
| `find /home -type d -name cache`          | Only directories.                                           |
| `find /home -size +100M`                  | Files larger than 100 MiB.                                  |
| `find /var/log -mtime -1`                 | Files changed within the last 24 hours.                     |
| `find . -name '*.tmp' -delete`            | Deletes matches. Run without `-delete` first.               |
| `find . -name '*.sh' -exec chmod +x {} +` | Runs a command on all matches.                              |
| `find / -xdev -user alice`                | Files of a user, without descending into other filesystems. |

:::caution
Quote patterns: unquoted, the shell expands `*.log` to the matching files in the **current** directory before `find`
sees it.
:::

## Programs and packages

| Command                | Effect                                                                      |
| ---------------------- | --------------------------------------------------------------------------- |
| `command -v app`       | Path of the program the shell would run (also finds aliases and functions). |
| `type -a app`          | All programs, aliases and functions with that name.                         |
| `rpm -qf /usr/bin/app` | Which package owns a file (Fedora/RHEL); `dpkg -S` on Debian.               |
| `dnf list --installed` | Installed packages (Fedora/RHEL); `apt list --installed` on Debian.         |
