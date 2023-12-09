---
layout: default
title: Monitoring Role
parent: General Collection
grand_parent: Ansible
---

# {{ page.title }}

This Ansible role can be used to install grafana agent and node-exporter.

______________________________________________________________________

## Variables

| Variables                                        | Type   | Options                               | Defaults                                                                                                                                                                                         |
| ------------------------------------------------ | ------ | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| monitoring_agent_package_state:                  | string | present, absent, latest               | present                                                                                                                                                                                          |
| monitoring_agent_package:                        | string | ---                                   | https://github.com/grafana/agent/releases/download/{{ monitoring_agent_tag }}/grafana-agent-flow-{{ monitoring_agent_tag }}-1.{{ monitoring_agent_arch }}.rpm                                    |
| monitoring_agent_arch:                           | string | ---                                   | amd64                                                                                                                                                                                            |
| monitoring_agent_tag:                            | string | ---                                   | v0.38.1                                                                                                                                                                                          |
| monitoring_agent_config_remoteserver_prometheus: | string | ---                                   | http://127.0.0.1:3100/loki/api/v1/push                                                                                                                                                           |
| monitoring_agent_config_remoteserver_loki:       | string | ---                                   | http://127.0.0.1:9100/api/v1/push                                                                                                                                                                |
| monitoring_agent_config_path:                    | string | ---                                   | /etc/grafana-agent-flow.river                                                                                                                                                                    |
| monitoring_agent_service_name:                   | string | ---                                   | grafana-agent-flow.service                                                                                                                                                                       |
| monitoring_agent_service_state:                  | string | reloaded, restarted, started, stopped | started                                                                                                                                                                                          |
| monitoring_agent_service_enabled:                | bool   | false, true                           | true                                                                                                                                                                                             |
| monitoring_nodeexporter_bin_state:               | string | present, skip                         | present                                                                                                                                                                                          |
| monitoring_nodeexporter_url:                     | string | ---                                   | https://github.com/prometheus/node_exporter/releases/download/v{{ monitoring_nodeexporter_tag }}/node_exporter-{{ monitoring_nodeexporter_tag }}.linux-{{ monitoring_nodeexporter_arch }}.tar.gz |
| monitoring_nodeexporter_arch:                    | string | ---                                   | amd64                                                                                                                                                                                            |
| monitoring_nodeexporter_tag:                     | string | ---                                   | 1.7.0                                                                                                                                                                                            |
| monitoring_nodeexporter_path:                    | string | ---                                   | /usr/local/bin                                                                                                                                                                                   |
| monitoring_nodeexporter_service_name:            | string | ---                                   | node-exporter.service                                                                                                                                                                            |
| monitoring_nodeexporter_service_path:            | string | ---                                   | /usr/lib/systemd/system/{{ monitoring_nodeexporter_service_name }}                                                                                                                               |
| monitoring_nodeexporter_service_state:           | string | reloaded, restarted, started, stopped | started                                                                                                                                                                                          |
| monitoring_nodeexporter_service_enabled:         | bool   | false, true                           | true                                                                                                                                                                                             |
| monitoring_nodeexporter_service_args:            | string | ---                                   | "--web.listen-address=127.0.0.1:9090"                                                                                                                                                            |

______________________________________________________________________

## Example Playbook

```yaml
- name: Import monitoring Role
  hosts: all
  roles:
    - role: giftpilz0.general.monitoring
```
