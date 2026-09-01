---
title: Lego Role
---

Issue and renew ACME (Let's Encrypt) certificates with lego.

______________________________________________________________________

## Variables

| Variable                   | Type           | Options                               | Default                                                                                                               | Description                                         |
| -------------------------- | -------------- | ------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| `lego_keytype`             | string         | ---                                   | rsa4096                                                                                                               | certificate key type (e.g. rsa4096)                 |
| `lego_cert_path`           | string         | ---                                   | /etc/ssl/lego                                                                                                         | directory to store certificates                     |
| `lego_acme_email`          | string         | ---                                   | ""                                                                                                                    | ACME account email address                          |
| `lego_dns_resolver`        | string         | ---                                   | 8.8.8.8:53                                                                                                            | DNS resolver for domain validation                  |
| `lego_acme_provider`       | string         | ---                                   | cloudflare                                                                                                            | ACME DNS challenge provider (e.g. cloudflare)       |
| `lego_cloudflare_api_key`  | string         | ---                                   |                                                                                                                       | Cloudflare API key for DNS challenge                |
| `lego_manager_script_path` | string         | ---                                   | /usr/local/bin/manage_lego_certs.sh                                                                                   | path to the certificate management script           |
| `lego_acme_domains`        | string         | ---                                   | ""                                                                                                                    | comma-separated list of domains for the certificate |
| `lego_service_state`       | string         | reloaded, restarted, started, stopped | started                                                                                                               | desired state of the lego services                  |
| `lego_service_enabled`     | bool           | true, false                           | true                                                                                                                  | whether lego services are enabled at boot           |
| `lego_service_name`        | list of string | ---                                   | ["lego-manage.service","lego-manage.timer"]                                                                           | systemd service and timer unit names                |
| `lego_bin_state`           | string         | present, skip                         | present                                                                                                               | desired state of the lego binary                    |
| `lego_url`                 | string         | ---                                   | `https://github.com/go-acme/lego/releases/download/v{{ lego_tag }}/lego_v{{ lego_tag }}_linux_{{ lego_arch }}.tar.gz` | download URL for the lego binary                    |
| `lego_arch`                | string         | ---                                   | amd64                                                                                                                 | target architecture (e.g. amd64, arm64)             |
| `lego_tag`                 | string         | ---                                   | 5.4.0                                                                                                                 | release version tag                                 |
| `lego_path`                | string         | ---                                   | /usr/local/bin                                                                                                        | installation directory for the binary               |
| `lego_package`             | list of string | ---                                   | openssl                                                                                                               | list of dependencies to install                     |
| `lego_package_state`       | string         | present, absent, latest               | present                                                                                                               | desired state of dependency packages                |
