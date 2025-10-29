from fetch_news import fetch_articles
from summarize import summarize_articles

def main():
    topic = "AI ethics"
    print(f"Fetching latest articles on: {topic}")
    articles = fetch_articles(topic)

    print("\nSummarizing...")
    summary = summarize_articles(articles)

    print("\n📰 Daily Digest:")
    print(summary)

if __name__ == "__main__":
    main()