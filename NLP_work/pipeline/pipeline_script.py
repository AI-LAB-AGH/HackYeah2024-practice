from Machine_learning.speech_to_text import SpeechToText
from NLP_work.gpt.GPT import GPT
from NLP_work.readability_index import Readability_index
import nltk

class Pipeline:
    def __init__(self, video_path):
        self.transcript = None
        self.gpt = GPT()
        self.path = video_path
        self.transcript_path = None

    def create_transcript(self):
        speechToText = SpeechToText()
        self.result = speechToText.transcribe_wav(self.path)

    def load_transcript(self):
        self.transcript = self.result["DisplayText"]

    def clean_transcripts(self):
        self.transcript = self.gpt.clean_transcript(self.transcript)

    def do_tasks_on_video(self):
        return self.gpt.get_tasks_results(self.transcript)

    def get_fog_index(self):
        nltk.download('punkt_tab')
        r = Readability_index(self.transcript)
        # return r.calculate_metrics()
        return 0