---
title: Update Role
---

Apply system package updates with an optional automatic reboot.

______________________________________________________________________

## Variables

| Variable                       | Type           | Options     | Default | Description                                      |
| ------------------------------ | -------------- | ----------- | ------- | ------------------------------------------------ |
| `update_package_names`         | list of string | ---         | \*      | list of packages to update (empty for all)       |
| `update_package_security_only` | bool           | true, false | false   | only apply security updates                      |
| `update_package_bugfix_only`   | bool           | true, false | false   | only apply bugfix updates                        |
| `update_reboot_enabled`        | bool           | true, false |         | whether to reboot after updates if required      |
| `update_reboot_timeout`        | integer        | ---         |         | timeout in seconds to wait for reboot completion |
