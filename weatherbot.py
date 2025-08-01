import requests

API_KEY = "YOUR_API_KEY"  # Your OpenWeatherMap API key

def get_weather(city):
    base_url = f"http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(base_url, params=params)
    data = response.json()

    if data.get("cod") != 200:
        return f"❌ Error: {data.get('message', 'City not found.')}"
    
    weather = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    return f"🌦 Weather in {city.title()}:\n - {weather}\n - Temp: {temp}°C (feels like {feels_like}°C)"

def weather_bot():
    print("🌤️ Welcome to Weather Bot!")
    while True:
        city = input("🏙️ Enter city name (or 'exit'): ").strip()
        if city.lower() == "exit":
            print("👋 Goodbye!")
            break
        print(get_weather(city))

# Run code
weather_bot()
