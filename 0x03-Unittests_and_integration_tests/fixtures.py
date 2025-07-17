#!/usr/bin/env python3
# fixtures.py
 
TEST_PAYLOAD = [
    {
        "org_payload": {
            "login": "google",
            "repos_url": "https://api.github.com/orgs/google/repos",
            "id": 1,
        },
        "repos_payload": [
            {"id": 1, "name": "repo1", "license": {"key": "apache-2.0"}},
            {"id": 2, "name": "repo2", "license": {"key": "mit"}},
            {"id": 3, "name": "repo3", "license": {"key": "apache-2.0"}},
        ],
        "expected_repos": ["repo1", "repo2", "repo3"],
        "apache2_repos": ["repo1", "repo3"],
    }
]
