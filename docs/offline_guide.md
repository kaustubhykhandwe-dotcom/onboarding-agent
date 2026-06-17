# Offline Guide - Onboarding Agent

This guide is for students who want to get from zero setup to a pull
request on this repo without guessing the Git or GitHub steps.

## What you will do

You will:
1. Set up Git and Python
2. Create an SSH key and connect it to GitHub
3. Fork and clone this repo
4. Create a working branch
5. Run the onboarding agent locally
6. Make a change
7. Commit, push, and open a pull request

## 1) Install the basics

Make sure these are installed:

- Git
- Python 3.9 or newer
- A GitHub account
- A text editor such as VS Code

Check them from PowerShell:

```powershell
git --version
python --version
```

If `python` does not work, try:

```powershell
py --version
```

## Windows and Linux

Use the Windows PowerShell commands in the main steps if you are on
Windows.

If you are on Linux or macOS, use the same flow but switch to:

```bash
python3 --version
ssh-keygen -t ed25519 -C "your_email@example.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
cat ~/.ssh/id_ed25519.pub
ssh -T git@github.com
git clone git@github.com:YOUR_USERNAME/onboarding-agent.git
cd onboarding-agent
git checkout -b student/your-name-city
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python agent.py --dry-run
```

## 2) Create an SSH key

This is the most important step if you want to avoid HTTPS login prompts
and many `403` style GitHub errors.

Run:

```powershell
ssh-keygen -t ed25519 -C "your_email@example.com"
```

Press Enter to accept the default location:

```text
C:\Users\YOUR_NAME\.ssh\id_ed25519
```

If you want, add a passphrase. It is recommended.

## 3) Start the SSH agent

On Windows PowerShell:

```powershell
Get-Service ssh-agent
Start-Service ssh-agent
ssh-add $env:USERPROFILE\.ssh\id_ed25519
```

If `ssh-agent` is already running, `Start-Service` will simply do nothing.

## 4) Add the public key to GitHub

Copy the public key:

```powershell
Get-Content $env:USERPROFILE\.ssh\id_ed25519.pub | Set-Clipboard
```

Then on GitHub:

1. Open GitHub
2. Go to `Settings`
3. Open `SSH and GPG keys`
4. Click `New SSH key`
5. Paste the key
6. Save it

## 5) Test SSH

Run:

```powershell
ssh -T git@github.com
```

The first time, GitHub may ask you to confirm the host fingerprint.
Type `yes`.

If it works, you should see a message that you authenticated successfully.

If you get `Permission denied (publickey)`, go to the troubleshooting
section below before continuing.

## 6) Fork and clone this repo

Fork this repository on GitHub first.

Then clone your fork using SSH, not HTTPS:

```powershell
git clone git@github.com:YOUR_USERNAME/onboarding-agent.git
cd onboarding-agent
```

Check your remotes:

```powershell
git remote -v
```

You should see `git@github.com:...` URLs, not `https://...`.

If you want to keep the original repo as an upstream remote, add it now:

```powershell
git remote add upstream git@github.com:ORIGINAL_OWNER/onboarding-agent.git
git remote -v
```

## 7) Create your branch

Use one branch for your work:

```powershell
git checkout -b student/your-name-city
```

Keep the branch name short and readable.

## 8) Run the repo locally

Create and activate a virtual environment first:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Linux or macOS equivalent:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Start with the dry run:

```powershell
python agent.py --dry-run
```

If the dry run passes, set your API key and run the real agent:

```powershell
$env:GROQ_API_KEY="your-key-here"
python agent.py --employee EMP-2026-0847
```

If you want to show the compliance gate bypass demo:

```powershell
python agent.py --employee EMP-2026-0847 --no-enforcement
```

## 9) Make your change

Open these files first:

- `README.md`
- `docs/offline_guide.md`
- `docs/resources.md`
- `system_prompt.md`
- `agent.py`

Start with one small change. For example:

- improve a doc section
- adjust the onboarding prompt
- change a console label
- add a resource link

Do not edit the mock data unless the task explicitly asks for it.

## 10) Commit your work

Check what changed:

```powershell
git status
git diff
```

Stage and commit:

```powershell
git add README.md docs/offline_guide.md docs/resources.md system_prompt.md agent.py
git commit -m "Onboarding fix: update student guide and repo branding"
```

Use a meaningful commit message. Short messages like `fix` or `done`
do not help anyone review the work.

## 11) Push your branch

Push to your fork:

```powershell
git push -u origin student/your-name-city
```

If you see a `403` or permission error, jump to troubleshooting.

## 12) Open the pull request

On GitHub, open your fork and click `Compare & pull request`.

Make sure:

- base repository is the original `onboarding-agent` repo
- base branch is `main`
- compare branch is your `student/...` branch

Write a short PR description:

- what you changed
- what you tested
- any issue you fixed

## Troubleshooting

### `Permission denied (publickey)`

Your SSH key is not being used.

Check:

```powershell
ssh-add -l
git remote -v
```

Fixes:

- make sure `ssh-agent` is running
- make sure your public key is added to GitHub
- make sure the remote uses `git@github.com:...`

### `403` when pushing

This usually means one of these:

- you cloned with HTTPS instead of SSH
- you are pushing to the wrong repo
- your GitHub account does not have access to that remote

Run:

```powershell
git remote -v
```

If the URL starts with `https://`, switch it to SSH:

```powershell
git remote set-url origin git@github.com:YOUR_USERNAME/onboarding-agent.git
```

### `fatal: not a git repository`

You are not inside the cloned folder.

Run:

```powershell
Get-Location
git status
```

Move into the repo folder and try again.

### `python` is not found

Use the Python launcher:

```powershell
py --version
py agent.py --dry-run
```

### PR is pointing to the wrong branch

Check your branch name:

```powershell
git branch --show-current
```

Then confirm the PR compares your branch against `main`.

## What success looks like

At the end, you should have:

- SSH working
- the repo cloned locally
- one feature branch
- a successful dry run
- a commit with a clear message
- a pushed branch
- a pull request opened against `main`
