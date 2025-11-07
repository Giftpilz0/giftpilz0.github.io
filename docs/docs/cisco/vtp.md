---
title: VLAN Trunking Protocol
---

______________________________________________________________________

## Introduction

The VLAN Trunking Protocol (VTP) is a Cisco proprietary protocol used to simplify the management and configuration of Virtual LANs (VLANs) on Cisco networking devices. VTP allows network administrators to manage VLAN configurations across multiple switches in a network. This cheat sheet provides a quick reference for configuring and understanding VTP on Cisco devices.

______________________________________________________________________

## VTP Modes

| VTP Mode         | Description                                                                                                                         |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Server Mode      | In this mode, a switch can create, modify, and delete VLANs. Changes are propagated to other switches in the VTP domain.            |
| Client Mode      | A switch in client mode can't create, modify, or delete VLANs. It synchronizes its VLAN database with the VTP server.               |
| Transparent Mode | A switch in transparent mode doesn't participate in VTP updates but forwards them. It allows for the manual configuration of VLANs. |

### Configuring VTP Modes

To configure VTP modes, use these commands:

```
Switch# configure terminal
Switch(config)# vtp mode {MODE}
Switch(config)# vtp domain {DOMAIN_NAME}
Switch(config)# end
Switch# write memory
```

## VTP Domains

A VTP domain is a logical group of switches that share VTP information. Switches in the same domain synchronize their VLAN databases.

### Configuring VTP Domain

To set the VTP domain, use the following command:

```
Switch# configure terminal
Switch(config)# vtp domain {DOMAIN_NAME}
Switch(config)# end
Switch# write memory
```

## VTP Password

Setting a VTP password helps secure VTP updates. All switches in the VTP domain must use the same password.

### Configuring a VTP Password

To configure a VTP password, use the following command:

```
Switch# configure terminal
Switch(config)# vtp password {PASSWORD}
Switch(config)# end
Switch# write memory
```

______________________________________________________________________

## Commands

### Enter Configuration Mode

To enter global configuration mode for making VTP configuration changes, use:

```
Switch# configure terminal
```

### Set VTP Mode

To set the VTP mode (server, client, or transparent), use the following command:

```
Switch(config)# vtp mode {MODE}
```

### Set VTP Domain

To specify the VTP domain, use:

```
Switch(config)# vtp domain {DOMAIN_NAME}
```

### Set VTP Password

To configure a VTP password, use:

```
Switch(config)# vtp password {PASSWORD}
```

### Exit Configuration Mode

To exit configuration mode and return to privileged EXEC mode, run:

```
Switch(config)# end
```

### Save Configuration Changes

To save the changes made to the configuration, use the following command:

```
Switch# write memory
```
