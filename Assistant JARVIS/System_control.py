#from transformers import pipeline
import speech_recognition as sr
import pyttsx3
import pyautogui
import webbrowser
import datetime
import random
import time
import logging
import os
import requests
from bs4 import BeautifulSoup




# Set up logging
logging.basicConfig(filename='voice_control.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Initialize NLP model for command understanding
try:
    #nlp = pipeline('zero-shot-classification')
    logging.info("NLP pipeline initialized successfully.")
except Exception as e:
    logging.error(f"Failed to initialize NLP pipeline: {str(e)}")
    raise

def speak(text):
    engine.say(text)
    engine.runAndWait()
    logging.info(f"Spoke: {text}")

def schedule_task(task, time_str):
    try:
        task_time = datetime.datetime.strptime(time_str, "%H:%M")
        current_time = datetime.datetime.now()
        if task_time < current_time:
            task_time += datetime.timedelta(days=1)
        delay = (task_time - current_time).total_seconds()
        speak(f"Scheduling task: {task} at {time_str}.")
        logging.info(f"Task scheduled: {task} at {task_time}")
        time.sleep(delay)
        speak(f"Time to perform task: {task}.")
    except ValueError as ve:
        speak(f"Invalid time format. Please use HH:MM. Error: {str(ve)}")
        logging.error(f"Invalid time format: {str(ve)}")
    except Exception as e:
        speak(f"Error scheduling task: {str(e)}")
        logging.error(f"Error scheduling task: {str(e)}")



def get_weather(city):
    try:
        search = f"temperature in {city}"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        r.raise_for_status()  # Raise an exception for HTTP errors
        data = BeautifulSoup(r.text, "html.parser")
        temperature_div = data.find("div", class_="BNeawe")
        if temperature_div:
            temperature = temperature_div.text
            speak(f"The temperature in {city} is {temperature}")
        else:
            speak(f"Could not find temperature information for {city}.")
            logging.warning(f"Temperature information not found for {city}.")
    except requests.RequestException as re:
        speak(f"Error retrieving weather data: {str(re)}")
        logging.error(f"Request error: {str(re)}")
    except Exception as e:
        speak(f"Error retrieving weather data: {str(e)}")
        logging.error(f"Error retrieving weather data: {str(e)}")

def execute_command(command):   
    # Use zero-shot classification to understand the command
    try:
        command = command.lower()
        
        if "search" in command:
            search_query = command.split('search', 1)[1].strip()
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
            speak(f"Searching for {search_query}.")
        elif "take screenshot" in command:
            screenshot = pyautogui.screenshot()
            screenshot.save('screenshot.png')
            speak("Screenshot taken and saved.")
        elif "scroll" in command:
            if 'down' in command:
                pyautogui.scroll(-100)
                speak("Scrolling down.")
            elif 'up' in command:
                pyautogui.scroll(100)
                speak("Scrolling up.") 
        elif "click" in command:
            pyautogui.click()
            speak("Clicking at the current position.")
        elif "type" in command:
            text_to_type = command.split('type', 1)[1].strip()
            pyautogui.typewrite(text_to_type)
            speak(f"Typing {text_to_type}.")
        elif "volume" in command:
            if 'up' in command:
                pyautogui.press('volumeup')
                speak("Volume up.")
            elif 'down' in command:
                pyautogui.press('volumedown')
                speak("Volume down.")
            elif 'mute' in command:
                pyautogui.press('volumemute')
                speak("Volume muted.")
        elif "schedule" in command:
            try:
                task, time_str = command.split('at', 1)
                schedule_task(task.strip(), time_str.strip())
            except ValueError:
                speak("Please provide the task and time in the format: 'task at HH:MM'")
                logging.warning("Failed to parse task and time from command.")
        elif "weather" in command:
            city = command.split('weather in', 1)[1].strip()
            get_weather(city)
        else:
            speak("Sorry, I don't understand that command.")
            logging.warning(f"Unrecognized command: {command}")
    except Exception as e:
        speak(f"Error executing command: {str(e)}")
        logging.error(f"Error executing command: {str(e)}")

def listen_for_commands():
    print("..........Starting..........")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("   ")
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")   
        print("   ") 
        command = r.recognize_google(audio, language='en-in')
        print(f"Your Said :  {command}\n")

    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        speak("Sorry, I did not understand that.")
    except sr.RequestError:
        print("Sorry, there was an error with the speech recognition service.")
        speak("Sorry, there was an error with the speech recognition service.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        speak(f"An unexpected error occurred: {str(e)}")
        logging.error(f"Unexpected error: {str(e)}")
        
    return command.lower()

if __name__ == "__main__":
    while True:
        listen_for_commands()
