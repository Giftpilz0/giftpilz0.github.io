---
title: Network
---

______________________________________________________________________

Display all network interfaces and IP addresses

`ip a`

Query or control network driver and hardware settings

`ethtool eth0`

Send ICMP echo request to host

`ping host`

Display DNS information for domain

```
dig domain
host domain
nslookup domain
```

Display the network address of the host name

`hostname -i`

Display all local IP addresses of the host

`hostname -I`

Download file

`wget http://domain.com/file`

Display listening tcp and udp ports and corresponding programs

`ss -tulpn`

Display active connections

`ss -tupn`

List arp-entries

`arp --numeric -e | sort --numeric-sort`

Quick scan

`nmap -sS --top-ports 100 192.168.178.0/24`

Scan ports

`nmap -sS 192.168.178.151`

Scan ports, if host is not reachable

`nmap -Pn 192.168.178.151`

Change MAC address

```
ip link set {device} down
ip link set {device} address aa:aa:aa:aa:aa:aa
ip link set {device} up
```

Get network info

`nmcli connection show {network} | grep DHCP`

Get wireless networks

```
nmcli -p --mode tabular --fields BSSID,SSID,MODE,CHAN,FREQ,BARS,ACTIVE,SECURITY device wifi list
```

iptables

[https://wiki.archlinux.org/title/iptables](https://wiki.archlinux.org/title/iptables)

Network Bridges - NetworkManager

```
nmcli connection add type bridge
nmcli connection modify Connection bridge.stp no ipv4.addresses 10.0.0.1/24
nmcli connection up Connection
```
