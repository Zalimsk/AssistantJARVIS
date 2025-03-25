from Body.Text_to_Speech import speak
from Body.Speech_to_Text import Speech_to_Text_Python
import wikipedia
import webbrowser

def search_wikipedia(command):
    try:
        query = command.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences=2)
        speak(f"Wikipedia summary: {result}")
    except Exception as e:
        speak(f"Error searching Wikipedia: {e}")


def Search_Data():
    if "wikipedia" in command:
        search_wikipedia(command)
    elif "search for" in command:
        search_query = command.split("search for ")[1]
        webbrowser.open(f"https://www.google.com/search?q={search_query}")
    
if __name__ == "__main__":
    while True:
        command = Speech_to_Text_Python()
        
        if "exit" in command:
            speak("Exiting...")
            break
        
        if command:
            Search_Data(command)
