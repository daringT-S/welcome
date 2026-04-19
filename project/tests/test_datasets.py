"""
datasets パッケージのユニットテスト。
実行: pytest tests/test_datasets.py
"""
import torch
import pytest
from datasets.cifar10 import CLASSES, get_loaders


def test_classes_count():
    assert len(CLASSES) == 10


def test_classes_are_strings():
    assert all(isinstance(c, str) for c in CLASSES)


def test_train_batch_shape():
    train_loader, _ = get_loaders(batch_size=16, augment=False, num_workers=0)
    images, labels = next(iter(train_loader))
    assert images.shape == (16, 3, 32, 32)
    assert labels.shape == (16,)


def test_test_batch_shape():
    _, test_loader = get_loaders(batch_size=32, augment=False, num_workers=0)
    images, labels = next(iter(test_loader))
    assert images.shape == (32, 3, 32, 32)
    assert labels.shape == (32,)


def test_label_range():
    train_loader, _ = get_loaders(batch_size=64, augment=False, num_workers=0)
    _, labels = next(iter(train_loader))
    assert labels.min().item() >= 0
    assert labels.max().item() <= 9


def test_image_dtype():
    train_loader, _ = get_loaders(batch_size=16, augment=False, num_workers=0)
    images, _ = next(iter(train_loader))
    assert images.dtype == torch.float32
