import requests
from bs4 import BeautifulSoup
from Body.Advance_speak import speak
from Body.Recognizing import takecommand


def get_temperature_openweathermap():
    try:
        speak("Tell me the name of the place where you want to know the temperature")
        name = takecommand()
        search = f"temperature in {name}"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temperature = data.find("div",class_ = "BNeawe").text
        speak(f"The Temperature in {name} is {temperature}")
        
    except:
        speak("I Am Not Listening Your Speak Place")
        speak("So I Am Sorry Sir") 
        pass




