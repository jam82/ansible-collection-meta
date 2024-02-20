"""Lookup plugin to get the latest release version of a GitHub repo."""

import requests
from ansible.errors import AnsibleError
from ansible.plugins.lookup import LookupBase

DOCUMENTATION = """
    name: github_version
    author: Jonas Mauer
    version_added: "0.1.0"
    short_description: get the latest release version of a GitHub repo
    description:
        - This lookup returns the latest release version of a specified GitHub repository.
    options:
      github_token:
        description: GitHub personal access token for authentication.
        required: True
      user_or_org:
        description: The GitHub user or organization name.
        required: True
      repo:
        description: The repository name.
        required: True
    requirements:
        - requests
"""

class LookupModule(LookupBase):
    """Lookup plugin to get the latest release version of a GitHub repo."""
    def run(self, terms, variables=None, **kwargs):

        if not isinstance(terms, list) or len(terms) != 3:
            raise AnsibleError(
                "github_version lookup expects a list of three items:" + \
                     " github_token, user_or_org, and repo."
            )

        github_token, user_or_org, repo = terms

        headers = {
            "Authorization": f"token {github_token}",
            "Accept": "application/vnd.github.v3+json",
        }

        url = f"https://api.github.com/repos/{user_or_org}/{repo}/releases/latest"

        response = requests.get(url, headers=headers, timeout=5)

        # Check for rate limiting before proceeding
        if response.status_code == 403 and "rate limit exceeded" in response.text.lower():
            raise AnsibleError("GitHub API rate limit exceeded.")

        if response.status_code == 404:
            # Repository or releases not found, return '0.0.0'
            return ['0.0.0']

        if response.status_code != 200:
            raise AnsibleError(
                f"GitHub API responded with status code {response.status_code}: {response.text}"
            )

        release_data = response.json()
        return [release_data.get('tag_name', '0.0.0')]
