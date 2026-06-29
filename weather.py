import json
import urllib.request
import urllib.parse
import urllib.error
from datetime import datetime


def fetch_weather_data(place):
    """
    Sends a request to wttr.in and returns the parsed JSON response.
    Returns None if something goes wrong.
    """
    query = urllib.parse.quote(place)
    endpoint = f"https://wttr.in/{query}?format=j1"

    try:
        with urllib.request.urlopen(endpoint, timeout=10) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as err:
        print(f"[!] Couldn't fetch weather (HTTP {err.code}). Try a different location.")
    except urllib.error.URLError:
        print("[!] No internet connection or the weather service is down.")
    except json.JSONDecodeError:
        print("[!] Received an unreadable response from the server.")
    return None


def show_weather_report(weather_data):
    """Prints a simple weather summary to the console."""
    try:
        current = weather_data["current_condition"][0]
        location_info = weather_data["nearest_area"][0]

        city = location_info["areaName"][0]["value"]
        country = location_info["country"][0]["value"]

        condition = current["weatherDesc"][0]["value"]
        temp_c = current["temp_C"]
        temp_f = current["temp_F"]
        humidity = current["humidity"]
        wind_kmph = current["windspeedKmph"]
        wind_dir = current["winddir16Point"]
        pressure = current["pressure"]

        timestamp = datetime.now().strftime("%d %b %Y, %I:%M %p")

        print("\n+" + "-" * 38 + "+")
        print(f"|  {city}, {country}".ljust(39) + "|")
        print(f"|  As of: {timestamp}".ljust(39) + "|")
        print("+" + "-" * 38 + "+")
        print(f"|  Sky        : {condition}".ljust(39) + "|")
        print(f"|  Temp       : {temp_c} C / {temp_f} F".ljust(39) + "|")
        print(f"|  Humidity   : {humidity}%".ljust(39) + "|")
        print(f"|  Wind       : {wind_kmph} km/h ({wind_dir})".ljust(39) + "|")
        print(f"|  Pressure   : {pressure} hPa".ljust(39) + "|")
        print("+" + "-" * 38 + "+\n")

    except (KeyError, IndexError):
        print("[!] Unexpected data format - couldn't read weather details.\n")


def run():
    print("=" * 40)
    print("        QUICK WEATHER CHECKER")
    print("=" * 40)
    print("Type a city name or ZIP/postal code.")
    print("Type 'q' to quit.\n")

    while True:
        place = input(">> Location: ").strip()

        if place.lower() == "q":
            print("Stay safe out there. Bye!")
            break

        if not place:
            print("Please type something.\n")
            continue

        print(f"Looking up weather for '{place}'...")
        weather_data = fetch_weather_data(place)

        if weather_data:
            show_weather_report(weather_data)


if __name__ == "__main__":
    run()