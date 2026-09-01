---
title: Firewalld Role
---

Install, configure, and manage firewalld zones and rules.

______________________________________________________________________

## Variables

| Variable                               | Type           | Options                               | Default           | Description                                      |
| -------------------------------------- | -------------- | ------------------------------------- | ----------------- | ------------------------------------------------ |
| `firewalld_service_name`               | string         | ---                                   | firewalld.service | systemd service unit name                        |
| `firewalld_service_state`              | string         | reloaded, restarted, started, stopped | started           | desired state of the firewalld service           |
| `firewalld_service_enabled`            | bool           | true, false                           | true              | whether the firewalld service is enabled at boot |
| `firewalld_package_state`              | string         | present, absent, latest               | present           | desired state of firewalld packages              |
| `firewalld_package`                    | list of string | ---                                   | ["firewalld"]     | list of packages to install                      |
| `firewalld_logging`                    | string         | ---                                   | all               | LogDenied setting in firewalld.conf              |
| `firewalld_permanent`                  | bool           | true, false                           | true              | whether rules are applied permanently            |
| `firewalld_immediate`                  | bool           | true, false                           | true              | whether rules are applied immediately            |
| `firewalld_default_zone`               | string         | ---                                   | block             | default firewall zone                            |
| `firewalld_zones_define`               | list of dict   | ---                                   |                   | list of zones to create and configure            |
| `firewalld_zones_define.zone`          | string         | ---                                   |                   | zone name                                        |
| `firewalld_zones_define.source`        | string         | ---                                   |                   | zone source (e.g. CIDR)                          |
| `firewalld_zones_define.target`        | string         | ---                                   |                   | zone target                                      |
|                                        |                |                                       |                   |                                                  |
| `firewalld_rules_icmp`                 | list of dict   | ---                                   |                   | list of ICMP block rules                         |
| `firewalld_rules_icmp.icmp_type`       | string         | ---                                   |                   | ICMP type to block                               |
| `firewalld_rules_icmp.zone`            | string         | ---                                   |                   | target zone                                      |
| `firewalld_rules_icmp.state`           | string         | enabled, disabled                     |                   | whether the rule is enabled or disabled          |
|                                        |                |                                       |                   |                                                  |
| `firewalld_rules_services`             | list of dict   | ---                                   |                   | list of service rules                            |
| `firewalld_rules_services.service`     | string         | ---                                   |                   | service name                                     |
| `firewalld_rules_services.zone`        | string         | ---                                   |                   | target zone                                      |
| `firewalld_rules_services.state`       | string         | enabled, disabled                     |                   | whether the rule is enabled or disabled          |
|                                        |                |                                       |                   |                                                  |
| `firewalld_rules_ports`                | list of dict   | ---                                   |                   | list of port rules                               |
| `firewalld_rules_ports.port`           | string         | ---                                   |                   | port number                                      |
| `firewalld_rules_ports.protocol`       | string         | tcp, udp                              |                   | protocol                                         |
| `firewalld_rules_ports.zone`           | string         | ---                                   |                   | target zone                                      |
| `firewalld_rules_ports.state`          | string         | enabled, disabled                     |                   | whether the rule is enabled or disabled          |
|                                        |                |                                       |                   |                                                  |
| `firewalld_richrules_ports`            | list of dict   | ---                                   |                   | list of rich rules for port access               |
| `firewalld_richrules_ports.allowip`    | string         | ---                                   |                   | source IP to allow                               |
| `firewalld_richrules_ports.port`       | string         | ---                                   |                   | port number                                      |
| `firewalld_richrules_ports.protocol`   | string         | tcp, udp                              |                   | protocol                                         |
| `firewalld_richrules_ports.action`     | string         | ---                                   |                   | rich rule action (e.g. accept)                   |
| `firewalld_richrules_ports.zone`       | string         | ---                                   |                   | target zone                                      |
|                                        |                |                                       |                   |                                                  |
| `firewalld_richrules_services`         | list of dict   | ---                                   |                   | list of rich rules for service access            |
| `firewalld_richrules_services.allowip` | string         | ---                                   |                   | source IP to allow                               |
| `firewalld_richrules_services.service` | string         | ---                                   |                   | service name                                     |
| `firewalld_richrules_services.action`  | string         | ---                                   |                   | rich rule action (e.g. accept)                   |
| `firewalld_richrules_services.zone`    | string         | ---                                   |                   | target zone                                      |
|                                        |                |                                       |                   |                                                  |
