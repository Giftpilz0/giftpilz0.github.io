---
title: Mariadb Role
---

Install and manage the MariaDB server, databases, and users.

______________________________________________________________________

## Variables

| Variable                     | Type           | Options                                  | Default                                            | Description                                    |
| ---------------------------- | -------------- | ---------------------------------------- | -------------------------------------------------- | ---------------------------------------------- |
| `mariadb_service_name`       | string         | ---                                      | mariadb.service                                    | systemd service unit name                      |
| `mariadb_service_state`      | string         | reloaded, restarted, started, stopped    | started                                            | desired state of the mariadb service           |
| `mariadb_service_enabled`    | bool           | true, false                              | true                                               | whether the mariadb service is enabled at boot |
| `mariadb_package_state`      | string         | present, absent, latest                  | present                                            | desired state of mariadb packages              |
| `mariadb_package`            | list of string | ---                                      | ["mariadb","mariadb-server","python3-mysqlclient"] | list of packages to install                    |
| `mariadb_database`           | string         | ---                                      | default                                            | database name to manage                        |
| `mariadb_database_encoding`  | string         | ---                                      | utf8                                               | database character encoding (e.g. utf8mb4)     |
| `mariadb_database_collation` | string         | ---                                      | ""                                                 | database collation (e.g. utf8mb4_unicode_ci)   |
| `mariadb_database_state`     | string         | present, absent, skip                    | present                                            | desired state of the database                  |
| `mariadb_user`               | string         | ---                                      | `{{ ansible_user }}`                               | database username                              |
| `mariadb_user_password`      | string         | ---                                      | changeme                                           | database user password                         |
| `mariadb_user_database`      | string         | ---                                      | `{{ mariadb_database }}`                           | database to grant user access to               |
| `mariadb_user_privileges`    | string         | ---                                      | ALL                                                | SQL privileges string (e.g. ALL ON db.\*)      |
| `mariadb_user_state`         | string         | present, absent, skip                    | present                                            | desired state of the database user             |
| `mariadb_firewalld_zone`     | string         | ---                                      |                                                    | firewall zone for mariadb rules                |
| `mariadb_firewalld_service`  | string         | ---                                      | mysql                                              | firewall service name                          |
| `mariadb_firewalld_state`    | string         | present, absent, enabled, disabled, skip | enabled                                            | desired state of firewall rules                |
