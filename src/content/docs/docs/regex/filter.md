---
title: Useful Filters
---

| Task                                        | Command                                           |
| ------------------------------------------- | ------------------------------------------------- |
| Trim whitespace at the end of lines         | `sed -E 's/\s+$//' file`                          |
| Wrap long lines after at most 40 characters | `sed -E 's/.{1,40}( \|$)/&\n/g' file`             |
| Delete empty lines                          | `sed '/^\s*$/d' file`                             |
| Delete comment lines                        | `grep -v '^\s*#' file`                            |
| Show a config without comments and blanks   | `grep -Ev '^\s*(#\|$)' file`                      |
| Remove duplicate lines, keeping the order   | `awk '!seen[$0]++' file`                          |
| Count occurrences of each line              | `sort file \| uniq -c \| sort -rn`                |
| Extract all IPv4 addresses                  | `grep -oE '\b([0-9]{1,3}\.){3}[0-9]{1,3}\b' file` |
| Replace in place, with a backup             | `sed -i.bak 's/old/new/g' file`                   |

`fold -s -w 40 file` wraps at word boundaries too, without regex.
