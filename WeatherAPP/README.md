# Project Title: Weather Lookup Application
## Author: Bernard Owusu Sefah
## Date: February 28, 2024
## Overview:
A Python command-line application that allows users to retrieve current weather data for a specified city or zip code using the OpenWeatherMap API.

## Features:
City and Zip Code Lookup:

Supports searching weather details by city name, state code, and country code.
Allows searching via zip code for simplicity.
Weather Information:

Temperature (Celsius, Fahrenheit, or Kelvin).
Feels like, Min/Max temperature, Pressure, Humidity, and Weather condition.
User Interaction:

A command-line menu with options like city, zip, help, and exit.
APIs Used:

OpenWeatherMap Geocoding API for location data.
OpenWeatherMap Current Weather API for weather details.

## How to Run:
Install Python 3.x.
Install required libraries: requests.
Replace the api_key with a valid OpenWeatherMap API key.
Run the program:
python WeatherApp.py
Follow the prompts.

## Commands:
city: Lookup weather by city name, state, and country.
zip: Lookup weather by zip code.
help: Display help menu.
exit: Exit the program.
