---
title: HAProxy Role
---

This Ansible role can be used to set up HAProxy.

______________________________________________________________________

## Variables

| Variables                              | Type   | Options                 | Defaults                  |
| -------------------------------------- | ------ | ----------------------- | ------------------------- |
| haproxy_service_name:                  | string | ---                     | haproxy.service           |
| haproxy_service_state:                 | string | started, stopped        | started                   |
| haproxy_service_enabled:               | bool   | false, true             | true                      |
| haproxy_package_state:                 | string | present, absent, latest | present                   |
| haproxy_package:                       | list   | ---                     | haproxy                   |
| haproxy_config_path:                   | string | ---                     | /etc/haproxy/haproxy.cfg  |
| haproxy_config_ssl:                    | bool   | false, true             | true                      |
| haproxy_config_force_https:            | bool   | false, true             | true                      |
| haproxy_config_maxconn:                | int    | ---                     | 2000                      |
| haproxy_selinux_permissive:            | bool   | false, true             | true                      |
|                                        |        |                         |                           |
| haproxy_config_http_apps:              | dict   | ---                     | ---                       |
| haproxy_config_http_apps.name:         | string | ---                     | example-app1              |
| haproxy_config_http_apps.domain:       | string | ---                     | example.com               |
| haproxy_config_http_apps.force_https:  | bool   | false, true             | true                      |
| haproxy_config_http_apps.certificate:  | string | ---                     | /etc/ssl/example-app1.pem |
| haproxy_config_http_apps.servers:      | dict   | ---                     | ---                       |
| haproxy_config_http_apps.servers.name: | string | ---                     | example_server1           |
| haproxy_config_http_apps.servers.host: | string | ---                     | 192.168.1.101             |
| haproxy_config_http_apps.servers.port: | int    | ---                     | 8080                      |
|                                        |        |                         |                           |
| haproxy_config_tcp_apps:               | dict   | ---                     | ---                       |
| haproxy_config_tcp_apps.name:          | string | ---                     | example-tcp-app1          |
| haproxy_config_tcp_apps.port:          | int    | ---                     | 3306                      |
| haproxy_config_tcp_apps.servers:       | dict   | ---                     | ---                       |
| haproxy_config_tcp_apps.servers.name:  | string | ---                     | example_server1           |
| haproxy_config_tcp_apps.servers.host:  | string | ---                     | 192.168.1.101             |
| haproxy_config_tcp_apps.servers.port:  | int    | ---                     | 3306                      |

______________________________________________________________________

## Example Playbook

```yaml
- name: Import haproxy Role
  hosts: all
  roles:
    - role: giftpilz0.server.haproxy
```
