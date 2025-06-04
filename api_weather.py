# Import required modules
import requests, json

# Enter your OpenWeatherMap API key here
api_key = "7fadc892ffe24acaade184301250306"  # Replace with your actual API key

# Base URL of the API
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Get city name from user input
city_name = input("Enter city name: ")

# Complete URL for the API request
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

# Send GET request
response = requests.get(complete_url)

# Convert the response into JSON format
data = response.json()

# Check the HTTP status code in JSON response
if data["cod"] != "404":
    main = data["main"]
    weather = data["weather"][0]

    # Extract values
    temp_kelvin = main["temp"]
    temp_celsius = round(temp_kelvin - 273.15, 2)  # Optional: Convert to Celsius
    pressure = main["pressure"]
    humidity = main["humidity"]
    description = weather["description"]

    # Display results
    print(f"\nWeather in {city_name.title()}:\n"
          f"Temperature: {temp_kelvin}K ({temp_celsius}°C)\n"
          f"Pressure: {pressure} hPa\n"
          f"Humidity: {humidity}%\n"
          f"Description: {description.capitalize()}")
else:
    print("City Not Found ")
