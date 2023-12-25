import requests
from datetime import datetime

# OpenWeatherMap API key
api_key='4dac143db9520d5f0d5053625e79815b'  # Replace with your actual API key

def get_weather(api_key, city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # You can change this to "imperial" for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            weather_description = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            result = (
                f"The weather in {city} is {weather_description}. "
                f"The temperature is {temperature}°C, humidity is {humidity}%, "
                f"and wind speed is {wind_speed} m/s."
            )
        else:
            result = f"Failed to fetch weather data. Error: {data['message']}"
    except Exception as e:
        result = f"Error: {e}"

    return result

# Example of using the get_weather function
city_name = "Karachi,PK"  # You can replace this with any other city name
weather_result = get_weather(api_key, city_name)
print(weather_result)
