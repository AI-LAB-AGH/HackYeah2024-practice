import tqdm

class MyTrainer():
    def __init__(self) -> None:
        self.optimizer = None
        self.loss = None
        self.batch_size = None

    def __repr__(self) -> str:
        return "Klasa do trenowania modelu, zbiera w sobie dataloader, dataset, model"
    
    def train(self):
        "Tu będzie trenowanie modelu -> pętla po epokach, batchach, itd."
        pass