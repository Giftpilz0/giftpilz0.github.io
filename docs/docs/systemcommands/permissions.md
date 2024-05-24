---
title: Linux Permissions
---

______________________________________________________________________

## Introduction

File permissions in a Linux environment determine who can access, modify, and execute files.

______________________________________________________________________

## File Permission Example

| User | Group | World | Short |
| ---- | ----- | ----- | ----- |
| rwx  | r-x   | r-x   | 755   |
| rw-  | r--   | r--   | 644   |

### Explanation:

- The file permissions are rwx for the user and r-x for the group and world, totaling 755 numerically.
- The file permissions are rw- for the user and r-- for the group and world, totaling 644 numerically.

## Legend

| Permission | Short | Numeric Value |
| ---------- | ----- | ------------- |
| Read       | r     | 4             |
| Write      | w     | 2             |
| Execute    | x     | 1             |

- User: The owner of the file.
- Group: Users who are in the same group as the owner.
- World: All other users.

## Special Bits:

| Special Bit    | Numeric Code | Description                                                                                                    |
| -------------- | ------------ | -------------------------------------------------------------------------------------------------------------- |
| Setuid (s)     | 4            | Allows an executable file to run with the owner's permissions, regardless of the user running it.              |
| Setgid (s)     | 2            | Enables an executable file to run with the group's permissions that own it, regardless of the user running it. |
| Sticky Bit (t) | 1            | Prevents deletion of files in a directory by users other than the owner.                                       |
