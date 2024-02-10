---
layout: default
title: General Collection
has_children: true
parent: Ansible
has_toc: false
---

# {{ page.title }}

![Ansible-Lint](https://github.com/giftpilz0/ansible-collection-general/actions/workflows/ci.yml/badge.svg)

Ansible Collection to perform simple configurations on Linux systems.

______________________________________________________________________

## Installation

`ansible-galaxy collection install git+https://github.com/Giftpilz0/ansible-collection-general.git`

## Included Roles

- [dnf](dnf/)
- [dotfiles](dotfiles/)
- [firewalld](firewalld/)
- [git](git/)
- [monitoring](monitoring/)
- [packages](packages/)
- [sysutil](sysutil/)
- [timezone](timezone/)
- [update](update/)
- [user](user/)

## Requirements

- Fedora >= 38
