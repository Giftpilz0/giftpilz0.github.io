---
layout: default
title: Port Channels
parent: Cisco
---

# {{ page.title }}

______________________________________________________________________

## Introduction

Port Channels are a network configuration concept that allows network administrators to aggregate multiple physical network interfaces into a single logical interface. This aggregation increases bandwidth, redundancy, and load balancing capabilities for network connections. This cheat sheet serves as a quick reference for configuring Port Channels on Cisco devices.

______________________________________________________________________

## Configuration Steps

### Creating Port Channels

Use the following commands to create Port Channels:

```
Switch# configure terminal
Switch(config)# interface Port-channel {PORT_CHANNEL_NUMBER}
Switch(config-if)# description {DESCRIPTION}
Switch(config-if)# end
Switch# write memory
```

### Adding Physical Interfaces to a Port Channel

To add physical interfaces to a Port Channel, use the following commands:

```
Switch# configure terminal
Switch(config)# interface {INTERFACE_TYPE} {INTERFACE_NUMBER}
Switch(config-if)# channel-group {PORT_CHANNEL_NUMBER} mode {MODE}
Switch(config-if)# end
Switch# write memory
```

______________________________________________________________________

## Commands

### Enter Configuration Mode

To enter global configuration mode for making Port Channel configuration changes, use:

```
Switch# configure terminal
```

### Create a Port Channel

To create a Port Channel on a Cisco device, use this command:

```
Switch(config)# interface Port-channel {PORT_CHANNEL_NUMBER}
```

### View Port Channel Information

To view information about a Port Channel, use the following command:

```
Switch# show interface Port-channel {PORT_CHANNEL_NUMBER}
```

### Exit Configuration Mode

To exit configuration mode and return to privileged EXEC mode, run:

```
Switch(config-if)# end
```

### Save Configuration Changes

To save the changes made to the configuration, use the following command:

```
Switch# write memory
```
