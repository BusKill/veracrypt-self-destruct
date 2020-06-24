################################################################################
# File:    admintest.py
# Purpose: Windows UAC Elevation Tester
# Authors: Jacob Neplokh <me at jacobneplokh dot com>
# Created: 2020-06-22
# Updated: 2020-06-22
# Version: 0.1
#############################################################################

import ctypes
import sys


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():
    f = open("C:\\test.txt", "w+")
else:
    # Re-run with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
