import os
import requests
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

NEWSDATA_API_KEY = os.getenv("NEWSDATA_API_KEY")
TWILIO_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE = os.getenv("TWILIO_PHONE_NUMBER")
MY_PHONE = os.getenv("MY_PHONE_NUMBER")

def simple_summarize(text):
    sentences = text.split(". ")
    return ". ".join(sentences[:3]) + "." if len(sentences) > 2 else text

categories = {
    "Technology": "technology",
    "Politics": "politics",
    "Sports": "sports",
    "Economy": "business",
    "Industries": "world"
}

def fetch_and_summarize():
    summaries = []
    for name, category in categories.items():
        url = f"https://newsdata.io/api/1/news?apikey={NEWSDATA_API_KEY}&country=in&language=en&category={category}"
        res = requests.get(url).json()
        articles = res.get("results", [])

        news_texts = []
        for a in articles[:3]:
            if a.get("title") and a.get("description"):
                news_texts.append(f"{a['title']}. {a['description']}")

        if news_texts:
            joined = " ".join(news_texts)[:1000]
            summary = simple_summarize(joined)
            summaries.append(f"🔹 *{name}*\n{summary}")

    return "\n\n".join(summaries)

def send_whatsapp(summary_text):
    client = Client(TWILIO_SID, TWILIO_AUTH)
    client.messages.create(
        body="📰 *Daily India News Digest*\n\n" + summary_text,
        from_=TWILIO_PHONE,
        to=MY_PHONE
    )
    print("✅ WhatsApp message sent!")

if __name__ == "__main__":
    digest = fetch_and_summarize()
    print("SUMMARY PREVIEW:\n", digest)
    send_whatsapp(digest)
