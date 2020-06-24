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

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():
    # Put code here
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)