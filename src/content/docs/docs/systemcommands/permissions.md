---
title: Linux Permissions
---

Every file has an owner, a group, and three sets of permissions: for the owner (**u**ser), the **g**roup and all
**o**thers. `ls -l` shows them as the first column:

```text
-rwxr-x---  1 alice developers  4096 Jan 1 12:00 deploy.sh
│└┬┘└┬┘└┬┘
│ │  │  └── others: no permissions
│ │  └───── group "developers": read, execute
│ └──────── owner "alice": read, write, execute
└────────── type: - file, d directory, l symlink
```

Each permission has a value, and the sum per set gives the octal notation: `rwx` = 4+2+1 = 7, `r-x` = 5, `---` = 0, so
the file above is `750`.

| Permission | Value | On a file            | On a directory                         |
| ---------- | :---: | -------------------- | -------------------------------------- |
| `r`        |   4   | Read the content.    | List the names of the entries.         |
| `w`        |   2   | Change the content.  | Create, rename and **delete** entries. |
| `x`        |   1   | Run it as a program. | Enter it and access entries by name.   |

:::note
Deleting a file is a change to the directory, so it needs `w` on the directory, not on the file.
:::

## Common modes

| Mode  | Symbolic    | Typical use                         |
| ----- | ----------- | ----------------------------------- |
| `644` | `rw-r--r--` | Regular files.                      |
| `755` | `rwxr-xr-x` | Directories and programs.           |
| `600` | `rw-------` | Private files, e.g. SSH keys.       |
| `700` | `rwx------` | Private directories, e.g. `~/.ssh`. |

## Commands

| Command                       | Effect                                                                                      |
| ----------------------------- | ------------------------------------------------------------------------------------------- |
| `chmod 640 file`              | Sets the mode in octal.                                                                     |
| `chmod u+x,g-w file`          | Adds or removes single permissions.                                                         |
| `chmod -R u=rwX,go=rX dir`    | Recursively; capital `X` sets execute only on directories and files that already have it.   |
| `chown alice:developers file` | Changes owner and group.                                                                    |
| `umask`                       | The permissions removed from new files, e.g. `022` gives `644` files and `755` directories. |
| `stat -c '%a %U:%G %n' file`  | Mode in octal with owner and group.                                                         |
| `namei -l /path/to/file`      | Permissions of every directory on the way, to find which one blocks access.                 |

## Special bits

A fourth leading digit sets them, e.g. `chmod 2775 dir`.

| Bit    | Value | `ls -l` shows    | On a file                                    | On a directory                                                        |
| ------ | :---: | ---------------- | -------------------------------------------- | --------------------------------------------------------------------- |
| setuid |   4   | `s` in owner `x` | Runs with the owner's rights, e.g. `passwd`. | (no effect)                                                           |
| setgid |   2   | `s` in group `x` | Runs with the group's rights.                | New entries inherit the directory's group; useful for shared folders. |
| sticky |   1   | `t` in other `x` | (no effect)                                  | Only the owner of an entry can delete it, e.g. `/tmp`.                |
