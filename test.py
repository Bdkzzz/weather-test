import requests
import json

def get_weather_data():

  city = input("Enter the city name: ")

  api_key = '3a97089cb79affdfc9b0f748d7a4e9b2'

  url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an 1  exception for unsuccessful requests

    data = response.json()
    return city, data  # Return the city name and weather data

  except requests.exceptions.RequestException as e:
    print(f"Error: An error occurred while fetching weather data: {e}")
    return None, None  # Return None on error

  except KeyError as e:
    print(f"Error: Missing key in API response: {e}")
    return None, None  # Return None on error

def display_weather(city, data):
  """
  Args:
    city: The city name for which the weather was fetched.
    data: A dictionary containing the weather data.
  """

  if data:
    temperature = data['main']['temp'] - 273.15
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']
    wind_speed = data['wind']['speed']
    pressure = data['main']['pressure']
    visibility = data['visibility']

    print(f"\nWeather in {city}:")
    print(f"Temperature: {temperature:.2f}°C")
    print(f"Humidity: {humidity}%")
    print(f"Description: {description}")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Pressure: {pressure} hPa")
    print(f"Visibility: {visibility} m")
  else:
    print("No weather data found for the specified city.")

if __name__ == "__main__":
  city, weather_data = get_weather_data()
  display_weather(city, weather_data)