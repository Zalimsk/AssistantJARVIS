import pyttsx3

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[5].id)
    print(f": {text}")
    engine.say(text)
    engine.runAndWait() 
