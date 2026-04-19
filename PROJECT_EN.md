# Separating Projects and Packages

The most important concept in Python project design is separating **projects** from **packages**.

---

## What is a Package?

A folder containing `__init__.py` is a "package." Making a folder a package allows other files to `import` from it.

```
models/
├── __init__.py   ← this makes it a package
└── mymodel.py
```

```python
# with __init__.py, you can import
from models.mymodel import MyModel
```

The biggest advantage of a package is that **code can be reused as a module**. Instead of copy-pasting the same function across multiple scripts, you can share it with `import`.

### Let's Write Tests

The greatest benefit of making your code a package is that **you can write tests**.

Because the code is importable, test files can call and verify it.

```
project/
├── models/
│   ├── __init__.py
│   └── mymodel.py     ← what we're testing
└── tests/
    └── test_model.py  ← imports models and tests it
```

```python
# tests/test_model.py
from models.mymodel import predict   # importable because it's a package

def test_predict_returns_label():
    result = predict([1.0, 2.0, 3.0])
    assert isinstance(result, str)
```

**Without `__init__.py`, `from models.mymodel import predict` will fail.** This is the main reason to separate project folders from packages.

Run tests from the `project/` folder as follows.

```bash
# Run all tests in the tests/ folder
cd project
pytest tests/

# Run a specific file
pytest tests/test_model.py

# Show detailed output
pytest tests/ -v
```

---

## What is a Project?

The project folder is the **container that wraps your packages**. It's the place where everything lives together — code and non-code alike.

```
project/            ← project (the container)
├── README.md
├── datasets/       ← data (not code)
├── models/         ← package (importable model code)
│   ├── __init__.py
│   └── mymodel.py
├── ex1/            ← execution script (uses models)
│   └── train.py
├── ex2/            ← execution script (another experiment)
│   └── train.py
└── tests/          ← tests (imports and verifies models)
    └── test_model.py
```

The project folder itself does not have `__init__.py`. There is no need to `import project` — it simply acts as a box to organize files.

| | Package (`models/`) | Project (`project/`) |
|---|---|---|
| `__init__.py` | yes | no |
| Can be `import`ed | yes | no |
| Contents | reusable code | code + data + tests |
| Role | reusable module | container for everything |

---

## How to Run and the Working Directory

Run scripts from the `project/` folder.

```bash
cd project
python ex1/train.py
python ex2/train.py
```

However, relative paths in Python are resolved from the **current working directory at the time of execution**, not from the script's location. To ensure scripts work correctly regardless of where they are called from — including via the VSCode Run button — **always write the following at the top of every execution script.**

```python
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
```

This fixes the current working directory to **the folder where the script itself lives**. Writing it in `ex1/train.py` sets the cwd to `ex1/`, and in `ex2/train.py` sets it to `ex2/`, so relative paths in the script are always stable regardless of where it is called from.

```python
# ex1/train.py
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # ← always write at the top

data_path = "../datasets/train.csv"  # relative path from ex1/ — always works
```

---

## The Proper Way

Using `uv` and `pyproject.toml` solves this more cleanly.

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
uv pip install -e .   # install the package in "editable" mode
```

With this setup, no `sys.path` manipulation or `os.chdir()` is needed at all — `from models.mymodel import ...` works from anywhere.

**But it's a hassle.**

The practical approach is to first understand the structure described above, then migrate to `uv` + `pyproject.toml` when the need arises.
