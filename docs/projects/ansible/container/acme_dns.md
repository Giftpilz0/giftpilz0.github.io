---
title: Acme Dns Role
---

Deploy the acme-dns ACME challenge server as a Podman quadlet.

______________________________________________________________________

## Variables

| Variable                        | Type           | Options     | Default                                          | Description                                                                         |
| ------------------------------- | -------------- | ----------- | ------------------------------------------------ | ----------------------------------------------------------------------------------- |
| `podman_user`                   | string         | ---         | `{{ ansible_user }}`                             | system user for rootless podman operations                                          |
| `acme_dns_proxy_enabled`        | bool           | true, false | false                                            | enable HTTP proxy for image pulls                                                   |
| `acme_dns_proxy_http`           | string         | ---         | ""                                               | HTTP proxy URL                                                                      |
| `acme_dns_proxy_https`          | string         | ---         | ""                                               | HTTPS proxy URL                                                                     |
| `acme_dns_proxy_no_proxy`       | string         | ---         | ""                                               | comma-separated list of proxy exclusions                                            |
| `acme_dns_proxy_env`            | list of string | ---         | []                                               | generated proxy environment entries                                                 |
| `acme_dns_network_enabled`      | bool           | true, false | true                                             | create and manage the Podman network                                                |
| `acme_dns_network_driver`       | string         | ---         | bridge                                           | Podman network driver                                                               |
| `acme_dns_network_internal`     | bool           | true, false | false                                            | create an internal-only Podman network                                              |
| `acme_dns_network_name`         | string         | ---         | acme_dns-internal                                | Podman network name                                                                 |
| `acme_dns_bind_ip`              | string         | ---         | `{{ ansible_facts['default_ipv4']['address'] }}` | host IP to bind the public DNS ports to                                             |
| `acme_dns_port_map_enabled`     | bool           | true, false | true                                             | expose DNS ports on the host                                                        |
| `acme_dns_port_map`             | list of string | ---         | ["53:53","53:53/udp"]                            | host:container port mappings                                                        |
| `acme_dns_version`              | string         | ---         | v2.0.2                                           | acme-dns container image version                                                    |
| `acme_dns_autoupdate`           | bool           | true, false | true                                             | enable Podman auto-update for this container                                        |
| `acme_dns_domain`               | string         | ---         | auth.example.org                                 | delegated zone served by acme-dns                                                   |
| `acme_dns_nsname`               | string         | ---         | ns1.example.org                                  | authoritative nameserver name advertised for the delegated zone                     |
| `acme_dns_nsadmin`              | string         | ---         | admin.example.org                                | administrative email with the @ represented as a dot                                |
| `acme_dns_records`              | list of string | ---         | ["auth.example.org. NS ns1.example.org."]        | additional records served by acme-dns                                               |
| `acme_dns_disable_registration` | bool           | true, false | false                                            | disable the registration endpoint                                                   |
| `acme_dns_api_port`             | string         | ---         | 80                                               | REST API listen port                                                                |
| `acme_dns_loglevel`             | string         | ---         | info                                             | logging level                                                                       |
| `acme_dns_logformat`            | string         | ---         | json                                             | logging format                                                                      |
| `acme_dns_environment_vars`     | dict           | ---         | `{}`                                             | extra environment variables injected into the container                             |
| `acme_dns_extra_files`          | list of dict   | ---         | []                                               | arbitrary file entries with src or source, dest, optional mount, mode, and template |
| `acme_dns_extra_dirs`           | list of dict   | ---         | []                                               | arbitrary directory entries with src or source, dest, optional mount and mode       |
| `acme_dns_entrypoint`           | string         | ---         | ""                                               | optional container entrypoint override                                              |
