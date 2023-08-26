---
layout: default
title: Dotfiles Role
parent: General Collection
grand_parent: Ansible
---

# {{ page.title }}

This Ansible role can be used to configure vim, bash and readline.

______________________________________________________________________

## Variables

| Variables                     | Type   | Options                 | Defaults     |
| ----------------------------- | ------ | ----------------------- | ------------ |
| dotfiles_package_state:       | string | present, absent, latest | present      |
| dotfiles_package:             | list   | ---                     | bash,vim     |
| dotfiles_inputrc_file         | string | ---                     | /etc/inputrc |
| dotfiles_inputrc_state:       | string | present, absent, skip   | present      |
| dotfiles_bashprofile_enabled: | bool   | false, true             | true         |

______________________________________________________________________

## Example Playbook

```yaml
- name: Import dotfiles Role
  hosts: all
  roles:
    - role: giftpilz0.general.dotfiles
```
