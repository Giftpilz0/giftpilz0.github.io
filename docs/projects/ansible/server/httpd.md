---
layout: default
title: Httpd Role
parent: Server Collection
grand_parent: Ansible
---

This Ansible role can be used to install Httpd.

______________________________________________________________________

## Variables

| Variables                | Type   | Options                                        | Defaults       |
| ------------------------ | ------ | ---------------------------------------------- | -------------- |
| httpd_service_name:      | string | ---                                            | httpd.service  |
| httpd_service_state:     | string | reloaded, restarted, started, stopped          | started        |
| httpd_service_enabled:   | bool   | false, true                                    | true           |
| httpd_package_state:     | string | present, absent, latest                        | present        |
| httpd_package:           | list   | ---                                            | httpd, mod_ssl |
|                          |        |                                                |                |
| httpd_firewalld_zone:    | string | block, dmz, drop, internal, public, trusted... | ---            |
| httpd_firewalld_service: | string | ---                                            | http           |
| httpd_firewalld_state:   | string | present, absent, enabled, disabled, skip       | present        |

______________________________________________________________________

## Example Playbook

```yaml
- name: Import httpd Role
  hosts: all
  roles:
    - role: giftpilz0.server.httpd
```
