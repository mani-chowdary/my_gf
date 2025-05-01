import speech_recognition as sr
import os
import webbrowser
from config import generator
import datetime
import random

chatStr = ""

def chat(query):
    global chatStr
    chatStr += f"User: {query}\nAI: "
    response = generator(chatStr, max_length=256, do_sample=True, temperature=0.7)
    output = response[0]["generated_text"]
    say(output)
    chatStr += output + "\n"
    return output

def ai(prompt):
    text = f"Hugging Face Response for Prompt: {prompt} \n *************************\n\n"
    response = generator(prompt, max_length=256, do_sample=True, temperature=0.7)
    output = response[0]["generated_text"]
    text += output

    if not os.path.exists("HuggingFace"):
        os.mkdir("HuggingFace")
    with open(f"HuggingFace/{''.join(prompt.split()[:5])}.txt", "w") as f:
        f.write(text)

def say(text):
    os.system(f'say "{text}"')  # Optional: Change for cross-platform compatibility

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception:
            return "Some Error Occurred. Sorry from Jarvis"

if __name__ == '__main__':
    print('Welcome to Jarvis A.I')
    say("Jarvis A.I")
    while True:
        print("Listening...")
        query = takeCommand()
        if "quit" in query.lower():
            exit()
        elif "reset chat" in query.lower():
            chatStr = ""
        elif "using artificial intelligence" in query.lower():
            ai(query)
        else:
            print("Chatting...")
            chat(query)
