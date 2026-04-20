"""
models パッケージのユニットテスト。

SimpleCNN の出力形状・パラメータ数・推論モードなどを検証する。
実行: pytest tests/test_models.py
"""

import torch
import pytest

from models.simple_cnn import SimpleCNN


@pytest.fixture()
def model() -> SimpleCNN:
    """テスト用の SimpleCNN インスタンスを返す（CPU）。"""
    return SimpleCNN(num_classes=10)


# ── 出力形状のテスト ───────────────────────────────────────────

def test_output_shape_single(model: SimpleCNN) -> None:
    """バッチサイズ 1 で正しい出力形状になることを確認する。"""
    x = torch.randn(1, 3, 32, 32)
    out = model(x)
    assert out.shape == (1, 10), f"Output shape: {out.shape}"


def test_output_shape_batch(model: SimpleCNN) -> None:
    """バッチサイズ 8 で正しい出力形状になることを確認する。"""
    x = torch.randn(8, 3, 32, 32)
    out = model(x)
    assert out.shape == (8, 10), f"Output shape: {out.shape}"


def test_output_num_classes_custom() -> None:
    """num_classes を変えると出力次元が変わることを確認する。"""
    model = SimpleCNN(num_classes=5)
    x = torch.randn(4, 3, 32, 32)
    out = model(x)
    assert out.shape == (4, 5), f"Output shape: {out.shape}"


# ── パラメータ数のテスト ───────────────────────────────────────

def test_parameter_count(model: SimpleCNN) -> None:
    """パラメータ数が 10 万〜1000 万の範囲内であることを確認する。"""
    n_params = sum(p.numel() for p in model.parameters())
    assert 100_000 < n_params < 10_000_000, f"Param count: {n_params}"


# ── 推論モードのテスト ─────────────────────────────────────────

def test_eval_mode_no_grad(model: SimpleCNN) -> None:
    """eval モードで torch.no_grad() 下でも正常に推論できることを確認する。"""
    model.eval()
    x = torch.randn(4, 3, 32, 32)
    with torch.no_grad():
        out = model(x)
    assert out.shape == (4, 10)


def test_output_is_float(model: SimpleCNN) -> None:
    """出力テンソルが float32 であることを確認する。"""
    x = torch.randn(2, 3, 32, 32)
    out = model(x)
    assert out.dtype == torch.float32
