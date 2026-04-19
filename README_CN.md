# 🐙 GitHub 操作练习

🇯🇵 [日本語版はこちら](README.md) ｜ 🇺🇸 [English version here](README_EN.md) ｜ 🌊 [git-flow 入门推荐](FLOW_CN.md)

本仓库用于练习研究室的 GitHub 操作流程。

> [!IMPORTANT]
> 开始操作前，请务必先阅读 **[GitHub 操作规范](RULES_CN.md)**。

## 分支结构

| 分支名 | 作用 |
|---|---|
| `main` | 用于发布和备份（请勿直接修改）|
| `develop` | 用于开发集成（请勿直接 push）|
| `[name]` | 学生个人分支 例）`mtanaka` |
| `[name]_[feature]` | 功能开发分支 例）`mtanaka_func` |

---

## 📝 任务概要

1. 创建 `func_[name].py`，实现自己的函数
2. 在 `main.py` 中添加调用自己函数的代码
3. 按照正确的分支流程创建 Pull Request

---

## 🚀 操作步骤

### Step 1 : 创建 `[name]` 分支（Web 操作）

在 GitHub 网页界面上，从 `develop` 分支创建自己的个人分支。

1. 打开仓库页面
2. 点击分支切换菜单（左上角显示 `develop`）
3. 在文本框中输入自己的名字（例：`mtanaka`）
4. 点击 `Create branch: mtanaka from develop`

---

### Step 2 : 将仓库的 `[name]` 分支克隆到本地

```bash
git clone -b [name] --single-branch git@github.com:visionimageprocessing/welcome.git
cd welcome/src
```

> 💡 Organization 名称为 `visionimageprocessing`，仓库名称为 `welcome`
> 💡 将 `[name]` 替换为自己的名字

---

### Step 3 : 创建 `[name]_[feature]` 分支（本地操作）

```bash
git pull origin mtanaka:mtanaka
git checkout mtanaka
git checkout -b mtanaka_func
```

---

### Step 4 : 创建 `func_[name].py`

在 `[name]_[feature]` 分支上新建 `func_[name].py`，并实现自己的函数。

**文件名：** `func_mtanaka.py`

```python
def func_mtanaka():
    print("Welcome to Vision and Image Processing lab.!")

if __name__ == "__main__":
    func_mtanaka()
```

> 💡 将 `[name]` 替换为自己的名字（例：`mtanaka` → `func_mtanaka.py`）

---

### Step 5 : 提交开发内容

```bash
git add func_mtanaka.py
git commit -m "Add func_mtanaka"
```

---

### Step 6 : 合并到本地 `[name]` 分支并 push 到远程 `[name]` 分支

首先，将更改合并到本地 `[name]` 分支。

```bash
git checkout mtanaka
git merge mtanaka_func
```

然后，push 到远程 `[name]` 分支。

```bash
git push origin mtanaka
```

---

### Step 7 : 删除 `[name]_[feature]` 分支（可选）

建议在开发完成后删除 `[name]_[feature]` 分支。

```bash
# 删除本地分支
git checkout mtanaka
git branch -d mtanaka_func
```

> 💡 不删除也可以继续下一步开发，但建议保持分支整洁

---

### Step 8 : 将 `[name]` 分支与最新的 `develop` 同步（Web 操作 + 本地操作）

在开始下一个开发任务之前，将 `develop` 的最新内容合并到 `[name]` 分支。
此次操作可能不会产生任何变化，但请作为练习进行操作。

**Web 操作：** 在 GitHub 网页界面创建 `develop` → `mtanaka` 的 Pull Request 并合并。

1. 打开 GitHub 仓库页面
2. 点击 `Compare & pull request`
3. 确认以下设置

| 项目 | 设置 |
|---|---|
| base | `mtanaka` |
| compare | `develop` |

4. 输入标题和说明，点击 `Create pull request`
5. 确认无误后点击 `Merge pull request` 进行合并

**本地操作：** 合并后，将本地 `mtanaka` 分支更新到最新。

```bash
git checkout mtanaka
git pull origin mtanaka
```

---

### Step 9 : 创建新的 `[name]_[feature]` 分支（本地操作）

```bash
git checkout mtanaka
git checkout -b mtanaka_main
```

---

### Step 10 : 编辑 `main.py`

在 `main.py` 中添加 import 并调用自己函数的代码。

**文件名：** `main.py`

```python
from func_mtanaka import func_mtanaka

func_mtanaka()
```

> 💡 如果文件中已有其他同学的代码，请勿删除，只添加自己的代码行

---

### Step 11 : 提交开发内容

```bash
git add main.py
git commit -m "Add func_mtanaka to main.py"
```

---

### Step 12 : 合并到本地 `[name]` 分支并 push 到远程 `[name]` 分支

首先，将更改合并到本地 `[name]` 分支。

```bash
git checkout mtanaka
git merge mtanaka_main
```

然后，push 到远程 `[name]` 分支。

```bash
git push origin mtanaka
```

---

### Step 13 : 删除 `[name]_[feature]` 分支（可选）

```bash
# 删除本地分支
git checkout mtanaka
git branch -d mtanaka_main
```

---

### Step 14 : 向 `develop` 创建 Pull Request

在 GitHub 网页界面创建 Pull Request。

1. 打开 GitHub 仓库页面
2. 点击 `Compare & pull request`
3. 确认以下设置

| 项目 | 设置 |
|---|---|
| base | `develop` |
| compare | `mtanaka` |

4. 输入标题和说明，点击 `Create pull request`
5. 等待仓库管理员合并

> [!WARNING]
> 请勿直接 push 到 `develop` 