import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("NEWS_API_KEY")

def fetch_articles(topic):
    url = f"https://newsapi.org/v2/everything?q={topic}&language=en&sortBy=publishedAt&pageSize=5&apiKey={API_KEY}"
    response = requests .get(url)
    data = response.json()
    articles = data.get("articles", [])

    return [
        {"title": a["title"], "description": a["description"], "url": a["url"]}
        for a in articles
    ]

# print(fetch_articles("AI ethics"))