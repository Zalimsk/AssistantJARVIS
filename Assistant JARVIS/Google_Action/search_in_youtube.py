import random
import time
import pyautogui as ui
import webbrowser
from DATA.DLG import yt_search, s1, s2
from Body.Advance_speak import speak


def youtube_search(text):
    dlg = random.choice(yt_search)
    speak(dlg)
    webbrowser.open("https://www.youtube.com/")
    time.sleep(2)
    ui.press("/")
    ui.write(text)
    s10 = random.choice(s1)
    speak( s10 )
    time.sleep(0.5)
    ui.press("enter")
    s12 = random.choice(s2)
    speak(s12)

