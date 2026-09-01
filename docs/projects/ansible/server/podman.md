---
title: Podman Role
---

Install Podman and configure the rootless port forwarder.

______________________________________________________________________

## Variables

| Variable                         | Type           | Options                               | Default                          | Description                                               |
| -------------------------------- | -------------- | ------------------------------------- | -------------------------------- | --------------------------------------------------------- |
| `podman_kube_path`               | string         | ---                                   | `/home/{{ ansible_user }}/kube/` | directory for Kubernetes YAML manifests                   |
| `podman_user`                    | string         | ---                                   | `{{ ansible_user }}`             | system user for rootless podman operations                |
| `podman_service_name`            | string         | ---                                   | podman.service                   | systemd service unit name                                 |
| `podman_service_state`           | string         | reloaded, restarted, started, stopped | started                          | desired state of the podman service                       |
| `podman_service_enabled`         | bool           | true, false                           | true                             | whether the podman service is enabled at boot             |
| `podman_package_state`           | string         | present, absent, latest               | present                          | desired state of podman packages                          |
| `podman_package`                 | list of string | ---                                   | ["podman"]                       | list of packages to install                               |
| `podman_rootless_port_forwarder` | string         | ---                                   | pasta                            | rootless port forwarder backend (e.g. pasta, slirp4netns) |
