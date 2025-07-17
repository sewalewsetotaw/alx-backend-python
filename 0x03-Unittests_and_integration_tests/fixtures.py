#!/usr/bin/env python3
# fixtures.py
 
ORG_PAYLOAD = {
    "login": "google",
    "repos_url": "https://api.github.com/orgs/google/repos",
    "id": 1,
}

REPOS_PAYLOAD = [
    {"id": 1, "name": "repo1", "license": {"key": "apache-2.0"}},
    {"id": 2, "name": "repo2", "license": {"key": "mit"}},
    {"id": 3, "name": "repo3", "license": {"key": "apache-2.0"}},
]

EXPECTED_REPOS = ["repo1", "repo2", "repo3"]
APACHE2_REPOS = ["repo1", "repo3"]

TEST_PAYLOAD = [
    {
        "org_payload": ORG_PAYLOAD,
        "repos_payload": REPOS_PAYLOAD,
        "expected_repos": EXPECTED_REPOS,
        "apache2_repos": APACHE2_REPOS,
    }
]
