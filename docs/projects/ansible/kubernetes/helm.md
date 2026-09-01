---
title: Helm Role
---

Install the Helm package manager binary.

______________________________________________________________________

## Variables

| Variable         | Type   | Options       | Default                                                                 | Description                             |
| ---------------- | ------ | ------------- | ----------------------------------------------------------------------- | --------------------------------------- |
| `helm_bin_state` | string | present, skip | present                                                                 | desired state of the helm binary        |
| `helm_url`       | string | ---           | `https://get.helm.sh/helm-v{{ helm_tag }}-linux-{{ helm_arch }}.tar.gz` | download URL for the helm binary        |
| `helm_arch`      | string | ---           | amd64                                                                   | target architecture (e.g. amd64, arm64) |
| `helm_tag`       | string | ---           | 4.2.4                                                                   | release version tag                     |
| `helm_path`      | string | ---           | /usr/local/sbin                                                         | installation directory for the binary   |
