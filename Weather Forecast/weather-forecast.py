# Import beautifulsoup library
import requests
from bs4 import BeautifulSoup

# Fetch weather data
api_key = 'f760e8f15a7cfc73bbdf3f9e8a4d6662'
city = 'Oulu'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)

if response.status_code == 200:
    weather_data = response.json()
else:
    print(f"Failed to retrieve weather data. Status code: {response.status_code}")
    exit()

# Extract data
temperature = weather_data['main']['temp']
temperature_celsius = temperature - 273.15

humidity = weather_data['main']['humidity']
weather_condition = weather_data['weather'][0]['description']

print(f"Temperature: {temperature_celsius}°C")
print(f"Humidity: {humidity}%")
print(f"Weather Condition: {weather_condition}")