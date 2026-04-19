# 🌊 Introduction to git-flow

🇯🇵 [日本語版はこちら](FLOW_JP.md) ｜ 🇨🇳 [中文版在此](FLOW_CN.md)

This repository's workflow is based on the well-known development strategy called **git-flow**.
Understanding git-flow will help you see why the rules are structured the way they are!

---

## 🤔 What is git-flow?

**git-flow** is a set of rules for how to use Git branches when multiple people are developing together.
It was proposed by Vincent Driessen in 2010 and has been adopted by many projects worldwide.

In git-flow, each branch is given a **role**, and development follows a defined procedure.
This prevents code conflicts and confusion, enabling smooth team development.

> 💡 **git-flow is useful even when working solo!**
> Since each branch is dedicated to a specific feature, it's easy to see at a glance what each branch is for — keeping your work organized and easy to follow.
> The git-flow approach is recommended not only for team projects but also for managing your own research code.

---

## 🌿 git-flow Branch Structure

git-flow uses the following 5 types of branches.

| Branch | Role |
|---|---|
| `main` | Holds stable, released code |
| `develop` | Integrates code currently in development |
| `feature/xxx` | Used to develop individual features |
| `release/xxx` | Used for final adjustments before a release |
| `hotfix/xxx` | Used for urgent bug fixes in production |

```
main        ●─────────────────────────────────────● release
             \                                   /
hotfix        \               ●────────────────●
               \             /                /
develop         ●───────────●────────────────●
                 \         / \              /
feature           ●───────●   ●────────────●
                feature A done  feature B done
```

---

## 🔗 Mapping git-flow to This Repository

This repository applies the git-flow concept directly.

| git-flow | This Repository | Role |
|---|---|---|
| `main` | `main` | For releases and backups |
| `develop` | `develop` | For development integration |
| `feature/xxx` | `[name]_[feature]` (local) | For feature development |
| ─ | `[name]` (personal branch) | Buffer between develop and feature |

> 💡 **Key Point:** Your personal branch `[name]` acts as your own **personal version of `develop`** in git-flow terms.
> Locally, treat `[name]` as `develop` and follow the git-flow approach!

---

## 💻 Develop Locally in git-flow Style!

Your local development flow is exactly the same as the git-flow `develop` → `feature` cycle.

### Basic git-flow (Local Work)

```
[name] branch (= equivalent to develop in git-flow)
    │
    ├─── Create [name]_[feature] branch (= git-flow feature branch)
    │         │
    │         │  Develop and commit repeatedly here
    │         │
    │    Done!
    │         │
    └─── Merge back into [name] branch (= feature → develop merge)
```

### Concrete Command Example (for mtanaka)

#### 1️⃣ Starting development (create feature branch)

```bash
# Pull latest changes and create a working branch
git checkout mtanaka
git pull origin mtanaka
git checkout -b mtanaka_unet   # create feature branch
```

#### 2️⃣ During development (work and commit on feature branch)

```bash
# Repeat work and commit
git add .
git commit -m "Add UNet encoder block"
```

#### 3️⃣ When development is done (merge feature → [name])

```bash
# Go back to [name] branch (= develop) and merge
git checkout mtanaka
git merge mtanaka_unet

# Push to remote
git push origin mtanaka

# Delete feature branch (recommended)
git branch -d mtanaka_unet
```

#### 4️⃣ At a development milestone (Pull Request to develop)

From the GitHub web interface, create a Pull Request from **`mtanaka` → `develop`**.
This is the equivalent of "merging into `develop`" in git-flow!

---

## 🛠️ Installing the git-flow Library

The git-flow library lets you create, merge, and delete branches all in a single command!

### macOS

```bash
# Using Homebrew (recommended)
brew install git-flow-avh

# Using MacPorts
port install git-flow-avh
```

### Linux (Ubuntu / Debian)

```bash
sudo apt-get install git-flow
```

### Windows

If you are using Git for Windows (Git Bash), install with the following:

```bash
# Run in Git Bash
wget -q -O - --no-check-certificate \
  https://raw.github.com/petervanderdoes/gitflow-avh/develop/contrib/gitflow-installer.sh \
  install stable | bash
```

> 💡 `wget` and `util-linux` are required.

### Verify Installation

```bash
git flow version
```

If a version number is displayed, the installation was successful 🎉

---

## ⚡ Development Commands Using the git-flow Library

With the git-flow library, the manual commands from the previous section become **much simpler**!

### First: Initialize git-flow

After cloning the repository, initialize git-flow once.
You will be asked questions interactively — just **press Enter for all of them** to use the defaults.

```bash
cd welcome
git flow init
```

You will see prompts like the following (press Enter to accept all defaults):

```
Which branch should be used for bringing forth production releases?
   - develop
   - main
Branch name for production releases: [main]  ← Enter

Which branch should be used for integration of the "next release"?
   - develop
Branch name for "next release" development: [develop]  ← Enter

How to name your supporting branch prefixes?
Feature branches? [feature/]  ← Enter
Release branches? [release/]  ← Enter
Hotfix branches? [hotfix/]    ← Enter
Support branches? [support/]  ← Enter
Version tag prefix? []        ← Enter
```

> ⚠️ In this repository, `[name]` acts as `develop` in git-flow terms.
> Read git-flow's `develop` as your `[name]` branch (e.g. `mtanaka`) throughout.

---

### 🔀 Feature Branch Development Flow (for mtanaka)

#### 1️⃣ Starting development (create feature branch)

```bash
# Without git-flow (manual)
git checkout mtanaka
git checkout -b mtanaka_unet

# ✅ With git-flow (simple!)
git flow feature start unet
# → "feature/unet" branch is automatically created and checked out
```

#### 2️⃣ During development (work and commit on feature branch)

```bash
# Same as normal git commands
git add .
git commit -m "Add UNet encoder block"
```

#### 3️⃣ When development is done (merge feature → [name])

```bash
# Without git-flow (manual)
git checkout mtanaka
git merge mtanaka_unet
git branch -d mtanaka_unet

# ✅ With git-flow (simple!)
git flow feature finish unet
# → Auto-merges into develop (= mtanaka), deletes branch, and switches back — all at once!
```

#### 4️⃣ Push to remote and create Pull Request

```bash
git push origin mtanaka
```

From the GitHub web interface, create a Pull Request from **`mtanaka` → `develop`**.

---

### 📋 git-flow Command Quick Reference

| Action | Manual Command | git-flow Command |
|---|---|---|
| Create feature branch | `git checkout -b mtanaka_unet` | `git flow feature start unet` |
| Finish feature branch | `git checkout mtanaka` → `git merge` → `git branch -d` | `git flow feature finish unet` |
| List active branches | `git branch` | `git flow feature list` |

> 💡 `git flow feature finish` handles merge, branch deletion, and switching back — all in **one command**!

---

## ✅ Summary: git-flow Mapping

| Action | In git-flow Terms | In This Repository |
|---|---|---|
| Start a new feature | Create `feature` branch from `develop` | Create `[name]_[feature]` from `[name]` |
| Work in progress | Commit on `feature` branch | Commit on `[name]_[feature]` |
| Finish development | Merge `feature` → `develop` | Merge `[name]_[feature]` → `[name]` |
| Share with the team | Pull Request to `develop` | Pull Request `[name]` → `develop` |
| Sync latest changes | Merge `develop` into `feature` | Merge `develop` into `[name]` via Pull Request |

---

## 🚨 Important Rules to Follow

> [!WARNING]
> Do **NOT** push directly to the `develop` branch!
> Always create a **Pull Request** from your `[name]` branch.

This rule also applies in git-flow. Since `develop` is everyone's shared integration branch,
pushing directly can cause conflicts with others' work or introduce unreviewed,
unfinished code into the shared codebase.

---

## 📚 Want to Learn More?

Check out these resources for more details on git-flow.

- [Atlassian: Gitflow Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)
- [git-flow cheatsheet](https://danielkummer.github.io/git-flow-cheatsheet/index.html)
- [Original post (English): A successful Git branching model](https://nvie.com/posts/a-successful-git-branching-model/)
