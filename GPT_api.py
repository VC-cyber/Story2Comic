import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv('API_KEY')

def summarize_to_script(story):
    response = openai.chat.completions.create(
        model="gpt-4",  # Or use "gpt-3.5-turbo" if GPT-4 is unavailable
        messages=[
            {"role": "system", "content": "Convert the following story into a comic script with dialogue."},
            {"role": "user", "content": story}
        ],
        max_tokens=1500,  # Adjust based on the expected script length
        temperature=0.7,  # Creativity level
        n=1
    )
    script = response.choices[0].message.content
    return script

with open("story.txt", "r") as file:
    story = file.read()

script = summarize_to_script(story)
print(script)
