import speedtest
#from Body.Advance_speak import speak
import pyttsx3

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[5].id)
    print(f": {text}")
    engine.say(text)
    engine.runAndWait() 


def get_internet_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    
    download_speed = st.download() / 1_000_000  # Convert from bits/s to Megabits/s
    upload_speed = st.upload() / 1_000_000  # Convert from bits/s to Megabits/s
    
    return download_speed, upload_speed

def Internet_Speed():
    speak("Sir Give me some time, I will check and give you the internet speed. So Please Wait...")
    download_speed, upload_speed = get_internet_speed()
    speak(f"Download Speed: {download_speed:.2f} Mbps")
    speak(f"Upload Speed: {upload_speed:.2f} Mbps")
Internet_Speed()