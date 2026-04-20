# 项目与包的分离

Python 项目设计中最重要的概念，就是将「**项目**」与「**包**」分离。

---

## 什么是包？

包含 `__init__.py` 的文件夹即为「包」。将文件夹设为包后，其他文件就可以通过 `import` 来使用其中的代码。

```
models/
├── __init__.py   ← 有这个文件就是包
└── mymodel.py
```

```python
# 有 __init__.py 就可以 import
from models.mymodel import MyModel
```

包最大的优点在于，**代码可以作为模块复用**。无需在多个脚本间复制粘贴同一个函数，只需通过 `import` 共享使用即可。

### 来写测试吧

将代码做成包的最大好处就是**可以编写测试**。

正因为代码是可导入的形式，测试文件才能调用并验证它。

```
project/
├── models/
│   ├── __init__.py
│   └── mymodel.py     ← 测试对象
└── tests/
    └── test_model.py  ← 在这里 import models 并进行测试
```

```python
# tests/test_model.py
from models.mymodel import predict   # 因为是包，所以可以 import

def test_predict_returns_label():
    result = predict([1.0, 2.0, 3.0])
    assert isinstance(result, str)
```

**如果没有 `__init__.py`，`from models.mymodel import predict` 将会失败。** 这正是将项目文件夹与包分离的主要原因。

测试在 `project/` 文件夹下按如下方式执行。

```bash
# 执行 tests/ 文件夹中的所有测试
cd project
pytest tests/

# 只执行特定文件
pytest tests/test_model.py

# 显示详细结果
pytest tests/ -v
```

---

## 什么是项目？

项目文件夹是**包裹包的容器**，是将所有内容（代码与非代码）统一存放的地方。

```
project/            ← 项目（容器）
├── README.md
├── datasets/       ← 数据（非代码）
├── models/         ← 包（可 import 的模型代码）
│   ├── __init__.py
│   └── mymodel.py
├── ex1/            ← 执行脚本（使用 models）
│   └── train.py
├── ex2/            ← 执行脚本（另一个实验）
│   └── train.py
└── tests/          ← 测试（import models 并进行验证）
    └── test_model.py
```

项目文件夹本身不需要放置 `__init__.py`。无需 `import project`，它只是一个用于整理文件的容器。

| | 包（`models/`） | 项目（`project/`） |
|---|---|---|
| `__init__.py` | 有 | 无 |
| 是否可 `import` | 可以 | 不需要 |
| 内容 | 可复用的代码 | 代码 ＋ 数据 ＋ 测试 |
| 作用 | 可复用的模块 | 整合所有内容的容器 |

---

## 执行方式与当前目录的切换

脚本在 `project/` 文件夹下执行。

```bash
cd project
python ex1/train.py
python ex2/train.py
```

但是，Python 中的相对路径是以**执行时的当前目录**为基准的，而非脚本文件所在的位置。因此，无论从哪里调用脚本（包括通过 VSCode 的运行按钮），**请务必在所有执行脚本的开头写上以下代码。**

```python
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
```

这样，无论从哪里调用，当前目录都会被固定为**脚本自身所在的文件夹**。在 `ex1/train.py` 中写入，当前目录就变为 `ex1/`；在 `ex2/train.py` 中写入，就变为 `ex2/`。这样，脚本内的相对路径就不会受执行位置的影响，始终保持稳定。

```python
# ex1/train.py
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # ← 开头必须写

data_path = "../datasets/train.csv"  # 以 ex1/ 为基准的相对路径，始终有效
```

---

## 更规范的做法

使用 `uv` 和 `pyproject.toml` 可以更优雅地解决这个问题。

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
uv pip install -e .   # 以「开发模式」安装包
```

这样就完全不需要操作 `sys.path`，也不需要 `os.chdir()`，无论从哪里执行，`from models.mymodel import ...` 都可以正常运行。

**但是，很麻烦。**

建议先理解上面介绍的结构，等到真正有需要的时候再迁移到 `uv` + `pyproject.toml`。
