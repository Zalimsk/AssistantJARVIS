import random
from DATA.DLG import welcomedlg
from Body.Advance_speak import speak


def welcome():
    welcome = random.choice(welcomedlg)
    speak(welcome)
