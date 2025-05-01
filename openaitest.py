import openai
from config import apikey

openai.api_key = apikey

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Write an email to my boss for resignation?"}
    ],
    temperature=0.7,
    max_tokens=256
)

print(response.choices[0].message['content'])
