---
title: Quadlet Role
---

Deploy the quadlet files of a service role and (re)start its units.

______________________________________________________________________

## Variables

| Variable                         | Type           | Options     | Default                                                                           | Description                                                                                                                        |
| -------------------------------- | -------------- | ----------- | --------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `podman_user`                    | string         | ---         | `{{ ansible_user }}`                                                              | System user for rootless Podman operations                                                                                         |
| `podman_unprivileged_port_start` | integer        | ---         | 80                                                                                | Lowest host port rootless containers may bind                                                                                      |
| `podman_proxy_enabled`           | bool           | true, false | false                                                                             | Configure an HTTP proxy for image pulls and all containers on the host                                                             |
| `podman_proxy_http`              | string         | ---         | ""                                                                                | HTTP proxy URL                                                                                                                     |
| `podman_proxy_https`             | string         | ---         | ""                                                                                | HTTPS proxy URL                                                                                                                    |
| `podman_proxy_no_proxy`          | string         | ---         | ""                                                                                | Comma-separated list of proxy exclusions                                                                                           |
| `quadlet_role`                   | string         | ---         | ""                                                                                | Service role whose templates/ and files/ trees are deployed                                                                        |
| `quadlet_role_path`              | path           | ---         | `{{ role_path \| dirname }}/{{ quadlet_role }}`                                   | Path of the service role, needed for roles outside this collection                                                                 |
| `quadlet_dir`                    | string         | ---         | `{{ quadlet_role \| replace('_', '-') }}-pod`                                     | Main quadlet directory of the service; extra files and dirs are placed here                                                        |
| `quadlet_dir_modes`              | dict           | ---         | `{}`                                                                              | Directory modes that differ from the role source tree, keyed by path relative to the quadlet base dir                              |
| `quadlet_units`                  | list of string | ---         | []                                                                                | systemd user units to start in order; restarted when deployed files changed                                                        |
| `quadlet_force_restart`          | bool           | true, false | false                                                                             | Restart the units even if no file changed                                                                                          |
| `quadlet_images_changed`         | bool           | true, false | false                                                                             | Set by tasks_from build when an image was rebuilt                                                                                  |
| `quadlet_extra_files`            | list of dict   | ---         | []                                                                                | Extra file entries with src (controller path) or source (host path), dest, optional mount, mode, template and relabel (SELinux :Z) |
| `quadlet_extra_dirs`             | list of dict   | ---         | []                                                                                | Extra directory entries with src (controller path) or source (host path), dest, optional mount, mode and relabel (SELinux :Z)      |
| `quadlet_extra_file_defaults`    | dict           | ---         | `{"mode":"0640","template":false,"mount":"","source":"","src":"","relabel":true}` | Values for keys missing in quadlet_extra_files entries                                                                             |
| `quadlet_extra_dir_defaults`     | dict           | ---         | `{"mode":"0755","mount":"","source":"","src":"","relabel":true}`                  | Values for keys missing in quadlet_extra_dirs entries                                                                              |
