# 🐙 GitHub 操作规范

## 分支结构

| 分支名 | 作用 |
|---|---|
| `main` | 用于发布和备份（请勿直接修改）|
| `develop` | 用于开发集成（请勿直接 push）|
| `[name]` | 学生个人分支（远程管理）|
| `[name]_[feature]` | 功能开发分支 |

**示例：**

| 分支名 | 说明 |
|---|---|
| `mtanaka` | 田中的个人分支 |
| `mtanaka_unet` | 田中的 UNet 开发分支 |


---
## 要点

> [!WARNING]
> 请勿直接 push 到 `develop` 分支！

1. 创建远程 `[name]` 分支
2. 从 `develop` pull 到远程 `[name]` 分支，保持最新状态
3. 将远程 `[name]` 分支 pull 到本地 `[name]` 分支
4. 将本地 `[name]` 分支 push 到远程 `[name]` 分支
5. 从远程 `[name]` 分支向 `develop` 分支创建 **Pull Request**

本地 `[name]` 分支的开发方式由你自己决定。


---

## 📁 新建仓库时

1. 创建 `main` 分支
2. 从 `main` 创建 `develop` 分支
3. 将 `develop` 设为默认分支

---

## 🙋 学生加入仓库时

1. 从 `develop` 创建 `[name]` 分支（远程）

```
例）mtanaka
```

---

## 💻 学生开始开发时

1. 从 `develop` pull 到远程 `[name]` 分支，保持最新状态
2. 将远程 `[name]` 分支 pull 到本地 `[name]` 分支
3. 从本地 `[name]` 分支创建本地 `[name]_[feature]` 分支
4. 在本地 `[name]_[feature]` 分支上进行开发

---

## ✅ 学生完成开发时

1. 将本地 `[name]_[feature]` 分支 merge 到本地 `[name]` 分支
2. 将本地 `[name]` 分支 push 到远程 `[name]` 分支
3. 删除本地 `[name]_[feature]` 分支

---

## 🔀 学生完成一阶段开发时

1. 从远程 `[name]` 分支向 `develop` 分支创建 **Pull Request**
2. 仓库管理员审查并合并 Pull Request

> [!WARNING]
> 请勿直接 push 到 `develop` 分支！必须通过 Pull Request 提交！

---
