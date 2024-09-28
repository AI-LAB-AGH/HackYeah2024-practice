from Machine_learning.speech_to_text import SpeechToText
from NLP_work.gpt.GPT import GPT
from NLP_work.readability_index import Readability_index

class Pipeline:
    def __init__(self):
        self.transcript = None
        self.gpt = GPT()

    def create_transcript(self):
        speechToText = SpeechToText()
        speechToText.convert_audio()
        speechToText.transcribe_wav()

    def load_transcript(self):
        with open("E:/Python/Projects/HackYeah2024-practice/data/video-transcription-manually/TXT_HY_2024_film_03.txt", "r") as f:
            self.transcript = f.read()

    def clean_transcripts(self):
        self.transcript = self.gpt.clean_transcript(self.transcript)

    def do_tasks_on_video(self):
        return self.gpt.get_tasks_results(self.transcript)

    def get_fog_index(self):
        r = Readability_index(self.transcript)
        return r.calculate_metrics()




def main():
    pipeline = Pipeline()
    pipeline.load_transcript()
    pipeline.clean_transcripts()
    print(pipeline.transcript)
    print(pipeline.get_fog_index())


if __name__ == "__main__":
    main()
