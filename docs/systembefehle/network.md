---
layout: default
title: Netzwerk
parent: Systembefehle
---

# {{ page.title }}

______________________________________________________________________

Display all network interfaces and IP address

`ip a`

Query or control network driver and hardware settings

`ethtool eth0`

Send ICMP echo request to host

`ping host`

Display whois information for domain

`whois domain`

Display DNS information for domain

`dig domain`
`nslookup domain`

Reverse lookup of IP_ADDRESS

`dig -x 192.168.178.151`

Display DNS IP address for domain

`host domain`

Display the network address of the host name

`hostname -i`

Display all local IP addresses of the host

`hostname -I`

Download file

`wget http://domain.com/file`

Display listening tcp and udp ports and corresponding programs

`netstat -nutlp`
`ss -lpntu`

List arp-entries

`arp --numeric -e | sort --numeric-sort`

Quick scan

`sudo nmap -sS --top-ports 100 192.168.178.0/24`

Scan ports of IP

`nmap -sS 192.168.178.151`

Scan ports of IP, if host isnt reachable

`nmap -Pn 192.168.178.151`

MAC-address ändern

`ip link set {device} down`
`ip link set {device} address aa:aa:aa:aa:aa:aa`
`ip link set {device} up`

Get network info

`nmcli connection show {network} | grep DHCP`

Get wireless networks

`nmcli -p --mode tabular --fields BSSID,SSID,MODE,CHAN,FREQ,BARS,ACTIVE,SECURITY device wifi list`
`wavemon`

nmap vuln scan

https://geekflare.com/de/nmap-vulnerability-scan
https://nmap.org/book/nse-usage.html

Spoof IP

`iptables -t nat -A POSTROUTING -j SNAT --to-source ipaddress`

https://sandilands.info/sgordon/address-spoofing-with-iptables-in-linux

![](/app/joplin-desktop/resources/app/:/db6f9316a6d4d9c047f7d90ed6580935.png)
