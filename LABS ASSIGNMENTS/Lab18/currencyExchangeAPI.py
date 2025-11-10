import requests
import time
import logging

logging.basicConfig(filename="error_log.txt", level=logging.ERROR,
                    format="%(asctime)s - %(levelname)s - %(message)s")

API_KEY = "demo1234apikey"  # for display only

def get_exchange_rate(from_currency, to_currency, retries=3):
    url = f"https://open.er-api.com/v6/latest/{from_currency}"

    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()

            # Check if API returned a valid rate
            if "rates" not in data or to_currency not in data["rates"]:
                raise ValueError("Invalid currency code or missing rate data.")

            return data["rates"][to_currency]

        except (requests.exceptions.RequestException, ValueError) as e:
            logging.error(f"Attempt {attempt}: Failed - {e}")
            print(f"⚠️ Attempt {attempt} failed. Retrying...")
            time.sleep(2)

    print("❌ Failed to fetch exchange rate after 3 attempts. Check error_log.txt.")
    return None


def convert_currency(amount, from_currency, to_currency):
    print(f"\nUsing Demo API Key: {API_KEY}")
    rate = get_exchange_rate(from_currency.upper(), to_currency.upper())

    if rate:
        converted = amount * rate
        print(f"\n💱 {amount:.2f} {from_currency.upper()} = {converted:.2f} {to_currency.upper()}")
    else:
        print("Conversion failed due to API or network issues.")


if __name__ == "__main__":
    print("=== Currency Converter (Demo API with Key Display) ===")
    try:
        amount = float(input("Enter amount: "))
        from_currency = input("Enter source currency (e.g., USD): ").strip().upper()
        to_currency = input("Enter target currency (e.g., EUR): ").strip().upper()

        convert_currency(amount, from_currency, to_currency)
    except ValueError:
        print("❌ Invalid input. Please enter valid numbers and currency codes.")
