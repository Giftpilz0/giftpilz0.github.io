---
title: Nfs Role
---

Install and configure the NFS server and its exports.

______________________________________________________________________

## Variables

| Variable                  | Type           | Options                                  | Default                                                      | Description                                  |
| ------------------------- | -------------- | ---------------------------------------- | ------------------------------------------------------------ | -------------------------------------------- |
| `nfs_service_name`        | list of dict   | ---                                      | `[{"name":"nfs-server.service"},{"name":"rpcbind.service"}]` | list of NFS services to manage               |
| `nfs_service_name.name`   | string         | ---                                      |                                                              | systemd service unit name                    |
|                           |                |                                          |                                                              |                                              |
| `nfs_service_state`       | string         | reloaded, restarted, started, stopped    | started                                                      | desired state of NFS services                |
| `nfs_service_enabled`     | bool           | true, false                              | true                                                         | whether NFS services are enabled at boot     |
| `nfs_package_state`       | string         | present, absent, latest                  | present                                                      | desired state of NFS packages                |
| `nfs_package`             | list of string | ---                                      | ["nfs-utils"]                                                | list of packages to install                  |
| `nfs_exports_file`        | string         | ---                                      | /etc/exports                                                 | path to the exports file                     |
| `nfs_exports`             | list of dict   | ---                                      |                                                              | list of NFS exports to manage                |
| `nfs_exports.path`        | string         | ---                                      |                                                              | exported directory path                      |
| `nfs_exports.host`        | string         | ---                                      |                                                              | allowed client host or CIDR                  |
| `nfs_exports.options`     | string         | ---                                      |                                                              | export options (e.g. rw,sync,no_root_squash) |
| `nfs_exports.group`       | string         | ---                                      |                                                              | directory group owner                        |
| `nfs_exports.user`        | string         | ---                                      |                                                              | directory user owner                         |
| `nfs_exports.permissions` | string         | ---                                      |                                                              | directory permissions (e.g. 0755)            |
|                           |                |                                          |                                                              |                                              |
| `nfs_exports_state`       | string         | present, absent, skip                    | present                                                      | desired state of export entries              |
| `nfs_firewalld_zone`      | string         | ---                                      |                                                              | firewall zone for NFS rules                  |
| `nfs_firewalld_service`   | string         | ---                                      | nfs                                                          | firewall service name                        |
| `nfs_firewalld_state`     | string         | present, absent, enabled, disabled, skip | enabled                                                      | desired state of firewall rules              |
