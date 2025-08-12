from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient, errors
from dotenv import load_dotenv
import os
import requests
import time

# Load environment variables from .env.dev or .env
load_dotenv()

app = Flask(__name__)
CORS(app)

# MongoDB connection (read from env)
MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongodb:27017/newsdb_dev")
DB_NAME = MONGO_URI.rsplit("/", 1)[-1]  # Extract db name from URI

# Wait for MongoDB to be ready
for i in range(10):
    try:
        mongo_client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=2000)
        mongo_client.server_info()  # Force connection
        print("✅ Connected to MongoDB")
        break
    except errors.ServerSelectionTimeoutError as e:
        print(f"⏳ MongoDB not ready yet, retrying ({i+1}/10)...")
        time.sleep(3)
else:
    raise RuntimeError("❌ Could not connect to MongoDB after several attempts.")

db = mongo_client[DB_NAME]
news_collection = db["news"]

# News API settings
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_API_URL = "https://newsapi.org/v2/top-headlines"
COUNTRY = os.getenv("NEWS_COUNTRY", "us")

@app.route("/api/news", methods=["GET"])
def get_news():
    try:
        params = {
            "country": COUNTRY,
            "apiKey": NEWS_API_KEY
        }
        response = requests.get(NEWS_API_URL, params=params)
        response.raise_for_status()

        articles = response.json().get("articles", [])

        # Store new articles in MongoDB
        for article in articles:
            if not news_collection.find_one({"title": article["title"]}):
                news_collection.insert_one({
                    "title": article["title"],
                    "content": article.get("description", ""),
                    "url": article.get("url", ""),
                    "source": article.get("source", {}).get("name", ""),
                    "publishedAt": article.get("publishedAt", "")
                })

        # Return sorted news list
        news_list = list(news_collection.find({}, {"_id": 0}).sort("publishedAt", -1))
        return jsonify(news_list)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.getenv("BACKEND_PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
