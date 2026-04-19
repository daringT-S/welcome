# CIFAR-10 Deep Learning 入門

## セットアップ
```bash
pip install torch torchvision pytest
```

## パッケージフォルダ

| | |
|---|---|
| `tests/` | テスト |
| `datasets/` | データセット関連の共通パッケージ |
| `models/` | モデル定義の共通パッケージ |


### テスト実行
```bash
pytest tests/ 
```

## プロジェクトフォルダ

| | |
|---|---|
| `ex1/` | データ拡張なし（ベースライン） |
| `ex2/` | データ拡張あり（ex1 との比較） |

### ex1:実験１の実行
```bash
python -m ex1.train   
```

### ex2:実験２の実行
```bash
python -m ex2.train   
```

