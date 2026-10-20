---
title: Vaultwarden Role
---

Deploy Vaultwarden (Bitwarden-compatible password manager) as a Podman quadlet.

______________________________________________________________________

## Variables

| Variable                       | Type           | Options     | Default                                                                                                  | Description                                                                                                         |
| ------------------------------ | -------------- | ----------- | -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `podman_user`                  | string         | ---         | `{{ ansible_user }}`                                                                                     | System user for rootless podman operations                                                                          |
| `vaultwarden_image`            | string         | ---         | docker.io/vaultwarden/server                                                                             | Image name without tag                                                                                              |
| `vaultwarden_version`          | string         | ---         | 1.37.4-alpine                                                                                            | Container image version                                                                                             |
| `vaultwarden_autoupdate`       | bool           | true, false | true                                                                                                     | Enable podman auto-update for this container                                                                        |
| `vaultwarden_network_enabled`  | bool           | true, false | true                                                                                                     | Create and manage the podman network                                                                                |
| `vaultwarden_network_name`     | string         | ---         | vaultwarden-internal                                                                                     | Podman network name                                                                                                 |
| `vaultwarden_network_driver`   | string         | ---         | bridge                                                                                                   | Podman network driver                                                                                               |
| `vaultwarden_port_map_enabled` | bool           | true, false | true                                                                                                     | Expose container ports on the host                                                                                  |
| `vaultwarden_bind_ip`          | string         | ---         | 127.0.0.1                                                                                                | Host IP to bind exposed ports to                                                                                    |
| `vaultwarden_port_map`         | list of string | ---         | ["80:80"]                                                                                                | Host:container port mappings                                                                                        |
| `vaultwarden_domain`           | string         | ---         | ""                                                                                                       | External URL for the Vaultwarden instance                                                                           |
| `vaultwarden_admin_token`      | string         | ---         | ""                                                                                                       | Admin token for the Vaultwarden admin panel                                                                         |
| `vaultwarden_environment_vars` | dict           | ---         | `{"DOMAIN":"{{ vaultwarden_domain }}","ADMIN_TOKEN":"{{ vaultwarden_admin_token }}","ROCKET_PORT":"80"}` | Extra environment variables injected into the container                                                             |
| `vaultwarden_entrypoint`       | string         | ---         | ""                                                                                                       | Optional container entrypoint override                                                                              |
| `vaultwarden_extra_files`      | list of dict   | ---         | []                                                                                                       | Arbitrary file entries with src (controller path) or source (target path), dest, optional mount, mode, and template |
| `vaultwarden_extra_dirs`       | list of dict   | ---         | []                                                                                                       | Arbitrary directory entries with src (controller directory) or source (target path), dest, optional mount and mode  |
