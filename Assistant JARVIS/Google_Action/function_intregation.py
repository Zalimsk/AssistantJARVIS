from Google_Action.check_temperature import *
from Google_Action.CHECK_SPEED import *
from Google_Action.check_online_offline_status import *
from Action.clap_with_music import *
from Action.CLOCK import *
from Automation_System.find_my_ip import *
from Genrate_Code.seo_generator import *
from Action.Screenshot import *


def Function_cmd(text):
    if "check internet speed" in text or "check speed test" in text or "speed test" in text:
        Internet_Speed()
    elif "are you there" in text or "hello there" in text or "hello jarvis" in text :
        internet_status()
    elif "check temperature" in text or "temperature" in text or "what is the temperature" in text:
        text = text.replace("temperature","")
        text = text.replace("check temperature","")
        text = text.replace("what is the temperature","")
        text = text.replace("tell me the temperature","")
        get_temperature_openweathermap()
    elif "find my ip" in text or "ip address" in text:
        find_my_ip()
    elif "what is the time" in text or "time" in text or "tell me the time" in text:
        what_is_the_time()
    elif "take a screenshot" in text or "take screenshot" in text or "screenshot" in text:
        screen()
    elif "what is the date" in text or "date" in text or "tell me the date" in text:
        Date()
    elif "start clap with music system" in text or "start smart music system" in text or "start music" in text:
        speak("Ok Now Starting The Music")
        main()
    elif "activate seo generator" in text or "activate youtube title generator" in text or "activate seo generator" in text:
        seo_gen()
    else:
        pass

