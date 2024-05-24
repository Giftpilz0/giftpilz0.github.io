---
title: Cilium Role
---

This Ansible role can be used to install cilium.

______________________________________________________________________

## Variables

| Variables       | Type   | Options | Defaults               |
| --------------- | ------ | ------- | ---------------------- |
| cilium_version  | string | ---     | 1.15.4                 |
| cilium_repo_url | string | ---     | https://helm.cilium.io |

______________________________________________________________________

```yaml
- name: Import cilium Role
  hosts: all
  roles:
    - role: giftpilz0.kubernetes.cilium
```
