---
title: GitLab Runner Role
---

Deploy a GitLab Runner as a Podman quadlet.

______________________________________________________________________

## Variables

| Variable                         | Type         | Options     | Default                        | Description                                                                                                         |
| -------------------------------- | ------------ | ----------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| `podman_user`                    | string       | ---         | `{{ ansible_user }}`           | System user for rootless podman operations                                                                          |
| `gitlab_runner_image`            | string       | ---         | docker.io/gitlab/gitlab-runner | Image name without tag                                                                                              |
| `gitlab_runner_version`          | string       | ---         | v19.5.0                        | Container image version                                                                                             |
| `gitlab_runner_autoupdate`       | bool         | true, false | true                           | Enable podman auto-update for this container                                                                        |
| `gitlab_runner_network_enabled`  | bool         | true, false | true                           | Create and manage the podman network                                                                                |
| `gitlab_runner_network_name`     | string       | ---         | gitlab-runner-internal         | Podman network name                                                                                                 |
| `gitlab_runner_network_driver`   | string       | ---         | bridge                         | Podman network driver                                                                                               |
| `gitlab_runner_concurrent`       | integer      | ---         | 1                              | Maximum number of concurrent jobs                                                                                   |
| `gitlab_runner_name`             | string       | ---         | ""                             | Runner display name                                                                                                 |
| `gitlab_runner_url`              | string       | ---         | ""                             | GitLab instance URL                                                                                                 |
| `gitlab_runner_token`            | string       | ---         | ""                             | Runner registration token                                                                                           |
| `gitlab_runner_environment_vars` | dict         | ---         | `{}`                           | Extra environment variables injected into the container                                                             |
| `gitlab_runner_entrypoint`       | string       | ---         | ""                             | Optional container entrypoint override                                                                              |
| `gitlab_runner_extra_files`      | list of dict | ---         | []                             | Arbitrary file entries with src (controller path) or source (target path), dest, optional mount, mode, and template |
| `gitlab_runner_extra_dirs`       | list of dict | ---         | []                             | Arbitrary directory entries with src (controller directory) or source (target path), dest, optional mount and mode  |
