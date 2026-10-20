---
title: Homeassistant Role
---

Deploy Home Assistant as a Podman quadlet.

______________________________________________________________________

## Variables

| Variable                         | Type           | Options     | Default                               | Description                                                                                                         |
| -------------------------------- | -------------- | ----------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `podman_user`                    | string         | ---         | `{{ ansible_user }}`                  | System user for rootless podman operations                                                                          |
| `homeassistant_image`            | string         | ---         | ghcr.io/home-assistant/home-assistant | Image name without tag                                                                                              |
| `homeassistant_version`          | string         | ---         | 2026.10.1                             | Container image version                                                                                             |
| `homeassistant_autoupdate`       | bool           | true, false | true                                  | Enable podman auto-update for this container                                                                        |
| `homeassistant_network_enabled`  | bool           | true, false | true                                  | Create and manage the podman network                                                                                |
| `homeassistant_network_name`     | string         | ---         | homeassistant-internal                | Podman network name                                                                                                 |
| `homeassistant_network_driver`   | string         | ---         | bridge                                | Podman network driver                                                                                               |
| `homeassistant_port_map_enabled` | bool           | true, false | true                                  | Expose container ports on the host                                                                                  |
| `homeassistant_bind_ip`          | string         | ---         | 127.0.0.1                             | Host IP to bind exposed ports to                                                                                    |
| `homeassistant_port_map`         | list of string | ---         | ["8123:8123"]                         | Host:container port mappings                                                                                        |
| `homeassistant_device_access`    | bool           | true, false | false                                 | Grant access to devices mounted via extra files (dialout group, original groups, SELinux spc_t)                     |
| `homeassistant_environment_vars` | dict           | ---         | `{"TZ":"Europe/Berlin"}`              | Extra environment variables injected into the container                                                             |
| `homeassistant_entrypoint`       | string         | ---         | ""                                    | Optional container entrypoint override                                                                              |
| `homeassistant_extra_files`      | list of dict   | ---         | []                                    | Arbitrary file entries with src (controller path) or source (target path), dest, optional mount, mode, and template |
| `homeassistant_extra_dirs`       | list of dict   | ---         | []                                    | Arbitrary directory entries with src (controller directory) or source (target path), dest, optional mount and mode  |
