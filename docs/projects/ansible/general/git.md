---
title: Git Role
---

Install git and optionally configure system-wide git settings.

______________________________________________________________________

## Variables

| Variable                  | Type           | Options                 | Default | Description                           |
| ------------------------- | -------------- | ----------------------- | ------- | ------------------------------------- |
| `git_package_state`       | string         | present, absent, latest | present | desired state of git packages         |
| `git_package`             | list of string | ---                     | ["git"] | list of packages to install           |
| `git_config_system`       | list of dict   | ---                     |         | system-wide git configuration entries |
| `git_config_system.key`   | string         | ---                     |         | git configuration key                 |
| `git_config_system.value` | string         | ---                     |         | git configuration value               |
|                           |                |                         |         |                                       |
| `git_config`              | list of dict   | ---                     |         | per-user git configuration entries    |
| `git_config.key`          | string         | ---                     |         | git configuration key                 |
| `git_config.value`        | string         | ---                     |         | git configuration value               |
| `git_config.scope`        | string         | file, local, global     |         | git configuration scope               |
|                           |                |                         |         |                                       |
