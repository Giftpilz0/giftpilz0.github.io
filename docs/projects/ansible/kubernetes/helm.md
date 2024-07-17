---
title: Helm Role
---

This Ansible role can be used to install helm.

______________________________________________________________________

## Variables

| Variables       | Type   | Options       | Defaults                                                                |
| --------------- | ------ | ------------- | ----------------------------------------------------------------------- |
| helm_bin_state: | string | present, skip | present                                                                 |
| helm_url:       | string | ---           | `https://get.helm.sh/helm-v{{ helm_tag }}-linux-{{ helm_arch }}.tar.gz` |
| helm_arch:      | string | ---           | amd64                                                                   |
| helm_tag:       | string | ---           | 3.15.3                                                                  |
| helm_path:      | string | ---           | /usr/local/sbin                                                         |

______________________________________________________________________

## Example Playbook

```yaml
- name: Import helm Role
  hosts: all
  roles:
    - role: giftpilz0.kubernetes.helm
```
