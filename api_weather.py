
import requests, json


api_key = "7fadc892ffe24acaade184301250306" 


base_url = "http://api.openweathermap.org/data/2.5/weather?"


city_name = input("Enter city name: ")


complete_url = base_url + "appid=" + api_key + "&q=" + city_name


response = requests.get(complete_url)

data = response.json()


if data["cod"] == 200:
    main = data["main"]
    weather = data["weather"][0]
    time = data["dt"]
    timezone = data["timezone"]
    
    temp_kelvin = main["temp"]
    temp_celsius = round(temp_kelvin - 273.15, 2)  
    pressure = main["pressure"]
    humidity = main["humidity"]
    description = weather["description"]

    
    print(f"\nWeather in {city_name.title()}:\n"
          f"Temperature: {temp_kelvin}K ({temp_celsius}°C)\n"
          f"Pressure: {pressure} hPa\n"
          f"Humidity: {humidity}%\n"
          f"Description: {description.capitalize()}")
else:
    print("City Not Found ")
