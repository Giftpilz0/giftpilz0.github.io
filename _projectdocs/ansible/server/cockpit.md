---
layout: default
title: Cockpit Role
parent: Ansible Server Collection
grand_parent: Ansible
---

# {{ page.title }}

This Ansible role can be used to configure the Cockpit Server Administration Web UI.

______________________________________________________________________

## Variables

| Variables                               | Type   | Options                                        | Defaults                                          |
| --------------------------------------- | ------ | ---------------------------------------------- | ------------------------------------------------- |
| cockpit_service_name:                   | string | ---                                            | cockpit.socket                                    |
| cockpit_service_state:                  | string | reloaded, restarted, started, stopped          | started                                           |
| cockpit_service_enabled:                | bool   | false, true                                    | true                                              |
| cockpit_package_state:                  | string | present, absent, latest                        | present                                           |
| cockpit_package:                        | list   | ---                                            | cockpit, cockpit-storaged, cockpit-networkmanager |
|                                         |        |                                                |                                                   |
| cockpit_additional_package:             | dict   | ---                                            | ---                                               |
| cockpit_additional_package.package:     | string | ---                                            | ---                                               |
| cockpit_additional_package.requirement: | string | ---                                            | ---                                               |
| cockpit_additional_package.state:       | string | present, absent, latest, skip                  | present                                           |
|                                         |        |                                                |                                                   |
| cockpit_firewalld_zone:                 | string | block, dmz, drop, internal, public, trusted... | ---                                               |
| cockpit_firewalld_service:              | string | ---                                            | cockpit                                           |
| cockpit_firewalld_state:                | string | present, absent, enabled, disabled, skip       | enabled                                           |

______________________________________________________________________

## Example Playbook

```yaml
- name: Import cockpit Role
  hosts: all
  roles:
    - role: giftpilz0.server.cockpit
```
