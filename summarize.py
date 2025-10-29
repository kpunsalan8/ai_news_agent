from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def summarize_articles(articles):
    joined_text = "\n\n".join(
        [f"Title: {a['title']}\nDescription: {a['description']}" for a in articles]
    )

    prompt = f"""Summarize these articles into a short, well-written daily digest for a tech professional. 
    Focus on key themes, important developments, and insights:\n\n{joined_text}"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant", 
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content