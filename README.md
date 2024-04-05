# Ansible Collection - jomrr.dev

![GitHub](https://img.shields.io/github/license/jomrr/ansible-collection-dev) ![GitHub last commit](https://img.shields.io/github/last-commit/jomrr/ansible-collection-dev) ![GitHub issues](https://img.shields.io/github/issues-raw/jomrr/ansible-collection-dev)

## Description

This collection provides a set of modules, plugins and playbooks designed to streamline ansible
role development and maintenance.

## Installation

Your need to install the collection from github, as my galaxy account is broken:

```bash
ansible-galaxy collection install git+https://github.com/jomrr/ansible-collection-dev.git,main
```

## Usage

The following examples demonstrate how to use modules and plugins from this collection.

### Module `generate_argument_specs`

```yaml
    - hosts: all
      tasks:
        - name: "Generate meta/argument_specs.yml"
          jomrr.dev.generate_argument_specs:
            defaults_file: /path/to/role/defaults/main.yml
            ouput_file: /path/to/role/meta/argument_specs.yaml
```

### Inventory plugin `ansible_role_inventory`

#### Ansible configuration in `ansible.cfg`

```ini
[defaults]

collections_path    = ./collections
inventory           = ./inventory.yml
playbook_dir        = ./playbooks
roles_path          = ./roles
remote_tmp          = /tmp/ansible

pipelining          = False
strategy            = free

[inventory]
enable_plugins      = jomrr.dev.ansible_role_inventory
```

#### Inventory file `inventory.yml`

```yaml
---
plugin: jomrr.dev.ansible_role_inventory
base_path: "~/src/ansible/roles/"
search_prefix: ansible-role-

```

## Modules

- **fetch_github_repos**: A module for fetching and caching repository data from Github.
- **generate_argument_specs**: A module for generating `meta/argument_specs.yml` from a roles' `defaults/main.yml`.

## Plugins

### Inventory

- **ansible_role_inventory**: Inventory plugin for using role directories as inventory hosts with `ansible_connection=local`.

### Lookup

- **github_version**: Lookup plugin to fetch latest release version of a repo from Github.

## Requirements

- ansible >= 2.15

## Contributing

Contributions to this collection are welcome. Please ensure to follow best practices for Ansible role and module development, including documentation for new features and roles. For more details, see the CONTRIBUTING.md file.

## License

[MIT](LICENSE)

## Authors

- Jonas Mauer (@jomrr)
