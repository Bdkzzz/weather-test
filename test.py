import requests
import json
import tkinter as tk

def get_weather_data():
    city = input("Enter the city name: ")
    api_key = '3a97089cb79affdfc9b0f748d7a4e9b2'  # Replace with your actual API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return city, data
    except requests.exceptions.RequestException as e:
        print(f"Error: An error occurred while fetching weather data: {e}")
        return None, None
    except KeyError as e:
        print(f"Error: Missing key in API response: {e}")
        return None, None

def display_weather_gui(city, weather_data):
    if weather_data:
        temperature = weather_data['main']['temp'] - 273.15
        humidity = weather_data['main']['humidity']
        description = weather_data['weather'][0]['description']
        wind_speed = weather_data['wind']['speed']
        pressure = weather_data['main']['pressure']
        visibility = weather_data['visibility']

        window = tk.Tk()
        window.title("Weather App")

        city_label = tk.Label(window, text=f"City: {city}")
        temperature_label = tk.Label(window, text=f"Temperature: {temperature:.2f}°C")
        humidity_label = tk.Label(window, text=f"Humidity: {humidity}%")
        description_label = tk.Label(window, text=f"Description: {description}")
        wind_speed_label = tk.Label(window, text=f"Wind Speed: {wind_speed} m/s")
        pressure_label = tk.Label(window, text=f"Pressure: {pressure} hPa")
        visibility_label = tk.Label(window, text=f"Visibility: {visibility} m")

        city_label.pack()
        temperature_label.pack()
        humidity_label.pack()
        description_label.pack()
        wind_speed_label.pack()
        pressure_label.pack()
        visibility_label.pack()

        window.mainloop()
    else:
        print("No weather data found for the specified city.")

if __name__ == "__main__":
    city, weather_data = get_weather_data()
    if weather_data:
        display_weather_gui(city, weather_data)
    else:
        print("No weather data found for the specified city.")