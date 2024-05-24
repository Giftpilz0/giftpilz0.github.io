---
title: Ansible Cheat Sheet
---

______________________________________________________________________

## Introduction

This Ansible cheat sheet provides a quick reference for essential Ansible commands, YAML syntax, and key principles for managing and automating IT infrastructure.

______________________________________________________________________

## Core Concepts

### 1. Inventory

An inventory is a list of target hosts or groups of hosts where Ansible will run tasks.

Example Inventory:

```yaml
all:
  hosts:
    webserver1:
      ansible_host: 192.168.1.101
    webserver2:
      ansible_host: 192.168.1.102
  children:
    webservers:
      hosts:
        webserver1
        webserver2
```

### 2. Playbook

A playbook is a YAML file containing a set of tasks and configurations for Ansible to execute.

Example Playbook:

```yaml
- name: Install Apache
  hosts: webservers
  tasks:
    - name: Install Apache
      apt:
        name: apache2
        state: present
```

### 3. Task

A task is a single unit of work to be performed on a target host.

Example Task:

```yaml
- name: Create a Directory
  file:
    path: /path/to/directory
    state: directory
```

### 4. Module

Modules are reusable, standalone scripts that Ansible uses to perform tasks on target hosts.

### 5. Role

A role is a way to organize and reuse playbooks and related files.

Example Role Structure:

```
roles/
  webserver/
    tasks/
      main.yml
    handlers/
      main.yml
    templates/
    vars/
      main.yml
```

### 6. Variables

Variables are values that can be used in playbooks, templates, and roles.

Example Variable:

```yaml
web_server_port: 80
```

______________________________________________________________________

## Common Commands

### Running Playbooks

To run a playbook on target hosts:

```
ansible-playbook playbook.yml
```

### Ad-Hoc Commands

To run single tasks or commands on target hosts without writing a playbook:

```
ansible webservers -m ping
```

### Inventory Management

To view and manage inventory data:

```
ansible-inventory --list
```

### Vault (Encryption)

To encrypt sensitive data like passwords and keys in Ansible files:

```
ansible-vault encrypt secrets.yml
```

### Roles Management

To install, create, and manage Ansible roles:

```
ansible-galaxy install namespace.role_name
```
