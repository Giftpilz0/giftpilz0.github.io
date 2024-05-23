---
layout: default
title: Podman Role
parent: Server Collection
grand_parent: Ansible
---

This Ansible role can be used to install Podman Container Tools.

______________________________________________________________________

## Variables

| Variables               | Type   | Options                               | Defaults                         |
| ----------------------- | ------ | ------------------------------------- | -------------------------------- |
| podman_kube_path:       | string | ---                                   | `/home/{{ ansible_user }}/kube/` |
| podman_user:            | string | ---                                   | `{{ ansible_user }}`             |
| podman_service_name:    | string | ---                                   | podman.service                   |
| podman_service_state:   | string | reloaded, restarted, started, stopped | started                          |
| podman_service_enabled: | bool   | false, true                           | true                             |
| podman_package_state:   | string | present, absent, latest               | present                          |
| podman_package:         | list   | ---                                   | podman                           |

______________________________________________________________________

## Example Playbook

```yaml
- name: Import podman Role
  hosts: all
  roles:
    - role: giftpilz0.server.podman
```
