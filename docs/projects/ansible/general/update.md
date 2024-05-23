---
layout: default
title: Update Role
parent: General Collection
grand_parent: Ansible
---

This Ansible role can be used to update systems with dnf.

______________________________________________________________________

## Variables

| Variables                     | Type | Options     | Defaults |
| ----------------------------- | ---- | ----------- | -------- |
| update_package_names:         | list | ---         | \*       |
| update_package_security_only: | bool | false, true | false    |
| update_package_bugfix_only:   | bool | false, true | false    |

______________________________________________________________________

## Example Playbook

```yaml
- name: Import update Role
  hosts: all
  roles:
    - role: giftpilz0.general.update
```
