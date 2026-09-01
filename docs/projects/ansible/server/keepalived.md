---
title: Keepalived Role
---

Install and configure keepalived for a virtual IP (VRRP).

______________________________________________________________________

## Variables

| Variable                              | Type           | Options                               | Default                         | Description                                       |
| ------------------------------------- | -------------- | ------------------------------------- | ------------------------------- | ------------------------------------------------- |
| `keepalived_service_name`             | string         | ---                                   | keepalived.service              | systemd service unit name                         |
| `keepalived_service_state`            | string         | reloaded, restarted, started, stopped | started                         | desired state of the keepalived service           |
| `keepalived_service_enabled`          | bool           | true, false                           | true                            | whether the keepalived service is enabled at boot |
| `keepalived_package_state`            | string         | present, absent, latest               | present                         | desired state of keepalived packages              |
| `keepalived_package`                  | list of string | ---                                   | ["keepalived"]                  | list of packages to install                       |
| `keepalived_config_path`              | string         | ---                                   | /etc/keepalived/keepalived.conf | path to the keepalived configuration file         |
| `keepalived_config_virtual_ip`        | string         | ---                                   |                                 | virtual IP address to manage                      |
| `keepalived_config_interface`         | string         | ---                                   | eth0                            | network interface for VRRP advertisements         |
| `keepalived_config_priority`          | integer        | ---                                   | 255                             | VRRP priority (higher wins election)              |
| `keepalived_config_virtual_router_id` | integer        | ---                                   | 100                             | VRRP virtual router ID                            |
| `keepalived_config_vrrp_instance`     | string         | ---                                   | VG                              | VRRP instance name                                |
| `keepalived_config_state`             | string         | ---                                   | MASTER                          | initial VRRP state (MASTER or BACKUP)             |
