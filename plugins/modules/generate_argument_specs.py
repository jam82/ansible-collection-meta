# -*- coding: utf-8 -*-

"""
Ansible Module for generating meta/argument_specs.yml from a provided
default variable file, e.g. defaults/main.yml.
"""

import os
import yaml
from ansible.module_utils.basic import AnsibleModule

DOCUMENTATION = '''
---
module: generate_argument_specs
short_description: Generates argument specifications from default role variables
version_added: "1.0"
description:
    - "This module reads variables from a specified defaults/main.yml file within an Ansible role and generates a meta/argument_specs.yml file with argument specifications for those variables, including type inference."
options:
    defaults_file:
        description:
            - The path to the role's defaults/main.yml file from which to read variables.
        required: true
        type: str
    output_file:
        description:
            - The path to the meta/argument_specs.yml file to generate or update.
        required: true
        type: str
author:
    - Your Name (@yourgithub)
'''

EXAMPLES = '''
# Example of how to use generate_argument_specs
- name: Generate argument specs from role defaults
  generate_argument_specs:
    defaults_file: "{{ role_path }}/defaults/main.yml"
    output_file: "{{ role_path }}/meta/argument_specs.yml"
'''

RETURN = '''
message:
    description: A message about the result of the operation.
    type: str
    returned: always
changed:
    description: Indicates whether any changes were made by the module.
    type: bool
    returned: always
'''

def infer_type(value):
    """
    Infer the type of a variable for documentation purposes.

    Args:
        value: The value of the variable.

    Returns:
        A string representing the inferred type ('str', 'int', 'bool', 'list', 'dict').
    """
    if isinstance(value, bool):
        return 'bool'
    elif isinstance(value, int):
        return 'int'
    elif isinstance(value, list):
        return 'list'
    elif isinstance(value, dict):
        return 'dict'
    else:
        return 'str'

def load_defaults(file_path, module):
    """
    Load variables from a YAML file.

    Args:
        file_path: Path to the YAML file.
        module: An instance of AnsibleModule for error handling.

    Returns:
        A dictionary of variables loaded from the file.
        Returns an empty dictionary if the file does not exist or is empty.
    """
    if not os.path.exists(file_path):
        return {}  # Return an empty dictionary for consistency
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            return yaml.safe_load(file) or {}
    except OSError as e:
        module.fail_json(msg=f"Failed to open YAML file {file_path}: {e}")
    except yaml.YAMLError as e:
        module.fail_json(msg=f"Failed to parse YAML file {file_path}: {e}")

def generate_argument_specs(variables):
    """
    Generate argument specifications based on variables.

    Args:
        variables: Dictionary of variables to generate specs for.

    Returns:
        A dictionary representing the argument specifications.
    """
    argument_specs = {'role_parameters': {}}
    for var_name, default_value in variables.items():
        var_type = infer_type(default_value)
        argument_specs['role_parameters'][var_name] = {
            'description': [f'The {var_name} parameter.'],
            'default': default_value,
            'type': var_type
        }
    return argument_specs

def read_existing_content(file_path, module):
    """
    Read the existing content of a YAML file and fail gracefully on error.

    Args:
        file_path: Path to the YAML file.
        module: The Ansible module object for error handling.

    Returns:
        The content of the file if it exists and is valid YAML, otherwise None.
    """
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return yaml.safe_load(file)
        except OSError as e:
            module.fail_json(msg=f"Unable to open file {file_path}: {e}")
        except yaml.YAMLError as e:
            module.fail_json(msg=f"Error parsing YAML content in file {file_path}: {e}")
    return None

def save_argument_specs(specs, file_path, module):
    """
    Save argument specs to a YAML file, only if changed.

    Args:
        specs: The argument specs to save.
        file_path: Path to the YAML file to save specs to.
        module: The Ansible module object for error handling.

    Returns:
        changed: Boolean indicating if the file was updated.
    """
    existing_content = read_existing_content(file_path, module)
    if specs != existing_content:
        try:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w', encoding="utf-8") as file:
                yaml.safe_dump(specs, file, default_flow_style=False)
            return True
        except OSError as e:
            module.fail_json(msg=f"Failed to create directories or open the file {file_path}: {e}")
        except yaml.YAMLError as e:
            module.fail_json(msg=f"Failed to dump YAML content to {file_path}: {e}")
        return False

def run_module():
    """
    Execute module logic.
    """
    module_args = dict(
        defaults_file=dict(type='str', required=True),
        output_file=dict(type='str', required=True)
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if module.check_mode:
        module.exit_json(changed=False)

    defaults_file = module.params['defaults_file']
    output_file = module.params['output_file']

    variables = load_defaults(defaults_file, module)
    if variables is None or not variables:
        module.exit_json(changed=False,
                         msg="No variables found or defaults/main.yml does not exist.")

    argument_specs = generate_argument_specs(variables)
    changed = save_argument_specs(argument_specs, output_file, module)

    module.exit_json(changed=changed,
                     message="Argument specs have been successfully generated." if changed
                     else "No changes detected in argument specs.")

if __name__ == '__main__':
    run_module()
