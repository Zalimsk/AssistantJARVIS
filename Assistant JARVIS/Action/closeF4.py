import random
import pyautogui as ui
from DATA.DLG import closedlg
from Body.Advance_speak import speak

closedlg_random = random.choice(closedlg)
def close():
    speak(closedlg_random)
    ui.hotkey("alt","f4")