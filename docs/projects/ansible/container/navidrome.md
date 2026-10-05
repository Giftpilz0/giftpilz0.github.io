---
title: Navidrome Role
---

Deploy Navidrome as a Podman Quadlet pod.

______________________________________________________________________

## Variables

| Variable                           | Type           | Options     | Default                                  | Description                                                                                                         |
| ---------------------------------- | -------------- | ----------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `podman_user`                      | string         | ---         | `{{ ansible_user }}`                     | System user for rootless Podman operations                                                                          |
| `navidrome_network_enabled`        | bool           | true, false | true                                     | Create and manage the Podman network                                                                                |
| `navidrome_network_name`           | string         | ---         | navidrome-internal                       | Podman network name                                                                                                 |
| `navidrome_network_driver`         | string         | ---         | bridge                                   | Podman network driver                                                                                               |
| `navidrome_bind_ip`                | string         | ---         | 127.0.0.1                                | Host IP for optional direct port publishing                                                                         |
| `navidrome_port_map_enabled`       | bool           | true, false | false                                    | Publish Navidrome ports directly on the host                                                                        |
| `navidrome_port_map`               | list of string | ---         | ["4533:4533"]                            | Host-to-container port mappings                                                                                     |
| `navidrome_version`                | string         | ---         | 0.64.0                                   | Navidrome image tag                                                                                                 |
| `navidrome_autoupdate`             | bool           | true, false | true                                     | Enable Podman registry auto-update for Navidrome                                                                    |
| `navidrome_environment_vars`       | dict           | ---         | `{}`                                     | Environment variables passed to Navidrome                                                                           |
| `navidrome_webui_enabled`          | bool           | true, false | false                                    | Deploy the music library management WebUI in the Navidrome pod                                                      |
| `navidrome_webui_image_name`       | string         | ---         | localhost/music-library-webui            | Local image name for the music library WebUI                                                                        |
| `navidrome_webui_image_tag`        | string         | ---         | 0.1.0                                    | Local image tag for the music library WebUI                                                                         |
| `navidrome_webui_commit`           | string         | ---         | 657b0256dd2b8f7e048c92b824f92d11e57dce3f | Git commit to clone for the music library WebUI image build                                                         |
| `navidrome_webui_build_file`       | string         | ---         | Containerfile                            | Container build file relative to the WebUI repository root                                                          |
| `navidrome_webui_user`             | string         | ---         | 1001:1001                                | UID and GID used by the WebUI container for shared-volume writes                                                    |
| `navidrome_webui_environment_vars` | dict           | ---         | `{}`                                     | Environment variables passed to the music library WebUI                                                             |
| `navidrome_extra_files`            | list of dict   | ---         | []                                       | arbitrary file entries with src (controller path) or source (target path), dest, optional mount, mode, and template |
| `navidrome_extra_dirs`             | list of dict   | ---         | []                                       | arbitrary directory entries with src (controller directory) or source (target path), dest, optional mount and mode  |
| `navidrome_entrypoint`             | string         | ---         | ""                                       | optional container entrypoint override                                                                              |
| `navidrome_proxy_enabled`          | bool           | true, false | false                                    | enable HTTP proxy for image pulls                                                                                   |
| `navidrome_proxy_http`             | string         | ---         | ""                                       | HTTP proxy URL                                                                                                      |
| `navidrome_proxy_https`            | string         | ---         | ""                                       | HTTPS proxy URL                                                                                                     |
| `navidrome_proxy_no_proxy`         | string         | ---         | ""                                       | comma-separated list of proxy exclusions                                                                            |
| `navidrome_proxy_env`              | list of string | ---         | []                                       | generated proxy environment entries                                                                                 |
