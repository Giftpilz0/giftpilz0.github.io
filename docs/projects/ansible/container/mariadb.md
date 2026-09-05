---
title: Mariadb Role
---

Deploy MariaDB as a Podman quadlet.

______________________________________________________________________

## Variables

| Variable                        | Type           | Options     | Default              | Description                                                                                                                             |
| ------------------------------- | -------------- | ----------- | -------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `podman_user`                   | string         | ---         | `{{ ansible_user }}` | system user for rootless podman operations                                                                                              |
| `mariadb_proxy_enabled`         | bool           | true, false | false                | enable HTTP proxy for image pulls                                                                                                       |
| `mariadb_proxy_http`            | string         | ---         | ""                   | HTTP proxy URL                                                                                                                          |
| `mariadb_proxy_https`           | string         | ---         | ""                   | HTTPS proxy URL                                                                                                                         |
| `mariadb_proxy_no_proxy`        | string         | ---         | ""                   | comma-separated list of proxy exclusions                                                                                                |
| `mariadb_proxy_env`             | list of string | ---         | []                   | generated proxy environment entries                                                                                                     |
| `mariadb_network_enabled`       | bool           | true, false | true                 | create and manage the podman network                                                                                                    |
| `mariadb_network_driver`        | string         | ---         | bridge               | podman network driver                                                                                                                   |
| `mariadb_network_name`          | string         | ---         | mariadb-internal     | podman network name                                                                                                                     |
| `mariadb_bind_ip`               | string         | ---         | 127.0.0.1            | host IP to bind exposed ports to                                                                                                        |
| `mariadb_port_map_enabled`      | bool           | true, false | true                 | expose container ports on the host                                                                                                      |
| `mariadb_port_map`              | list of string | ---         | ["3306:3306"]        | host:container port mappings                                                                                                            |
| `mariadb_version`               | string         | ---         | 12.3                 | container image version                                                                                                                 |
| `mariadb_autoupdate`            | bool           | true, false | true                 | enable podman auto-update for this container                                                                                            |
| `mariadb_backup_autoupdate`     | bool           | true, false | true                 | enable podman auto-update for the backup container                                                                                      |
| `mariadb_admin_database`        | string         | ---         | mariadb              | administrator database created by the MariaDB image                                                                                     |
| `mariadb_admin_user`            | string         | ---         | mariadb              | administrator user created by the MariaDB image                                                                                         |
| `mariadb_admin_password`        | string         | ---         | ""                   | password for the MariaDB administrator user                                                                                             |
| `mariadb_backup_user`           | string         | ---         | root                 | database user used by the backup and restore container; set this to an existing user's credentials when migrating an initialized volume |
| `mariadb_backup_password`       | string         | ---         | ""                   | password for the backup and restore database user; MARIADB_ROOT_PASSWORD does not change an initialized volume                          |
| `mariadb_databases`             | list of dict   | ---         | []                   | secondary databases and users to provision and include in backups; each entry has name, user, and password                              |
| `mariadb_environment_vars`      | dict           | ---         | `{}`                 | extra environment variables injected into the container                                                                                 |
| `mariadb_backup_schedule_times` | string         | ---         | 03:00                | backup schedule in HH:MM format                                                                                                         |
| `mariadb_backup_retention_days` | integer        | ---         | 7                    | number of days to keep backups                                                                                                          |
| `mariadb_backup_compression`    | integer        | ---         | 6                    | zlib compression level (0-9)                                                                                                            |
| `mariadb_extra_files`           | list of dict   | ---         | []                   | arbitrary file entries with src (controller path) or source (target path), dest, optional mount, mode, and template                     |
| `mariadb_extra_dirs`            | list of dict   | ---         | []                   | arbitrary directory entries with src (controller directory) or source (target path), dest, optional mount and mode                      |
| `mariadb_entrypoint`            | string         | ---         | ""                   | optional MariaDB container entrypoint override                                                                                          |
| `mariadb_backup_entrypoint`     | string         | ---         | ""                   | optional MariaDB backup container entrypoint override                                                                                   |
