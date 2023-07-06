import subprocess, sys
import os

def RunPowerShell():
    #opens the file from the K: drive in powershell.
    #important note: the file path contains spaces. This was the only way i could escape the spaces. R string did not work / did not work.
    nameGrab = subprocess.Popen(["powershell.exe", "\\\\LOG-S8MO-1FS\\GROUPS\\\"IT Support\"\\\"Windows 10\"\\Scripts\\workstationGrabNameOnly.ps1"], stdout=sys.stdout)
    nameGrab.communicate()
    # p = subprocess.Popen(["powershell.exe", "K:\\MO\\\"IT Support\"\\\"Windows 10\"\\Scripts\\FreeDiskSpace.ps1"], stdout=sys.stdout)
    p = subprocess.Popen(["powershell.exe", "\\\\LOG-S8MO-1FS\\GROUPS\\\"IT Support\"\\\"Windows 10\"\\Scripts\\FreeDiskSpace.ps1"], stdout=sys.stdout)
    p.communicate()
    programPause = input("Press the <ENTER> key to continue...")