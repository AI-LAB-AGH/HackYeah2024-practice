from openai import OpenAI
import api_key
from prompts import *

CLIENT = OpenAI(api_key=api_key.get_api_key())
MODEL = "gpt-4o"


class GPT:

    def get_tasks_results(self, transcript):
        return {
            "filler_words": self.query_gpt(filler_word_prompt(transcript)),
            "repeated_words": self.query_gpt(repetitions_prompt(transcript)),
            "complex_words": self.query_gpt(complex_words_prompt_pl(transcript)),
            "jargon_words": self.query_gpt(jargon_words_prompt_pl(transcript)),
            "non-polish_words": self.query_gpt(non_polish_words_prompt(transcript)),
            "non-existing_words": self.query_gpt(non_existing_words_prompt(transcript)),
            "passive_voice": self.query_gpt(passive_voice_prompt_pl(transcript)),
            "change_of_topic": self.query_gpt(unexpected_topic_change_prompt(transcript)),
            "numbers": self.query_gpt(unusual_numbers_prompt(transcript)),
            "target_group": self.query_gpt(target_group_prompt(transcript)),
            "questions": self.query_gpt(valid_questions_prompt(transcript)),
            "important_phrases": self.query_gpt(important_phrases_prompt(transcript))
        }

    def clean_transcript(self, transcript):
        return self.query_gpt("Podziel tekst podany na końcu tej wiadomości na zdania oraz dodaj wielkie litery na początku zdań. "
                              "Nie zwracaj w odpowiedzi nic oprócz poprawionego tekstu."
                              f"Oto tekst: <TEXT> \"{transcript}\" <\\TEXT>")

    def query_gpt(self, prompt):
        completion = CLIENT.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system",
                 "content": "You are my assistant, who helps me to improve my statements before I publish them on the internet. You"
                            "will receive a transcript of my statement and will be asked to do some actions basing on this transcript."},
                {"role": "user",
                 "content": prompt}
            ]
        )
        answer = completion.choices[0].message.content
        return answer


