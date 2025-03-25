from Body.Advance_speak import speak
import platform
import psutil


def System_Information():
    try:
        def get_system_info():
            system_info = (
                f"System: {platform.system()}\n"
                f"Version: {platform.version()}\n"
                f"Processor: {platform.processor()}\n"
                f"Architecture: {platform.architecture()}\n"
                f"Machine: {platform.machine()}"
            )
            speak("System Information")
            speak(system_info)
        get_system_info()

        # Get CPU information
        def cpu():
            cpu_info = {
                'Physical cores': psutil.cpu_count(logical=False),
                'Total cores': psutil.cpu_count(logical=True),
                'CPU Frequency': psutil.cpu_freq().current,
                'CPU Usage Per Core': psutil.cpu_percent(percpu=True)
            }
        # speak CPU information
            speak("CPU Information:")
            for key, value in cpu_info.items():
                speak(f"{key}: {value}")
        cpu()

        # Get memory information
        def memory():
            mem_info = {
                'Total Memory': round(psutil.virtual_memory().total / (1024**3), 2),  # in GB
                'Available Memory': round(psutil.virtual_memory().available / (1024**3), 2),
                'Used Memory': round(psutil.virtual_memory().used / (1024**3), 2),
                'Memory Usage Percentage': psutil.virtual_memory().percent
            }
            # speak memory information
            speak("\nMemory Information:")
            for key, value in mem_info.items():
                speak(f"{key}: {value} GB" if isinstance(value, float) else f"{key}: {value}")
        memory()

        # Get disk information
        def disk():
            disk_info = {
                'Partitions and Usage': [(part.device, part.mountpoint, part.fstype, psutil.disk_usage(part.mountpoint))
                                        for part in psutil.disk_partitions()],
                'Total Disk Usage': psutil.disk_usage('/').total / (1024**3),  # in GB
            }
        # speak disk information
            speak("\nDisk Information:")
            for key, value in disk_info.items():
                if key == 'Partitions and Usage':
                    speak(f"{key}:")
                    for item in value:
                        speak(f"  {item[0]} - {item[1]} ({item[2]})")
                        speak(f"    Total: {item[3].total / (1024**3):.2f} GB")
                        speak(f"    Used: {item[3].used / (1024**3):.2f} GB")
                        speak(f"    Free: {item[3].free / (1024**3):.2f} GB")
                        speak(f"    Percentage: {item[3].percent}%")
                else:
                    speak(f"{key}: {value:.2f} GB" if isinstance(value, float) else f"{key}: {value}")


        disk()
    except:
        speak("I'm sorry sir, that's all I can tell you. To know more, you will have to add more information to the system.")

