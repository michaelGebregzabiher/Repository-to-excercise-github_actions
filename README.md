# github_actions
This is a practice repo for CI/CD, workflow orchestration

# Architecture(simple mental model how Githubactions workflow works):
Your Repo (GitHub)
        ↓
Trigger Event (push / PR)
        ↓
GitHub Actions Orchestrator
        ↓
Creates VM (Ubuntu / Windows)
        ↓
Runs your steps
        ↓
Destroys VM