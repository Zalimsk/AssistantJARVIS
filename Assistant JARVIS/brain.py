from Google_Action.google_big_data import *
from Google_Action.google_small_data import *
from Body.Advance_speak import speak
from Genrate_Code.llm1 import llm1
from Genrate_Code.llm2 import llm2
from load_file import *


def brain(text):
    if "jarvis" in text:
        text = text.replace("jarvis","")
        text = text.strip()
        if text in qa_dict:
            ans = qa_dict[text]
        elif "define" in text or "brief" in text or "research" in text or "teach me" in text:
           ans = deep_search(text)
        elif "jarvis real time data" in text or "jarvis give me real time data" in text or "jarvis who is " in text or "jarvis where is" in text :
            ans = search_brain(text)
        elif "write a python code" in text or "code generate" in text or "create the python code" in text or "tell me the code" in text or "create the code" in text:
            ans= llm2(text)
        else:
            ans = llm1(text)
        return ans

    else:
        pass