# API-INTEGRATION-AND-DATA-VISUALIZATION

Name: GADAPA NAVEEN KUMAR

Company: CODTECH IT SOLUTIONS

ID: CT0806AW

Domain: Python Programming

Duration: December 2024 to January 2025

Mentor: N.Santosh


Project: API-INTEGRATION-AND-DATA-VISUALIZATION

Overview:

The above program retrieves and visualizes current weather data for the city of Hyderabad using the OpenWeather API and `matplotlib` for visualization. Here's a breakdown of the code:

### 1. **Importing Necessary Modules:**
   - `requests`: To make HTTP requests to the OpenWeather API and fetch the weather data.
   - `matplotlib.pyplot`: To create a bar chart to visualize the weather data.

### 2. **Setting Up the API Request:**
   - `API_KEY`: The key required to authenticate with the OpenWeather API.
   - `CITY`: The name of the city (in this case, Hyderabad).
   - `URL`: A formatted URL that includes the city name and API key, which will be used to make the request to the OpenWeather API.

### 3. **Making an API Request:**
   - `requests.get(URL)`: This sends a GET request to the OpenWeather API using the `URL` defined above.
   - `response.json()`: The response from the API is in JSON format. This line converts the response into a Python dictionary (`data`) that we can easily work with.

### 4. **Extracting Relevant Data:**
   The program extracts the following weather data from the API response:
   - `temperature`: The current temperature in Kelvin (the OpenWeather API returns temperature in Kelvin by default).
   - `pressure`: The atmospheric pressure at sea level in hPa (hectopascals).
   - `humidity`: The humidity percentage of the air.
   - `weather_description`: A textual description of the weather (e.g., clear sky, overcast, etc.).

### 5. **Printing the Weather Information:**
   The program prints the city name and the extracted weather data to the console.

### 6. **Visualizing the Data:**
   - `labels`: A list containing the names of the weather metrics (Temperature, Pressure, and Humidity).
   - `values`: A list containing the corresponding values of each metric (temperature, pressure, and humidity).
   - `plt.bar(labels, values)`: This creates a bar chart where each bar represents one of the weather metrics.
   - `plt.xlabel('Weather Metrics')`: Sets the label for the x-axis.
   - `plt.ylabel('Values')`: Sets the label for the y-axis.
   - `plt.title('Current Weather Data')`: Sets the title of the chart.
   - `plt.show()`: Displays the chart to the user.

### Points to Note:
- The temperature returned by the OpenWeather API is in **Kelvin**. If you want to display it in Celsius or Fahrenheit, you'll need to convert it.
   - Celsius: `temperature_celsius = temperature - 273.15`
   - Fahrenheit: `temperature_fahrenheit = (temperature - 273.15) * 9/5 + 32`
  
- You may also want to add error handling in case the API call fails (e.g., invalid city name, network issues).

### Summary:
This program pulls real-time weather data for Hyderabad, extracts important metrics (temperature, pressure, humidity, description), and visualizes this data in the form of a bar chart.

OUTPUT:

![Screenshot 2025-01-07 163102](https://github.com/user-attachments/assets/9610e5cd-c654-4189-b4b9-cb9be2beedf3)
