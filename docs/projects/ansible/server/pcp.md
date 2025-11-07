---
title: PCP Role
---

This Ansible role can be used to install Performance Co-Pilot.

______________________________________________________________________

## Variables

| Variables            | Type   | Options                               | Defaults                                     |
| -------------------- | ------ | ------------------------------------- | -------------------------------------------- |
| pcp_service_name:    | list   | ---                                   | pmie.service, pmlogger.service, pmcd.service |
| pcp_service_state:   | string | reloaded, restarted, started, stopped | started                                      |
| pcp_service_enabled: | bool   | false, true                           | true                                         |
| pcp_package_state:   | string | present, absent, latest               | present                                      |
| pcp_package:         | list   | ---                                   | pcp                                          |

______________________________________________________________________

## Example Playbook

```yaml
- name: Import pcp Role
  hosts: all
  roles:
    - role: giftpilz0.server.pcp
```
