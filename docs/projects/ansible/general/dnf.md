---
title: DNF Role
---

This Ansible role can be used to configure automatic updates via dnf-automatic.

______________________________________________________________________

## Variables

| Variables                          | Type   | Options                               | Defaults                    |
| ---------------------------------- | ------ | ------------------------------------- | --------------------------- |
| dnf_automatic_service_name:        | string | ---                                   | dnf-automatic-install.timer |
| dnf_automatic_service_state:       | string | reloaded, restarted, started, stopped | started                     |
| dnf_automatic_service_enabled:     | bool   | false, true                           | true                        |
| dnf_automatic_package_state:       | string | present, absent, latest               | present                     |
| dnf_automatic_package:             | list   | ---                                   | dnf-automatic               |
| dnf_automatic_config_path:         | string | ---                                   | /etc/dnf/automatic.conf     |
| dnf_automatic_config_auto_apply:   | bool   | false, true                           | true                        |
| dnf_automatic_config_upgrade_type: | string | default, security                     | default                     |
| dnf_automatic_config_reboot:       | string | never, when-changed, when-needed      | never                       |

______________________________________________________________________

## Example Playbook

```yaml
- name: Import dnf Role
  hosts: all
  roles:
    - role: giftpilz0.general.dnf
```
