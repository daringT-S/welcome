"""CIFAR-10 の DataLoader を返すユーティリティ。"""
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

MEAN = (0.4914, 0.4822, 0.4465)
STD  = (0.2023, 0.1994, 0.2010)
CLASSES = ('plane','car','bird','cat','deer','dog','frog','horse','ship','truck')


def get_loaders(data_root="./data", batch_size=128, augment=False, num_workers=2):
    aug = [transforms.RandomCrop(32, padding=4), transforms.RandomHorizontalFlip()]
    base = [transforms.ToTensor(), transforms.Normalize(MEAN, STD)]

    train_tf = transforms.Compose((aug if augment else []) + base)
    test_tf  = transforms.Compose(base)

    train = datasets.CIFAR10(data_root, train=True,  download=True, transform=train_tf)
    test  = datasets.CIFAR10(data_root, train=False, download=True, transform=test_tf)

    return (
        DataLoader(train, batch_size=batch_size, shuffle=True,  num_workers=num_workers),
        DataLoader(test,  batch_size=batch_size, shuffle=False, num_workers=num_workers),
    )
