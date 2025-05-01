import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Write an email to my boss for resignation?"}
    ],
    temperature=0.7,
    max_tokens=256
)

print(response.choices[0].message['content'])
