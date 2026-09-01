---
title: Fluxcli Role
---

Install the Flux CLI (flux) binary.

______________________________________________________________________

## Variables

| Variable            | Type   | Options       | Default                                                                                                                       | Description                             |
| ------------------- | ------ | ------------- | ----------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| `fluxcli_bin_state` | string | present, skip | present                                                                                                                       | desired state of the flux binary        |
| `fluxcli_url`       | string | ---           | `https://github.com/fluxcd/flux2/releases/download/v{{ fluxcli_tag }}/flux_{{ fluxcli_tag }}_linux_{{ fluxcli_arch }}.tar.gz` | download URL for the flux binary        |
| `fluxcli_arch`      | string | ---           | amd64                                                                                                                         | target architecture (e.g. amd64, arm64) |
| `fluxcli_tag`       | string | ---           | 2.9.4                                                                                                                         | release version tag                     |
| `fluxcli_path`      | string | ---           | /usr/local/sbin                                                                                                               | installation directory for the binary   |
