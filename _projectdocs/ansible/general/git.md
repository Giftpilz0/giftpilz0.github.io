---
layout: default
title: Git Role
parent: General Collection
grand_parent: Ansible
---

# {{ page.title }}

This Ansible role can be used to install git and customize git config.

______________________________________________________________________

## Variables

| Variables                | Type   | Options                 | Defaults |
| ------------------------ | ------ | ----------------------- | -------- |
| git_package_state:       | string | present, absent, latest | present  |
| git_package:             | list   | ---                     | git      |
|                          |        |                         |          |
| git_config_system:       | dict   | ---                     | ---      |
| git_config_system.key:   | string | ---                     | ---      |
| git_config_system.value: | string | ---                     | ---      |
|                          |        |                         |          |
| git_config:              | dict   | ---                     | ---      |
| git_config.key:          | string | ---                     | ---      |
| git_config.value:        | string | ---                     | ---      |
| git_config.scope:        | string | file, local, global     | ---      |

______________________________________________________________________

## Example Playbook

```yaml
- name: Import git Role
  hosts: all
  roles:
    - role: giftpilz0.general.git
```
