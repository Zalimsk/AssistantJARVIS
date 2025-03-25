from Body.Advance_speak import speak
from Automation_System.System_Info import System_Information



def system_cmd(text):
    try:
        if "system information" in text:
            speak("Ok Sir, Let's Check First And Then Let You Know.")
            System_Information()
        else:
            return None
    except Exception as e:
        speak(f"Error performing action: {e}")