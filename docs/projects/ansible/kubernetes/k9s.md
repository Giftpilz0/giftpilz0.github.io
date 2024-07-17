---
title: k9s Role
---

This Ansible role can be used to install k9s.

______________________________________________________________________

## Variables

| Variables      | Type   | Options       | Defaults                                                                                           |
| -------------- | ------ | ------------- | -------------------------------------------------------------------------------------------------- |
| k9s_bin_state: | string | present, skip | present                                                                                            |
| k9s_url:       | string | ---           | `https://github.com/derailed/k9s/releases/download/v{{ k9s_tag }}/k9s_Linux_{{ k9s_arch }}.tar.gz` |
| k9s_arch:      | string | ---           | amd64                                                                                              |
| k9s_tag:       | string | ---           | 0.32.5                                                                                             |
| k9s_path:      | string | ---           | /usr/local/sbin                                                                                    |

______________________________________________________________________

## Example Playbook

```yaml
- name: Import k9s Role
  hosts: all
  roles:
    - role: giftpilz0.kubernetes.k9s
```
