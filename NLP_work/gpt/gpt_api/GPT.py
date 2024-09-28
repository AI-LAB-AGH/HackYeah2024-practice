from openai import OpenAI
import api_key
from prompts import *

client = OpenAI(api_key=api_key.get_api_key())
MODEL = "gpt-4o"


with open("./../../../data/video-transcription-manually/TXT_HY_2024_film_05.txt", 'r', encoding='utf-8') as file:
    transcript = file.read()


def query_gpt(prompt):
    completion = client.chat.completions.create(
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


answers = {
    "filler_words": query_gpt(filler_word_prompt(transcript)),
    "repeated_words": query_gpt(repetitions_prompt(transcript)),
    "complex_words": query_gpt(complex_words_prompt_pl(transcript)),
    "jargon_words": query_gpt(jargon_words_prompt_pl(transcript)),
    "non-polish_words": query_gpt(non_polish_words_prompt(transcript)),
    "non-existing_words": query_gpt(non_existing_words_prompt(transcript)),
    "passive_voice": query_gpt(passive_voice_prompt_pl(transcript)),
    "change_of_topic": query_gpt(unexpected_topic_change_prompt(transcript)),
    "numbers": query_gpt(unusual_numbers_prompt(transcript))
}

for key in answers:
    print(key, ":\n", answers[key])




