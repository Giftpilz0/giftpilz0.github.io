---
layout: default
title: Kubernetes Collection
has_children: true
parent: Ansible
has_toc: false
---

![Ansible-Lint](https://github.com/giftpilz0/ansible-collection-kubernetes/actions/workflows/ci.yml/badge.svg)

Ansible Collection to configure and install a k3s cluster on multiple Linux systems.

______________________________________________________________________

## Installation

`ansible-galaxy collection install git+https://github.com/Giftpilz0/ansible-collection-kubernetes.git`

## Included Roles

- [cilium](cilium/)
- [helm](helm/)
- [k3s](k3s/)

## Requirements

- Fedora >= 38
