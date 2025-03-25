from Body.Advance_speak import speak
from Body.Speech_to_Text import listen
from Google_Action._intregation_automation import Automation
from Google_Action.function_intregation import Function_cmd
from Action.wish_greatings import *
from Action.welcome_greatings import *
from DATA.DLG import *
from brain import *


def comain():
    while True:
        text = listen()
        text = text.replace(" jar","jarvis")
        Automation(text)
        Function_cmd(text)
        Greating(text)

        if text in bye_key_word:
            x = random.choice(res_bye)
            speak(x)
            break

        elif "jarvis" in text:
            response = brain(text)
            speak(response)
        else:
            pass


def main():
    while True:
        wake_cmd = listen()
        if wake_cmd in wake_key_word:
            welcome()
        else:
            speak("Please try again....")
            pass
if __name__ == "__main__":
    comain()
    main()