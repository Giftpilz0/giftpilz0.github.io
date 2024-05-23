---
layout: default
title: VLAN
parent: Cisco
---

______________________________________________________________________

## Introduction

Virtual Local Area Networks (VLANs) are a fundamental network configuration concept that enables network administrators to logically divide a physical network into multiple isolated segments. Each VLAN operates as its own virtual network, providing enhanced network security, traffic management, and flexibility in network design. This cheat sheet serves as a quick reference for configuring VLANs on Cisco devices.

______________________________________________________________________

## Configuration Steps

### Creating VLANs

Use the following commands to create VLANs:

```
Switch# configure terminal
Switch(config)# vlan {VLAN_ID}
Switch(config-vlan)# name {VLAN_NAME}
Switch(config-vlan)# end
Switch# write memory
```

### Assign a VLAN to an Interface

To assign a VLAN to an interface, use the following commands:

```
Switch# configure terminal
Switch(config)# interface {INTERFACE_TYPE} {INTERFACE_NUMBER}
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan {VLAN_ID}
Switch(config-if)# end
Switch# write memory
```

### Configure VLAN Trunk

To configure a VLAN trunk, follow these steps:

```
Switch# configure terminal
Switch(config)# interface {INTERFACE_TYPE} {INTERFACE_NUMBER}
Switch(config-if)# switchport mode trunk
Switch(config-if)# switchport trunk allowed vlan {VLAN_LIST}
Switch(config-if)# end
Switch# write memory
```

______________________________________________________________________

## Commands

### Enter Configuration Mode

To enter global configuration mode for making VLAN configuration changes, use:

```
Switch# configure terminal
```

### Create a VLAN

To create a VLAN on a Cisco device, use this command:

```
Switch(config)# vlan {VLAN_ID}
```

### Assign a Name to a VLAN

To assign a meaningful name to a VLAN, use:

```
Switch(config-vlan)# name {VLAN_NAME}
```

### Exit Configuration Mode

To exit configuration mode and return to privileged EXEC mode, run:

```
Switch(config-vlan)# end
```

### Save Configuration Changes

To save the changes made to the configuration, use the following command:

```
Switch# write memory
```
