from Body.Text_to_Speech import speak
from Body.Speech_to_Text import Speech_to_Text_Python
from bs4 import BeautifulSoup
import urllib.request
import os
import boto


def web_scraping(command):
    try:
        url = "https://example.com"  # Replace with your target URL
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, 'html.parser')
        
        # Implement scraping logic to extract desired information from the webpage
        # Example: extracting title
        title = soup.title.string
        speak(f"Title of the webpage: {title}")
    except Exception as e:
        speak(f"Error performing web scraping: {e}")


def set_reminder(command):
    try:
        # Extract reminder details from the command and implement reminder functionality
        speak(f"Reminder set for: {command.split('set reminder ')[1]}")
    except Exception as e:
        speak(f"Error setting reminder: {e}")

def speak_text(command):
    try:
        # Initialize AWS Polly client
        polly_client = boto.client('polly', region_name='us-east-1')  # Replace with your region
        
        # Extract text to be spoken
        text_to_speak = command.replace("speak ", "")
        
        # Synthesize speech
        response = polly_client.synthesize_speech(
            Text=text_to_speak,
            OutputFormat='mp3',
            VoiceId='Joanna'  # Replace with desired voice (e.g., Joanna, Matthew)
        )
        
        # Save audio stream to file
        with open('output.mp3', 'wb') as file:
            file.write(response['AudioStream'].read())
        
        # Play audio file
        os.system("start output.mp3")
        
        speak(f"Spoken text: {text_to_speak}")
    except Exception as e:
        speak(f"Error speaking text: {e}")



def Action_Data():
    if "set reminder" in command:
        set_reminder(command)
    elif "scrape" in command:
        web_scraping(command)
    elif "speak" in command:
        speak_text(command)
    else:
        speak(f"Command '{command}' not recognized.")

if __name__ == "__main__":
    while True:
        command = Speech_to_Text_Python()
        
        if "exit" in command:
            speak("Exiting...")
            break
        
        if command:
            Action_Data(command)