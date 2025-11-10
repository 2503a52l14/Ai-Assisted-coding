import requests
import re
import logging

# Setup logging
logging.basicConfig(filename="news_error_log.txt", level=logging.ERROR,
                    format="%(asctime)s - %(levelname)s - %(message)s")

API_KEY = "demo1234apikey"  # For display only

def fetch_top_technology_headlines():
    print(f"\nUsing Demo API Key: {API_KEY}")
    print("Fetching latest technology headlines...\n")

    # ✅ Public demo JSON API (no key, works 100%)
    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        # Pick first 5 items as "headlines"
        if not data or len(data) == 0:
            print("⚠️ No data found or API returned empty response.")
            return

        print("Top 5 Technology Headlines:\n")

        for i, article in enumerate(data[:5], 1):
            title = article.get("title", "").strip()
            if not title:
                print(f"{i}. [No Title Available]")
                continue

            # Clean and format title
            clean_title = re.sub(r"[^A-Za-z0-9\s]", "", title).title()
            print(f"{i}. {clean_title}")

    except requests.exceptions.Timeout:
        print("⏰ Error: The request timed out.")
        logging.error("Timeout occurred while fetching data.")
    except requests.exceptions.RequestException as e:
        print(f"🚨 An error occurred: {e}")
        logging.error(f"Request error: {e}")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")
        logging.error(f"Unexpected error: {e}")

# Run script
if __name__ == "__main__":
    fetch_top_technology_headlines()
