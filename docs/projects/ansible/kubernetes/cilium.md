---
title: Cilium Role
---

This Ansible role can be used to install cilium.

______________________________________________________________________

## Variables

| Variables                                              | Type   | Options | Defaults                  |
| ------------------------------------------------------ | ------ | ------- | ------------------------- |
| cilium_version                                         | string | ---     | 1.15.7                    |
| cilium_repo_url                                        | string | ---     | https://helm.cilium.io    |
| cilium_kubeconfig                                      | string | ---     | /etc/rancher/k3s/k3s.yaml |
| cilium_config_kubeproxyreplacement                     | bool   | ---     | false                     |
| cilium_config_k8sclientratelimit_qps                   | int    | ---     | 10                        |
| cilium_config_k8sclientratelimit_burst                 | int    | ---     | 20                        |
| cilium_config_rolloutciliumpods                        | bool   | ---     | false                     |
| cilium_config_l2announcements_enabled                  | bool   | ---     | false                     |
| cilium_config_bgp_enabled                              | bool   | ---     | false                     |
| cilium_config_bgpcontrolplane_enabled                  | bool   | ---     | false                     |
| cilium_config_ingresscontroller_enabled                | bool   | ---     | false                     |
| cilium_config_ingresscontroller_default                | bool   | ---     | false                     |
| cilium_config_gatewayapi_enabled                       | bool   | ---     | false                     |
| cilium_config_hostfirewall_enabled                     | bool   | ---     | false                     |
| cilium_config_hubble_enabled                           | bool   | ---     | true                      |
| cilium_config_hubble_relay_enabled                     | bool   | ---     | false                     |
| cilium_config_hubble_relay_rolloutpods                 | bool   | ---     | false                     |
| cilium_config_hubble_ui_enabled                        | bool   | ---     | true                      |
| cilium_config_hubble_ui_rolloutpods                    | bool   | ---     | false                     |
| cilium_config_ipam_mode                                | string | ---     | cluster-pool              |
| cilium_config_ipam_operator_clusterpoolipv4podcidrlist | list   | ---     | \[10.0.0.0/8\]            |
| cilium_config_ipv4_enabled                             | bool   | ---     | true                      |
| cilium_config_ipv6_enabled                             | bool   | ---     | false                     |
| cilium_config_egressgateway_enabled                    | bool   | ---     | false                     |
| cilium_config_operator_enabled                         | bool   | ---     | true                      |
| cilium_config_operator_rolloutpods                     | bool   | ---     | false                     |

______________________________________________________________________

```yaml
- name: Import cilium Role
  hosts: all
  roles:
    - role: giftpilz0.kubernetes.cilium
```
