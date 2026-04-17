# 🐙 GitHub Operation Rules

## Branch Structure

| Branch Name | Role |
|---|---|
| `main` | For releases and backups (do not touch directly) |
| `develop` | For integration (do not push directly) |
| `[name]` | Personal branch for each student (managed remotely) |
| `[name]_[feature]` | Feature development branch |

**Examples:**

| Branch Name | Description |
|---|---|
| `mtanaka` | Tanaka's personal branch |
| `mtanaka_unet` | Tanaka's UNet development branch |


---
## Key Points

> [!WARNING]
> Do NOT push directly to the `develop` branch!

1. Create the remote `[name]` branch
2. Pull from `develop` into the remote `[name]` branch to keep it up to date
3. Pull the remote `[name]` branch to the local `[name]` branch
4. Push the local `[name]` branch to the remote `[name]` branch
5. Create a **Pull Request** from the remote `[name]` branch to `develop`

How you develop on the local `[name]` branch is up to you.


---

## 📁 When Creating a New Repository

1. Create the `main` branch
2. Create the `develop` branch from `main`
3. Set `develop` as the default branch

---

## 🙋 When a Student Joins the Repository

1. Create a `[name]` branch (remote) from `develop`

```
e.g.) mtanaka
```

---

## 💻 When a Student Starts Development

1. Pull from `develop` into the remote `[name]` branch to keep it up to date
2. Pull the remote `[name]` branch to the local `[name]` branch
3. Create a local `[name]_[feature]` branch from the local `[name]` branch
4. Develop on the local `[name]_[feature]` branch

---

## ✅ When a Student Finishes Development

1. Merge the local `[name]_[feature]` branch into the local `[name]` branch
2. Push the local `[name]` branch to the remote `[name]` branch
3. Delete the local `[name]_[feature]` branch

---

## 🔀 When a Student Reaches a Development Milestone

1. Create a **Pull Request** from the remote `[name]` branch to `develop`
2. The repository administrator reviews and merges the Pull Request

> [!WARNING]
> Do NOT push directly to the `develop` branch!

---
