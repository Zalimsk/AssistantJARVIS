import numpy as np
import pyautogui
import datetime
import os
from datetime import date
from Body.Advance_speak import speak

call = np.random.choice(["Boss","Sir"])


def screen():
    try:
        s = np.random.choice([f"Ok {call} , Wait For A While ?",
                f" {call}, Just A Second",
                f" {call} , Hold A Second",f"Wait ,{call}"])
        speak(s)
        path = (str(date.today())).replace(" ","-") + (str(datetime.datetime.now().time().strftime("%I:%M:%S %p"))).replace(" ","-")
        path = path.replace(":","-")
        path = path.replace(".","-")
        path1name = path + ".jpg"
        path1 = "J:\\Assistant JARVIS\\data provided by jarvis\\ScreenShot By JARVIS\\"+ path1name
        kk = pyautogui.screenshot()
        kk.save(path1)
        os.startfile("J:\\Assistant JARVIS\\data provided by jarvis\\ScreenShot By JARVIS")
        sp = np.random.choice([f" {call} ,Successfully Saved Screenshot",f"{call}, Screenshot has been saved Successfully Your Choice The Folder"])
        speak(sp)
    except UnicodeError as e:
        speak("I am not able to Take Screenshot, There is Some Problem, So Please try again, If Still not Working to Check Screenshot Code") 
        speak(e)
        pass