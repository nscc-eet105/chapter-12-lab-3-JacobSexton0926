#Jacob Sexton 7/8/25

import requests

API_KEY = "79c07b0ffb5671862c2bf8f17fa8fb96"

zip_code = input("Enter your zip code: ")
country_code = "us"

url = f"http://api.openweathermap.org/data/2.5/weather?zip={zip_code},{country_code}&appid={API_KEY}&units=imperial"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    city = data['name']
    conditions = data['weather'][0]['description'].title()
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    wind_deg = data['wind']['deg']

    print(f"\nCurrent Weather for {city}:")
    print(f"Conditions: {conditions}")
    print(f"Temperature: {round(temp)} Degrees")
    print(f"Feels Like: {round(feels_like)} Degrees")
    print(f"Humidity: {humidity}%")
    print(f"Wind: {wind_speed} knots @ {wind_deg} degrees")

else:
    print("Error retrieving weather data. Please check your zip code and API key.")
