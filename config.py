import requests
import os

API_URL = "API_URL = API_URL = "https://api-inference.huggingface.co/models/username/my_gf2"  # Replace with your model
headers = {"Authorization": f"Bearer {os.getenv('HF_API_KEY')}"}

def query(prompt):
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
    try:
        return response.json()[0]["generated_text"]
    except Exception as e:
        print("Error:", e)
        print("Response content:", response.text)
        return "Sorry, something went wrong with the AI response."
