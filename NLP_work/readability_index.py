import textstat

class Readability_index:
    def __init__(self, transcript):
        self.transcript = transcript

    def calculate_metrics(self):
        value = textstat.gunning_fog(self.transcript)
        return value

