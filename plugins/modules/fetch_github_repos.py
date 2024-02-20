# -*- coding: utf-8 -*-

"""
This module fetches GitHub repositories based on a search query and
caches the response locally as a JSON file.
"""

import json
import os
import time
import requests
from ansible.module_utils.basic import AnsibleModule

DOCUMENTATION = '''
---
module: fetch_github_repos
short_description: Fetches GitHub repositories and caches them locally.
version_added: "1.0"
description:
    - "This module fetches GitHub repositories based on a search query and caches the response locally as a JSON file.
    - It is designed to reduce API calls by updating the cache based on a specified update threshold."
options:
    github_token:
        description:
            - GitHub personal access token for authentication.
        required: false
        default: ''
        type: str
    user_or_org:
        description:
            - The user or organization name to search within.
        required: true
        type: str
    is_org:
        description:
            - Flag to indicate if the search is for an organization.
        required: false
        default: false
        type: bool
    search_query:
        description:
            - The search query to filter repositories by name.
        required: true
        type: str
    cache_file:
        description:
            - Path to the file where the fetched data will be cached.
        required: false
        default: "/tmp/ansible/github_repos.json"
        type: str
    update_threshold_seconds:
        description:
            - The threshold in seconds to determine when to update the cache.
        required: false
        default: 3600
        type: int
author:
    - Your Name (@yourgithub)
'''

EXAMPLES = '''
# Example to fetch and cache repositories
- name: Fetch and cache GitHub repositories info
  fetch_github_repos:
    github_token: "{{ github_token }}"
    user_or_org: "example_user_or_org"
    is_org: false
    search_query: "ansible-role-"
    cache_file: "/path/to/cache_file.json"
'''

RETURN = '''
changed:
    description: Indicates whether any changes were made by the module.
    type: bool
    returned: always
message:
    description: Message about the action's result.
    type: str
    returned: always
gh_repos:
    description: Fetched GitHub repositories data.
    type: dict
    returned: always
'''

def fetch_repos(github_token, user_or_org, is_org, search_query):
    """Fetches repositories from GitHub based on a search query."""
    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github.v3+json",
    }
    url = f"https://api.github.com/search/repositories?q={
        search_query + '+in:name+' if search_query else '' }{
            'org:' if is_org else 'user:'}{user_or_org}"
    response = requests.get(url, headers=headers, timeout=10)

    # Handle rate limit exceeded error
    if response.status_code == 403 and "rate limit exceeded" in response.text.lower():
        raise Exception("GitHub API rate limit exceeded.")

    if response.status_code != 200:
        raise Exception(f"GitHub API responded with status code {
            response.status_code}: {response.text}")

    return response.json()

def save_repos_to_file(data, file_path):
    """Saves the fetched repository data to a local JSON file."""
    with open(file_path, 'w', encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def is_update_needed(file_path, update_threshold_seconds):
    """Checks if the cache file needs to be updated."""
    if not os.path.exists(file_path):
        return True
    last_mod_time = os.path.getmtime(file_path)
    current_time = time.time()
    return (current_time - last_mod_time) > update_threshold_seconds

def run_module():
    """Contains the module's main logic."""
    module = AnsibleModule(
        argument_spec={
            "github_token": {"type": "str", "required": False, "default": ''},
            "user_or_org": {"type": "str", "required": True},
            "is_org": {"type": "bool", "required": False, "default": False},
            "search_query": {"type": "str", "required": False, "default": None},
            "cache_file": {
                "type": "str", "required": False, "default": "/tmp/ansible/github_repos.json"
            },
            "update_threshold_seconds": {"type": "int", "default": 3600}
        },
        supports_check_mode=False
    )

    try:
        if is_update_needed(module.params['cache_file'], module.params['update_threshold_seconds']):
            repos = fetch_repos(
                github_token=module.params['github_token'],
                user_or_org=module.params['user_or_org'],
                is_org=module.params['is_org'],
                search_query=module.params['search_query']
            )

            save_repos_to_file(repos, module.params['cache_file'])
            message = 'Repository data fetched and cached successfully.'
            changed = True
        else:
            message = 'Cache file is up to date, no update needed.'
            changed = False

        with open(module.params['cache_file'], 'r', encoding="utf-8") as file:
            gh_repos = json.load(file)

        module.exit_json(changed=changed, message=message, gh_repos=gh_repos)
    except Exception as e:
        module.fail_json(msg=str(e))

def main():
    """Runs the module."""
    run_module()

if __name__ == '__main__':
    main()
