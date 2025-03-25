from Body.Advance_speak import speak
import speedtest


def get_internet_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    
    download_speed = st.download() / 1_000_000  # Convert from bits/s to Megabits/s
    upload_speed = st.upload() / 1_000_000  # Convert from bits/s to Megabits/s
    
    return download_speed, upload_speed

def Internet_Speed():
    speak("Sir Give me some time, I will check and give you the internet speed. So Please Wait...")
    download_speed, upload_speed = get_internet_speed()
    if download_speed or upload_speed is not None:
        speak(f"Download Speed: {download_speed:.2f} Mbps")
        speak(f"Upload Speed: {upload_speed:.2f} Mbps")
    else:
        speak("Error: Unable to retrieve internet speed.")