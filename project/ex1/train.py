"""
ex1 — データ拡張なし（ベースライン）
実行: python -m ex1.train
"""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import torch
import torch.nn as nn
import torch.optim as optim

from datasets.cifar10 import get_loaders
from models.simple_cnn import SimpleCNN

EPOCHS, BATCH, LR = 20, 128, 1e-3

device       = torch.device("cuda" if torch.cuda.is_available() else "cpu")
train_loader, test_loader = get_loaders(batch_size=BATCH, augment=False)
model        = SimpleCNN().to(device)
criterion    = nn.CrossEntropyLoss()
optimizer    = optim.Adam(model.parameters(), lr=LR)
scheduler    = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=EPOCHS)


def run_epoch(loader, train=True):
    model.train() if train else model.eval()
    loss_sum, correct, total = 0.0, 0, 0
    with torch.set_grad_enabled(train):
        for x, y in loader:
            x, y = x.to(device), y.to(device)
            out  = model(x)
            loss = criterion(out, y)
            if train:
                optimizer.zero_grad(); loss.backward(); optimizer.step()
            loss_sum += loss.item() * x.size(0)
            correct  += out.argmax(1).eq(y).sum().item()
            total    += x.size(0)
    return loss_sum / total, correct / total


best = 0.0
for epoch in range(1, EPOCHS + 1):
    tr_loss, tr_acc = run_epoch(train_loader, train=True)
    te_loss, te_acc = run_epoch(test_loader,  train=False)
    scheduler.step()
    print(f"[{epoch:>2}/{EPOCHS}] train {tr_acc:.3f}  test {te_acc:.3f}")
    if te_acc > best:
        best = te_acc
        torch.save(model.state_dict(), "ex1_best.pth" )

print(f"Best: {best:.4f}")
