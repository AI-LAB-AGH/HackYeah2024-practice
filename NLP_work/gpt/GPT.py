from openai import OpenAI
from . import prompts
from . import api_key
from . import textanalyzer

CLIENT = OpenAI(api_key=api_key.get_api_key())
MODEL = "gpt-4o"


class GPT:

    def get_tasks_results(self, transcript):
        return {
            "filler_words": self.query_gpt(prompts.filler_word_prompt(transcript)),
            "repeated_words": self.query_gpt(prompts.repetitions_prompt(transcript)),
            "complex_words": textanalyzer.TextAnalyzer().complex_word_searcher(transcript),
            "complex_sentences": textanalyzer.TextAnalyzer().complex_sentence_searcher(transcript),
            "jargon_words": textanalyzer.TextAnalyzer().jargon_searcher(transcript),
            "non-polish_words": self.query_gpt(prompts.non_polish_words_prompt(transcript)),
            "non-existing_words": self.query_gpt(prompts.non_existing_words_prompt(transcript)),
            "passive_voice": textanalyzer.TextAnalyzer().passive_form_verifier_spacy(transcript),
            "change_of_topic": self.query_gpt(prompts.unexpected_topic_change_prompt(transcript)),
            "numbers": self.query_gpt(prompts.unusual_numbers_prompt(transcript)),
            "target_group": self.query_gpt(prompts.target_group_prompt(transcript)),
            "questions": self.query_gpt(prompts.valid_questions_prompt(transcript)),
            "important_phrases": textanalyzer.TextAnalyzer().important_phrases_searcher(transcript)
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


