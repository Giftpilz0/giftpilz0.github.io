---
layout: default
title: Spanning Tree Protocol
parent: Cisco
---

______________________________________________________________________

## Introduction

The Spanning Tree Protocol (STP) is a crucial network protocol used to prevent and manage network loops in Ethernet networks. It ensures network reliability and redundancy by creating a loop-free logical topology. This cheat sheet serves as a quick reference for configuring and understanding the Spanning Tree Protocol on Cisco devices.

______________________________________________________________________

## Overview

STP operates by designating a root bridge and blocking redundant paths to avoid network loops. It uses Bridge Protocol Data Units (BPDU) to communicate and elect the root bridge.

______________________________________________________________________

## Configuration Steps

### Enabling Spanning Tree Protocol

To enable STP on a Cisco device, follow these commands:

```
Switch# configure terminal
Switch(config)# spanning-tree vlan {VLAN_RANGE} priority {PRIORITY}
Switch(config)# end
Switch# write memory
```

### Override Root Bridge

To manually change the root bridge, use:

```
Switch# configure terminal
Switch(config)# spanning-tree vlan {VLAN_RANGE} root primary
Switch(config)# end
Switch# write memory
```

### Adjusting Port Costs

Modify the interface cost to influence path selection with the following command:

```
Switch# configure terminal
Switch(config)# interface INTERFACE_TYPE INTERFACE_NUMBER
Switch(config-if)# spanning-tree cost {COST}
Switch(config-if)# end
Switch# write memory
```

______________________________________________________________________

## Commands

### Enter Configuration Mode

To enter global configuration mode for making STP configuration changes, use:

```
Switch# configure terminal
```

### Set Priority

To set the priority of a bridge for root bridge election, use:

```
Switch(config)# spanning-tree vlan {VLAN_RANGE} priority {PRIORITY}
```

### Override Root Bridge

To manually change the root bridge, use:

```
Switch(config)# spanning-tree vlan {VLAN_RANGE} root primary
```

### Adjust Port Costs

To modify the cost of an interface for path selection, use:

```
Switch(config-if)# spanning-tree cost {COST}
```

### Check STP Status

To verify the STP status and details, use:

```
Switch# show spanning-tree
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
