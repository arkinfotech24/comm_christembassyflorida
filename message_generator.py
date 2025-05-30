import openai
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_devotional(topic):
    prompt = f"Write a 250-word weekly devotional for Christ Embassy Church on '{topic}'. Include a Bible verse and a call to invite others to church this Sunday."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant for a church."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']