import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("HUGGINGFACE_API_KEY")

headers = {
    "Authorization": f"Bearer {api_key}"
}

def query(prompt):
    response = requests.post(
        "https://api-inference.huggingface.co/models/tiiuae/falcon-rw-1b",  # lighter model
        headers=headers,
        json={"inputs": prompt}
    )
    return response.json()[0]["generated_text"]

# Example usage
print(query("Write an email to resign from my job."))
