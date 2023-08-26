---
layout: default
title: Pdfgen Role
parent: Ansible Desktop Collection
grand_parent: Ansible
---

# {{ page.title }}

This Ansible role can be used to install libreoffice and set up a Python script that watches for changes in Office documents and automatically converts it to PDF.

______________________________________________________________________

## Variables

| Variables                | Type   | Options                               | Defaults                               |
| ------------------------ | ------ | ------------------------------------- | -------------------------------------- |
| pdfgen_document_path:    | string | ---                                   | /home/"ansible_user"/Documents/        |
| pdfgen_user:             | string | ---                                   | "ansible_user"                         |
| pdfgen_service_name:     | string | ---                                   | pdfgen.service                         |
| pdfgen_service_state:    | string | reloaded, restarted, started, stopped | started                                |
| pdfgen_service_enabled:  | bool   | false, true                           | true                                   |
| pdfgen_package_state:    | string | present, absent, latest               | present                                |
| pdfgen_package:          | list   | ---                                   | python3, python3-pip, libreoffice-core |
| pdfgen_pip_package_state | string | present, absent, latest               | present                                |
| pdfgen_pip_package       | list   | ---                                   | watchdog                               |

______________________________________________________________________

## Example Playbook

```yaml
- name: Import pdfgen Role
  hosts: all
  roles:
    - role: giftpilz0.desktop.pdfgen
```
