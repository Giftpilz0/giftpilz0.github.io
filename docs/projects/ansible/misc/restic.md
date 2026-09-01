---
title: Restic Role
---

Install and configure restic/resticprofile for automated repository backups.

______________________________________________________________________

## Variables

| Variable                               | Type           | Options              | Default                                                    | Description                                        |
| -------------------------------------- | -------------- | -------------------- | ---------------------------------------------------------- | -------------------------------------------------- |
| `resticprofile_version`                | string         | ---                  | 0.33.1                                                     | resticprofile release version                      |
| `rest_server_version`                  | string         | ---                  | 0.14.0                                                     | rest-server release version                        |
| `restic_mode`                          | string         | client, server, both | client                                                     | role operating mode                                |
| `restic_user`                          | string         | ---                  | backup                                                     | system user for restic operations                  |
| `restic_user_home`                     | string         | ---                  | `/home/{{ restic_user }}`                                  | home directory of the restic user                  |
| `restic_config_dir`                    | string         | ---                  | /etc/resticprofile                                         | directory for resticprofile configuration          |
| `restic_cache_dir`                     | string         | ---                  | /var/cache/restic                                          | directory for restic cache data                    |
| `restic_log_dir`                       | string         | ---                  | `{{ restic_config_dir }}/logs`                             | directory for restic log files                     |
| `restic_password_dir`                  | string         | ---                  | `{{ restic_config_dir }}/passwords`                        | directory for repository password files            |
| `restic_ssh_key_type`                  | string         | ---                  | ed25519                                                    | SSH key type for backup connections                |
| `restic_ssh_key_path`                  | string         | ---                  | `{{ restic_user_home }}/.ssh/id_{{ restic_ssh_key_type }}` | path to the SSH private key                        |
| `restic_server_repo_base`              | string         | ---                  | /var/lib/restic                                            | base directory for server-side repositories        |
| `restic_server_host`                   | string         | ---                  | ""                                                         | hostname or IP of the rest-server                  |
| `restic_repositories`                  | list of dict   | ---                  | []                                                         | list of restic repositories to manage              |
| `restic_repositories.name`             | string         | ---                  |                                                            | repository name                                    |
| `restic_repositories.password`         | string         | ---                  |                                                            | repository password                                |
| `restic_repositories.backup_paths`     | list of string | ---                  |                                                            | paths to back up                                   |
| `restic_repositories.exclude_patterns` | list of string | ---                  |                                                            | patterns to exclude from backup                    |
| `restic_repositories.schedule`         | string         | ---                  |                                                            | systemd calendar schedule (e.g. \*-\*-\* 02:00:00) |
| `restic_repositories.retention`        | dict           | ---                  |                                                            | ---                                                |
|                                        |                |                      |                                                            |                                                    |
