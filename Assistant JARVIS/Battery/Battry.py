import psutil  # Install with 'pip install psutil'
import time
import ctypes  # For displaying Windows MessageBox
from Body.Advance_speak import speak


def check_battery_level():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent
    return plugged, percent

def show_alert(message):
    ctypes.windll.user32.MessageBoxW(0, message, "Battery Alert", 0x40 | 0x1)  # 0x40: MB_ICONEXCLAMATION, 0x1: MB_OK

def battery_alert(threshold=20):
    while True:
        speak("Wait...")
        plugged, percent = check_battery_level()
        if not plugged and percent < threshold:
            message = f"Battery is at {percent}%. Connect charger!"
            speak(message)  # Print message to console (optional)
            show_alert(message)  # Display message box alert
        time.sleep(60)  # Check battery level every minute

if __name__ == "__main__":
    battery_alert(threshold=20)
