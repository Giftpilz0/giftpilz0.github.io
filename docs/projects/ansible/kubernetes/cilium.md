---
title: Cilium Role
---

Install and configure the Cilium CNI on a Kubernetes cluster.

______________________________________________________________________

## Variables

| Variable                                                 | Type    | Options     | Default                   | Description                              |
| -------------------------------------------------------- | ------- | ----------- | ------------------------- | ---------------------------------------- |
| `cilium_version`                                         | string  | ---         | 1.20.1                    | cilium Helm chart version                |
| `cilium_repo_url`                                        | string  | ---         | https://helm.cilium.io    | cilium Helm repository URL               |
| `cilium_kubeconfig`                                      | string  | ---         | /etc/rancher/k3s/k3s.yaml | path to kubeconfig for cluster access    |
| `cilium_config_kubeproxyreplacement`                     | bool    | true, false | true                      | enable kube-proxy replacement            |
| `cilium_config_k8sclientratelimit_qps`                   | integer | ---         | 30                        | Kubernetes client QPS rate limit         |
| `cilium_config_k8sclientratelimit_burst`                 | integer | ---         | 150                       | Kubernetes client burst rate limit       |
| `cilium_config_rolloutciliumpods`                        | bool    | true, false | true                      | trigger pod rollout after config changes |
| `cilium_config_l2announcements_enabled`                  | bool    | true, false | false                     | enable L2 announcements                  |
| `cilium_config_bgp_enabled`                              | bool    | true, false | false                     | enable BGP peering                       |
| `cilium_config_bgpcontrolplane_enabled`                  | bool    | true, false | false                     | enable BGP control plane                 |
| `cilium_config_ingresscontroller_enabled`                | bool    | true, false | true                      | enable cilium ingress controller         |
| `cilium_config_ingresscontroller_default`                | bool    | true, false | true                      | set cilium as default ingress controller |
| `cilium_config_gatewayapi_enabled`                       | bool    | true, false | true                      | enable Gateway API support               |
| `cilium_config_hostfirewall_enabled`                     | bool    | true, false | true                      | enable host firewall                     |
| `cilium_config_hubble_enabled`                           | bool    | true, false | true                      | enable Hubble observability              |
| `cilium_config_hubble_relay_enabled`                     | bool    | true, false | true                      | enable Hubble Relay                      |
| `cilium_config_hubble_relay_rolloutpods`                 | bool    | true, false | true                      | trigger pod rollout for Hubble Relay     |
| `cilium_config_hubble_ui_enabled`                        | bool    | true, false | true                      | enable Hubble UI                         |
| `cilium_config_hubble_ui_rolloutpods`                    | bool    | true, false | true                      | trigger pod rollout for Hubble UI        |
| `cilium_config_ipam_mode`                                | string  | ---         | cluster-pool              | IPAM mode (e.g. cluster-pool)            |
| `cilium_config_ipam_operator_clusterpoolipv4podcidrlist` | list    | ---         | ["10.0.0.0/8"]            | list of IPv4 pod CIDRs for cluster-pool  |
| `cilium_config_ipv4_enabled`                             | bool    | true, false | true                      | enable IPv4 networking                   |
| `cilium_config_ipv6_enabled`                             | bool    | true, false | false                     | enable IPv6 networking                   |
| `cilium_config_egressgateway_enabled`                    | bool    | true, false | false                     | enable egress gateway                    |
| `cilium_config_operator_enabled`                         | bool    | true, false | true                      | deploy the cilium operator               |
| `cilium_config_operator_rolloutpods`                     | bool    | true, false | false                     | trigger pod rollout for the operator     |
