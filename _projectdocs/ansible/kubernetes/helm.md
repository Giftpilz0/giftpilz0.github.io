---
layout: default
title: Helm Role
parent: Kubernetes Collection
grand_parent: Ansible
---

# {{ page.title }}

This Ansible role can be used to install helm.

______________________________________________________________________

## Variables

| Variables       | Type   | Options       | Defaults                                                                                                         |
| --------------- | ------ | ------------- | ---------------------------------------------------------------------------------------------------------------- |
| helm_bin_state: | string | present, skip | present                                                                                                          |
| helm_url:       | string | ---           | https://github.com/helm/helm/releases/download/v{{ helm_tag }}/helm-v{{ helm_tag }}-linux-{{ helm_arch }}.tar.gz |
| helm_arch:      | string | ---           | amd64                                                                                                            |
| helm_tag:       | string | ---           | 3.14.4                                                                                                           |
| helm_path:      | string | ---           | /usr/local/bin                                                                                                   |

______________________________________________________________________

## Example Playbook

```yaml
- name: Import helm Role
  hosts: all
  roles:
    - role: giftpilz0.kubernetes.helm
```
