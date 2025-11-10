"""
Weather fetcher with robust fallback.

Flow:
 1. Try Visual Crossing (DEMO_KEY).
 2. If Visual Crossing fails (invalid key or other error), fallback to:
    - Geocode city using Nominatim (OpenStreetMap) — no key required.
    - Get current weather from Open-Meteo using the lat/lon — no key required.
 3. Save to weather_data.csv while avoiding duplicate city entries.

Requires: requests
pip install requests
"""

import requests
import csv
import os
import time

# -----------------------------
# CONFIGURATION
# -----------------------------
API_KEY = "DEMO_KEY"  # Visual Crossing demo key (may sometimes be rejected)
VC_BASE_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
CSV_FILE = "weather_data.csv"

# Nominatim and Open-Meteo endpoints (no API key)
NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"
OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"


# -----------------------------
# HELPER: save to CSV (no duplicates)
# -----------------------------
def save_to_csv(weather_data):
    if not weather_data:
        return
    try:
        file_exists = os.path.isfile(CSV_FILE)
        existing_cities = set()

        if file_exists:
            with open(CSV_FILE, mode="r", newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                existing_cities = {row["city"] for row in reader}

        if weather_data["city"] not in existing_cities:
            with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as f:
                fieldnames = ["city", "temperature", "description", "source"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                if not file_exists:
                    writer.writeheader()
                writer.writerow(weather_data)
            print(f"💾 Data saved for {weather_data['city']}.")
        else:
            print(f"⚠️ Duplicate entry skipped for {weather_data['city']}.")
    except IOError as e:
        print(f"File I/O error: {e}")


# -----------------------------
# TRY VISUAL CROSSING (demo)
# -----------------------------
def get_weather_visualcrossing(city):
    try:
        url = f"{VC_BASE_URL}{city}?unitGroup=metric&key={API_KEY}&contentType=json"
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            # Defensive extraction
            cc = data.get("currentConditions") or {}
            temp = cc.get("temp")
            desc = cc.get("conditions") or cc.get("icon") or "No description"
            if temp is None:
                raise KeyError("Missing temperature in Visual Crossing response")
            return {"city": city.title(), "temperature": temp, "description": desc, "source": "VisualCrossing"}
        # Treat authentication or other failures as failure to use fallback
        if resp.status_code in (401, 403):
            # Invalid API key or forbidden
            print("VisualCrossing: Invalid API key or access forbidden.")
            return None
        # Other 4xx/5xx
        print(f"VisualCrossing returned status {resp.status_code}. Falling back.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"VisualCrossing network error: {e}. Falling back.")
        return None
    except Exception as e:
        print(f"VisualCrossing parsing error: {e}. Falling back.")
        return None


# -----------------------------
# FALLBACK: NOMINATIM (geocode) + OPEN-METEO (current weather)
# -----------------------------
def geocode_city_nominatim(city, pause=1.0):
    """
    Returns (lat, lon) for city using Nominatim.
    Nominatim asks for a User-Agent; include one.
    """
    try:
        params = {"q": city, "format": "json", "limit": 1}
        headers = {"User-Agent": "WeatherLab/1.0 (your_email@example.com)"}
        resp = requests.get(NOMINATIM_URL, params=params, headers=headers, timeout=10)
        if resp.status_code != 200:
            print(f"Nominatim geocoding failed: status {resp.status_code}")
            return None
        results = resp.json()
        if not results:
            print(f"Nominatim: city '{city}' not found.")
            return None
        lat = float(results[0]["lat"])
        lon = float(results[0]["lon"])
        # Respect usage policy: small pause between calls
        time.sleep(pause)
        return lat, lon
    except requests.exceptions.RequestException as e:
        print(f"Nominatim network error: {e}")
        return None
    except Exception as e:
        print(f"Nominatim parsing error: {e}")
        return None


def get_weather_open_meteo(lat, lon):
    """
    Calls Open-Meteo's current weather endpoint.
    Returns {"temperature": ..., "description": ...}
    """
    try:
        params = {
            "latitude": lat,
            "longitude": lon,
            "current_weather": "true",
            # open-meteo also offers weathercode; we will turn the code into a basic text
            "timezone": "auto",
        }
        resp = requests.get(OPEN_METEO_URL, params=params, timeout=10)
        if resp.status_code != 200:
            print(f"Open-Meteo failed: status {resp.status_code}")
            return None
        data = resp.json()
        cw = data.get("current_weather")
        if not cw:
            print("Open-Meteo: no current_weather in response.")
            return None
        temp = cw.get("temperature")
        wcode = cw.get("weathercode")
        desc = weathercode_to_text(wcode)
        return {"temperature": temp, "description": desc}
    except requests.exceptions.RequestException as e:
        print(f"Open-Meteo network error: {e}")
        return None
    except Exception as e:
        print(f"Open-Meteo parsing error: {e}")
        return None


def weathercode_to_text(code):
    """
    Convert Open-Meteo weathercode into a human readable short description.
    This mapping is a small subset for demo purposes.
    """
    try:
        code = int(code)
    except Exception:
        return "Unknown"
    mapping = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        71: "Slight snow",
        73: "Moderate snow",
        75: "Heavy snow",
        80: "Rain showers",
        81: "Moderate rain showers",
        82: "Violent rain showers",
        95: "Thunderstorm",
    }
    return mapping.get(code, f"Weather code {code}")


# -----------------------------
# HIGH LEVEL: get_weather (tries VC then fallback)
# -----------------------------
def get_weather(city):
    city = city.strip()
    if not city:
        print("No city provided.")
        return None

    # Try Visual Crossing first
    vc = get_weather_visualcrossing(city)
    if vc:
        return vc

    # Fallback: geocode + open-meteo
    geo = geocode_city_nominatim(city)
    if not geo:
        # Final fallback: return a mock result so program can proceed (optional)
        print("Falling back to mock data (demo).")
        return {"city": city.title(), "temperature": 25.0, "description": "Clear (mock)", "source": "Mock"}

    lat, lon = geo
    om = get_weather_open_meteo(lat, lon)
    if om:
        return {"city": city.title(), "temperature": om["temperature"], "description": om["description"], "source": "Open-Meteo"}
    else:
        print("Open-Meteo failed; using mock data.")
        return {"city": city.title(), "temperature": 25.0, "description": "Clear (mock)", "source": "Mock"}


# -----------------------------
# MAIN
# -----------------------------
if __name__ == "__main__":
    city = input("Enter city name: ").strip()
    weather_data = get_weather(city)
    if weather_data:
        print(f"✅ {weather_data['city']} - Temperature: {weather_data['temperature']}°C, Weather: {weather_data['description']} (source: {weather_data.get('source')})")
    save_to_csv(weather_data)
