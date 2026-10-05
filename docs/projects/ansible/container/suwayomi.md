---
title: Suwayomi Role
---

Deploy Suwayomi Server and its FlareSolverr companion as a Podman Quadlet pod.

______________________________________________________________________

## Variables

| Variable                                 | Type           | Options     | Default              | Description                                                                                 |
| ---------------------------------------- | -------------- | ----------- | -------------------- | ------------------------------------------------------------------------------------------- |
| `podman_user`                            | string         | ---         | `{{ ansible_user }}` | System user for rootless Podman operations                                                  |
| `suwayomi_network_enabled`               | bool           | true, false | true                 | Create and manage the Podman network                                                        |
| `suwayomi_network_name`                  | string         | ---         | suwayomi-internal    | Podman network name                                                                         |
| `suwayomi_network_driver`                | string         | ---         | bridge               | Podman network driver                                                                       |
| `suwayomi_bind_ip`                       | string         | ---         | 127.0.0.1            | Host IP for optional direct port publishing                                                 |
| `suwayomi_port_map_enabled`              | bool           | true, false | false                | Publish Suwayomi ports directly on the host                                                 |
| `suwayomi_port_map`                      | list of string | ---         | ["4567:4567"]        | Host-to-container port mappings                                                             |
| `suwayomi_version`                       | string         | ---         | v2.4.2366            | Suwayomi Server image tag                                                                   |
| `suwayomi_autoupdate`                    | bool           | true, false | true                 | Enable Podman registry auto-update for Suwayomi                                             |
| `suwayomi_flaresolverr_version`          | string         | ---         | 3.0.4                | Byparr image tag used for the FlareSolverr-compatible companion                             |
| `suwayomi_flaresolverr_autoupdate`       | bool           | true, false | true                 | Enable Podman registry auto-update for FlareSolverr                                         |
| `suwayomi_environment_vars`              | dict           | ---         | `{}`                 | Environment variables passed to Suwayomi. Set WebUI update interval to 0 for manual updates |
| `suwayomi_flaresolverr_environment_vars` | dict           | ---         | `{}`                 | Environment variables passed to FlareSolverr                                                |
| `suwayomi_extra_files`                   | list of dict   | ---         | []                   | Arbitrary file entries with src or source, dest, optional mount, mode, and template         |
| `suwayomi_extra_dirs`                    | list of dict   | ---         | []                   | Arbitrary directory entries with src or source, dest, optional mount and mode               |
| `suwayomi_entrypoint`                    | string         | ---         | ""                   | Optional Suwayomi container entrypoint override                                             |
| `suwayomi_flaresolverr_entrypoint`       | string         | ---         | ""                   | Optional FlareSolverr container entrypoint override                                         |
| `suwayomi_proxy_enabled`                 | bool           | true, false | false                | Enable HTTP proxy for image pulls and container traffic                                     |
| `suwayomi_proxy_http`                    | string         | ---         | ""                   | HTTP proxy URL                                                                              |
| `suwayomi_proxy_https`                   | string         | ---         | ""                   | HTTPS proxy URL                                                                             |
| `suwayomi_proxy_no_proxy`                | string         | ---         | ""                   | Comma-separated list of proxy exclusions                                                    |
| `suwayomi_proxy_env`                     | list of string | ---         | []                   | Generated proxy environment entries                                                         |
