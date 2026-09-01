---
title: Httpd Role
---

Install and configure the Apache HTTP server.

______________________________________________________________________

## Variables

| Variable                  | Type           | Options                                  | Default             | Description                                  |
| ------------------------- | -------------- | ---------------------------------------- | ------------------- | -------------------------------------------- |
| `httpd_service_name`      | string         | ---                                      | httpd.service       | systemd service unit name                    |
| `httpd_service_state`     | string         | reloaded, restarted, started, stopped    | started             | desired state of the httpd service           |
| `httpd_service_enabled`   | bool           | true, false                              | true                | whether the httpd service is enabled at boot |
| `httpd_package_state`     | string         | present, absent, latest                  | present             | desired state of httpd packages              |
| `httpd_package`           | list of string | ---                                      | ["httpd","mod_ssl"] | list of packages to install                  |
| `httpd_firewalld_zone`    | string         | ---                                      |                     | firewall zone for httpd rules                |
| `httpd_firewalld_service` | string         | ---                                      | http                | firewall service name                        |
| `httpd_firewalld_state`   | string         | present, absent, enabled, disabled, skip | enabled             | desired state of firewall rules              |
