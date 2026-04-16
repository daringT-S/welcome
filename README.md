# 🐙 GitHub 運用練習

🇺🇸 [English version here](README_EN.md)

本リポジトリは、研究室の GitHub 運用フローを練習するためのリポジトリです。

## ブランチ構成

| ブランチ名 | 役割 |
|---|---|
| `main` | リリース・バックアップ用（直接触らない）|
| `develop` | 開発統合用（直接pushしない）|
| `[name]` | 学生個人ブランチ 例）`mtanaka` |
| `[name]_[feature]` | 機能開発用ブランチ 例）`mtanaka_func` |

---

## 📝 課題概要

1. `func_[name].py` を作成し、自分の関数を実装する
2. `main.py` に自分の関数を呼び出すコードを追加する
3. 正しいブランチ運用で Pull Request を作成する

---

## 🚀 手順

### Step 1 : リポジトリをローカルにクローンする

```bash
git clone git@github.com:visionimageprocessing/welcome.git
cd welcome
```

> 💡 Organization名は `visionimageprocessing`、リポジトリ名は `welcome`

---

### Step 2 : `[name]` ブランチを作成する（Web操作）

GitHub の Web 画面から `develop` ブランチをもとに自分の名前のブランチを作成する。

1. リポジトリページを開く
2. ブランチ切り替えメニュー（左上の `develop`）をクリック
3. テキストボックスに自分の名前を入力する（例：`mtanaka`）
4. `Create branch: mtanaka from develop` をクリック

---

### Step 3 : リモートの `[name]` ブランチを取得し、`[name]_[feature]` ブランチを作成する（ローカル操作）

```bash
git checkout mtanaka
git pull origin mtanaka
git checkout -b mtanaka_func
```

---

### Step 4 : `func_[name].py` を作成する

`[name]_[feature]` ブランチ上で `func_[name].py` を新規作成し、自分の関数を実装する。

**ファイル名：** `func_mtanaka.py`

```python
def func_mtanaka():
    print("Welcome to Vision and Image Processing lab.!")

if __name__ == "__main__":
    func_mtanaka()
```

> 💡 `[name]` の部分は自分の名前に置き換えること（例：`mtanaka` → `func_mtanaka.py`）

---

### Step 5 : 開発内容を commit する

```bash
git add func_mtanaka.py
git commit -m "Add func_mtanaka"
```

---

### Step 6 : `[name]` ブランチに push する

まず、ローカルの `mtanaka` ブランチに変更をマージする。

```bash
git checkout mtanaka
git merge mtanaka_func
```

次に、リモートの `mtanaka` ブランチに push する。

```bash
git push origin mtanaka
```

---

### Step 7 : `[name]_[feature]` ブランチを削除する（任意）

`[name]_[feature]` ブランチは開発完了後に削除することを推奨する。

```bash
# ローカルブランチを削除する場合
git checkout mtanaka
git branch -d mtanaka_func
```

> 💡 削除しなくても次の開発に進めるが、ブランチが増えすぎると管理が煩雑になるため削除を推奨

---

### Step 8 : `develop` から `[name]` ブランチを最新にする（Web操作 + ローカル操作）

次の開発を始める前に、`develop` の最新内容を `[name]` ブランチに取り込む。

**Web操作：** GitHub の Web 画面から `develop` → `mtanaka` への Pull Request を作成してマージする。

1. GitHub のリポジトリページを開く
2. `Compare & pull request` をクリック
3. 以下を確認する

| 項目 | 設定 |
|---|---|
| base | `mtanaka` |
| compare | `develop` |

4. タイトルと説明を入力して `Create pull request` をクリック
5. 問題がなければ `Merge pull request` をクリックしてマージする

**ローカル操作：** マージ後、ローカルの `mtanaka` ブランチを最新にする。

```bash
git checkout mtanaka
git pull origin mtanaka
```

---

### Step 9 : 新しい `[name]_[feature]` ブランチを作成する（ローカル操作）

```bash
git checkout mtanaka
git checkout -b mtanaka_main
```

---

### Step 10 : `main.py` を編集する

`main.py` に自分の関数を import して呼び出すコードを追加する。

**ファイル名：** `main.py`

```python
from func_mtanaka import func_mtanaka

func_mtanaka()
```

> 💡 すでに他の学生のコードが追加されている場合は、既存のコードを削除せず、自分の行だけ追加すること

---

### Step 11 : 開発内容を commit する

```bash
git add main.py
git commit -m "Add func_mtanaka to main.py"
```

---

### Step 12 : `[name]` ブランチに push する

まず、ローカルの `mtanaka` ブランチに変更をマージする。

```bash
git checkout mtanaka
git merge mtanaka_main
```

次に、リモートの `mtanaka` ブランチに push する。

```bash
git push origin mtanaka
```

---

### Step 13 : `[name]_[feature]` ブランチを削除する（任意）

```bash
# ローカルブランチを削除する場合
git checkout mtanaka
git branch -d mtanaka_main
```

---

### Step 14 : `develop` へ Pull Request を作成する

GitHub の Web 画面から Pull Request を作成する。

1. GitHub のリポジトリページを開く
2. `Compare & pull request` をクリック
3. 以下を確認する

| 項目 | 設定 |
|---|---|
| base | `develop` |
| compare | `mtanaka` |

4. タイトルと説明を入力して `Create pull request` をクリック
5. リポジトリ管理者のマージを待つ

> [!WARNING]
> `develop` ブランチへ直接 push しないこと！必ず Pull Request を通すこと！
