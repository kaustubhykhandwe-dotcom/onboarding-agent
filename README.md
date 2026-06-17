# Onboarding Agent

Beginner-friendly workshop repo for building an onboarding AI agent.
The goal is to help students learn the full path from prompt to working
agent: read the scenario, understand the tools, run the code, and open a
pull request with a real change.

## Start here

1. Read [docs/concepts.md](docs/concepts.md) - what an AI agent is
2. Read [docs/scenario_brief.md](docs/scenario_brief.md) - the worked example
3. Read [docs/offline_guide.md](docs/offline_guide.md) - setup, Git, and PR steps
4. Read [docs/resources.md](docs/resources.md)
5. Skim [system_prompt.md](system_prompt.md) and [agent.py](agent.py)
6. Run `python agent.py --dry-run`
7. Do the exercise in [docs/first_task.md](docs/first_task.md) and open a PR

## What this repo demonstrates

The sample agent completes onboarding in four steps:
1. Retrieve the employee profile
2. Check compliance acknowledgement status
3. Provision system access only after compliance is cleared
4. Send a welcome notification

The implementation uses a small, transparent ReAct loop so students can
see the control flow without a framework hiding it.

## Quick start

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python agent.py --dry-run
python agent.py --employee EMP-2026-0847
python agent.py --employee EMP-2026-0847 --no-enforcement
```

Linux or macOS shell:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python agent.py --dry-run
python agent.py --employee EMP-2026-0847
python agent.py --employee EMP-2026-0847 --no-enforcement
```

The full run requires a `GROQ_API_KEY`. Get one free at
<https://console.groq.com> (sign up, then create an API key). The free tier is
enough for this workshop. The offline guide walks through the setup, virtual
environment, API key, and GitHub pull request flow step by step.

## Repo layout

```
agent.py              - ReAct loop, tools, CLI
system_prompt.md      - agent rules and onboarding policy
docs/offline_guide.md - beginner setup guide from SSH to PR
docs/resources.md     - curated learning links
tools/                - stubbed side-effect functions
data/                 - mock employee and compliance data
```

## Notes for students

This repo is a teaching scaffold. The onboarding scenario is the worked
example, but the real lesson is how prompt instructions, tool calls, and
GitHub workflow fit together when you build an agent end to end.
