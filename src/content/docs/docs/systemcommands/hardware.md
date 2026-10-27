---
title: Hardware
---

| Command                    | Shows                                                                   |
| -------------------------- | ----------------------------------------------------------------------- |
| `lscpu`                    | CPU model, cores, threads and virtualization support.                   |
| `cat /proc/cpuinfo`        | Detailed information per CPU thread.                                    |
| `free -h`                  | Memory and swap usage.                                                  |
| `cat /proc/meminfo`        | Detailed memory statistics.                                             |
| `lspci -tv`                | PCI devices as a tree; `lspci -k` adds the kernel driver.               |
| `lsusb -tv`                | USB devices as a tree.                                                  |
| `lsblk`                    | Block devices and partitions.                                           |
| `sudo dmidecode -t memory` | RAM modules from the firmware tables (`-t system` for the model).       |
| `sudo dmesg -w`            | Kernel messages, live. Shows hardware errors and newly plugged devices. |
| `sensors`                  | Temperatures and fan speeds (package `lm_sensors`).                     |

## Disks

| Command                           | Effect                                                       |
| --------------------------------- | ------------------------------------------------------------ |
| `sudo smartctl -a /dev/sda`       | SMART health data and error log (package `smartmontools`).   |
| `sudo smartctl -t short /dev/sda` | Starts a short self-test; results appear in `-a` afterwards. |
| `sudo hdparm -tT /dev/sda`        | Measures read speed.                                         |
| `sudo badblocks -sv /dev/sda`     | Read-only scan for unreadable blocks.                        |

:::tip
In `free`, the _available_ column is what matters. Linux uses idle memory as a disk cache (_buff/cache_) and releases
it when programs need it, so low _free_ memory is normal.
:::

:::danger
`badblocks -w` overwrites the whole disk. Without `-w` (or with `-n`, non-destructive read-write) the data stays intact.
:::
