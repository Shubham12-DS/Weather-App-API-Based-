import requests

# Replace this with your actual API key from OpenWeatherMap
API_KEY = 'YOUR_API_KEY_HERE'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # to get temperature in Celsius
    }

    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        print("\n📍 Location:", data['name'], ",", data['sys']['country'])
        print("🌡️ Temperature:", data['main']['temp'], "°C")
        print("💧 Humidity:", data['main']['humidity'], "%")
        print("🌬️ Wind Speed:", data['wind']['speed'], "km/h")
        print("🌤️ Weather:", data['weather'][0]['description'].title())
    else:
        print("❌ City not found or API error. Please try again.")

# Main program
print("== 🌦️ Real-Time Weather App ==")
city_name = input("Enter city name: ")
get_weather(city_name)
