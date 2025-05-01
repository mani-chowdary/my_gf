from transformers import pipeline
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("HUGGINGFACE_API_KEY")

generator = pipeline("text-generation", model="HuggingFaceH4/zephyr-7b-beta", token=api_key)

response = generator("Write an email to my boss for resignation?", max_length=256, do_sample=True, temperature=0.7)
print(response[0]["generated_text"])
