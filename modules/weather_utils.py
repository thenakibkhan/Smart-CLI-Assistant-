import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

api_key = os.getenv('NEWS_API_KEY')

api_key = os.getenv('WEATHER_API_KEY')

def get_weather():
    city = input("Enter city name : ").strip()

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        temp = data['main']['temp']
        humidity = data['main']['humidity']
        wind = data['wind']['speed']
        condition = data['weather'][0]['description']

        print(f"\n🌤️ Weather in {city.title()}:")
        print(f"🌡️ Temperature: {temp}°C")
        print(f"🌥️ Condition: {condition.capitalize()}")
        print(f"💧 Humidity: {humidity}%")
        print(f"🌬️ Wind Speed: {wind} m/s\n")

    else:
        print("❌ Couldn't fetch weather. Check the city name or your API key.")
