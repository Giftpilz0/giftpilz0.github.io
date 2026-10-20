---
title: Misc Role
---

Deploy the Misc web application (built from a git commit) as a Podman quadlet.

______________________________________________________________________

## Variables

| Variable                | Type           | Options     | Default                                                | Description                                                                                                         |
| ----------------------- | -------------- | ----------- | ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| `podman_user`           | string         | ---         | `{{ ansible_user }}`                                   | System user for rootless podman operations                                                                          |
| `misc_image`            | string         | ---         | localhost/misc-custom                                  | Image name without tag                                                                                              |
| `misc_version`          | string         | ---         | latest                                                 | Container image version                                                                                             |
| `misc_git_repo`         | string         | ---         | https://forgejo.nixpi.de/moritz/service-misc.git       | Git repository the misc image is built from                                                                         |
| `misc_commit`           | string         | ---         | db16ab7ca40f6e1e98e6e7a3947fb9e2aa04f527               | Git commit to build from                                                                                            |
| `misc_dockerfile`       | string         | ---         | docker/docker-minimal/Dockerfile                       | Dockerfile path inside the misc repository                                                                          |
| `misc_autoupdate`       | bool           | true, false | true                                                   | Enable podman auto-update for this container                                                                        |
| `misc_network_enabled`  | bool           | true, false | true                                                   | Create and manage the podman network                                                                                |
| `misc_network_name`     | string         | ---         | misc-internal                                          | Podman network name                                                                                                 |
| `misc_network_driver`   | string         | ---         | bridge                                                 | Podman network driver                                                                                               |
| `misc_port_map_enabled` | bool           | true, false | true                                                   | Expose container ports on the host                                                                                  |
| `misc_bind_ip`          | string         | ---         | `{{ ansible_facts['default_ipv4']['address'] }}`       | Host IP to bind exposed ports to                                                                                    |
| `misc_port_map`         | list of string | ---         | ["8080:8080"]                                          | Host:container port mappings                                                                                        |
| `misc_environment_vars` | dict           | ---         | `{"TZ":"Europe/Berlin","LOGLEVEL":"INFO","PORT":8080}` | Extra environment variables injected into the container                                                             |
| `misc_entrypoint`       | string         | ---         | ""                                                     | Optional container entrypoint override                                                                              |
| `misc_extra_files`      | list of dict   | ---         | []                                                     | Arbitrary file entries with src (controller path) or source (target path), dest, optional mount, mode, and template |
| `misc_extra_dirs`       | list of dict   | ---         | []                                                     | Arbitrary directory entries with src (controller directory) or source (target path), dest, optional mount and mode  |
