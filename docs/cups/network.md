---
layout: default
title: Netzwerk
parent: Cups
---

# {{ page.title }}

Ports for IPP Printer Sharing

______________________________________________________________________

| (Destination) Port | TCP/UDP | Direction | Description                                                                             |
| ------------------ | ------- | --------- | --------------------------------------------------------------------------------------- |
| 53 (DNS)           | TCP/UDP | OUT       | Domain Name System lookup and service registrations.                                    |
| 631 (IPP/IPPS)     | TCP     | IN        | Internet Printing Protocol requests and responses (print jobs, status monitoring, etc.) |
| 5353 (mDNS)        | UDP     | IN+OUT    | Multicast DNS lookup and service registrations.                                         |

Ports for SMB Printer Sharing

| (Destination) Port(s) | TCP/UDP | Direction | Description                                                     |
| --------------------- | ------- | --------- | --------------------------------------------------------------- |
| 137 (WINS)            | UDP     | IN+OUT    | Windows Internet Naming Service (name lookup for SMB printing). |
| 139 (SMB)             | TCP     | IN        | Windows SMB printing.                                           |
| 445 (SMBDS)           | TCP     | IN+OUT    | Windows SMB Domain Server (authenticated SMB printing).         |

Printing Ports

| (Destination) Port(s) | TCP/UDP | Description                                                                             |
| --------------------- | ------- | --------------------------------------------------------------------------------------- |
| 53 (DNS)              | TCP/UDP | Domain Name System lookups.                                                             |
| 137 (WINS)            | UDP     | Windows Internet Naming Service (name lookup for SMB printing).                         |
| 139 (SMB)             | TCP     | Windows SMB printing.                                                                   |
| 161 (SNMP)            | UDP     | SNMP browsing (broadcast) and status monitoring (directed to printer IP address).       |
| 443 (IPPS)            | TCP     | Internet Printing Protocol requests and responses (print jobs, status monitoring, etc.) |
| 445 (SMBDS)           | TCP     | Windows SMB Domain Server (authenticated SMB printing).                                 |
| 515 (LPD)             | TCP     | Line Printer Daemon (LPD/lpr) print job submission and status monitoring.               |
| 631 (IPP/IPPS)        | TCP     | Internet Printing Protocol requests and responses (print jobs, status monitoring, etc.) |
| 5353 (mDNS)           | UDP     | Multicast DNS lookup.                                                                   |
| 9100-9102             | TCP     | Raw print data stream (AppSocket/JetDirect).                                            |
