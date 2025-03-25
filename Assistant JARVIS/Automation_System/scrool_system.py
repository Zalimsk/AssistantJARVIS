import pyautogui
from Body.Text_to_Speech import speak
from Body.Speech_to_Text import listen

def scroll_up():
    # Scroll up by pressing the Up arrow key five times
    pyautogui.press('up', presses=5)

def scroll_down():
    # Scroll down by pressing the Down arrow key five times
    pyautogui.press('down', presses=5)

def scroll_to_top():
    # Scroll to the top of the page
    pyautogui.hotkey('home')

def scroll_to_bottom():
    # Scroll to the bottom of the page
    pyautogui.hotkey('end')

def perform_scroll_action(command):
    if "scroll up" in command or "upar scroll karo" in command:
        scroll_up()
    elif "scroll down" in command or "niche scroll karo" in command:
        scroll_down()
    elif "scroll to top" in command or "shuruat par jao" in command:
        scroll_to_top()
    elif "scroll to bottom" in command or "ant par jao" in command or "last mein jao" in command:
        scroll_to_bottom()
    else:
        pass

if __name__ == "__main__":
    while True:
        command = listen()
        
        if "exit" in command:
            speak("Exiting...")
            break
        
        if command:
            perform_scroll_action(command)
