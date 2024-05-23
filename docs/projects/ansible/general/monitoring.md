---
layout: default
title: Monitoring Role
parent: General Collection
grand_parent: Ansible
---

This Ansible role can be used to install grafana agent.

______________________________________________________________________

## Variables

| Variables                                        | Type   | Options                               | Defaults                                                                                                                                                        |
| ------------------------------------------------ | ------ | ------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| monitoring_agent_package_state:                  | string | present, absent, latest               | present                                                                                                                                                         |
| monitoring_agent_package:                        | string | ---                                   | `https://github.com/grafana/agent/releases/download/{{ monitoring_agent_tag }}/grafana-agent-flow-{{ monitoring_agent_tag }}-1.{{ monitoring_agent_arch }}.rpm` |
| monitoring_agent_arch:                           | string | ---                                   | amd64                                                                                                                                                           |
| monitoring_agent_tag:                            | string | ---                                   | v0.38.1                                                                                                                                                         |
| monitoring_agent_config_remoteserver_prometheus: | string | ---                                   | http://127.0.0.1:3100/loki/api/v1/push                                                                                                                          |
| monitoring_agent_config_remoteserver_loki:       | string | ---                                   | http://127.0.0.1:9100/api/v1/push                                                                                                                               |
| monitoring_agent_config_path:                    | string | ---                                   | /etc/grafana-agent-flow.river                                                                                                                                   |
| monitoring_agent_service_name:                   | string | ---                                   | grafana-agent-flow.service                                                                                                                                      |
| monitoring_agent_service_state:                  | string | reloaded, restarted, started, stopped | started                                                                                                                                                         |
| monitoring_agent_service_enabled:                | bool   | false, true                           | true                                                                                                                                                            |
| monitoring_agent_service_path:                   | string | ---                                   | `/usr/lib/systemd/system/{{ monitoring_agent_service_name }}`                                                                                                   |

______________________________________________________________________

## Example Playbook

```yaml
- name: Import monitoring Role
  hosts: all
  roles:
    - role: giftpilz0.general.monitoring
```
