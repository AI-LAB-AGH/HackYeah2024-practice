from torch.utils.data import Dataset

class MyDataset(Dataset):
    def __init__(self):
        pass

    def __repr__(self) -> str:
        return "Class to load custom data from local source"
    
    def __getitem__(self, index) -> None:
        pass