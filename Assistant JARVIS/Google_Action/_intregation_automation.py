from Action.common_intregation import *
from Google_Action.google_intregation_main import *
from Battery.battery_intregation_main import *
from Google_Action.youtube_intregation_main import *
from Automation_System.system_intregation import *
from Action.Shayari_Hindi import *

def Automation(text):
    youtube_cmd(text)
    google_cmd(text)
    battery_cmd(text)
    common_cmd(text)
    system_cmd(text)
    Hin_Shay_cmd(text)

