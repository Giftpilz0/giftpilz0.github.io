---
layout: default
title: DNF Role
parent: General Collection
grand_parent: Ansible
---

This Ansible role can be used to configure automatic updates via dnf-automatic.

______________________________________________________________________

## Variables

| Variables                      | Type   | Options                               | Defaults                    |
| ------------------------------ | ------ | ------------------------------------- | --------------------------- |
| dnf_automatic_service_name:    | string | ---                                   | dnf-automatic-install.timer |
| dnf_automatic_service_state:   | string | reloaded, restarted, started, stopped | started                     |
| dnf_automatic_service_enabled: | bool   | false, true                           | true                        |
| dnf_automatic_package_state:   | string | present, absent, latest               | present                     |
| dnf_automatic_package:         | list   | ---                                   | dnf-automatic               |

______________________________________________________________________

## Example Playbook

```yaml
- name: Import dnf Role
  hosts: all
  roles:
    - role: giftpilz0.general.dnf
```
