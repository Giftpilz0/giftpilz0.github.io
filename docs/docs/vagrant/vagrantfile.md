---
layout: default
title: Vagrantfile
parent: Vagrant
---

______________________________________________________________________

## Introduction

A Vagrantfile is a configuration file written in Ruby that defines the characteristics of your virtual machines and their provisioning. It serves as a blueprint for creating and configuring VMs, making it easier to collaborate on projects and recreate consistent development environments across different machines.

______________________________________________________________________

## Example

______________________________________________________________________

```ruby
nodes = [
    {
        :name => "node1",
        :mem => "1024",
        :cpu => "2"
    },
    {
        :name => "node2",
        :mem => "1024",
        :cpu => "2"
    }
]

Vagrant.configure("2") do |config|
  nodes.each do |node|

    # Configuration for libvirt provider
    config.vm.provider "libvirt" do |lv|
      lv.cpus = node[:cpu]
      lv.memory = node[:mem]
      lv.qemu_use_session = false
      lv.management_network_device = 'virbr0'
    end

    # Configuration for virtualbox provider
    config.vm.provider "virtualbox" do |vb|
      vb.cpus = node[:cpu]
      vb.memory = node[:mem]
      vb.linked_clone = true
    end

    # Configuration for hyper-v provider
    config.vm.provider "hyperv" do |hv|
      hv.cpus = node[:cpu]
      hv.memory = node[:mem]
      hv.linked_clone = true
    end

    # Configuration for individual nodes
    config.vm.define node[:name] do |instance|
      instance.vm.box = "fedora/38-cloud-base"
      instance.vm.hostname = node[:name]
      instance.vm.network :private_network, :ip => "10.0.0.0"
    end
  end
end

# Provisioning script
Vagrant.configure("2") do |config|
   config.vm.provision "shell", inline: <<-SHELL
     dnf update -y
     dnf install -y httpd
     systemctl enable --now httpd
   SHELL
end
```
