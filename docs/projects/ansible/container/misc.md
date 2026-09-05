---
title: Misc Role
---

Deploy the Misc web application (built from a git commit) as a Podman quadlet.

______________________________________________________________________

## Variables

| Variable                | Type           | Options     | Default                                                | Description                                                                                                         |
| ----------------------- | -------------- | ----------- | ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| `podman_user`           | string         | ---         | `{{ ansible_user }}`                                   | system user for rootless podman operations                                                                          |
| `misc_proxy_enabled`    | bool           | true, false | false                                                  | enable HTTP proxy for image pulls                                                                                   |
| `misc_proxy_http`       | string         | ---         | ""                                                     | HTTP proxy URL                                                                                                      |
| `misc_proxy_https`      | string         | ---         | ""                                                     | HTTPS proxy URL                                                                                                     |
| `misc_proxy_no_proxy`   | string         | ---         | ""                                                     | comma-separated list of proxy exclusions                                                                            |
| `misc_proxy_env`        | list of string | ---         | []                                                     | generated proxy environment entries                                                                                 |
| `misc_network_enabled`  | bool           | true, false | true                                                   | create and manage the podman network                                                                                |
| `misc_network_driver`   | string         | ---         | bridge                                                 | podman network driver                                                                                               |
| `misc_network_name`     | string         | ---         | misc-internal                                          | podman network name                                                                                                 |
| `misc_bind_ip`          | string         | ---         | `{{ ansible_facts['default_ipv4']['address'] }}`       | host IP to bind exposed ports to                                                                                    |
| `misc_port_map_enabled` | bool           | true, false | true                                                   | expose container ports on the host                                                                                  |
| `misc_port_map`         | list of string | ---         | ["8080:8080"]                                          | host:container port mappings                                                                                        |
| `misc_version`          | string         | ---         | latest                                                 | container image version                                                                                             |
| `misc_commit`           | string         | ---         | db16ab7ca40f6e1e98e6e7a3947fb9e2aa04f527               | git commit to build from                                                                                            |
| `misc_autoupdate`       | bool           | true, false | true                                                   | enable podman auto-update for this container                                                                        |
| `misc_environment_vars` | dict           | ---         | `{"TZ":"Europe/Berlin","LOGLEVEL":"INFO","PORT":8080}` | extra environment variables injected into the container                                                             |
| `misc_extra_files`      | list of dict   | ---         | []                                                     | arbitrary file entries with src (controller path) or source (target path), dest, optional mount, mode, and template |
| `misc_extra_dirs`       | list of dict   | ---         | []                                                     | arbitrary directory entries with src (controller directory) or source (target path), dest, optional mount and mode  |
| `misc_entrypoint`       | string         | ---         | ""                                                     | optional container entrypoint override                                                                              |
