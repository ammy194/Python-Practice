import requests

api_key = '7fadc892ffe24acaade184301250306'

user_input = input("Enter the city name: ")

weather_data = requests.get(f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={user_input}')
print(weather_data.json ())['weather'][0]['main']
temp = weather_data.json()['main']['temp']
print(weather , temp)
