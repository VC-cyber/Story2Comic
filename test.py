import os
from openai import OpenAI
import openai
from dotenv import load_dotenv
import os

load_dotenv()
my_api_key = os.getenv('API_KEY')

client = OpenAI(
    # This is the default and can be omitted
    api_key=my_api_key,
)

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message.content)