---
title: Autoupgrade Role
---

Configure automatic package upgrades on Debian or Red Hat systems.

______________________________________________________________________

## Variables

| Variable                      | Type           | Options                                       | Default                                                                | Description                                                                                   |
| ----------------------------- | -------------- | --------------------------------------------- | ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `autoupgrade_service_name`    | string         | ---                                           |                                                                        | systemd service or timer unit name                                                            |
| `autoupgrade_service_state`   | string         | reloaded, restarted, started, stopped         |                                                                        | desired state of the autoupgrade service                                                      |
| `autoupgrade_service_enabled` | bool           | true, false                                   |                                                                        | whether the autoupgrade service is enabled at boot                                            |
| `autoupgrade_package_state`   | string         | present, absent, latest                       |                                                                        | desired state of autoupgrade packages                                                         |
| `autoupgrade_package_list`    | list of string | ---                                           |                                                                        | list of packages to install for automatic upgrades                                            |
| `autoupgrade_config_path`     | string         | ---                                           |                                                                        | path to the autoupgrade configuration file                                                    |
| `autoupgrade_auto_apply`      | bool           | true, false                                   | true                                                                   | whether to automatically apply package upgrades                                               |
| `autoupgrade_upgrade_type`    | string         | default, security                             | default                                                                | type of upgrades to apply                                                                     |
| `autoupgrade_reboot`          | string         | false, true, never, when-changed, when-needed | `{{ 'false' if ansible_facts['os_family'] == 'Debian' else 'never' }}` | reboot policy; use false or true on Debian and never, when-changed, or when-needed on Red Hat |
| `autoupgrade_blacklist`       | list of string | ---                                           | []                                                                     | list of packages excluded from automatic upgrades                                             |
| `autoupgrade_mail_report`     | string         | ---                                           | ""                                                                     | email reporting frequency (e.g. on-change, always, only-on-error)                             |
| `autoupgrade_mail`            | string         | ---                                           | ""                                                                     | recipient email address for upgrade reports                                                   |
