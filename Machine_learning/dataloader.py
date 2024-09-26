from torch.utils.data import DataLoader

class MyDataloader(DataLoader):
    def __init__(self) -> None:
        pass

    def __repr__(self) -> str:
        return "Klasa do dataloadera"