---
layout: default
title: Sysutil Role
parent: General Collection
grand_parent: Ansible
---

# {{ page.title }}

This Ansible role can be used to install a small sysutil written in golang.

______________________________________________________________________

## Variables

| Variables          | Type   | Options         | Defaults                                                                                                          |
| ------------------ | ------ | --------------- | ----------------------------------------------------------------------------------------------------------------- |
| sysutil_bin_state: | string | present, absent | present                                                                                                           |
| sysutil_url:       | string | ---             | https://github.com/Giftpilz0/sysutil/releases/download/{{ sysutil_tag }}/sysutil_Linux\_{{ sysutil_arch }}.tar.gz |
| sysutil_arch:      | string | ---             | x86_64                                                                                                            |
| sysutil_tag:       | string | ---             | 1.0.0                                                                                                             |
| sysutil_path:      | string | ---             | /usr/local/bin                                                                                                    |

______________________________________________________________________

## Example Playbook

```yaml
- name: Import sysutil Role
  hosts: all
  roles:
    - role: giftpilz0.general.sysutil
```
