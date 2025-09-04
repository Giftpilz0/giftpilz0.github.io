---
title: Autoupgrade Role
---

This Ansible role can be used to configure automatic updates.

______________________________________________________________________

## Variables

| Variables                        | Type   | Options                               | Defaults                    |
| -------------------------------- | ------ | ------------------------------------- | --------------------------- |
| autoupgrade_service_name:        | string | ---                                   | dnf-automatic-install.timer |
| autoupgrade_service_state:       | string | reloaded, restarted, started, stopped | started                     |
| autoupgrade_service_enabled:     | bool   | false, true                           | true                        |
| autoupgrade_package_state:       | string | present, absent, latest               | present                     |
| autoupgrade_package:             | list   | ---                                   | dnf-automatic               |
| autoupgrade_config_path:         | string | ---                                   | /etc/dnf/automatic.conf     |
| autoupgrade_config_auto_apply:   | bool   | false, true                           | true                        |
| autoupgrade_config_upgrade_type: | string | default, security                     | default                     |
| autoupgrade_config_reboot:       | string | never, when-changed, when-needed      | never                       |

______________________________________________________________________

## Example Playbook

```yaml
- name: Import autoupgrade Role
  hosts: all
  roles:
    - role: giftpilz0.general.autoupgrade
```
