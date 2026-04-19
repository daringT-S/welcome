# 🐙 GitHub Practice

🇯🇵 [日本語版はこちら](README.md) ｜ 🇨🇳 [中文版在此](README_CN.md) ｜ 🌊 [Introduction to git-flow](FLOW_EN.md)

This repository is for practicing the GitHub workflow used in our lab.

> [!IMPORTANT]
> Before you start, please read the **[GitHub Operation Rules](RULES_EN.md)** first.

## Branch Structure

| Branch Name | Role |
|---|---|
| `main` | For releases and backups (do not touch directly) |
| `develop` | For integration (do not push directly) |
| `[name]` | Personal branch for each student e.g. `mtanaka` |
| `[name]_[feature]` | Feature development branch e.g. `mtanaka_func` |

---

## 📝 Task Overview

1. Create `func_[name].py` and implement your function
2. Add code to `main.py` to call your function
3. Create a Pull Request following the correct branch workflow

---

## 🚀 Steps

### Step 1 : Create your `[name]` branch (Web)

Create your personal branch from `develop` on the GitHub web interface.

1. Open the repository page
2. Click the branch switcher menu (showing `develop` in the top left)
3. Type your name in the text box (e.g. `mtanaka`)
4. Click `Create branch: mtanaka from develop`

---

### Step 2 : Clone the `[name]` branch of the repository locally

```bash
git clone -b [name] --single-branch git@github.com:visionimageprocessing/welcome.git
cd welcome/src
```

> 💡 Organization: `visionimageprocessing`, Repository: `welcome`
> 💡 Replace `[name]` with your own name

---

### Step 3 : Create the `[name]_[feature]` branch (Local)

```bash
git pull origin mtanaka:mtanaka
git checkout mtanaka
git checkout -b mtanaka_func
```

---

### Step 4 : Create `func_[name].py`

On the `[name]_[feature]` branch, create a new file `func_[name].py` and implement your function.

**Filename:** `func_mtanaka.py`

```python
def func_mtanaka():
    print("Welcome to Vision and Image Processing lab.!")

if __name__ == "__main__":
    func_mtanaka()
```

> 💡 Replace `[name]` with your own name (e.g. `mtanaka` → `func_mtanaka.py`)

---

### Step 5 : Commit your changes

```bash
git add func_mtanaka.py
git commit -m "Add func_mtanaka"
```

---

### Step 6 : Merge into the local `[name]` branch and push to the remote `[name]` branch

First, merge your changes into the local `[name]` branch.

```bash
git checkout mtanaka
git merge mtanaka_func
```

Then, push to the remote `[name]` branch.

```bash
git push origin mtanaka
```

---

### Step 7 : Delete the `[name]_[feature]` branch (optional)

It is recommended to delete the `[name]_[feature]` branch after development is complete.

```bash
# To delete the local branch
git checkout mtanaka
git branch -d mtanaka_func
```

> 💡 You can proceed without deleting, but it is recommended to keep branches tidy

---

### Step 8 : Sync `[name]` branch with the latest `develop` (Web + Local)

Before starting the next development task, pull the latest changes from `develop` into your `[name]` branch.
Nothing may happen in this operation, but please do it as practice.

**Web:** Create a Pull Request from `develop` → `mtanaka` on the GitHub web interface and merge it.

1. Open the repository page on GitHub
2. Click `Compare & pull request`
3. Verify the following settings

| Field | Setting |
|---|---|
| base | `mtanaka` |
| compare | `develop` |

4. Enter a title and description, then click `Create pull request`
5. If there are no issues, click `Merge pull request` to merge

**Local:** After merging, update your local `mtanaka` branch.

```bash
git checkout mtanaka
git pull origin mtanaka
```

---

### Step 9 : Create a new `[name]_[feature]` branch (Local)

```bash
git checkout mtanaka
git checkout -b mtanaka_main
```

---

### Step 10 : Edit `main.py`

Add code to `main.py` to import and call your function.

**Filename:** `main.py`

```python
from func_mtanaka import func_mtanaka

func_mtanaka()
```

> 💡 If other students' code is already in the file, do not remove it — only add your own lines

---

### Step 11 : Commit your changes

```bash
git add main.py
git commit -m "Add func_mtanaka to main.py"
```

---

### Step 12 : Merge into the local `[name]` branch and push to the remote `[name]` branch

First, merge your changes into the local `[name]` branch.

```bash
git checkout mtanaka
git merge mtanaka_main
```

Then, push to the remote `[name]` branch.

```bash
git push origin mtanaka
```

---

### Step 13 : Delete the `[name]_[feature]` branch (optional)

```bash
# To delete the local branch
git checkout mtanaka
git branch -d mtanaka_main
```

---

### Step 14 : Create a Pull Request to `develop`

Create a Pull Request from the GitHub web interface.

1. Open the repository page on GitHub
2. Click `Compare & pull request`
3. Verify the following settings

| Field | Setting |
|---|---|
| base | `develop` |
| compare | `mtanaka` |

4. Enter a title and description, then click `Create pull request`
5. Wait for the repository administrator to merge

> [!WARNING]
> Do NOT push directly to the `dev