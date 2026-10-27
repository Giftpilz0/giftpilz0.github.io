---
title: Tar Command
---

tar bundles files into one archive and can compress it in the same step. Options combine into a single word: one mode
(`c`, `x` or `t`), then modifiers, with `f` and the archive name last.

| Command                                         | Effect                                                                  |
| ----------------------------------------------- | ----------------------------------------------------------------------- |
| `tar caf archive.tar.zst dir`                   | Creates an archive; `a` picks the compression from the file extension.  |
| `tar xf archive.tar.zst`                        | Extracts. The compression is detected automatically.                    |
| `tar xf archive.tar.zst -C /target`             | Extracts into another directory.                                        |
| `tar tf archive.tar.zst`                        | Lists the contents.                                                     |
| `tar xf archive.tar.zst path/in/archive`        | Extracts only some files.                                               |
| `tar caf backup.tar.zst --exclude='*.log' dir`  | Skips matching files.                                                   |
| `tar -I 'zstd -19 -T0' -cf archive.tar.zst dir` | Passes options to the compressor, here maximum zstd level on all cores. |

| Option                  | Meaning                           |
| ----------------------- | --------------------------------- |
| `c`                     | Create an archive.                |
| `x`                     | Extract.                          |
| `t`                     | List the contents.                |
| `f`                     | Archive file name (follows next). |
| `v`                     | List files while working.         |
| `a`                     | Compression by file extension.    |
| `z`, `j`, `J`, `--zstd` | gzip, bzip2, xz, zstd.            |

| Format     | Speed     | Size     | Note                        |
| ---------- | --------- | -------- | --------------------------- |
| `.tar.gz`  | fast      | larger   | Works everywhere.           |
| `.tar.xz`  | slow      | smallest | Common for source releases. |
| `.tar.zst` | very fast | small    | Good default today.         |

:::tip
tar strips the leading `/` from absolute paths, so archives always extract relative to the current directory (or `-C`).
Check with `tar tf` before extracting archives from others to see whether they contain a top-level directory.
:::
