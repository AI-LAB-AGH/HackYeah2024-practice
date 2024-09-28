import torch

from model_torch import ModelTorch
from tqdm import tqdm

class MyTrainer():
    def __init__(self) -> None:
        self.optimizer = None
        self.loss = None
        self.batch_size = None
        self.epochs = None
        self.dataloader = None
        self.dataset = None
        self.model = ModelTorch.get_model()
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    def __repr__(self) -> str:
        return "Klasa do trenowania modelu, zbiera w sobie dataloader, dataset, model"
    
    def train(self):
        "Tu będzie trenowanie modelu -> pętla po epokach, batchach, itd."
        pass