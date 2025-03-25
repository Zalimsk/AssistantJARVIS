from DATA.Hindi_Shayari import shayaris
import pyttsx3
import random


query = ["Sir, I am female Jervis, the command you provided is probably not in my database. So Please Try Again...","Sir, मैं महिला जर्विस हूं, आपके द्वारा प्रदान किया गया आदेश संभवतः मेरे डेटाबेस में नहीं है, इसलिए कृपया पुनः प्रयास करें"]

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)
engine.setProperty('rate',130)

def speakk(Audio):
    print(f"Female J.A.R.V.I.S : {Audio}")
    engine.say(Audio)
    engine.runAndWait()

def Hin_Shay_cmd(text):
        if text:
            if "hindi shayari" in text or "again" in text or "listen again" in text or "one more time" in text or "repeat" in text:
                text = text.replace(" jar","jarvis")
                text = text.replace("sunao","")
                shayar = random.choice(shayaris)
                speakk(shayar)
            else:
                pass
        return None
