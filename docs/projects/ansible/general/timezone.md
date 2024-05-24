---
title: Timezone Role
---

This Ansible role can be used to set the time zone of the system.

______________________________________________________________________

## Variables

| Variables          | Type   | Options | Defaults |
| ------------------ | ------ | ------- | -------- |
| timezone_timezone: | string | ---     | Etc/UTC  |

______________________________________________________________________

## Example Playbook

```yaml
- name: Import timezone Role
  hosts: all
  roles:
    - role: giftpilz0.general.timezone
```
