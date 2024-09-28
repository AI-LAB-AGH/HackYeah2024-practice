from Machine_learning.speech_to_text import SpeechToText
from NLP_work.gpt.GPT import GPT

class Pipeline:
    def __init__(self):
        self.transcript = None

    def create_transcript(self):
        speechToText = SpeechToText()
        speechToText.convert_audio()
        speechToText.transcribe_wav()

    def load_transcript(self):
        with open("E:/Python/Projects/HackYeah2024-practice/NLP_work/transcripts/HY_2024_film_04.txt", "r") as f:
            self.transcript = f.read()

    def do_tasks_on_video(self):
        return GPT().get_tasks_results(self.transcript)




def main():
    pipeline = Pipeline()
    pipeline.load_transcript()
    print(pipeline.do_tasks_on_video())


if __name__ == "__main__":
    main()
