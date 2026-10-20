---
title: Acme Dns Role
---

Deploy the acme-dns ACME challenge server as a Podman quadlet.

______________________________________________________________________

## Variables

| Variable                        | Type           | Options     | Default                                                | Description                                                                         |
| ------------------------------- | -------------- | ----------- | ------------------------------------------------------ | ----------------------------------------------------------------------------------- |
| `podman_user`                   | string         | ---         | `{{ ansible_user }}`                                   | System user for rootless podman operations                                          |
| `acme_dns_image`                | string         | ---         | docker.io/joohoi/acme-dns                              | Image name without tag                                                              |
| `acme_dns_version`              | string         | ---         | v2.0.2                                                 | Acme-dns container image version                                                    |
| `acme_dns_autoupdate`           | bool           | true, false | true                                                   | Enable Podman auto-update for this container                                        |
| `acme_dns_network_enabled`      | bool           | true, false | true                                                   | Create and manage the Podman network                                                |
| `acme_dns_network_name`         | string         | ---         | acme_dns-internal                                      | Podman network name                                                                 |
| `acme_dns_network_driver`       | string         | ---         | bridge                                                 | Podman network driver                                                               |
| `acme_dns_network_internal`     | bool           | true, false | false                                                  | Create an internal-only Podman network                                              |
| `acme_dns_port_map_enabled`     | bool           | true, false | true                                                   | Expose DNS ports on the host                                                        |
| `acme_dns_bind_ip`              | string         | ---         | `{{ ansible_facts['default_ipv4']['address'] }}`       | Host IP to bind the public DNS ports to                                             |
| `acme_dns_port_map`             | list of string | ---         | ["53:53","53:53/udp"]                                  | Host:container port mappings                                                        |
| `acme_dns_domain`               | string         | ---         | auth.example.org                                       | Delegated zone served by acme-dns                                                   |
| `acme_dns_nsname`               | string         | ---         | ns1.example.org                                        | Authoritative nameserver name advertised for the delegated zone                     |
| `acme_dns_nsadmin`              | string         | ---         | admin.example.org                                      | Administrative email with the @ represented as a dot                                |
| `acme_dns_records`              | list of string | ---         | `["{{ acme_dns_domain }}. NS {{ acme_dns_nsname }}."]` | Additional records served by acme-dns                                               |
| `acme_dns_disable_registration` | bool           | true, false | false                                                  | Disable the registration endpoint                                                   |
| `acme_dns_api_port`             | string         | ---         | 80                                                     | REST API listen port                                                                |
| `acme_dns_loglevel`             | string         | ---         | info                                                   | Logging level                                                                       |
| `acme_dns_logformat`            | string         | ---         | json                                                   | Logging format                                                                      |
| `acme_dns_environment_vars`     | dict           | ---         | `{}`                                                   | Extra environment variables injected into the container                             |
| `acme_dns_entrypoint`           | string         | ---         | ""                                                     | Optional container entrypoint override                                              |
| `acme_dns_extra_files`          | list of dict   | ---         | []                                                     | Arbitrary file entries with src or source, dest, optional mount, mode, and template |
| `acme_dns_extra_dirs`           | list of dict   | ---         | []                                                     | Arbitrary directory entries with src or source, dest, optional mount and mode       |
