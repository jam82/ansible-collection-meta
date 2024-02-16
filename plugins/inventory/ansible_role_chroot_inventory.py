"""
Ansible Inventory Plugin for Listing Directories with ansible-role- Prefix

This module defines an Ansible inventory plugin that scans a specified
base path for directories whose names start with 'ansible-role-'.
It uses the chroot connection method to manage the discovered directories
as inventory hosts.
"""

import os
from ansible.errors import AnsibleError
from ansible.plugins.inventory import BaseInventoryPlugin


DOCUMENTATION = '''
    name: ansible_role_chroot_inventory
    plugin_type: inventory
    short_description: Lists directories matching a configurable prefix under a given path
    description:
        - This inventory plugin lists directories under a given path that match a configurable prefix.
        - Only the substring of the directory name following the prefix is added as the inventory host.
    options:
        base_path:
            description: The base path to search for directories.
            required: true
            type: str
        search_prefix:
            description: The prefix to search for in directory names.
            required: false
            type: str
'''

EXAMPLES = '''
# Example ansible.cfg
[defaults]
inventory_plugins = ./plugins/inventories

# Example inventory file using the ansible_role_chroot_inventory plugin
plugin: ansible_role_chroot_inventory
base_path: /path/to/search
search_prefix: ansible-role-
'''

class InventoryModule(BaseInventoryPlugin):
    """
    Inventory plugin to list directories starting with ansible-role- under
    a given path using chroot.
    """

    NAME = 'ansible_role_chroot_inventory'

    def verify_file(self, path):
        """
        Verify if the given file is valid for this plugin.
        """
        super().verify_file(path)
        # Ensure file has proper content for this plugin
        valid = True

        return valid

    def parse(self, inventory, loader, path, cache=True):
        """
        Parses the inventory file and populates the inventory accordingly.
        """
        super().parse(inventory, loader, path)

        self._read_config_data(path)

        base_path = self.get_option('base_path')
        search_prefix = self.get_option('search_prefix') or ''

        if base_path.startswith('~'):
            base_path = os.path.expanduser(base_path)

        if not os.path.isdir(base_path):
            raise AnsibleError(f"Base path {base_path} is not a directory or does not exist.")

        for root, dirs, _ in os.walk(base_path):
            for dir_name in dirs:
                if search_prefix == '' or dir_name.startswith(search_prefix):
                    # Extract the part of the directory name following the search prefix
                    host_name = dir_name[len(search_prefix):]
                    self.inventory.add_host(host_name)
                    self.inventory.set_variable(host_name,
                                                'ansible_connection', 'chroot')
                    self.inventory.set_variable(host_name,
                                                'ansible_chroot_dir', os.path.join(root, dir_name))

def main():
    """
    Main function for standalone testing of the inventory plugin.
    """
    # For testing purposes, this main function won't be executed by Ansible
    # but can be used for direct testing.
    inventory = InventoryModule()
    loader = None
    path = 'inventory.yml'
    inventory.parse(None, loader, path)
    print(inventory.inventory.hosts)

if __name__ == '__main__':
    main()
