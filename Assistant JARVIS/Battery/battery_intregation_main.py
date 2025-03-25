from Battery.battery_alert import *
from Battery.battery_plug_check import *
from Battery.check_battery_persentage import *


def battery_cmd(text):
    if "check battery percentage" in text or "battery percentage" in text:
        battey_persentage()
    #elif "check plug" in text or "check battery plug" in text:
        #check_plugin_status1()
    elif "give me the battery alert" in text or "battery alert" in text:
        battery_alert1()
    else:
        check_plugin_status1()
        pass
