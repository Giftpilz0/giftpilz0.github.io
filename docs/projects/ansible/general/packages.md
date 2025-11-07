---
title: Packages Role
---

This Ansible role can be used to install and uninstall packages from flathub, pip and from the distribution packages. Also you can use this role to configure rpmfusion repos + mediacodecs on Fedora.

______________________________________________________________________

| Variables                          | Type   | Options                         | Defaults                                                                                                                                                                                                                                        |
| ---------------------------------- | ------ | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| packages_package_state:            | string | present, absent, latest, skip   | present                                                                                                                                                                                                                                         |
| packages_rpmfusion_package_state:  | string | present, latest, skip           | skip                                                                                                                                                                                                                                            |
| packages_additional_package_state: | string | present, absent, latest, skip   | present                                                                                                                                                                                                                                         |
| packages_flatpak_package_state:    | string | present, absent, latest, skip   | present                                                                                                                                                                                                                                         |
| packages_python_package_state:     | string | present, absent, latest, skip   | present                                                                                                                                                                                                                                         |
| packages_package:                  | list   | ---                             | curl, htop, mkpasswd, python3-pip, rsync, zstd                                                                                                                                                                                                  |
| packages_rpmfusion_package:        | list   | ---                             | `https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-{{ ansible_distribution_major_version }}.noarch.rpm, https://mirrors.rpmfusion.org/free/fedora/rpmfusion-nonfree-release-{{ ansible_distribution_major_version }}.noarch.rpm` |
| packages_additional_package:       | list   | ---                             | ---                                                                                                                                                                                                                                             |
| packages_flatpak_package:          | list   | ---                             | ---                                                                                                                                                                                                                                             |
| packages_python_package:           | list   | ---                             | ---                                                                                                                                                                                                                                             |
| packages_flatpak_repo:             | string | ---                             | https://dl.flathub.org/repo/flathub.flatpakrepo                                                                                                                                                                                                 |
| packages_flatpak_repo_name:        | string | ---                             | flatpakrepo                                                                                                                                                                                                                                     |
| packages_flatpak_repo_state:       | string | present, absent, skip           | present                                                                                                                                                                                                                                         |
| packages_copr_repo_name:           | string | ---                             | ""                                                                                                                                                                                                                                              |
| packages_copr_repo_state:          | string | absent, enabled, disabled, skip | skip                                                                                                                                                                                                                                            |

______________________________________________________________________

## Example Playbook

```yaml
- name: Import packages Role
  hosts: all
  roles:
    - role: giftpilz0.general.packages
```
