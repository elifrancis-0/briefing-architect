import os
from dotenv import load_dotenv
from groq import Groq
import re

load_dotenv()
client = Groq()

# Define the Model ID as a constant for easy configurability
MODEL_ID = "qwen/qwen3-32b"  # <--- Update this if your check_models.py showed something different

with open("transcript.txt", "r") as file:
    transcript = file.read()
    print(f"Transcript Word Count: {len(transcript.split())}")

print(f"Initializing inference with {MODEL_ID}...")

completion = client.chat.completions.create(
    model=MODEL_ID,
    messages=[
        {
            "role": "system",
            "content": "You are an English PhD with masterful summarization skills. You are given a body of text, and you need analyze the context of the text and summarize it accordingly in a way that is easy to understand and follow."
        },
        {
            "role": "user", 
            "content": f"Summarize the following text into a high-level executive briefing with bullet points: {transcript}"
        }
    ],
    temperature=2 
)

with open("briefing.md", "w") as file:
    content = completion.choices[0].message.content

    if '</think>' in content:
        content_new = content.split('</think>')[1].strip()
        file.write(content_new)
    else:
        file.write(content)

print("Inference Response:")
print(completion.choices[0].message.content)