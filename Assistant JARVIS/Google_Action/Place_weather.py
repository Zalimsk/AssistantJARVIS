from Body.Text_to_Speech import speak
from Body.Speech_to_Text import Speech_to_Text_Python
import requests


# Function to get weather information (example using OpenWeatherMap API)
def get_weather():
    try:
        # Replace with your OpenWeatherMap API key
        api_key = 'your_api_key'
        
        # Replace with desired location and units (metric/imperial)
        city = 'New York'
        units = 'metric'
        
        # API request URL
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units={units}&appid={api_key}"
        
        # Fetch weather data
        response = requests.get(url)
        data = response.json()
        
        if data["cod"] == 200:
            weather_description = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            
            speak(f"Weather in {city}:")
            speak(f"- Description: {weather_description}")
            speak(f"- Temperature: {temperature}°C")
            speak(f"- Humidity: {humidity}%")
            speak(f"- Wind Speed: {wind_speed} m/s")
        else:
            speak(f"Failed to fetch weather data: {data['message']}")
    except Exception as e:
        speak(f"Error fetching weather data: {e}")

# Function to locate a place using geolocation services (example using Google Maps API)
def locate_place(command):
    try:
        # Replace with your Google Maps API key
        api_key = 'your_api_key'
        
        # Extract location query from command
        location_query = command.replace("locate ", "")
        
        # Construct API request URL
        url = f"https://maps.googleapis.com/maps/api/geocode/json?address={location_query}&key={api_key}"
        
        # Fetch location data
        response = requests.get(url)
        data = response.json()
        
        if data["status"] == "OK":
            results = data["results"]
            for result in results:
                formatted_address = result["formatted_address"]
                location_type = result["types"][0]
                speak(f"Location: {formatted_address}")
                speak(f"Type: {location_type}")
                break  # speak only the first result
        else:
            speak(f"Failed to locate {location_query}")
    except Exception as e:
        speak(f"Error locating place: {e}")

def Place_Weather_Action():
        if "weather" in command:
            get_weather()
        elif "locate" in command:
            locate_place()
        
        else:
            speak(f"Command '{command}' not recognized.")
    

if __name__ == "__main__":
    while True:
        command = Speech_to_Text_Python()
        
        if "exit" in command:
            speak("Exiting...")
            break
        
        if command:
            Place_Weather_Action(command)