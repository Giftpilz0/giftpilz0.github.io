---
title: Navidrome Role
---

Deploy Navidrome as a Podman Quadlet pod.

______________________________________________________________________

## Variables

| Variable                     | Type           | Options     | Default              | Description                                                                                                         |
| ---------------------------- | -------------- | ----------- | -------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `podman_user`                | string         | ---         | `{{ ansible_user }}` | System user for rootless Podman operations                                                                          |
| `navidrome_network_enabled`  | bool           | true, false | true                 | Create and manage the Podman network                                                                                |
| `navidrome_network_name`     | string         | ---         | navidrome-internal   | Podman network name                                                                                                 |
| `navidrome_network_driver`   | string         | ---         | bridge               | Podman network driver                                                                                               |
| `navidrome_bind_ip`          | string         | ---         | 127.0.0.1            | Host IP for optional direct port publishing                                                                         |
| `navidrome_port_map_enabled` | bool           | true, false | false                | Publish Navidrome ports directly on the host                                                                        |
| `navidrome_port_map`         | list of string | ---         | ["4533:4533"]        | Host-to-container port mappings                                                                                     |
| `navidrome_version`          | string         | ---         | 0.64.0               | Navidrome image tag                                                                                                 |
| `navidrome_autoupdate`       | bool           | true, false | true                 | Enable Podman registry auto-update for Navidrome                                                                    |
| `navidrome_environment_vars` | dict           | ---         | `{}`                 | Environment variables passed to Navidrome                                                                           |
| `navidrome_extra_files`      | list of dict   | ---         | []                   | arbitrary file entries with src (controller path) or source (target path), dest, optional mount, mode, and template |
| `navidrome_extra_dirs`       | list of dict   | ---         | []                   | arbitrary directory entries with src (controller directory) or source (target path), dest, optional mount and mode  |
| `navidrome_entrypoint`       | string         | ---         | ""                   | optional container entrypoint override                                                                              |
| `navidrome_proxy_enabled`    | bool           | true, false | false                | enable HTTP proxy for image pulls                                                                                   |
| `navidrome_proxy_http`       | string         | ---         | ""                   | HTTP proxy URL                                                                                                      |
| `navidrome_proxy_https`      | string         | ---         | ""                   | HTTPS proxy URL                                                                                                     |
| `navidrome_proxy_no_proxy`   | string         | ---         | ""                   | comma-separated list of proxy exclusions                                                                            |
| `navidrome_proxy_env`        | list of string | ---         | []                   | generated proxy environment entries                                                                                 |
