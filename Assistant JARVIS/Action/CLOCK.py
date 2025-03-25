from datetime import datetime, date, time
from Body.Advance_speak import speak



def what_is_the_time():
    try:
        # Time object
        current_time = datetime.now().time()
        speak("Now is The Present Time:", current_time)
    except Exception as e:
        pass

def Date():    
    try:
        # Date object
        current_date = date.today()
        speak("Now is The Present Date:", current_date)

    except Exception as e:
        pass
        #speak("I am unable to listen to you, So I am Sorry Sir, Please can you speak again")