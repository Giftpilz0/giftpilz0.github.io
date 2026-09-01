---
title: Pcp Role
---

Install and enable Performance Co-Pilot for system performance monitoring.

______________________________________________________________________

## Variables

| Variable              | Type           | Options                               | Default                                            | Description                              |
| --------------------- | -------------- | ------------------------------------- | -------------------------------------------------- | ---------------------------------------- |
| `pcp_service_name`    | list of string | ---                                   | ["pmie.service","pmlogger.service","pmcd.service"] | list of PCP systemd services to manage   |
| `pcp_service_state`   | string         | reloaded, restarted, started, stopped | started                                            | desired state of PCP services            |
| `pcp_service_enabled` | bool           | true, false                           | true                                               | whether PCP services are enabled at boot |
| `pcp_package_state`   | string         | present, absent, latest               | present                                            | desired state of PCP packages            |
| `pcp_package`         | list of string | ---                                   | ["pcp"]                                            | list of packages to install              |
