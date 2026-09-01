---
title: K9S Role
---

Install the k9s terminal UI for Kubernetes.

______________________________________________________________________

## Variables

| Variable        | Type   | Options       | Default                                                                                            | Description                             |
| --------------- | ------ | ------------- | -------------------------------------------------------------------------------------------------- | --------------------------------------- |
| `k9s_bin_state` | string | present, skip | present                                                                                            | desired state of the k9s binary         |
| `k9s_url`       | string | ---           | `https://github.com/derailed/k9s/releases/download/v{{ k9s_tag }}/k9s_Linux_{{ k9s_arch }}.tar.gz` | download URL for the k9s binary         |
| `k9s_arch`      | string | ---           | amd64                                                                                              | target architecture (e.g. amd64, arm64) |
| `k9s_tag`       | string | ---           | 0.51.0                                                                                             | release version tag                     |
| `k9s_path`      | string | ---           | /usr/local/sbin                                                                                    | installation directory for the binary   |
