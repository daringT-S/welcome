# プロジェクトとパッケージの分離

Python のプロジェクト設計で最も重要な概念は「**プロジェクト**」と「**パッケージ**」を分離することです。

---

## パッケージとは

`__init__.py` が置かれたフォルダが「パッケージ」です。パッケージにすることで、他のファイルから `import` できるようになります。

```
models/
├── __init__.py   ← これがあるとパッケージ
└── mymodel.py
```

```python
# __init__.py があれば import できる
from models.mymodel import MyModel
```

パッケージの最大の利点は、**コードをモジュールとして再利用できる**ことです。同じ関数を複数のスクリプトからコピペせず、`import` で使い回せます。

### テストを作ろう

パッケージにした最大のご利益が「テストを書ける」ことです。

`import` できる形になっているからこそ、テストファイルがコードを呼び出して検証できます。

```
project/
├── models/
│   ├── __init__.py
│   └── mymodel.py     ← テスト対象
└── tests/
    └── test_model.py  ← ここから models を import してテスト
```

```python
# tests/test_model.py
from models.mymodel import predict   # パッケージなので import できる

def test_predict_returns_label():
    result = predict([1.0, 2.0, 3.0])
    assert isinstance(result, str)
```

**`__init__.py` がなければ `from models.mymodel import predict` は失敗します。** プロジェクトフォルダとパッケージを分離する理由の大半はここにあります。

テストは `project/` フォルダから以下のように実行します。

```bash
# tests/ フォルダ内のテストをすべて実行
cd project
pytest tests/

# 特定のファイルだけ実行
pytest tests/test_model.py

# 詳細な結果を表示
pytest tests/ -v
```

---

## プロジェクトとは

パッケージを「包む入れ物」がプロジェクトフォルダです。コード以外のものもすべて一緒に置く場所です。

```
project/            ← プロジェクト（入れ物）
├── README.md
├── datasets/       ← データ（コードではない）
├── models/         ← パッケージ（import できるモデルコード）
│   ├── __init__.py
│   └── mymodel.py
├── ex1/            ← 実行スクリプト（models を使う）
│   └── train.py
├── ex2/            ← 実行スクリプト（別の実験）
│   └── train.py
└── tests/          ← テスト（models を import して検証）
    └── test_model.py
```

プロジェクトフォルダ自体に `__init__.py` は置きません。`import project` とする必要はなく、あくまで「ファイルをまとめる箱」として機能します。

| | パッケージ（`models/`） | プロジェクト（`project/`）|
|---|---|---|
| `__init__.py` | あり | なし |
| `import` できるか | できる | しない |
| 中身 | 再利用するコード | コード ＋ データ ＋ テスト |
| 役割 | 再利用できるモジュール | 全体をまとめる入れ物 |

---

## 実行方法とカレントディレクトリの移動

スクリプトは `project/` フォルダから実行します。

```bash
cd project
python ex1/train.py
```

```bash
cd project
python ex2/train.py
```

ただし、Python の相対パスは**呼び出した場所（カレントディレクトリ）が基準**になるため、`project/` から実行しても VSCode のボタンから実行しても動くよう、**実行スクリプトの冒頭には必ず以下を書きます。**

```python
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
```

これにより、カレントディレクトリが**そのスクリプト自身のフォルダ**に固定されます。`ex1/train.py` に書けば `ex1/` が、`ex2/train.py` に書けば `ex2/` がカレントディレクトリになるので、スクリプト内の相対パスが実行場所に左右されず常に安定します。

```python
# ex1/train.py
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # ← 冒頭に必ず書く

data_path = "../datasets/train.csv"  # ex1/ 基準の相対パスで安定して動く
```

---

## 本当は

`uv` と `pyproject.toml` を使うともっときれいに解決できます。

```toml
# pyproject.toml
[project]
name = "models"
version = "0.1.0"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

```bash
uv pip install -e .   # パッケージを「開発モードで」インストール
```

こうすると `sys.path` の操作も `os.chdir()` も一切不要になり、どこから実行しても `from models.mymodel import ...` が動きます。

**でも、めんどくさい。**

まず上で説明した構成を理解してから、必要になったタイミングで `uv` + `pyproject.toml` に移行するのが現実的な進め方です。

