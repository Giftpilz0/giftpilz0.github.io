---
title: GitLab Runner Role
---

Deploy a GitLab Runner as a Podman quadlet.

______________________________________________________________________

## Variables

| Variable                         | Type           | Options     | Default                | Description                                                                                                         |
| -------------------------------- | -------------- | ----------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `podman_user`                    | string         | ---         | `{{ ansible_user }}`   | system user for rootless podman operations                                                                          |
| `gitlab_runner_proxy_enabled`    | bool           | true, false | false                  | enable HTTP proxy for image pulls                                                                                   |
| `gitlab_runner_proxy_http`       | string         | ---         | ""                     | HTTP proxy URL                                                                                                      |
| `gitlab_runner_proxy_https`      | string         | ---         | ""                     | HTTPS proxy URL                                                                                                     |
| `gitlab_runner_proxy_no_proxy`   | string         | ---         | ""                     | comma-separated list of proxy exclusions                                                                            |
| `gitlab_runner_proxy_env`        | list of string | ---         | []                     | generated proxy environment entries                                                                                 |
| `gitlab_runner_network_enabled`  | bool           | true, false | true                   | create and manage the podman network                                                                                |
| `gitlab_runner_network_driver`   | string         | ---         | bridge                 | podman network driver                                                                                               |
| `gitlab_runner_network_name`     | string         | ---         | gitlab-runner-internal | podman network name                                                                                                 |
| `gitlab_runner_version`          | string         | ---         | v19.3.1                | container image version                                                                                             |
| `gitlab_runner_autoupdate`       | bool           | true, false | true                   | enable podman auto-update for this container                                                                        |
| `gitlab_runner_environment_vars` | dict           | ---         | `{}`                   | extra environment variables injected into the container                                                             |
| `gitlab_runner_concurrent`       | integer        | ---         | 1                      | maximum number of concurrent jobs                                                                                   |
| `gitlab_runner_name`             | string         | ---         | ""                     | runner display name                                                                                                 |
| `gitlab_runner_url`              | string         | ---         | ""                     | GitLab instance URL                                                                                                 |
| `gitlab_runner_token`            | string         | ---         | ""                     | runner registration token                                                                                           |
| `gitlab_runner_extra_files`      | list of dict   | ---         | []                     | arbitrary file entries with src (controller path) or source (target path), dest, optional mount, mode, and template |
| `gitlab_runner_extra_dirs`       | list of dict   | ---         | []                     | arbitrary directory entries with src (controller directory) or source (target path), dest, optional mount and mode  |
| `gitlab_runner_entrypoint`       | string         | ---         | ""                     | optional container entrypoint override                                                                              |
