from Body.Text_to_Speech import speak
from Body.Speech_to_Text import listen
import os


def play_music():
    try:
        os.system("start your_music_file.mp3")  # Replace with your music file path
        speak("Playing music...")
    except Exception as e:
        speak(f"Error playing music: {e}")

# Function to pause music (example using media player hotkeys)
def pause_music():
    try:
        # Implement pause functionality using appropriate media player hotkeys or APIs
        speak("Pausing music...")
    except Exception as e:
        speak(f"Error pausing music: {e}")

# Function to resume music (example using media player hotkeys)
def resume_music():
    try:
        # Implement resume functionality using appropriate media player hotkeys or APIs
        speak("Resuming music...")
    except Exception as e:
        speak(f"Error resuming music: {e}")

# Function to stop music (example using media player hotkeys)
def stop_music():
    try:
        # Implement stop functionality using appropriate media player hotkeys or APIs
        speak("Stopping music...")
    except Exception as e:
        speak(f"Error stopping music: {e}")

# Function to set reminder
def set_reminder(command):
    try:
        # Extract reminder details from the command and implement reminder functionality
        speak(f"Reminder set for: {command.split('set reminder ')[1]}")
    except Exception as e:
        speak(f"Error setting reminder: {e}")

def Music_Action():
    try:
        if "play music" in command:
            play_music()
        elif "pause music" in command:
            pause_music()
        elif "resume music" in command:
            resume_music()
        elif "stop music" in command:
            stop_music()

        else:
            speak(f"Command '{command}' not recognized.")
    except Exception as e:
        speak(f"Error performing action: {e}")

if __name__ == "__main__":
    while True:
        command = listen()
        
        if "exit" in command:
            speak("Exiting...")
            break
        
        if command:
            Music_Action(command)