---
layout: default
title: Cheat Sheet
parent: Pacemaker
---

## Pacemaker configuration files and directories

______________________________________________________________________

```yaml
/var/lib/pacemaker/cib/cib.xml: Cluster configuration file
/var/log/cluster/corosync.log: Corosync log file
/etc/sysconfig/pacemaker: Pacemaker configuration file
/var/log/pacemaker.log: Pacemaker log file
/usr/lib/ocf/resource.d/heartbeat: Directory where all the cluster resource scripts are available
```

______________________________________________________________________

## Pacemaker administration Commands

______________________________________________________________________

Pacemaker cluster command to view cluster nodes status

`pcs cluster status`

Pacemaker cluster command to view detailed status of the cluster nodes and resources

`pcs status --full`

Pacemaker cluster command to view status of the cluster nodes and resources

`crm_mon -r1`

Pacemaker cluster command to view real time status of the cluster nodes and resources

`crm_mon r`

Pacemaker cluster command to view status of all cluster resources and resource groups

`pcs cluster standby`

Pacemaker cluster command to remove the cluster node from standby mode

`pcs cluster unstandby`

Pacemaker cluster command to move the cluster resource from one node to another node

`pcs resource show`

Pacemaker cluster command to put the cluster node on standby mode

`pcs resource move`

Pacemaker cluster command to restart the cluster resource on the running node

`pcs resource restart`

Pacemaker cluster command to start the cluster resource on current node

`pcs resource enable`

Pacemaker cluster command to stop cluster resource on running node

`pcs resource disable`

Pacemaker cluster command to start debug cluster resource. You can use the switch --full for more verbose output

`pcs resource debug-start`

Pacemaker cluster command to stop debugging cluster resource. You can use the switch --full for even more verbose output

`pcs resource debug-stop`

Pacemaker cluster command to monitor cluster resource debugging. You can use the switch --full for even more verbose output

`pcs resource debug-monitor`

Pacemaker cluster command to list available cluster resource agents

`pcs resource agents`

Pacemaker cluster command to list available cluster resource agents with more information

`pcs resource list`

Pacemaker cluster command to view detailed information about cluster resource agents and their configuration or settings

`pcs resource describe`

Pacemaker cluster command to create a cluster resource

`pcs resource create options`

Pacemaker cluster command to view cluster configuration settings of a perticular resource

`pcs resource show`

Pacemaker cluster command to update specific cluster resource configuration

`pcs resource update options`

Pacemaker cluster command to delete specific cluster resource

`pcs resource delete`

Pacemaker cluster command to cleanup specific cluster resource

`pcs resource cleanup`

Pacemaker cluster command to list available cluster fence agents

`pcs stonith list`

Pacemaker cluster command to view detail cluster configuration settings for fence agent

`pcs stonith describe`

Pacemaker cluster command to create Pacemaker cluster stonith agent

`pcs stonith create stonith options`

Display Pacemaker cluster configured settings of stonith agent

`pcs stonith show`

Update Pacemaker cluster stonith configuration

`pcs stonith update options`

Pacemaker cluster command to delete stonith agent

`pcs stonith delete`

Pacemaker cluster command to cleanup stonith agent failures

`pcs stonith cleanup`

Pacemaker cluster command to check cluster configuration

`pcs config`

Pacemaker cluster command to check cluster property

`pcs property list`

Pacemaker cluster command to get more details about cluster property

`pcs property list --all`

Pacemaker cluster command to check cluster Configuration with XML format

`pcs cluster cib`

Pacemaker cluster command to check cluster node status

`pcs status nodes`

Pacemaker cluster command to start cluster service on current node

`pcs cluster start`

Pacemaker cluster command to start cluster service on all the nodes

`pcs cluster start --all`

Pacemaker cluster command to stop cluster service on current node

`pcs cluster stop`

Pacemaker cluster command to stop cluster service on all the nodes

`pcs cluster stop --all`

Pacemaker cluster command to sync corosync.conf file

`pcs cluster sync`

Pacemaker cluster command to destroy cluster

`pcs cluster destroy`

Pacemaker cluster command to create new cluster configuration file. This file will be created on current location, you can add multiple cluster resource into this configuration file and apply them by using cib-push command

`pcs cluster cib`

Pacemaker cluster command to apply the resource created in configuration file into cluster

`pcs cluster cib-push`

Pacemaker cluster command to view cluster resource group list

`pcs resource group list`

Pacemaker cluster command to view corosync configuration output

`pcs cluster corosync`

Pacemaker cluster command to check the cluster resource order

`pcs constraint list`

Pacemaker cluster command to ignore quorum policy

`pcs property set no-quorum-policy=ignore`

Pacemaker cluster command to disable stonith

`pcs property set stonith-enabled=false`

Pacemaker cluster command to set cluster default stickiness value

`pcs resource defaults resource-stickiness=100`
