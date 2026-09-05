---
title: Homeassistant Role
---

Deploy Home Assistant as a Podman quadlet.

______________________________________________________________________

## Variables

| Variable                         | Type           | Options     | Default                  | Description                                                                                                         |
| -------------------------------- | -------------- | ----------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| `podman_user`                    | string         | ---         | `{{ ansible_user }}`     | system user for rootless podman operations                                                                          |
| `homeassistant_proxy_enabled`    | bool           | true, false | false                    | enable HTTP proxy for image pulls                                                                                   |
| `homeassistant_proxy_http`       | string         | ---         | ""                       | HTTP proxy URL                                                                                                      |
| `homeassistant_proxy_https`      | string         | ---         | ""                       | HTTPS proxy URL                                                                                                     |
| `homeassistant_proxy_no_proxy`   | string         | ---         | ""                       | comma-separated list of proxy exclusions                                                                            |
| `homeassistant_proxy_env`        | list of string | ---         | []                       | generated proxy environment entries                                                                                 |
| `homeassistant_network_enabled`  | bool           | true, false | true                     | create and manage the podman network                                                                                |
| `homeassistant_network_driver`   | string         | ---         | bridge                   | podman network driver                                                                                               |
| `homeassistant_network_name`     | string         | ---         | homeassistant-internal   | podman network name                                                                                                 |
| `homeassistant_bind_ip`          | string         | ---         | 127.0.0.1                | host IP to bind exposed ports to                                                                                    |
| `homeassistant_port_map_enabled` | bool           | true, false | true                     | expose container ports on the host                                                                                  |
| `homeassistant_port_map`         | list of string | ---         | ["8123:8123"]            | host:container port mappings                                                                                        |
| `homeassistant_version`          | string         | ---         | 2026.8.3                 | container image version                                                                                             |
| `homeassistant_autoupdate`       | bool           | true, false | true                     | enable podman auto-update for this container                                                                        |
| `homeassistant_environment_vars` | dict           | ---         | `{"TZ":"Europe/Berlin"}` | extra environment variables injected into the container                                                             |
| `homeassistant_extra_files`      | list of dict   | ---         | []                       | arbitrary file entries with src (controller path) or source (target path), dest, optional mount, mode, and template |
| `homeassistant_extra_dirs`       | list of dict   | ---         | []                       | arbitrary directory entries with src (controller directory) or source (target path), dest, optional mount and mode  |
| `homeassistant_entrypoint`       | string         | ---         | ""                       | optional container entrypoint override                                                                              |
