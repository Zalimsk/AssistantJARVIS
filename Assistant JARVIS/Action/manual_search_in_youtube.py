import pyautogui as ui
import random
import time
from DATA.DLG import s2, s1
from Body.Advance_speak import speak


def search_manual(text):
    text = text .replace("search","")
    ui.press("/")
    ui.write(text)
    s11 = random.choice(s1)
    speak( s11 )
    time.sleep(0.5)
    ui.press("enter")
    s12 = random.choice(s2)
    speak(s12)

