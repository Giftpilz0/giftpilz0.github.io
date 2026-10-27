---
title: Network
---

## Interfaces and addresses

| Command                | Shows                                                      |
| ---------------------- | ---------------------------------------------------------- |
| `ip -br a`             | Interfaces with state and addresses, one per line.         |
| `ip r`                 | Routing table, including the default gateway.              |
| `ip route get 1.1.1.1` | Which interface and gateway a packet to that address uses. |
| `ip neigh`             | ARP/neighbor cache (replaces `arp`).                       |
| `hostname -I`          | All local IP addresses.                                    |
| `ethtool eth0`         | Link speed, duplex and whether a cable is detected.        |

## Connectivity and DNS

When something is unreachable, test from the bottom up; the first step that fails is where to look.

| Step | Test              | Checks                             |
| :--: | ----------------- | ---------------------------------- |
|  1   | `ip -br a`        | The link is up and has an address. |
|  2   | `ping <gateway>`  | The local network works.           |
|  3   | `ping 1.1.1.1`    | Routing to the internet works.     |
|  4   | `dig example.com` | Name resolution works.             |
|  5   | `nc -zv host 443` | The service itself answers.        |

| Command                         | Effect                                                                   |
| ------------------------------- | ------------------------------------------------------------------------ |
| `ping -c 4 host`                | Sends four ICMP echo requests.                                           |
| `tracepath host`                | Shows the route and where packets get lost (`mtr` live).                 |
| `dig example.com`               | DNS lookup; `+short` for just the answer, `@1.1.1.1` for another server. |
| `dig -x 192.0.2.1`              | Reverse lookup.                                                          |
| `resolvectl status`             | DNS servers in use with systemd-resolved.                                |
| `nc -zv host 443`               | Tests whether a TCP port is open.                                        |
| `curl -I https://example.com`   | Fetches only the HTTP response headers.                                  |
| `wget https://example.com/file` | Downloads a file.                                                        |

## Ports and connections

| Command     | Shows                                                |
| ----------- | ---------------------------------------------------- |
| `ss -tulpn` | Listening TCP and UDP ports with the owning process. |
| `ss -tupn`  | Established connections.                             |

`ss` options: `-t` TCP, `-u` UDP, `-l` listening, `-p` process (needs root for other users' processes), `-n` numeric
ports instead of service names.

## Scanning with nmap

| Command                                     | Effect                                          |
| ------------------------------------------- | ----------------------------------------------- |
| `nmap -sn 192.168.178.0/24`                 | Finds hosts in a network without port scanning. |
| `nmap -sS --top-ports 100 192.168.178.0/24` | Scans the 100 most common ports (needs root).   |
| `nmap -sV 192.168.178.151`                  | Detects service versions on open ports.         |
| `nmap -Pn 192.168.178.151`                  | Scans even if the host doesn't answer ping.     |

:::caution
Only scan networks you own or are allowed to test.
:::

## NetworkManager

| Command                                                                                   | Effect                                           |
| ----------------------------------------------------------------------------------------- | ------------------------------------------------ |
| `nmcli device`                                                                            | Devices and their connections.                   |
| `nmcli connection show <name>`                                                            | All settings of a connection, e.g. DHCP details. |
| `nmcli device wifi list`                                                                  | Visible wireless networks.                       |
| `nmcli device wifi connect <ssid> --ask`                                                  | Connects to a wireless network.                  |
| `nmcli connection add type bridge ifname br0 con-name br0`                                | Creates a bridge.                                |
| `nmcli connection modify br0 bridge.stp no ipv4.method manual ipv4.addresses 10.0.0.1/24` | Configures it.                                   |
| `nmcli connection up br0`                                                                 | Activates it.                                    |

## Changing the MAC address

```sh
ip link set dev eth0 down
ip link set dev eth0 address aa:bb:cc:dd:ee:ff
ip link set dev eth0 up
```

The change is lost on reboot. With NetworkManager, set `802-3-ethernet.cloned-mac-address` (or `wifi.cloned-mac-address`)
on the connection instead; the value `random` picks a new address on every connect.
