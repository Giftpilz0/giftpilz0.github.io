---
title: Monitoring Role
---

This Ansible role can be used to install grafana agent.

______________________________________________________________________

## Variables

| Variables                                        | Type   | Options                               | Defaults                                                                                                                                            |
| ------------------------------------------------ | ------ | ------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| monitoring_agent_package_state:                  | string | present, absent, latest               | present                                                                                                                                             |
| monitoring_agent_package:                        | string | ---                                   | `https://github.com/grafana/alloy/releases/download/v{{ monitoring_agent_tag }}/alloy-{{ monitoring_agent_tag }}-1.{{ monitoring_agent_arch }}.rpm` |
| monitoring_agent_arch:                           | string | ---                                   | amd64                                                                                                                                               |
| monitoring_agent_tag:                            | string | ---                                   | 1.11.3                                                                                                                                              |
| monitoring_agent_config_remoteserver_prometheus: | string | ---                                   | http://127.0.0.1:3100/loki/api/v1/push                                                                                                              |
| monitoring_agent_config_remoteserver_loki:       | string | ---                                   | http://127.0.0.1:9100/api/v1/push                                                                                                                   |
| monitoring_agent_config_path:                    | string | ---                                   | /etc/alloy/config.alloy                                                                                                                             |
| monitoring_agent_service_name:                   | string | ---                                   | alloy.service                                                                                                                                       |
| monitoring_agent_service_state:                  | string | reloaded, restarted, started, stopped | started                                                                                                                                             |
| monitoring_agent_service_enabled:                | bool   | false, true                           | true                                                                                                                                                |

______________________________________________________________________

## Example Playbook

```yaml
- name: Import monitoring Role
  hosts: all
  roles:
    - role: giftpilz0.general.monitoring
```
