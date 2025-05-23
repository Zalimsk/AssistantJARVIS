from Automation_System.tab_automation import *
from Google_Action.search_in_google import *
from Google_Action.scrole_automation import *
from Google_Action.open_website import *

def google_cmd(text):

    if "scroll up" in text:
        scroll_up()

    elif "scroll down" in text:
       scroll_down()

    elif "scroll to top" in text:
       scroll_to_top()

    elif "scroll to bottom" in text:
       scroll_to_bottom()
    
    elif "search in google" in text or "search on google" in text or "search for google" in text or "search google" in text or "google search" in text:
        text = text.replace("search in google","")
        text = text.replace("search on google","")
        text = text.replace("search google","")
        text = text.replace("search for google","")
        text = text.replace("google search","")
        search_google(text)

    elif "close the tab" in text or "close tab" in text:
        close_tab()

    elif "open browser menu" in text:
        open_browser_menu()

    elif "zoom in" in text:
        zoom_in()

    elif "zoom out" in text:
        zoom_out()

    elif "refresh page" in text:
        refresh_page()

    elif "switch to next tab" in text:
        switch_to_next_tab()

    elif "switch to previous tab" in text:
        switch_to_previous_tab()

    elif "open history" in text:
        open_history()

    elif "open bookmarks" in text:
        open_bookmarks()

    elif "go back" in text:
        go_back()

    elif "go forward" in text:
        go_forward()

    elif "open dev tools" in text:
        open_dev_tools()

    elif "toggle full screen" in text:
        toggle_full_screen()

    elif "open private window" in text:
        open_private_window()

    elif "open new tab" in text:
        open_new_tab()
    else:
        pass