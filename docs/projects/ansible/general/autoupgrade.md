---
title: Autoupgrade Role
---

Configure automatic package upgrades on Debian or Red Hat systems.

______________________________________________________________________

## Variables

| Variable                      | Type           | Options                               | Default                                                                                                                | Description                                                       |
| ----------------------------- | -------------- | ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| `autoupgrade_service_name`    | string         | ---                                   | `{{ 'apt-daily-upgrade.timer' if ansible_facts['os_family'] == 'Debian' else 'dnf-automatic.timer' }}`                 | systemd service or timer unit name                                |
| `autoupgrade_service_state`   | string         | reloaded, restarted, started, stopped | started                                                                                                                | desired state of the autoupgrade service                          |
| `autoupgrade_service_enabled` | bool           | true, false                           | true                                                                                                                   | whether the autoupgrade service is enabled at boot                |
| `autoupgrade_package_state`   | string         | present, absent, latest               | present                                                                                                                | desired state of autoupgrade packages                             |
| `autoupgrade_package_list`    | list of string | ---                                   | `{{ ['unattended-upgrades'] if ansible_facts['os_family'] == 'Debian' else ['dnf-automatic'] }}`                       | list of packages to install for automatic upgrades                |
| `autoupgrade_config_path`     | string         | ---                                   | `{{ '/etc/apt/apt.conf.d/20auto-upgrades' if ansible_facts['os_family'] == 'Debian' else '/etc/dnf/automatic.conf' }}` | path to the autoupgrade configuration file                        |
| `autoupgrade_auto_apply`      | bool           | true, false                           | true                                                                                                                   | whether to automatically apply package upgrades                   |
| `autoupgrade_upgrade_type`    | string         | default, security                     | default                                                                                                                | type of upgrades to apply                                         |
| `autoupgrade_reboot`          | bool           | true, false                           | false                                                                                                                  | reboot when an upgrade requires it                                |
| `autoupgrade_blacklist`       | list of string | ---                                   | []                                                                                                                     | list of packages excluded from automatic upgrades                 |
| `autoupgrade_mail_report`     | string         | ---                                   | ""                                                                                                                     | email reporting frequency (e.g. on-change, always, only-on-error) |
| `autoupgrade_mail`            | string         | ---                                   | ""                                                                                                                     | recipient email address for upgrade reports                       |
