import requests
import json

# Replace 'YOUR_API_KEY' with your actual API key
api_key = '3a97089cb79affdfc9b0f748d7a4e9b2'
city = 'Sudan'

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

try:
  response = requests.get(url)
  response.raise_for_status()  # Raise an exception for unsuccessful requests

  data = response.json()

  # Extract relevant information
  temperature = data['main']['temp']
  humidity = data['main']['humidity']
  description = data['weather'][0]['description']

  # Convert temperature to Celsius (optional)
  celsius = temperature - 273.15

  print(f"Temperature: {celsius:.2f}°C")
  print(f"Humidity: {humidity}%")
  print(f"Weather Description: {description}")

except requests.exceptions.RequestException as e:
  print(f"Error: An error occurred while fetching weather data: {e}")

except KeyError as e:
  print(f"Error: Missing key in API response: {e}")