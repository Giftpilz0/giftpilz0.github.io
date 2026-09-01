---
title: Cfdyndns Role
---

Run a dynamic DNS updater that publishes the public IP to Cloudflare.

______________________________________________________________________

## Variables

| Variable                           | Type           | Options | Default                              | Description                                      |
| ---------------------------------- | -------------- | ------- | ------------------------------------ | ------------------------------------------------ |
| `cfdyndns_api_email`               | string         | ---     | ""                                   | Cloudflare account email used by the DDNS Worker |
| `cfdyndns_api_token`               | string         | ---     | ""                                   | Cloudflare API token for DNS updates             |
| `cfdyndns_update_url`              | string         | ---     | ""                                   | DDNS update endpoint URL                         |
| `cfdyndns_update_hostnames`        | list of string | ---     | []                                   | hostnames to update in one DDNS request          |
| `cfdyndns_cloudflare_trace_url`    | string         | ---     | https://cloudflare.com/cdn-cgi/trace | Cloudflare trace URL for IP detection            |
| `cfdyndns_script_path`             | string         | ---     | /usr/local/bin/ip_updater.py         | path to the IP updater script                    |
| `cfdyndns_state_dir`               | string         | ---     | /var/lib/cfdyndns                    | directory for storing state files                |
| `cfdyndns_last_ip_file`            | string         | ---     | `{{ cfdyndns_state_dir }}/last_ip`   | path to the file storing the last known IP       |
| `cfdyndns_check_interval`          | string         | ---     | 5min                                 | interval between IP change checks                |
| `cfdyndns_on_boot_delay`           | string         | ---     | 1min                                 | delay before first check after boot              |
| `cfdyndns_python_requests_package` | string         | ---     | python3-requests                     | name of the Python requests package to install   |
