from readability import Readability

class Readability_index:
    def __init__(self, transcript):
        self.transcript = transcript

    def calculate_metrics(self):
        r = Readability(self.transcript)
        return r.gunning_fog()