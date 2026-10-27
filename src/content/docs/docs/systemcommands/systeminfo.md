---
title: Systeminfo
---

| Command                   | Shows                                                   |
| ------------------------- | ------------------------------------------------------- |
| `cat /etc/os-release`     | Distribution and version, on every modern distribution. |
| `uname -r`                | Kernel version (`uname -a` for everything).             |
| `hostnamectl`             | Hostname, OS, kernel, architecture and hardware model.  |
| `uptime -p`               | How long the system has been running.                   |
| `last reboot`             | Reboot history.                                         |
| `journalctl -b -1 -p err` | Errors from the previous boot, e.g. after a crash.      |
| `systemctl --failed`      | Services that failed to start.                          |
| `systemd-analyze blame`   | Which services slow down the boot.                      |
| `timedatectl`             | Time, time zone and whether NTP sync is active.         |
| `fastfetch`               | A summary with the distribution logo.                   |
