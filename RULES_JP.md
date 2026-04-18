# 🐙 GitHub 運用ルール

## ブランチ構成

| ブランチ名 | 役割 |
|---|---|
| `main` | リリース・バックアップ用（直接触らない）|
| `develop` | 開発統合用（直接pushしない）|
| `[name]` | 学生個人ブランチ（リモート管理）|
| `[name]_[feature]` | 機能開発用ブランチ |

**例）**

| ブランチ名 | 説明 |
|---|---|
| `mtanaka` | 田中さんの個人ブランチ |
| `mtanaka_unet` | 田中さんのUNet開発ブランチ |


---
## 要点

> [!WARNING]
> `develop` ブランチへ直接 push しないこと！

1. リモート`[name]` ブランチを作成する
2. リモート`[name]` ブランチを`develop` から pull して最新の状態にする
3. リモート`[name]` ブランチを、ローカル`[name]` ブランチにpullする
4. ローカル`[name]` ブランチを、リモート`[name]` ブランチにpushする
5. リモート`[name]` ブランチから `develop` ブランチへ **Pull Request** を作成する

ローカル`[name]` ブランチをどのように開発するかはお任せします。


---

## 📁 リポジトリを新規作成するとき

1. `main` ブランチを作成する
2. `main` から `develop` ブランチを作成する
3. `develop` ブランチをデフォルトにする

---

## 🙋 学生がリポジトリに参加するとき

1. `develop` から `[name]` ブランチ（リモート）を作成する
2. `[name]` ブランチ（リモート）だけcloneする


例）[name] | mtanaka

```bash
git clone -b [name] --single-branch git@github.com:visionimageprocessing/welcome.git
```


---

## 💻 学生が開発をはじめるとき

1. リモート`[name]` ブランチを`develop` から pull して最新の状態にする
2. リモート`[name]` ブランチを、ローカル`[name]` ブランチにpullする
3. ローカル`[name]` ブランチからローカル`[name]_[feature]` ブランチを作成する
4. ローカル`[name]_[feature]` ブランチで開発を行う

---

## ✅ 学生が開発を終えたとき

1. ローカル`[name]` ブランチにローカル`[name]_[feature]` ブランチをmergeする
2. ローカル`[name]` ブランチをリモート`[name]` ブランチにpushする
3. ローカル`[name]_[feature]` ブランチを削除する

---

## 🔀 学生の開発が一段落したとき

1. リモート`[name]` ブランチから `develop` ブランチへ **Pull Request** を作成する
2. リポジトリ管理者が Pull Request をレビュー・マージする

> [!WARNING]
> `develop` ブランチへ直接 push しないこと！

---

