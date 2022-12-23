---
layout: default
title: Statistics
parent: Systemcommands
---

# {{ page.title }}

______________________________________________________________________

Interactive process viewer (top alternative)

`htop`

Display processor related statistics

`mpstat 1`

Display virtual memory statistics

`vmstat 1`

Display I/O statistics

`iostat 1`

Capture and display all packets on interface eth0

`tcpdump -i eth0`

Monitor all traffic on port 80 (HTTP)

`tcpdump -i eth0 'port 80'`

List all open files on the system

`lsof`

List files opened by user

`lsof -u user`

Display free and used memory ( -h for human readable, -m for MB, -g for GB.)

`free -h`

Execute "df -h", showing periodic updates

`watch df -h`
