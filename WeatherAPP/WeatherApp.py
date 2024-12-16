# Bernard Owusu Sefah
# Assignment Week12
# Weather Lookup App
# 2/28/2024

import requests


def main():
    # Display program header
    print_header()

    # Main loop for user interaction
    while True:
        # Prompt user for choice: city or zip code lookup
        user_choice = input(
            "Enter 'city' for city lookup or 'zip' for zip code lookup or 'help' for an overview of the app (or "
            "'exit' to exit): ").strip().lower()

        # Exit loop if user chooses to quit
        if user_choice == 'exit':
            break

        # Display help for country codes
        if user_choice == 'help':
            display_country_code()
            continue

        # If user chooses city lookup
        elif user_choice == 'city':
            city = input("Enter city name: ").strip()
            state_code = input("Enter state code (e.g., 'NY' for New York): ").strip().upper()
            country_code = input("Enter country code (e.g., 'US' for United States): ").strip().lower()
            location = f"{city},{state_code},{country_code}"
            try:
                # Get geolocation data
                geo_data = get_geo_location(location)
                if geo_data:
                    lat = geo_data['lat']
                    lon = geo_data['lon']
                    # Prompt user for temperature unit choice
                    units = input(
                        "Enter 'imperial' for Fahrenheit, 'metric' for Celsius, or 'standard' for Kelvin: ").strip().lower()
                    # Get weather data using geolocation
                    weather_data = get_weather(lat, lon, units)
                    if weather_data:
                        # Display weather information
                        display_weather(f"{city}, {state_code}, {country_code}", weather_data)
                    else:
                        print("Failed to retrieve weather data.")
                else:
                    print("Failed to retrieve geolocation data.")
            except requests.exceptions.RequestException as e:
                print(f"Error: {e}\nFailed to connect to the weather service.\n")

        # If user chooses zip code lookup
        elif user_choice == 'zip':
            zip_code = input("Enter zip code: ").strip()
            try:
                # Get geolocation data from zip code
                geo_data = get_geo_location_from_zip(zip_code)
                if geo_data:
                    lat = geo_data['lat']
                    lon = geo_data['lon']
                    # Prompt user for temperature unit choice
                    units = input(
                        "Enter 'imperial' for Fahrenheit, 'metric' for Celsius, or 'standard' for Kelvin: ").strip().lower()
                    # Get weather data using geolocation
                    weather_data = get_weather(lat, lon, units)
                    if weather_data:
                        # Display weather information
                        display_weather(f"{geo_data['city']}, {geo_data['state']}, {zip_code}", weather_data)
                    else:
                        print("Failed to retrieve weather data.")
                else:
                    print("Failed to retrieve geolocation data from the zip code.")
            except requests.exceptions.RequestException as e:
                print(f"Error: {e}\nFailed to connect to the weather service.\n")

        # If user enters invalid choice
        else:
            print("Invalid choice. Please enter 'city', 'zip', or 'help' or 'quit'.\n")


def print_header():
    # Display program header
    print('-' * 30)
    print('    Weather Lookup App')
    print('-' * 30)


def get_geo_location(location):
    # Get geolocation data from OpenWeatherMap API
    api_key = '559894e58b44c7b8b41d86b82e3728a7'
    url = f'https://api.openweathermap.org/geo/1.0/direct?q={location}&limit=1&appid={api_key}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        geo_data = response.json()
        return geo_data[0] if geo_data else None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}\nFailed to retrieve geolocation data.\n")
        return None


def get_geo_location_from_zip(zip_code):
    # Get geolocation data from OpenWeatherMap API using zip code
    api_key = '559894e58b44c7b8b41d86b82e3728a7'
    url = f'https://api.openweathermap.org/data/2.5/weather?zip={zip_code}&appid={api_key}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        geo_data = response.json()
        # Extract latitude and longitude from the response
        if 'coord' in geo_data and 'name' in geo_data:
            return {
                'city': geo_data['name'],
                'state': None,
                'lon': geo_data['coord']['lon'],
                'lat': geo_data['coord']['lat']}
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}\nFailed to retrieve geolocation data from the zip code.\n")
        return None


def get_weather(lat, lon, units):
    # Get current weather data from OpenWeatherMap API
    api_key = '559894e58b44c7b8b41d86b82e3728a7'
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units={units}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        #print(lat,lon)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}\nFailed to retrieve weather data.\n")
        return None


def display_weather(location, weather_data):
    # Check if the 'main' key exists in the weather data
    if 'main' in weather_data:
        # Display weather information
        print(f'\nCurrent weather in {location}:')
        print(f'Temperature: {weather_data["main"]["temp"]}')
        print(f'Feels like: {weather_data["main"]["feels_like"]}')
        print(f'Min Temperature: {weather_data["main"]["temp_min"]}')
        print(f'Max Temperature: {weather_data["main"]["temp_max"]}')
        print(f'Pressure: {weather_data["main"]["pressure"]} hPa')
        print(f'Humidity: {weather_data["main"]["humidity"]}%')
        print(f'Condition: {weather_data["weather"][0]["description"].capitalize()}\n')
    else:
        print(f"No weather data available for {location}.")


def display_country_code():
    # Display help menu
    print("HELP MENU: ")
    print("Enter 'city' to perform a city lookup.")
    print("Enter 'zip' to perform a zip code lookup.")
    print("Enter 'help' to display this help menu.")
    print("Enter 'exit' to exit the application.\n")
    print("For city lookup:")
    print("- Enter the city name, state code, and country code.")
    print("- Example: New York, NY, US")
    print("For zip code lookup:")
    print("- Enter the zip code.")
    print("- Example: 10001\n")
    print("You can also enter 'help' at any time to display this help menu.")
    print("Enjoy using the Weather Lookup App!\n")


if __name__ == '__main__':
    main()
    print("Program closed successfully!")
