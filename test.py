import requests
import json

# Replace 'YOUR_API_KEY' with your actual API key
api_key = '3a97089cb79affdfc9b0f748d7a4e9b2'
city = 'New York'

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)
data = response.json()

# Extract relevant information
temperature = data['main']['temp']
humidity = data['main']['humidity']
description = data['weather'][0]['description']

print(f"Temperature: {temperature}K")
print(f"Humidity: {humidity}%")
print(f"Weather Description: {description}")