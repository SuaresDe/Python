import requests
import json

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data


def display_weather(data):
    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        print(f"City: {data['name']}")
        print(f"Temperature: {main['temp']}°C")
        print(f"Weather: {weather['description']}")
        print(f"Humidity: {main['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    else:
        print("City not found!")

if __name__ == "__main__":
    with open("api_key_ow.json", "r") as file:
        data = json.load(file)

    api_key = data["api_key"]
    city = input("Enter city name: ")
    weather_data = get_weather(api_key, city)
    display_weather(weather_data)