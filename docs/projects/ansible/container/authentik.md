---
title: Authentik Role
---

Deploy the Authentik identity provider (server, worker, PostgreSQL, and Redis) as a Podman quadlet.

______________________________________________________________________

## Variables

| Variable                                | Type           | Options     | Default                   | Description                                                                                                         |
| --------------------------------------- | -------------- | ----------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `podman_user`                           | string         | ---         | `{{ ansible_user }}`      | system user for rootless podman operations                                                                          |
| `authentik_proxy_enabled`               | bool           | true, false | false                     | enable HTTP proxy for image pulls                                                                                   |
| `authentik_proxy_http`                  | string         | ---         | ""                        | HTTP proxy URL                                                                                                      |
| `authentik_proxy_https`                 | string         | ---         | ""                        | HTTPS proxy URL                                                                                                     |
| `authentik_proxy_no_proxy`              | string         | ---         | ""                        | comma-separated list of proxy exclusions                                                                            |
| `authentik_proxy_env`                   | list of string | ---         | []                        | generated proxy environment entries                                                                                 |
| `authentik_network_enabled`             | bool           | true, false | true                      | create and manage the podman network                                                                                |
| `authentik_network_driver`              | string         | ---         | bridge                    | podman network driver                                                                                               |
| `authentik_network_name`                | string         | ---         | authentik-internal        | podman network name                                                                                                 |
| `authentik_bind_ip`                     | string         | ---         | 127.0.0.1                 | host IP to bind exposed ports to                                                                                    |
| `authentik_port_map_enabled`            | bool           | true, false | true                      | expose container ports on the host                                                                                  |
| `authentik_port_map`                    | list of string | ---         | ["9000:9000","9443:9443"] | host:container port mappings                                                                                        |
| `valkey_version`                        | string         | ---         | 9.1.1-alpine              | Valkey (Redis) container image version                                                                              |
| `postgresql_version`                    | string         | ---         | 18.6-alpine               | PostgreSQL container image version                                                                                  |
| `authentik_version`                     | string         | ---         | 2026.8.0                  | Authentik container image version                                                                                   |
| `authentik_cache_autoupdate`            | bool           | true, false | true                      | enable auto-update for the Valkey container                                                                         |
| `authentik_postgresql_autoupdate`       | bool           | true, false | true                      | enable auto-update for the PostgreSQL container                                                                     |
| `authentik_server_autoupdate`           | bool           | true, false | true                      | enable auto-update for the Authentik server container                                                               |
| `authentik_worker_autoupdate`           | bool           | true, false | true                      | enable auto-update for the Authentik worker container                                                               |
| `authentik_secret_key`                  | string         | ---         | ""                        | application secret key (openssl rand -base64 60)                                                                    |
| `authentik_db_password`                 | string         | ---         | ""                        | PostgreSQL password for the Authentik database                                                                      |
| `authentik_domain`                      | string         | ---         | ""                        | external domain for the Authentik instance                                                                          |
| `authentik_base_environment_vars`       | dict           | ---         | `{}`                      | base environment variables shared by Authentik containers                                                           |
| `authentik_server_environment_vars`     | dict           | ---         | `{}`                      | extra environment variables for the server container                                                                |
| `authentik_worker_environment_vars`     | dict           | ---         | `{}`                      | extra environment variables for the worker container                                                                |
| `authentik_postgresql_environment_vars` | dict           | ---         | `{}`                      | extra environment variables for the PostgreSQL container                                                            |
| `authentik_cache_environment_vars`      | dict           | ---         | `{}`                      | extra environment variables for the Valkey container                                                                |
| `authentik_extra_files`                 | list of dict   | ---         | []                        | arbitrary file entries with src (controller path) or source (target path), dest, optional mount, mode, and template |
| `authentik_extra_dirs`                  | list of dict   | ---         | []                        | arbitrary directory entries with src (controller directory) or source (target path), dest, optional mount and mode  |
| `authentik_entrypoint`                  | string         | ---         | ""                        | optional Authentik server container entrypoint override                                                             |
| `authentik_worker_entrypoint`           | string         | ---         | ""                        | optional Authentik worker container entrypoint override                                                             |
| `authentik_cache_entrypoint`            | string         | ---         | ""                        | optional Authentik cache container entrypoint override                                                              |
| `authentik_postgresql_entrypoint`       | string         | ---         | ""                        | optional Authentik PostgreSQL container entrypoint override                                                         |
