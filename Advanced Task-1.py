#importing neccessary modules or packages

import requests
import matplotlib.pyplot as plt

# API key from open weather
API_KEY = 'cbe0575b118d350df66a38fec470c4e0'
CITY = 'Hyderabad'
URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}'

response = requests.get(URL)
data = response.json()

print("City name:",CITY)

# Extract relevant data
temperature = data['main']['temp']
pressure = data['main']['pressure']
humidity = data['main']['humidity']
weather_description = data['weather'][0]['description']

print(f'Temperature: {temperature}')
print(f'Pressure: {pressure}')
print(f'Humidity: {humidity}')
print(f'Description: {weather_description}')

labels = ['Temperature', 'Pressure', 'Humidity']
values = [temperature, pressure, humidity]

#visualizing the above data 
plt.bar(labels, values)
plt.xlabel('Weather Metrics')
plt.ylabel('Values')
plt.title('Current Weather Data')
plt.show()
