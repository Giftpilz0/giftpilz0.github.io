---
title: Vaultwarden Role
---

Deploy Vaultwarden (Bitwarden-compatible password manager) as a Podman quadlet.

______________________________________________________________________

## Variables

| Variable                       | Type           | Options     | Default              | Description                                                                                                         |
| ------------------------------ | -------------- | ----------- | -------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `podman_user`                  | string         | ---         | `{{ ansible_user }}` | system user for rootless podman operations                                                                          |
| `vaultwarden_proxy_enabled`    | bool           | true, false | false                | enable HTTP proxy for image pulls                                                                                   |
| `vaultwarden_proxy_http`       | string         | ---         | ""                   | HTTP proxy URL                                                                                                      |
| `vaultwarden_proxy_https`      | string         | ---         | ""                   | HTTPS proxy URL                                                                                                     |
| `vaultwarden_proxy_no_proxy`   | string         | ---         | ""                   | comma-separated list of proxy exclusions                                                                            |
| `vaultwarden_proxy_env`        | list of string | ---         | []                   | generated proxy environment entries                                                                                 |
| `vaultwarden_network_enabled`  | bool           | true, false | true                 | create and manage the podman network                                                                                |
| `vaultwarden_network_driver`   | string         | ---         | bridge               | podman network driver                                                                                               |
| `vaultwarden_network_name`     | string         | ---         | vaultwarden-internal | podman network name                                                                                                 |
| `vaultwarden_bind_ip`          | string         | ---         | 127.0.0.1            | host IP to bind exposed ports to                                                                                    |
| `vaultwarden_port_map_enabled` | bool           | true, false | true                 | expose container ports on the host                                                                                  |
| `vaultwarden_port_map`         | list of string | ---         | ["80:80"]            | host:container port mappings                                                                                        |
| `vaultwarden_version`          | string         | ---         | 1.37.2-alpine        | container image version                                                                                             |
| `vaultwarden_autoupdate`       | bool           | true, false | true                 | enable podman auto-update for this container                                                                        |
| `vaultwarden_domain`           | string         | ---         | ""                   | external URL for the Vaultwarden instance                                                                           |
| `vaultwarden_admin_token`      | string         | ---         | ""                   | admin token for the Vaultwarden admin panel                                                                         |
| `vaultwarden_environment_vars` | dict           | ---         | `{}`                 | extra environment variables injected into the container                                                             |
| `vaultwarden_extra_files`      | list of dict   | ---         | []                   | arbitrary file entries with src (controller path) or source (target path), dest, optional mount, mode, and template |
| `vaultwarden_extra_dirs`       | list of dict   | ---         | []                   | arbitrary directory entries with src (controller directory) or source (target path), dest, optional mount and mode  |
| `vaultwarden_entrypoint`       | string         | ---         | ""                   | optional container entrypoint override                                                                              |
