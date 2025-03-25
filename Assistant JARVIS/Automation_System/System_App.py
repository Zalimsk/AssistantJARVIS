from Body.Text_to_Speech import speak
from Body.Speech_to_Text import listen
import os

def perform_action(command):
    try:
        if "chrome" in command:
            os.system("start chrome")
        elif "notepad" in command:
            os.system("start notepad")
        elif "calculator" in command:
            os.system("start calc")
        elif "spotify" in command:
            os.system("start spotify")
        elif "file manager" in command:
            os.system("start explorer")
        elif "word" in command:
            os.system("start winword")
        elif "excel" in command:
            os.system("start excel")
        elif "powerpoint" in command:
            os.system("start powerpnt")
        elif "visual studio code" in command:
            os.system("code")
        elif "command prompt" in command:
            os.system("start cmd")
        elif "shutdown" in command:
            os.system("shutdown /s /t 1")  # Shutdown the system
        elif "restart" in command:
            os.system("shutdown /r /t 1")  # Restart the system
        elif "sleep" in command:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        
        
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
            perform_action(command)
