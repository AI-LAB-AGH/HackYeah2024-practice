from openai import OpenAI
import api_key

client = OpenAI(api_key=api_key.get_api_key())
MODEL = "gpt-4o"


with open("transkrypt1.txt", 'r', encoding='utf-8') as file:
    transcript = file.read()

answers = {}

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

filler_words_prompt = ("Transcript which I provide at the end of this prompt may contain some filler words. The definition of filler"
                       "word is: "
                       "'Filler words are words such as \"um,\" \"ah,\" \"hmm,\" \"like,\" \"you know,\" and \"alright\" "
                       "that are used to give the speaker time to think, express uncertainty or make something awkward feel less awkward, "
                       "or as a verbal tick. Filler words are also known as vocal disfluencies or hesitations.' "
                       "You have to find these filler words in the transcript. In your response, write only these filler words, one per line."
                       f"Here is the transcript: {transcript}")



