################################################################################
# File:    osoverwrite.py
# Purpose: Operating System Self-destruct trigger script for BusKill Kill Cord
#          For more info, see: https://buskill.in/
# WARNING: THIS IS EXPERIMENTAL SOFTWARE THAT IS DESIGNED TO CAUSE PERMANENT,
#          COMPLETE AND IRREVERSIBLE DATA LOSS!
# Authors: Jacob Neplokh <me at jacobneplokh dot com>
# Created: 2020-06-01
# Updated: 2020-06-01
# Version: 0.1
#############################################################################

# Import modules
import sys
import os
import secrets
import ctypes
import subprocess
import platform


# Check if User is Admin
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


# If so, run rest of code. If not, request permissions.
if is_admin():
    # Run VeraCrypt Command to force dismount all volumes, wipes cached passwords, and quit without user prompts
    subprocess.call('"C:\Program Files\VeraCrypt\VeraCrypt.exe" /d /f /w /q /s', shell=True)
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)