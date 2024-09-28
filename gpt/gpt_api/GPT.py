from openai import OpenAI
import api_key

client = OpenAI(api_key=api_key.get_api_key())
MODEL = "gpt-4o"


with open("transkrypt1.txt", 'r', encoding='utf-8') as file:
    sentence = file.read()

def query_gpt(prompt):
    completion = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system",
             "content": "You are my assistant, who helps me to improve my statements before I publish them on the internet."},
            {"role": "user",
             "content": prompt}
        ]
    )
    answer = completion.choices[0].message.content
    return answer



print(answer)