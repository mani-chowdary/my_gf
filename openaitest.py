from config import generator

response = generator("Write an email to my boss for resignation?", max_length=256, do_sample=True, temperature=0.7)
print(response[0]["generated_text"])
