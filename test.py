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

response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {
      "role": "system",
      "content": "Summarize content you are provided with for a second-grade student."
    },
    {
      "role": "user",
      "content": "Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. It is named after the Roman god Jupiter.[19] When viewed from Earth, Jupiter can be bright enough for its reflected light to cast visible shadows,[20] and is on average the third-brightest natural object in the night sky after the Moon and Venus."
    }
  ],
  temperature=0.7,
  max_tokens=64,
  top_p=1
)

print(response)