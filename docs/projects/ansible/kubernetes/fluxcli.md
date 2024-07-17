---
title: Fluxcli Role
---

This Ansible role can be used to install fluxcli.

______________________________________________________________________

## Variables

| Variables          | Type   | Options       | Defaults                                                                                                                      |
| ------------------ | ------ | ------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| fluxcli_bin_state: | string | present, skip | present                                                                                                                       |
| fluxcli_url:       | string | ---           | `https://github.com/fluxcd/flux2/releases/download/v{{ fluxcli_tag }}/flux_{{ fluxcli_tag }}_linux_{{ fluxcli_arch }}.tar.gz` |
| fluxcli_arch:      | string | ---           | amd64                                                                                                                         |
| fluxcli_tag:       | string | ---           | 2.3.0                                                                                                                         |
| fluxcli_path:      | string | ---           | /usr/local/sbin                                                                                                               |

______________________________________________________________________

## Example Playbook

```yaml
- name: Import fluxcli Role
  hosts: all
  roles:
    - role: giftpilz0.kubernetes.fluxcli
```
