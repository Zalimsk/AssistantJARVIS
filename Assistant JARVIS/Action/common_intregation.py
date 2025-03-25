from Action.Open_Application import open_application
from Action.Open_Application import close_application
from Body.Advance_speak import speak
from Genrate_Code.gen_image import generate_image
import keyboard


def common_cmd(text):
    if text:
        command = text.lower().replace("jarvis", "").strip()
        command = text.lower().replace("jar", "").strip()
        if "open" in command.lower():
            app_name = command.lower().replace("open", "").strip()
            if app_name:
                open_application(app_name)
                
                pass
            else:
                speak("I Don't Get Any text To Open The Application, So I Can't Open The Application , Please Try Opening The Application Again....")
        
        
        elif "close" in command.lower():
            app_name = command.lower().replace("close", "").strip()
            if app_name:
                close_application(app_name)
            else:
                speak("I did not find any applications to close, So Please Try Again...")
        
        elif "close the recent window" in command or "close the window" in command or "close this" in command:
            print("Okey")
            keyboard.press_and_release('alt + f4')
            speak("The window that was currently running has been closed.")
            
        elif "image generate karo" in command or "image create karo" in command or "generate image" in command:
            speak("Okey Sir")
            generate_image(command)
            
        
