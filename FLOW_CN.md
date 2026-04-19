# 🌊 git-flow 入门推荐

🇯🇵 [日本語版はこちら](FLOW_JP.md) ｜ 🇺🇸 [English version here](FLOW_EN.md)

本仓库的操作规范以著名的开发策略 **git-flow** 为基础。
理解 git-flow，就能明白为什么要这样设计操作规范！

---

## 🤔 什么是 git-flow？

**git-flow** 是一套多人协作使用 Git 时的「分支使用规则」。
由 Vincent Driessen 于 2010 年提出，被众多项目所采用。

git-flow 为每个分支赋予**角色**，并按照规定的流程推进开发。
这样可以防止代码混乱和冲突，实现顺畅的团队协作。

> 💡 **即使单人开发，git-flow 也同样有效！**
> 由于每个分支专注于一项功能，可以一眼看清每个分支的用途，让工作内容井井有条、一目了然。
> git-flow 的思路不仅适用于团队项目，在管理个人研究代码时同样推荐使用。

---

## 🌿 git-flow 的分支结构

git-flow 使用以下 5 种分支。

| 分支 | 作用 |
|---|---|
| `main` | 存放稳定的已发布代码 |
| `develop` | 集成当前开发中的代码 |
| `feature/xxx` | 用于开发各项功能 |
| `release/xxx` | 发布前的最终调整 |
| `hotfix/xxx` | 修复生产环境的紧急 Bug |

```
main        ●─────────────────────────────────────● 发布
             \                                   /
hotfix        \               ●────────────────●
               \             /                /
develop         ●───────────●────────────────●
                 \         / \              /
feature           ●───────●   ●────────────●
                功能A完成       功能B完成
```

---

## 🔗 git-flow 与本仓库的对应关系

本仓库直接运用了 git-flow 的思路。

| git-flow | 本仓库 | 作用 |
|---|---|---|
| `main` | `main` | 用于发布和备份 |
| `develop` | `develop` | 用于开发集成 |
| `feature/xxx` | `[name]_[feature]`（本地） | 用于功能开发 |
| ─ | `[name]`（个人分支） | develop 与 feature 之间的缓冲 |

> 💡 **要点：** 你的个人分支 `[name]` 相当于 git-flow 中的**个人版 `develop`**。
> 在本地开发时，请将 `[name]` 视为 `develop`，按照 git-flow 的思路进行开发！

---

## 💻 本地开发采用 git-flow 风格！

本地的开发流程与 git-flow 中 `develop` → `feature` 的流程完全相同。

### git-flow 基本流程（本地操作）

```
[name] 分支（= 相当于 git-flow 中的 develop）
    │
    ├─── 创建 [name]_[feature] 分支（= git-flow 的 feature 分支）
    │         │
    │         │  在此反复开发和提交
    │         │
    │    开发完成！
    │         │
    └─── 合并回 [name] 分支（= feature → develop 的合并）
```

### 具体命令示例（以 mtanaka 为例）

#### 1️⃣ 开始开发时（创建 feature 分支）

```bash
# 先拉取最新内容，再创建工作分支
git checkout mtanaka
git pull origin mtanaka
git checkout -b mtanaka_unet   # 创建 feature 分支
```

#### 2️⃣ 开发过程中（在 feature 分支上开发和提交）

```bash
# 反复进行开发和提交
git add .
git commit -m "Add UNet encoder block"
```

#### 3️⃣ 完成开发时（将 feature 合并到 [name]）

```bash
# 切回 [name] 分支（= develop）并合并
git checkout mtanaka
git merge mtanaka_unet

# push 到远程
git push origin mtanaka

# 删除 feature 分支（推荐）
git branch -d mtanaka_unet
```

#### 4️⃣ 完成一阶段开发时（向 develop 创建 Pull Request）

在 GitHub 网页界面创建 **`mtanaka` → `develop`** 的 Pull Request。
这就相当于 git-flow 中「合并到 `develop`」的操作！

---

## 🛠️ 安装 git-flow 工具库

使用 git-flow 工具库，可以用一条命令完成分支的创建、合并和删除！

### macOS

```bash
# 使用 Homebrew（推荐）
brew install git-flow-avh

# 使用 MacPorts
port install git-flow-avh
```

### Linux（Ubuntu / Debian）

```bash
sudo apt-get install git-flow
```

### Windows

使用 Git for Windows（Git Bash）时，可通过以下方式安装：

```bash
# 在 Git Bash 中执行
wget -q -O - --no-check-certificate \
  https://raw.github.com/petervanderdoes/gitflow-avh/develop/contrib/gitflow-installer.sh \
  install stable | bash
```

> 💡 需要 `wget` 和 `util-linux`。

### 确认安装

```bash
git flow version
```

显示版本号即表示安装成功 🎉

---

## ⚡ 使用 git-flow 工具库的开发命令示例

使用 git-flow 工具库后，前面介绍的手动命令会变得**简洁很多**！

### 首先：初始化 git-flow

克隆仓库后，需要进行一次初始化。
会以交互形式提问，**全部按 Enter** 使用默认值即可。

```bash
cd welcome
git flow init
```

执行后会显示如下提问（全部按 Enter 接受默认值）：

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

> ⚠️ 本仓库中 `[name]` 分支相当于 git-flow 的 `develop`，
> 请将 git-flow 中的 `develop` 理解为你的 `[name]` 分支（例：`mtanaka`）。

---

### 🔀 使用 feature 分支的开发流程（以 mtanaka 为例）

#### 1️⃣ 开始开发时（创建 feature 分支）

```bash
# 不使用 git-flow（传统方式）
git checkout mtanaka
git checkout -b mtanaka_unet

# ✅ 使用 git-flow（简洁！）
git flow feature start unet
# → 自动创建 "feature/unet" 分支并切换过去
```

#### 2️⃣ 开发过程中（在 feature 分支上开发和提交）

```bash
# 与普通 git 命令相同
git add .
git commit -m "Add UNet encoder block"
```

#### 3️⃣ 完成开发时（将 feature 合并到 [name]）

```bash
# 不使用 git-flow（传统方式）
git checkout mtanaka
git merge mtanaka_unet
git branch -d mtanaka_unet

# ✅ 使用 git-flow（简洁！）
git flow feature finish unet
# → 自动合并到 develop（= mtanaka）、删除分支、切换回 develop，一步完成！
```

#### 4️⃣ push 到远程并创建 Pull Request

```bash
git push origin mtanaka
```

在 GitHub 网页界面创建 **`mtanaka` → `develop`** 的 Pull Request。

---

### 📋 git-flow 命令速查表

| 操作 | 传统命令 | git-flow 命令 |
|---|---|---|
| 创建 feature 分支 | `git checkout -b mtanaka_unet` | `git flow feature start unet` |
| 完成 feature 分支 | `git checkout mtanaka` → `git merge` → `git branch -d` | `git flow feature finish unet` |
| 查看分支列表 | `git branch` | `git flow feature list` |

> 💡 `git flow feature finish` 可以一条命令完成合并、删除分支、切换回原分支，非常方便！

---

## ✅ 用 git-flow 思路整理一下！

| 操作 | git-flow 的表达 | 本仓库的操作 |
|---|---|---|
| 开始开发新功能 | 从 `develop` 创建 `feature` 分支 | 从 `[name]` 创建 `[name]_[feature]` |
| 开发过程中 | 在 `feature` 分支上提交 | 在 `[name]_[feature]` 上提交 |
| 完成开发 | `feature` → `develop` 合并 | `[name]_[feature]` → `[name]` 合并 |
| 分享给团队 | 向 `develop` 创建 Pull Request | `[name]` → `develop` 的 Pull Request |
| 同步最新内容 | 将 `develop` merge 到 `feature` | 通过 Pull Request 将 `develop` 合并到 `[name]` |

---

## 🚨 请务必遵守的重要规则

> [!WARNING]
> **请勿**直接 push 到 `develop` 分支！
> 必须从 `[name]` 分支创建 **Pull Request**。

这在 git-flow 中也是同样的规则。`develop` 是所有人共用的集成分支，
如果直接 push，可能会与他人的工作产生冲突，
或将未经审查的未完成代码混入共享代码库，非常危险。

---

## 📚 想了解更多？

以下资源可以帮助你深入了解 git-flow。

- [Atlassian: Gitflow 工作流（英文）](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)
- [git-flow cheatsheet（日文版）](https://danielkummer.github.io/git-flow-cheatsheet/index.ja_JP.html)
- [原始文章（英文）: A successful Git branching model](https://nvie.com/posts/a-successful-git-branching-model/)
