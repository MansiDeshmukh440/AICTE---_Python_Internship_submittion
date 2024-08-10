import requests

def get_weather_data(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data.")
        return None

def display_weather(data):
    if data:
        city = data['name']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        weather_description = data['weather'][0]['description']

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {weather_description}")
    else:
        print("No data to display.")

def main():
    api_key = 'your_api_key_here'
    location = input("Enter city name: ")
    weather_data = get_weather_data(api_key, location)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
