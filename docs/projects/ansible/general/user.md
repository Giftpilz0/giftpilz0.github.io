---
title: User Role
---

This Ansible role can be used to configure users.

______________________________________________________________________

| Variables      | Type   | Options         | Defaults |
| -------------- | ------ | --------------- | -------- |
| user_username: | string | ---             | ---      |
| user_groups:   | list   | ---             | ---      |
| user_password: | string | ---             | ---      |
| user_home:     | bool   | false, true     | ---      |
| user_shell:    | string | ---             | ---      |
| user_state:    | string | present, absent | present  |

______________________________________________________________________

## Example Playbook

```yaml
- name: Import user Role
  hosts: all
  roles:
    - role: giftpilz0.general.user
```
