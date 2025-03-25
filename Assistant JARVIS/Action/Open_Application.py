from Body.Advance_speak import speak
from DATA.Web_Data import websites
import webbrowser
import os
import psutil

# Function to open an application
def open_application(app_name):
    apps = {
        # Common Applications
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "wo mic": "WOMicClient.exe",
        "womic": "WOMicClient.exe",
        "browser": "start chrome",
        "chrome": "start chrome",
        "firefox": "start firefox",
        "edge": "start msedge",
        "word": "winword.exe",
        "excel": "excel.exe",
        "powerpoint": "powerpnt.exe",
        "outlook": "outlook.exe",
        "spotify": "spotify",
        "photoshop": "photoshop",
        "vlc": "vlc",
        "vlc media": "vlc",
        "vlc media player": "vlc",
        "cmd": "start cmd",
        "command prompt": "start cmd",
        "powershell": "start powershell",
        "explorer": "explorer.exe",
        "file manager": "explorer.exe",
        "this pc": "explorer.exe",
        "teams": "teams",
        "skype": "skype",
        "zoom": "zoom",
        "visual studio": "devenv.exe",
        "sublime": "subl",
        "filezilla": "filezilla",
        "git bash": "git-bash.exe",
        "java": "java -version",
        "pycharm": "pycharm64.exe",
        "adobe reader": "acrord32.exe",
        "notion": "notion",
        "slack": "slack",
        "discord": "discord",
        "paint": "mspaint.exe",
        "steam": "steam",
        "audacity": "audacity",
        "torrent": "utorrent",
        "evernote": "evernote",
        "whatsapp": "whatsapp",
        "trello": "trello",
        "postman": "postman",
        "teamviewer": "teamviewer",
        "mysql workbench": "mysqlworkbench",
        "mongodb compass": "mongodb-compass",
        "wamp": "wampmanager",
        "xamp": "xampp-control.exe",
        "docker": "docker",
        "kaspersky": "kaspersky",
        "intellij": "idea64.exe",
        "visual studio code": "code",
        "brave": "start brave",
        "kodi": "kodi",
        "blender": "blender",
        "gimp": "gimp",
        "handbrake": "HandBrake.exe",
        "netbeans": "netbeans64.exe",
        "gparted": "gparted",
        "quicken": "quicken",
        "quicktime": "quicktimeplayer",
        "telegram": "telegram",
        "foxit reader": "FoxitReader",
        "kmplayer": "kmplayer",
        "mpc hc": "mpc-hc64.exe",
        "virtualbox": "VirtualBox",
        "parallels": "parallels",
        "microsoft office": "start winword",
        "ubuntu": "ubuntu",
        
        # System Settings and Utilities
        "settings": "start ms-settings:",
        "setting": "start ms-settings:",
        "control panel": "control",
        "device manager": "devmgmt.msc",
        "network settings": "start ms-settings:network",
        "network setting": "start ms-settings:network",
        "sound settings": "start ms-settings:sound",
        "sound setting": "start ms-settings:sound",
        "power options": "powercfg.cpl",
        "system information": "msinfo32",
        "task manager": "taskmgr",
        "disk cleanup": "cleanmgr",
        "performance monitor": "perfmon",
        "system configuration": "msconfig",
        "event viewer": "eventvwr",
        "registry editor": "regedit",
        "group policy editor": "gpedit.msc",
        "user accounts": "control userpasswords2",
        "user account": "control userpasswords2",
        "update setting": "start ms-settings:windowsupdate",
        "update settings": "start ms-settings:windowsupdate",
        "printer settings": "start ms-settings:printers",
        "printer setting": "start ms-settings:printers",
        "firewall settings": "start wf.msc",
        "firewall setting": "start wf.msc",
        "privacy settings": "start ms-settings:privacy",
        "privacy setting": "start ms-settings:privacy",
        "backup settings": "start ms-settings:backup",
        "backup setting": "start ms-settings:backup",
        
        # Additional Settings and Utilities
        "services": "services.msc",
        "service": "services.msc",
        "computer management": "compmgmt.msc",
        "system restore": "rstrui",
        "network and sharing center": "control.exe /name Microsoft.NetworkAndSharingCenter",
        "device and printer settings": "control printers",
        "device and printer setting": "control printers",
        "storage settings": "start ms-settings:storage",
        "storage setting": "start ms-settings:storage",
        "default apps": "start ms-settings:defaultapps",
        "default app": "start ms-settings:defaultapps",
        "region settings": "start ms-settings:region",
        "region setting": "start ms-settings:region",
        "language settings": "start ms-settings:language",
        "language setting": "start ms-settings:language",
        "time and language settings": "start ms-settings:dateandtime",
        "time and language setting": "start ms-settings:dateandtime",
        "accessibility settings": "start ms-settings:easeofaccess",
        "accessibility setting": "start ms-settings:easeofaccess",
        "family and other users": "start ms-settings:otherusers",
        "family and other user": "start ms-settings:otherusers",
        "sync settings": "start ms-settings:sync",
        "sync setting": "start ms-settings:sync",
        "feedback and diagnostics": "start ms-settings:feedback",
        "protection settings": "start ms-settings:windowsdefender",
        "protection setting": "start ms-settings:windowsdefender",
        "task scheduler": "taskschd.msc",
        "bitlocker setting": "control /name Microsoft.BitLockerDriveEncryption",
        "bitlocker settings": "control /name Microsoft.BitLockerDriveEncryption",
        "windows features": "optionalfeatures",
        "window features": "optionalfeatures",
        "color management": "colorcpl",
        "mouse settings": "main.cpl",
        "mouse setting": "main.cpl",
        "keyboard settings": "main.cpl keyboard",
        "keyboard setting": "main.cpl keyboard",
        "touchpad settings": "control touchpad",
        "touchpad setting": "control touchpad",
        "network adapter settings": "ncpa.cpl",
        "network adapter setting": "ncpa.cpl",
        "sound recorder": "soundrecorder",
        
        # More Advanced Settings and Utilities
        "local security policy": "secpol.msc",
        "shared folder": "fsmgmt.msc",
        "storage space": "start ms-settings:storagespaces",
        "remote desktop setting": "systempropertiesremote",
        "internet option": "inetcpl.cpl",
        "font setting": "control fonts",
        "sync center": "mobsync",
        "device encryption": "start ms-settings:deviceencryption",
        "one drive setting": "start ms-settings:onedrive",
        "system properties": "sysdm.cpl",
        "system propertie": "sysdm.cpl",
        "user profile setting": "sysdm.cpl,,1",
        "automatic updates": "wuauserv",
        "windows security": "start ms-settings:windowsdefender",
        "credential manager": "control /name Microsoft.CredentialManager",
        "windows firewall": "wf.msc",
        "group policy editor": "gpedit.msc",
        "local group policy editor": "gpedit.msc",
        "network connection": "ncpa.cpl",
        "advanced system setting": "sysdm.cpl,,3",
        "sound control panel": "mmsys.cpl",
        "system info": "msinfo32",
        "remote assistance": "msra",
        "service": "services.msc",
        "window update": "start ms-settings:windowsupdate",
        "backup and restore": "control panel /name Microsoft.BackupAndRestore",
        "sync settings": "start ms-settings:sync"
        # Add more settings and utilities as needed
    }
    
    app_command = apps.get(app_name.lower())
    if app_command:
        os.system(app_command)
        speak(f"Opening The {app_name}")
    else:
        if app_name:
            websites_command = app_name
            openweb(websites_command)
            return None
        else:
            speak("Sir, the application you quoted is probably not complete or not in my database. so please try again")

def close_application(app_name):
    for proc in psutil.process_iter(['pid', 'name']):
        if app_name.lower() in proc.info['name'].lower():
            try:
                proc.terminate()
                speak(f"Closing The {app_name}")
            
            except psutil.NoSuchProcess:
                speak(f"Process {app_name} no longer exists")
            except psutil.AccessDenied:
                speak(f"Access denied when trying to terminate {app_name}")
            return None
    
def openweb(text):
    website_names = text.lower().split()
    urls_to_open = []

    for name in website_names:
        if name in websites:
            urls_to_open.append(websites[name])
        else:
            speak(f"Website '{name}' not found in the dictionary.")

    if urls_to_open:
        for url in urls_to_open:
            webbrowser.open(url)
        speak(f"Opening your website {name}")
