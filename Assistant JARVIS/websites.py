from DATA.Web_Data import websites
import webbrowser
from Body.Text_to_Speech import speak
from Body.Speech_to_Text import Speech_to_Text_Python

def Openwebsite(webname):
    website_name = webname.lower().split()
    counts = {}

    for name in website_name:
        counts[name] = counts.get(name,0) + 1
    urls_to_open = []

    for name,count in counts.items():
        if name in websites:
            urls_to_open.extend([websites[name]]*count)

    for url in urls_to_open:
        webbrowser.open(url)

    if urls_to_open:
        speak("opening your websites")

if __name__ == "__main__":
    while True:
        websites = Speech_to_Text_Python()
        
        if "exit" in websites:
            speak("Exiting...")
            break
        
        if websites:
            Openwebsite(websites)