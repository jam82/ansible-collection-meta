"""
Common filter plugins for Ansible.
"""
import yaml
from ansible.errors import AnsibleFilterError
from ansible.parsing.yaml.objects import AnsibleUnicode


class MyDumper(yaml.Dumper):
    """
    Custom YAML Dumper that increases indentation for nested collections.
    """
    def increase_indent(self, flow=False, indentless=False):
        return super().increase_indent(flow, False)

def ansible_unicode_representer(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:str', str(data))

# Register the representer with the Dumper
MyDumper.add_representer(AnsibleUnicode, ansible_unicode_representer)

def to_lintable_yaml(a, indent=2, sort_keys=False):
    """
    An Ansible filter to convert a Python object into a nicely formatted YAML string.
    Args:
        a: The Python object to convert.
        indent: The number of spaces to use for indentation.

    Returns:
        A YAML string representation of the Python object.
    """
    try:
        return yaml.dump(a, Dumper=MyDumper, default_flow_style=False, indent=indent, sort_keys=sort_keys)
    except Exception as e:
        raise AnsibleFilterError("to_lintable_yaml filter plugin error: %s" % str(e)) from e

class FilterModule():
    """
    Defines a filter module class that Ansible will auto-detect and use.
    """
    def filters(self):
        """ Returns a dict mapping filter names to functions. """
        return {
            'to_lintable_yaml': to_lintable_yaml
        }
