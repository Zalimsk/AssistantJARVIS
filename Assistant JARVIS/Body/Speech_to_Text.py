import speech_recognition as sr
import numpy as np
#from playsound import playsound
from mtranslate import translate
from colorama import Fore,Style,init
from time import sleep
from Body.Advance_speak import speak


call = np.random.choice(["Boss","Sir"])
listensound_path = "J:\\Assistant JARVIS\\Sound Effects\\Startup_Music.wav"
Recognizesound_path = "J:\\Assistant JARVIS\\Sound Effects\\Stopped_Listening.wav"

#init(autoreset=True)
print(Fore.RED + "..................................................Starting..................................................\n",end="",flush=True)
def print_loop():
    while True:
        voice = np.random.choice([f"{call} JARVIS is Listening...",f"{call} I am Listening...",f"{call} I am waiting for your command"])
        print(Fore.LIGHTYELLOW_EX + voice,end="",flush=True)
        print(Style.RESET_ALL,end="",flush=True)
        print("",end="",flush=True)


def Trans_hindi_to_english(txt):
    english_txt = translate(txt,to_language= "en=in")
    return english_txt

def listen():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold=34000
    recognizer.dynamic_energy_adjustment_damping = 0.010
    recognizer.dynamic_energy_ratio = 1.0
    recognizer.pause_threshold = 0.3
    recognizer.operation_timeout = None
    recognizer.pause_threshold = 0.2
    recognizer.non_speaking_duration = 0.2

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            #playsound(listensound_path)
            voice = np.random.choice([f"JARVIS is Listening {call}...\n",f"I Am Listening {call}...\n",f"I Am Waiting For Your Command {call}...\n"])
            print(Fore.LIGHTYELLOW_EX + voice,end="",flush=True)
            #print(Fore.LIGHTYELLOW_EX + "I Am Listening...\n", end="", flush=True)
            try:
                audio = recognizer.listen(source,timeout=None)
                #playsound(Recognizesound_path)
                nr = np.random.choice([f"I Understand Your Order {call}...\n",f"Got it, Now Recognizing {call}...\n",f"Give Me Some Time To Understand {call}...\n","Your voice is Recognizing...\n"])
                print("\r"+Fore.LIGHTMAGENTA_EX + nr ,end="",flush=True)
                recognized_txt = recognizer.recognize_google(audio).lower()
                sleep(1)
                if recognized_txt:
                    translated_txt = Trans_hindi_to_english(recognized_txt)
                    User = np.random.choice(["Mr.Sk : ","Zalim Sk : ","SK : ","Sarvendra Singh : "])
                    print("\r"+Fore.LIGHTGREEN_EX + User + translated_txt)
                    return translated_txt
                else:
                    return ""
            except:
                speak("I can not hear your voice, So please try again?\n")
                recognized_txt = ""
            finally:
                print("\r",end="",flush=True)
            pass
                
        
def hearing():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold=34500
    recognizer.dynamic_energy_adjustment_damping = 0.011
    recognizer.dynamic_energy_ratio = 1.9
    recognizer.pause_threshold = 0.3
    recognizer.operation_timeout = None
    recognizer.pause_threshold = 0.2
    recognizer.non_speaking_duration = 0.1
    
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            try:
                audio = recognizer.listen(source,timeout=None)
                recognized_txt = recognizer.recognize_google(audio).lower()
                if recognized_txt:
                    translated_txt = Trans_hindi_to_english(recognized_txt)
                    return translated_txt
                else:
                    return ""
            except sr.UnknownValueError:
                recognized_txt = ""
            finally:
                print("\r",end="",flush=True)
