import requests
API_KEY = "4737166cab043120dee085ec40a78c0c"

def get_weather(city):

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}"
        f"&appid={API_KEY}"
        f"&units=metric"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()
    print(data)
    return {
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "condition": data["weather"][0]["main"],

        # Approximate annual rainfall (mm/year)
        "rainfall": round(data.get("rain", {}).get("1h", 0) * 365 * 24, 2)
    }