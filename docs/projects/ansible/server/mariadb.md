---
title: Mariadb Role
---

This Ansible role can be used to configure mariadb.

______________________________________________________________________

## Variables

| Variables                   | Type   | Options                                        | Defaults                                     |
| --------------------------- | ------ | ---------------------------------------------- | -------------------------------------------- |
| mariadb_service_name:       | string | ---                                            | mariadb-server.service                       |
| mariadb_service_state:      | string | reloaded, restarted, started, stopped          | started                                      |
| mariadb_service_enabled:    | bool   | false, true                                    | true                                         |
| mariadb_package_state:      | string | present, absent, latest                        | present                                      |
| mariadb_package:            | list   | ---                                            | mariadb, mariadb-server, python3-mysqlclient |
|                             |        |                                                |                                              |
| mariadb_database:           | string | ---                                            | default                                      |
| mariadb_database_encoding:  | string | ---                                            | utf8                                         |
| mariadb_database_collation: | string | ---                                            | " "                                          |
| mariadb_database_state:     | string | present, absent, skip                          | present                                      |
|                             |        |                                                |                                              |
| mariadb_user                | string | ---                                            | `{{ ansible_user }}`                         |
| mariadb_user_password       | string | ---                                            | changeme                                     |
| mariadb_user_database       | string | ---                                            | `{{ mariadb_database }}`                     |
| mariadb_user_privileges     | string | ---                                            | ALL                                          |
| mariadb_user_state          | string | present, absent, skip                          | present                                      |
|                             |        |                                                |                                              |
| mariadb_firewalld_zone:     | string | block, dmz, drop, internal, public, trusted... | ---                                          |
| mariadb_firewalld_service:  | string | ---                                            | mysql                                        |
| mariadb_firewalld_state:    | string | present, absent, enabled, disabled, skip       | enabled                                      |

______________________________________________________________________

## Example Playbook

```yaml
- name: Import mariadb Role
  hosts: all
  roles:
    - role: giftpilz0.server.mariadb
```
