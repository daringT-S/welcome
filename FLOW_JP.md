# 🌊 git-flow のすすめ

🇺🇸 [English version here](FLOW_EN.md) ｜ 🇨🇳 [中文版在此](FLOW_CN.md)

本リポジトリの運用ルールは、有名な開発戦略 **git-flow** の考え方をベースにしています。
git-flow を理解すると、なぜこのような運用ルールになっているのかがよくわかります！

---

## 🤔 git-flow とは？

**git-flow** とは、複数人でGitを使って開発するときの「ブランチの使い方ルール」です。
2010年に Vincent Driessen 氏が提唱し、多くのプロジェクトで採用されています。

git-flow では、ブランチに **役割** を与え、決められた手順で開発を進めます。
これにより、コードの混乱・コンフリクトを防ぎ、スムーズなチーム開発ができるようになります。

> 💡 **1人で開発する場合でも有効です！**
> ブランチごとに機能がまとまるため、「このブランチでは何をしているか」が一目でわかり、作業内容の整理に役立ちます。
> チーム開発だけでなく、個人の研究コードの管理にも git-flow の考え方はおすすめです。

---

## 🌿 git-flow のブランチ構成

git-flow では、以下の5種類のブランチを使い分けます。

| ブランチ | 役割 |
|---|---|
| `main` | リリース済みの安定したコードを置く場所 |
| `develop` | 開発中のコードを統合する場所 |
| `feature/xxx` | 個々の機能を開発する場所 |
| `release/xxx` | リリース前の最終調整をする場所 |
| `hotfix/xxx` | 本番環境の緊急バグを修正する場所 |

```
main        ●─────────────────────────────────────● リリース
             \                                   /
hotfix        \               ●────────────────●
               \             /                /
develop         ●───────────●────────────────●
                 \         / \              /
feature           ●───────●   ●────────────●
                 機能A完成     機能B完成
```

---

## 🔗 本リポジトリの運用と git-flow の対応

本リポジトリでは、git-flow の考え方をそのまま活用しています。

| git-flow | 本リポジトリ | 役割 |
|---|---|---|
| `main` | `main` | リリース・バックアップ用 |
| `develop` | `develop` | 開発統合用 |
| `feature/xxx` | `[name]_[feature]`（ローカル） | 機能開発用 |
| ─ | `[name]`（個人ブランチ） | developとfeatureの中間バッファ |

> 💡 **ポイント：** あなたの個人ブランチ `[name]` は、git-flow でいう **`develop` の個人版** として機能します。
> ローカルでは `[name]` を `develop` に見立てて、git-flow の考え方で開発を進めましょう！

---

## 💻 ローカル開発は git-flow スタイルで！

ローカルでの開発フローは、まさに git-flow の `develop` → `feature` の流れと同じです。

### git-flow の基本フロー（ローカル作業）

```
[name] ブランチ（= git-flow の develop にあたる）
    │
    ├─── [name]_[feature] ブランチを作成（= git-flow の feature ブランチ）
    │         │
    │         │  ここで機能開発・コミットを繰り返す
    │         │
    │    開発完了！
    │         │
    └─── [name] ブランチにマージ（= feature → develop のマージ）
```

### 具体的なコマンド例（mtanaka の場合）

#### 1️⃣ 開発を始めるとき（feature ブランチ作成）

```bash
# [name] ブランチを最新にしてから作業ブランチを作る
git checkout mtanaka
git pull origin mtanaka
git checkout -b mtanaka_unet   # feature ブランチ作成
```

#### 2️⃣ 開発中（feature ブランチで作業・コミット）

```bash
# 作業・コミットを繰り返す
git add .
git commit -m "Add UNet encoder block"
```

#### 3️⃣ 開発を終えたとき（feature → [name] にマージ）

```bash
# [name] ブランチ（= develop）に戻ってマージ
git checkout mtanaka
git merge mtanaka_unet

# リモートに push
git push origin mtanaka

# feature ブランチを削除（推奨）
git branch -d mtanaka_unet
```

#### 4️⃣ 一段落したとき（Pull Request で develop へ）

GitHub の Web 画面から **`mtanaka` → `develop`** への Pull Request を作成する。
これが git-flow でいう「`develop` へのマージ」にあたります！

---

## 🛠️ git-flow ライブラリのインストール

git-flow ライブラリを使うと、ブランチの作成・マージ・削除をまとめて1コマンドでできるようになります！

### macOS

```bash
# Homebrew を使う場合（おすすめ）
brew install git-flow-avh

# MacPorts を使う場合
port install git-flow-avh
```

### Linux (Ubuntu / Debian)

```bash
sudo apt-get install git-flow
```

### Windows

Git for Windows（Git Bash）を使っている場合は、以下の方法でインストールできます。

```bash
# Git Bash 上で実行
wget -q -O - --no-check-certificate \
  https://raw.github.com/petervanderdoes/gitflow-avh/develop/contrib/gitflow-installer.sh \
  install stable | bash
```

> 💡 `wget` と `util-linux` が必要です。

### インストール確認

```bash
git flow version
```

バージョン番号が表示されればインストール成功です🎉

---

## ⚡ git-flow ライブラリを使った開発コマンド例

git-flow ライブラリを使うと、前のセクションで紹介した手動コマンドが **ぐっとシンプル** になります！

### はじめに：git-flow の初期化

リポジトリをクローンした後、一度だけ初期化が必要です。
対話形式で質問されますが、**すべてそのまま Enter** で OK です。

```bash
cd welcome
git flow init
```

実行すると以下のような質問が表示されます（全部 Enter でデフォルト値を使ってね）：

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

> ⚠️ 本リポジトリでは `[name]` ブランチを `develop` に見立てて使うため、
> git-flow の `develop` に相当するブランチを `[name]`（例：`mtanaka`）と読み替えてください。

---

### 🔀 feature ブランチを使った開発フロー（mtanaka の場合）

#### 1️⃣ 開発を始めるとき（feature ブランチ作成）

```bash
# git-flow を使わない場合（従来）
git checkout mtanaka
git checkout -b mtanaka_unet

# ✅ git-flow を使う場合（シンプル！）
git flow feature start unet
# → "feature/unet" ブランチが自動で作成され、そこに切り替わる
```

#### 2️⃣ 開発中（feature ブランチで作業・コミット）

```bash
# この部分は通常の git コマンドと同じ
git add .
git commit -m "Add UNet encoder block"
```

#### 3️⃣ 開発を終えたとき（feature → [name] へマージ）

```bash
# git-flow を使わない場合（従来）
git checkout mtanaka
git merge mtanaka_unet
git branch -d mtanaka_unet

# ✅ git-flow を使う場合（シンプル！）
git flow feature finish unet
# → develop（= mtanaka）への自動マージ・ブランチ削除・developへの切り替えが一気に完了！
```

#### 4️⃣ リモートに push して Pull Request へ

```bash
git push origin mtanaka
```

GitHub の Web 画面から **`mtanaka` → `develop`** への Pull Request を作成してね。

---

### 📋 git-flow コマンド早見表

| やること | 従来のコマンド | git-flow コマンド |
|---|---|---|
| feature ブランチ作成 | `git checkout -b mtanaka_unet` | `git flow feature start unet` |
| feature ブランチ完了 | `git checkout mtanaka` → `git merge` → `git branch -d` | `git flow feature finish unet` |
| 作業中のブランチ一覧 | `git branch` | `git flow feature list` |

> 💡 `git flow feature finish` は、マージ・ブランチ削除・元ブランチへの切り替えを **1コマンド** でやってくれる、とても便利なコマンドです！

---

## ✅ git-flow の考え方で整理するとこうなる！

| やること | git-flow での表現 | 本リポジトリでの操作 |
|---|---|---|
| 新機能の開発開始 | `feature` ブランチを `develop` から作成 | `[name]_[feature]` を `[name]` から作成 |
| 開発中の作業 | `feature` ブランチでコミット | `[name]_[feature]` でコミット |
| 開発完了 | `feature` → `develop` にマージ | `[name]_[feature]` → `[name]` にマージ |
| チームへの共有 | `develop` への Pull Request | `[name]` → `develop` への Pull Request |
| 最新の取り込み | `develop` を `feature` に merge | `develop` を `[name]` に Pull Request でマージ |

---

## 🚨 守ってほしい大事なルール

> [!WARNING]
> `develop` ブランチへ **直接 push しないこと！**
> 必ず `[name]` ブランチから **Pull Request** を作成してください。

これは git-flow でも同じです。`develop` は「みんなの統合ブランチ」なので、
個人が直接 push してしまうと、他の人の作業と衝突したり、
レビューなしで未完成のコードが混入してしまう危険があります。

---

## 📚 もっと知りたい人へ

git-flow の詳細は以下のリソースが参考になります。

- [Atlassian: Gitflow ワークフロー（日本語）](https://www.atlassian.com/ja/git/tutorials/comparing-workflows/gitflow-workflow)
- [git-flow cheatsheet（日本語版）](https://danielkummer.github.io/git-flow-cheatsheet/index.ja_JP.html)
- [オリジナル論文（英語）: A successful Git branching model](https://nvie.com/posts/a-successful-git-branching-model/)
