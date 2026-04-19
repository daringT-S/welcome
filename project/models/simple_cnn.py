"""
CIFAR-10 向けシンプルな CNN モデル。

3 層の畳み込みブロック（Conv → BN → ReLU → MaxPool）と
全結合層からなる入門用アーキテクチャ。
"""

import torch
import torch.nn as nn


class SimpleCNN(nn.Module):
    """3 層畳み込みブロック＋全結合層からなる基本的な CNN。

    入力: (N, 3, 32, 32) の CIFAR-10 画像テンソル
    出力: (N, num_classes) のクラスロジット

    Args:
        num_classes: 分類クラス数（デフォルト 10）。
    """

    def __init__(self, num_classes: int = 10) -> None:
        super().__init__()

        self.features = nn.Sequential(
            # ── Block 1: 3ch → 32ch, 32×32 → 16×16 ─────────────────
            nn.Conv2d(3,  32, kernel_size=3, padding=1, bias=False),
            nn.BatchNorm2d(32),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),

            # ── Block 2: 32ch → 64ch, 16×16 → 8×8 ──────────────────
            nn.Conv2d(32, 64, kernel_size=3, padding=1, bias=False),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),

            # ── Block 3: 64ch → 128ch, 8×8 → 4×4 ───────────────────
            nn.Conv2d(64, 128, kernel_size=3, padding=1, bias=False),
            nn.BatchNorm2d(128),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),
        )

        # 特徴マップサイズ: 128 × 4 × 4 = 2048
        self.classifier = nn.Sequential(
            nn.Dropout(p=0.5),
            nn.Linear(128 * 4 * 4, 256),
            nn.ReLU(inplace=True),
            nn.Dropout(p=0.3),
            nn.Linear(256, num_classes),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.features(x)          # (N, 128, 4, 4)
        x = x.view(x.size(0), -1)     # (N, 2048)
        return self.classifier(x)     # (N, num_classes)
