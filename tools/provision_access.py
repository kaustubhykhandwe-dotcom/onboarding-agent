"""
provision_access stub
Pre-built for the Onboarding Agent session.
Do not modify during the live build.

Simulates provisioning access in GitHub, JIRA, Confluence, and Slack.
Always succeeds. Prints to terminal so the audience can see what was provisioned.
"""

import json
from datetime import datetime


def provision_access(employee_id: str, access_profile: dict) -> dict:
    """
    Provision system access for the employee.

    In production, this would call:
      - GitHub Org API to add to teams
      - JIRA REST API to add to projects
      - Confluence API to grant space access
      - Slack API to add to channels

    For the session, this just prints what would be provisioned and returns success.

    Args:
        employee_id: the employee ID to provision access for
        access_profile: dict of systems and their access levels

    Returns:
        dict with status, provisioned items, and timestamp
    """
    timestamp = datetime.now().isoformat() + "Z"

    print(f"\n  == PROVISIONING ACCESS for {employee_id} ==")
    print(f"     GitHub:     {access_profile.get('github', 'none')}")
    print(f"     JIRA:       {access_profile.get('jira', 'none')}")
    print(f"     Confluence: {access_profile.get('confluence', 'none')}")
    slack = access_profile.get('slack_channels', [])
    print(f"     Slack:      {', '.join(slack) if slack else 'none'}")
    print(f"     Timestamp:  {timestamp}")
    print(f"  == ACCESS PROVISIONED ==\n")

    return {
        "status": "SUCCESS",
        "employee_id": employee_id,
        "provisioned": {
            "github": access_profile.get('github'),
            "jira": access_profile.get('jira'),
            "confluence": access_profile.get('confluence'),
            "slack_channels": access_profile.get('slack_channels', [])
        },
        "timestamp": timestamp
    }


if __name__ == '__main__':
    test_profile = {
        "github": "platform-team",
        "jira": "platform-project",
        "confluence": "platform-space",
        "slack_channels": ["platform-team", "onboarding-agent-hyderabad"]
    }
    result = provision_access("EMP-2026-0847", test_profile)
    print(json.dumps(result, indent=2))
