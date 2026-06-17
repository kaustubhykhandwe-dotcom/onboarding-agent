# Core Concepts

Read this before you read `agent.py`. Five short ideas explain everything this
repo does.

## 1. What is an AI agent?

A normal program follows fixed steps you wrote in advance. An **AI agent** uses
a language model (the "brain") to decide what to do next, one step at a time,
based on what it has seen so far. It can choose to call a tool, ask a human, or
declare the job finished. In this repo the agent's job is to onboard a new
employee.

## 2. What is a system prompt?

The **system prompt** is the instruction sheet we give the language model. It
defines the agent's role, its goal, the tools it may use, and the rules it must
never break. In this repo it lives in `system_prompt.md`. Read it - every rule
there is something the agent is expected to obey.

## 3. What is a tool?

A language model can only produce text. To actually *do* something - look up an
employee, grant access, send an email - it must call a **tool**: a normal
function we wrote. The agent decides *which* tool to call and *what arguments*
to pass; our code runs the function and hands the result back. This repo has
four tools (see `system_prompt.md`).

## 4. What is the ReAct loop?

**ReAct** = **Rea**son + **Act**. The agent repeats a simple loop:

1. **Reason** - the model thinks about what to do next (the `THOUGHT`).
2. **Act** - it calls a tool, asks a human, or completes (the `ACTION`).
3. **Observe** - it reads the result of that action (the `OBSERVATION`).
4. **Repeat** - the result is added to the history and the loop runs again.

The loop stops when the agent says it is `complete` or when it hits a step
limit. You can watch each pass print to your terminal when you run the agent.

## 5. Why the rules matter

This agent works in a financial company, so it has hard rules - for example, it
must never grant system access before compliance checks pass. A correct agent
is not just one that "runs"; it is one that follows the rules even when the
model is tempted to skip them. Try `python agent.py --employee EMP-2026-0847
--no-enforcement` to see what goes wrong when a rule is removed.

## Where to go next

- Read `system_prompt.md` (the agent's rules).
- Read `docs/scenario_brief.md` (the worked example).
- Then read `agent.py` from top to bottom and trace one loop by hand.
