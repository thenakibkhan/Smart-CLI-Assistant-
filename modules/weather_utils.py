import requests

def get_weather():
    api_key = '24ee7116bcdc2e9aaf513afe70898a04'
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
