---
title: NFS Role
---

This Ansible role can be used to configure NFS-shares.

______________________________________________________________________

## Variables

| Variables                | Type   | Options                                        | Defaults                            |
| ------------------------ | ------ | ---------------------------------------------- | ----------------------------------- |
| nfs_service_name:        | list   | ---                                            | nfs-server.service, rpcbind.service |
| nfs_service_state:       | string | reloaded, restarted, started, stopped          | started                             |
| nfs_service_enabled:     | bool   | false, true                                    | true                                |
| nfs_package_state:       | string | present, absent, latest                        | present                             |
| nfs_package:             | list   | ---                                            | nfs-utils                           |
|                          |        |                                                |                                     |
| nfs_exports:             | dict   | ---                                            | ---                                 |
| nfs_exports.path:        | string | ---                                            | ---                                 |
| nfs_exports.host:        | string | ---                                            | ---                                 |
| nfs_exports.options:     | string | ---                                            | ---                                 |
| nfs_exports_file:        | string | ---                                            | /etc/exports                        |
| nfs_exports.user:        | string | ---                                            | `{{ ansible_user }}`                |
| nfs_exports.group:       | string | ---                                            | `{{ ansible_user }}`                |
| nfs_exports.permissions: | string | ---                                            | 0755                                |
| nfs_exports_state:       | string | present, absent, skip                          | present                             |
|                          |        |                                                |                                     |
| nfs_firewalld_zone:      | string | block, dmz, drop, internal, public, trusted... | ---                                 |
| nfs_firewalld_service:   | string | ---                                            | nfs                                 |
| nfs_firewalld_state:     | string | present, absent, enabled, disabled, skip       | enabled                             |

______________________________________________________________________

## Example Playbook

```yaml
- name: Import nfs Role
  hosts: all
  roles:
    - role: giftpilz0.server.nfs
```
