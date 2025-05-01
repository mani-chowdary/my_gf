import os
from config import apikey
import openai

openai.api_key = apikey

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # or "gpt-4" if you have access
    messages=[
        {"role": "user", "content": "Write an email to my boss for resignation?"}
    ],
    temperature=0.7,
    max_tokens=256
)

print(response.choices[0].message['content'])
