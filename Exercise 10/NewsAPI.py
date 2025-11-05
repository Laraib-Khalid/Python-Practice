import requests

API_KEY = "744c9151b81f42c49343654a1dbf5c6f"
BASE_URL = "https://newsapi.org/v2/everything"

def get_news(topic):
    params = {
        "q": topic,
        "apiKey": API_KEY,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 5
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if data.get("status") != "ok":
        print(f"❌ Failed to fetch news for: {topic}")
        print("Reason:", data.get("message"))
        return

    print(f"\n📌 Top News for: {topic.upper()}")
    print("-" * 60)

    for idx, article in enumerate(data.get("articles", []), start=1):
        print(f"\n📰 {idx}. {article['title']}")
        print(f"Source: {article['source']['name']}")
        print(f"Published: {article['publishedAt']}")

        # Article summary if available
        description = article.get("description", "No description available.")
        content = article.get("content", "Full content not provided.")

        print(f"\n📄 Description:\n{description}")
        print(f"\n🧾 Content Preview:\n{content}")

        print(f"\n🔗 Read Full Article: {article['url']}")
        print("-" * 60)


# User chooses topic like button selection
print("Choose a topic:")
topics = ["technology", "sports", "health", "business", "science"]
for idx, t in enumerate(topics, start=1):
    print(f"{idx}. {t.capitalize()}")

# ✅ Keep asking until valid choice (1-5)
while True:
    try:
        choice = int(input("\nEnter topic number (1-5): "))
        if 1 <= choice <= len(topics):
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 5.")
    except ValueError:
        print("❌ Invalid input. Only numbers allowed (1-5).")
selected_topic = topics[choice - 1]

get_news(selected_topic)
