# INTERLAB — 研究室間 GitHub 運用ガイド

> 本ドキュメントは、複数の研究室が 1 つの GitHub Organization を通じてコードを共有・統合するための **管理者向け** 運用ガイドです。  
> 各研究室メンバー向けの Git 基本操作については [README.md](./README.md) を参照してください。

---

## 1. Overview

### Organization 全体の構成

```
GitHub Organization: MyResearch
│
├── project-main          ← 統合リポジトリ（管理者チームが管理）
│   ├── branch: main      ← リリース・バックアップ用
│   ├── branch: develop   ← 開発統合用
│   └── branch: lab-A     ← 各ラボからの PR 受け取り用（ラボごとに作成）
│
├── project-lab-A         ← project-main の Fork（Lab-A が管理）
│   └── branch: main
│
└── project-lab-B         ← project-main の Fork（Lab-B が管理）
    └── branch: main
```

### PR フロー

```
project-lab-A:main
      │
      │  Pull Request
      ▼
project-main:lab-A    ← ここでコードレビュー・修正依頼
      │
      │  マージ（管理者チームのみ）
      ▼
project-main:develop  ← 各ラボの統合ブランチ
      │
      │  安定確認後にマージ
      ▼
project-main:main     ← リリース・バックアップ
```

---

## 2. Repository 構成

### 2.1 project-main（統合リポジトリ）

| ブランチ | 役割 | 直接 push |
|---|---|---|
| `main` | リリース・バックアップ用 | ❌ 禁止 |
| `develop` | 全ラボの開発統合用 | ❌ 禁止（PR のみ） |
| `lab-A` | Lab-A からの PR 受け取り用 | ❌ 禁止（PR のみ） |
| `lab-B` | Lab-B からの PR 受け取り用 | ❌ 禁止（PR のみ） |

> ⚠️ `lab-X` ブランチは `project-main` の管理者が作成する。各ラボが自分で作成することはできない。

### 2.2 project-lab-X（各ラボ Fork）

| ブランチ | 役割 |
|---|---|
| `main` | PR 送信元。必ず作成すること |
| その他 | 各ラボの裁量で自由に管理してよい |

### 2.3 命名規則

| 対象 | 命名規則 | 例 |
|---|---|---|
| Fork リポジトリ | `project-lab-[ラボ識別子]` | `project-lab-A`, `project-lab-vip` |
| 受け取りブランチ | `lab-[ラボ識別子]` | `lab-A`, `lab-vip` |

---

## 3. Team 設定

### 3.1 チーム構成

| チーム名 | メンバー | 対象リポジトリ | 権限 |
|---|---|---|---|
| `main-admin` | 全ラボの管理者 | `project-main` | Write |
| `lab-A-team` | Lab-A メンバー | `project-main` | Read |
|              |               | `project-lab-A` | Write |
| `lab-B-team` | Lab-B メンバー | `project-main` | Read |
|              |               | `project-lab-B` | Write |

### 3.2 権限の考え方

- **`project-main` への Write 権限は `main-admin` チームのみ**が持つ。
- 各ラボメンバーは `project-main` を Read のみ参照でき、PR を通じてのみ貢献できる。
- 各ラボの Fork リポジトリは、そのラボが自由に管理する（Write 権限あり）。

### 3.3 新しいラボを追加するときのチーム設定

1. `lab-[X]-team` チームを Organization に作成する
2. 該当ラボメンバーをチームに追加する
3. `project-main` に対して **Read** 権限を付与する
4. `project-lab-X` に対して **Write** 権限を付与する

---

## 4. ブランチ保護と運用ルール

### 4.1 権限による実質的なブランチ保護

`project-main` への Write 権限は `main-admin` チームのみが持つ。各ラボメンバーは Read 権限しか持たないため、**`project-main` への直接 push は権限上不可能**であり、PR を通じた貢献のみが許可される。

これにより、GitHub の有料プランの Ruleset を使わなくても、以下の保護が実質的に担保される。

| ブランチ | 直接 push できる人 | 保護の根拠 |
|---|---|---|
| `main` | `main-admin` チームのみ | Write 権限が `main-admin` のみに付与されているため |
| `develop` | `main-admin` チームのみ | 同上 |
| `lab-X` | `main-admin` チームのみ | 同上 |

### 4.2 マージ権限

| 操作 | 実施者 |
|---|---|
| `project-lab-X:main` → `project-main:lab-X` への PR 作成 | 各ラボ管理者 |
| `project-main:lab-X` → `project-main:develop` へのマージ | `main-admin` チームのみ |
| `project-main:develop` → `project-main:main` へのマージ | `main-admin` チームのみ |

### 4.3 運用上の注意

`main-admin` チーム内では、自分の PR を自分でマージすること（セルフマージ）が技術的には可能。これが唯一の抜け穴となるため、**`main-admin` チーム内での PR は必ず他のメンバーがレビュー・マージすること**を運用ルールとして徹底する。

---

## 5. 管理担当ラボ

`project-main` の運用責任を担うラボを明記し、`project-main` の `README.md` に記載する。

### README.md への記載ルール

`project-main` の `README.md` の冒頭に、以下の形式で管理担当ラボを明記すること。

```markdown
## 管理担当

| 項目 | 内容 |
|---|---|
| 管理担当ラボ | Lab-X（○○大学 ○○研究室） |
| 管理者連絡先 | xxxx@example.ac.jp |
| 最終更新 | YYYY-MM-DD |
```

> ⚠️ 管理担当ラボが変更された場合は、速やかに `README.md` を更新し、`main-admin` チームのメンバー構成も見直すこと。

---

## 6. 新しいラボを追加するときの手順

新しい研究室（例: Lab-C）を追加する場合、以下の手順を **`main-admin` チームのメンバーが実施** する。

### Step 1: `project-main` に受け取りブランチを作成する

GitHub Web 画面から `develop` ブランチをもとに `lab-C` ブランチを作成する。

```
base: develop → 新ブランチ: lab-C
```

### Step 2: `project-main` を Fork する

GitHub Web 画面から `project-main` を同一 Organization 内に Fork する。

```
Fork 先リポジトリ名: project-lab-C
```

> ⚠️ Fork は必ず **同一 Organization 内** に作成すること。Organization 外（個人アカウント等）への Fork は private リポジトリでは機能しない。

### Step 3: Fork リポジトリに `main` ブランチがあることを確認する

`project-lab-C` の `main` ブランチが存在することを確認する。  
存在しない場合は Web 画面から作成する。

### Step 4: Team を作成・設定する

1. Organization → **Teams** → **New team** で `lab-C-team` を作成する
2. Lab-C のメンバーを追加する
3. `project-main` に **Read** 権限を付与する
4. `project-lab-C` に **Write** 権限を付与する

### Step 5: `project-main` の `README.md` を更新する

参加ラボ一覧に Lab-C を追記する。

---

## 7. 参加ラボ一覧テンプレート

`project-main` の `README.md` に以下の形式で参加ラボを管理する。

```markdown
## 参加ラボ一覧

| ラボ識別子 | 研究室名 | 大学 | Fork リポジトリ | 管理者 |
|---|---|---|---|---|
| lab-A | ○○研究室 | ○○大学 | project-lab-A | @github_id |
| lab-B | △△研究室 | △△大学 | project-lab-B | @github_id |
```

---

## 8. よくある操作リファレンス

### Fork リポジトリを project-main の最新に同期する

```bash
# ローカルで作業している場合
git remote add upstream https://github.com/MyResearch/project-main.git
git fetch upstream
git checkout main
git merge upstream/develop
git push origin main
```

または GitHub Web 画面の **Sync fork** ボタンを使う。

### PR を出す（各ラボ管理者が実施）

1. `project-lab-X` の GitHub ページを開く
2. **Contribute** → **Open pull request** をクリック
3. 以下を確認する

| 項目 | 設定 |
|---|---|
| base repository | `MyResearch/project-main` |
| base branch | `lab-X` |
| head repository | `MyResearch/project-lab-X` |
| compare branch | `main` |

4. タイトルと変更内容の説明を記入して **Create pull request** をクリック

### `lab-X` ブランチを `develop` にマージする（main-admin が実施）

1. `project-main` の `lab-X` ブランチの内容をレビューする
2. 問題なければ `lab-X` → `develop` への PR を作成してマージする

---

*本ドキュメントに関する質問・修正提案は `project-main` の Issue または管理担当ラボまで。*
