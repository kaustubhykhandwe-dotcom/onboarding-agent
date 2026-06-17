# Your First Task

This is the change you will make, commit, and open a pull request for. It is
small, safe, and produces a result you can see when you run the agent.

## The task: onboard a brand-new employee

Right now the agent can onboard `EMP-2026-0847` (compliance PENDING) and
`EMP-2026-0848` (also PENDING). You will add a third employee whose compliance
is already **CLEARED**, so you can watch the agent provision access without
needing human confirmation.

### Step 1 - Add the employee to the HR database

Open `data/employees.json`. Add this new record. Remember to put a comma after
the previous record's closing brace so the JSON stays valid:

    "EMP-2026-0849": {
      "employee_id": "EMP-2026-0849",
      "name": "Arjun Reddy",
      "email": "arjun.reddy@meridian.com",
      "role": "Software Engineer",
      "level": "L4",
      "department": "Platform Engineering",
      "manager_id": "EMP-2022-0103",
      "manager_name": "Vikram Nair",
      "employment_type": "fulltime",
      "location": "Hyderabad Engineering Hub",
      "start_date": "2026-06-15",
      "access_profile": {
        "github": "platform-team",
        "jira": "platform-project",
        "confluence": "platform-space",
        "slack_channels": ["platform-team", "all-engineering"]
      }
    }

### Step 2 - Add their compliance record (already CLEARED)

Open `data/compliance_state.json`. Add this record (again, mind the comma):

    "EMP-2026-0849": {
      "employee_id": "EMP-2026-0849",
      "code_of_conduct": "CLEARED",
      "data_handling_policy": "CLEARED",
      "security_guidelines": "CLEARED",
      "posh_training": "CLEARED",
      "last_updated": "2026-06-12T10:00:00Z",
      "overall_status": "CLEARED"
    }

### Step 3 - Check your JSON is valid

    python agent.py --dry-run

If you see a JSON error, you probably missed a comma or a closing brace. Fix it
before continuing.

### Step 4 - Run the agent on your new employee

    python agent.py --employee EMP-2026-0849

Because compliance is CLEARED, the agent should go straight to provisioning
access and sending the welcome notification - no human confirmation needed.
Compare this with `EMP-2026-0847`, which is PENDING and pauses to ask you.

### Step 5 - Commit and open a PR

Follow `docs/offline_guide.md` from step 10 onward. Use a clear commit message
such as:

    git commit -m "Add cleared-compliance test employee EMP-2026-0849"

In your PR description, say what you added and that you ran the agent on the new
employee successfully.

## Want to do more?

Once this works, try one of these as a second change:
- Change a console label in `agent.py` and observe the new output.
- Add one resource link to `docs/resources.md`.
- Adjust the welcome message wording in the system prompt.
