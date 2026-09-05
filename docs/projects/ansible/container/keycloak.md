---
title: Keycloak Role
---

Deploy Keycloak identity and access management as a Podman quadlet.

______________________________________________________________________

## Variables

| Variable                    | Type           | Options     | Default              | Description                                                                                                         |
| --------------------------- | -------------- | ----------- | -------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `podman_user`               | string         | ---         | `{{ ansible_user }}` | system user for rootless podman operations                                                                          |
| `keycloak_proxy_enabled`    | bool           | true, false | false                | enable HTTP proxy for image pulls                                                                                   |
| `keycloak_proxy_http`       | string         | ---         | ""                   | HTTP proxy URL                                                                                                      |
| `keycloak_proxy_https`      | string         | ---         | ""                   | HTTPS proxy URL                                                                                                     |
| `keycloak_proxy_no_proxy`   | string         | ---         | ""                   | comma-separated list of proxy exclusions                                                                            |
| `keycloak_proxy_env`        | list of string | ---         | []                   | generated proxy environment entries                                                                                 |
| `keycloak_network_enabled`  | bool           | true, false | true                 | create and manage the podman network                                                                                |
| `keycloak_network_driver`   | string         | ---         | bridge               | podman network driver                                                                                               |
| `keycloak_network_name`     | string         | ---         | keycloak-internal    | podman network name                                                                                                 |
| `keycloak_bind_ip`          | string         | ---         | 127.0.0.1            | host IP to bind exposed ports to                                                                                    |
| `keycloak_port_map_enabled` | bool           | true, false | true                 | expose container ports on the host                                                                                  |
| `keycloak_port_map`         | list of string | ---         | ["8080:8080"]        | host:container port mappings                                                                                        |
| `keycloak_version`          | string         | ---         | 26.7.2               | container image version                                                                                             |
| `keycloak_autoupdate`       | bool           | true, false | true                 | enable podman auto-update for this container                                                                        |
| `keycloak_domain`           | string         | ---         | login.nixpi.de       | external domain for the Keycloak instance                                                                           |
| `keycloak_db_name`          | string         | ---         | keycloak             | database name                                                                                                       |
| `keycloak_db_host`          | string         | ---         | postgresql-pod       | PostgreSQL container hostname                                                                                       |
| `keycloak_db_user`          | string         | ---         | keycloak             | database user                                                                                                       |
| `keycloak_db_password`      | string         | ---         | ""                   | database user password                                                                                              |
| `keycloak_admin_password`   | string         | ---         | ""                   | admin bootstrap password                                                                                            |
| `keycloak_environment_vars` | dict           | ---         | `{}`                 | extra environment variables injected into the container                                                             |
| `keycloak_extra_files`      | list of dict   | ---         | []                   | arbitrary file entries with src (controller path) or source (target path), dest, optional mount, mode, and template |
| `keycloak_extra_dirs`       | list of dict   | ---         | []                   | arbitrary directory entries with src (controller directory) or source (target path), dest, optional mount and mode  |
| `keycloak_entrypoint`       | string         | ---         | ""                   | optional container entrypoint override                                                                              |
