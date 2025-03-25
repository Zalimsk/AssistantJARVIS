from requests import get
from Body.Advance_speak import speak

def find_my_ip():
    try:
        ip = get('https://api.ipify.org').text
        speak(f"Your IP ADDRESS IS {ip}")

    except UnicodeError as e:
        speak(e)
        pass
