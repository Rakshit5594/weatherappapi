# Import the necessary modules
import datetime  # For working with date and time
import requests  # For making HTTP requests to get data from web APIs

# Define constants for the API
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"  # Base URL for the OpenWeatherMap API
API_KEY = "your-api-key"  # Your personal API key for authenticating with the OpenWeatherMap API
CITY = input("Enter your city: ")  # Prompt the user to input the city name for which they want the weather info

# Function to convert temperature from Kelvin to Celsius and Fahrenheit
def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15  # Convert Kelvin to Celsius
    farenhite = celsius * (9/5) + 32  # Convert Celsius to Fahrenheit
    return celsius, farenhite  # Return both Celsius and Fahrenheit values

# Build the full API URL by adding the city, API key, and base URL together
url = BASE_URL + "&appid=" + API_KEY + "&q=" + CITY

# Send a GET request to the API and convert the response to JSON format
response = requests.get(url).json()

# Extract the temperature from the API response (in Kelvin) and convert it to Celsius and Fahrenheit
temp_kelvin = response['main']['temp']
temp_celcius, temp_farenhite = kelvin_to_celsius(temp_kelvin)

# Extract the "feels like" temperature and convert it to Celsius and Fahrenheit
feels_like = response['main']['feels_like']
feels_like_celcius, feels_like_farehite = kelvin_to_celsius(feels_like)

# Get additional weather details from the response
weather_description = response['weather'][0]['description']  # Short description of the weather (e.g., "clear sky")
wind_speed = response['wind']['speed']  # Wind speed in meters per second (m/s)
pressure = response['main']['pressure']  # Atmospheric pressure in hPa (hectopascals)
humidity = response['main']['humidity']  # Humidity percentage

# Convert the Unix timestamp for sunrise and sunset times to a readable format
sunrise_time = datetime.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = datetime.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

# Print all the weather information in a user-friendly format
print(f"Temperature: {temp_celcius:.2f}C or {temp_farenhite:.2f}F")  # Temperature in Celsius and Fahrenheit
print(f"Feels like: {feels_like_celcius:.2f}C or {feels_like_farehite:.2f}F")  # Feels like temperature
print(f"Description: {weather_description}")  # Short description of the weather
print(f"Wind Speed: {wind_speed}m/s")  # Wind speed
print(f"Pressure: {pressure}hPa")  # Atmospheric pressure
print(f"Humidity: {humidity}%")  # Humidity level
print(f"Sunrise Time: {sunrise_time}")  # Local sunrise time
print(f"Sunset Time: {sunset_time}")  # Local sunset time
