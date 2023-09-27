---
layout: default
title: Tar Command
parent: Systemcommands
---

# {{ page.title }}

______________________________________________________________________

## Introduction

This document provides a cheat sheet for the tar command, which is used for archiving and compressing files and directories.

______________________________________________________________________

### Basic Operations

| Option | Function                         | Example                 |
| ------ | -------------------------------- | ----------------------- |
| c      | Create a tar archive             | tar cf Archive.tar Data |
| x      | Extract files from a tar archive | tar xf Archive.tar      |
| t      | List files in a tar archive      | tar tf Archive.tar      |
| f      | Specify the archive file name    |                         |

### Compression Options

| Option | Function                          | Example                            |
| ------ | --------------------------------- | ---------------------------------- |
| I      | Select compression program        | tar cI zst -f Archive.tar.zst Data |
| a      | Use automatic compression program | tar caf Archive.tar.zst Data       |

### Examples

Create a tar archive named `archive.tar` containing the `directory`:

```
tar cf archive.tar directory
```

Extract the contents from `archive.tar`:

```
tar xf archive.tar
```

List the contents from `archive.tar`:

```
tar tf archive.tar
```
