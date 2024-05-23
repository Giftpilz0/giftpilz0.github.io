---
layout: default
title: Vagrant Cheat Sheet
parent: Vagrant
---

______________________________________________________________________

## Introduction

This cheat sheet provides a quick reference to commonly used Vagrant commands.

______________________________________________________________________

### Create and Provision Virtual Machines

To create and provision virtual machines:

```
vagrant up
```

### Shut Down Virtual Machines

To gracefully shut down the virtual machines:

```
vagrant halt
```

### Suspend and Resume Virtual Machines

Suspend the virtual machines and save their state:

```
vagrant suspend
```

Resume suspended virtual machines:

```
vagrant resume
```

### Destroy Virtual Machines

To permanently delete all virtual machines:

```
vagrant destroy
```

### Check Virtual Machine Status

Check the status of virtual machines:

```
vagrant status
```

### SSH into Virtual Machines

To access the command line of a virtual machine using SSH:

```
vagrant ssh
```

### Trigger Provisioning

If you've made changes to your setup and want to re-run provisioning:

```
vagrant provision
```
