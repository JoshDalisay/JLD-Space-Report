import sys
import os
from ReportReader import ReadReport
from PowerShellScriptReader import RunPowerShell

def main():
    RunPowerShell()
    ReadReport()

if __name__ == '__main__':
    main()
    programPause = input("Press the <ENTER> key to continue...")
    



