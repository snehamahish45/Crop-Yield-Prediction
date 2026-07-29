import requests
API_KEY = "4737166cab043120dee085ec40a78c0c"

def get_weather(city):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()

    return {
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "condition": data["weather"][0]["main"]
    }


def get_forecast(city):
    url = (
        f"https://api.openweathermap.org/data/2.5/forecast"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return []

    data = response.json()

    forecast = []

    for item in data["list"][::8][:5]:
        forecast.append({
            "date": item["dt_txt"].split()[0],
            "temp": round(item["main"]["temp"], 2),
            "condition": item["weather"][0]["main"],
            "icon": item["weather"][0]["icon"]
        })

    return forecast