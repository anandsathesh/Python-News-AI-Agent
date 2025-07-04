# 📰 AI News Digest via WhatsApp (Free Setup)

This free project:
- Fetches India news
- Summarizes with Hugging Face (no OpenAI)
- Sends to WhatsApp via Twilio Sandbox (free)
- Schedule daily with PythonAnywhere or Windows Task Scheduler

## 🚀 Setup

1. `pip install -r requirements.txt`
2. Rename `.env.example` to `.env` and add your keys
3. Run: `python daily_news_digest.py`

## 🔁 Schedule Daily

Use [PythonAnywhere.com](https://www.pythonanywhere.com/) to run it daily at 7 AM for free.

env file has api keys for privacy concerns it is not shared here. 
file has the following data .
fill it with your own keys.

NEWSDATA_API_KEY=
TWILIO_ACCOUNT_SID=
TWILIO_AUTH_TOKEN=
TWILIO_PHONE_NUMBER=whatsapp:
MY_PHONE_NUMBER=whatsapp:+91 
