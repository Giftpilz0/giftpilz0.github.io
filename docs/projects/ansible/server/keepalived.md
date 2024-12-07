---
title: Keepalived Role
---

This Ansible role can be used to install keepalived.

______________________________________________________________________

## Variables

| Variables                            | Type   | Options                               | Defaults                        |
| ------------------------------------ | ------ | ------------------------------------- | ------------------------------- |
| keepalived_service_name:             | string | ---                                   | keepalived.service              |
| keepalived_service_state:            | string | reloaded, restarted, started, stopped | started                         |
| keepalived_service_enabled:          | bool   | false, true                           | true                            |
| keepalived_package_state:            | string | present, absent, latest               | present                         |
| keepalived_package:                  | list   | ---                                   | keepalived                      |
|                                      |        |                                       |                                 |
| keepalived_config_path:              | string | ---                                   | /etc/keepalived/keepalived.conf |
| keepalived_config_virtual_ip:        | string | ---                                   | ---                             |
| keepalived_config_interface:         | string | ---                                   | eth0                            |
| keepalived_config_priority:          | int    | 0-255                                 | 255                             |
| keepalived_config_virtual_router_id: | int    | 0-255                                 | 100                             |
| keepalived_config_vrrp_instance:     | string | ---                                   | VG                              |
| keepalived_config_state:             | string | MASTER, BACKUP                        | MASTER                          |

______________________________________________________________________

## Example Playbook

```yaml
- name: Import keepalived Role
  hosts: all
  roles:
    - role: giftpilz0.server.keepalived
```
