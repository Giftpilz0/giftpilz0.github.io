---
title: User Role
---

This Ansible role can be used to manage users, groups, passwords, SSH keys, and sudo permissions.

______________________________________________________________________

## Variables

| Variables                         | Type   | Options         | Defaults  |
| --------------------------------- | ------ | --------------- | --------- |
| user_mkpasswd_package:            | string | ---             | ---       |
| user_key_target_users:            | list   | ---             | root      |
|                                   |        |                 |           |
| user:                             | list   | ---             | []        |
| user.user_username:               | string | ---             | ---       |
| user.user_state:                  | string | present, absent | present   |
| user.user_password:               | string | ---             | !         |
| user.user_groups:                 | list   | ---             | []        |
| user.user_home:                   | bool   | false, true     | true      |
| user.user_shell:                  | string | ---             | /bin/bash |
| user.user_comment:                | string | ---             | ---       |
| user.user_sudo_pwless:            | bool   | false, true     | false     |
| user.user_pub:                    | list   | ---             | []        |
| user.user_install_key_to_targets: | bool   | false, true     | true      |

______________________________________________________________________

## Example Playbook

```yaml
- name: Import user Role
  hosts: all
  roles:
    - role: giftpilz0.general.user
```
