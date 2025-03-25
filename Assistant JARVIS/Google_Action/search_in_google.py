import pywhatkit
import random
import wikipedia as googleScrap
from DATA.DLG import search_result
from Body.Advance_speak import speak


def search_google(text):
    dlg = random.choice(search_result)
    text = text.replace("jarvis","")
    speak("This Is What I Found On The Web!")
    pywhatkit.search(text)
    speak(dlg)

    try:
        result = googleScrap.summary(text,2)
        speak(result)

    except:
        speak("No Speakable Data Available!")
