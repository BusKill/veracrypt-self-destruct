################################################################################
# File:    osoverwrite.py
# Purpose: Operating System Self-destruct trigger script for BusKill Kill Cord
#          For more info, see: https://buskill.in/
# WARNING: THIS IS EXPERIMENTAL SOFTWARE THAT IS DESIGNED TO CAUSE PERMANENT,
#          COMPLETE AND IRREVERSIBLE DATA LOSS!
# Authors: Jacob Neplokh <me at jacobneplokh dot com>
#############################################################################

# Import modules
import sys
import os
import secrets
import subprocess
import platform

# Check if Admin Function
def is_admin():
    if CURRENT_PLATFORM.startswith( 'WIN' ):
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    # if CURRENT_PLATFORM.startswith( 'LINUX' ):
        # TODO: Check if root on linux and re-run (need to test)

# Veracrypt Wipe Function
def veracrypt_wipe(veracrypt_volume):

    # Get size
    volume_size = os.path.getsize(veracrypt_volume)

    # Generate random bytes and overwrite all metadata until byte offset 131072 (data area)
    random_bytes = secrets.token_bytes(131072)
    random_byte_array = list(random_bytes)
    f = open(veracrypt_volume, 'r+b')
    f.seek(0)
    f.write(bytearray(random_byte_array))

    # Regenerate random bytes and overwrite all metadata from byte offset S-131072 onwards
    random_bytes = secrets.token_bytes(131072)
    random_byte_array = list(random_bytes)
    f.seek(int(volume_size - 131072))
    f.write(bytearray(random_byte_array))

    # Close file
    f.close()

# Check Platforms
CURRENT_PLATFORM = platform.system().upper()
if CURRENT_PLATFORM.startswith( 'LINUX' ):
    if is_admin():
        # Run VeraCrypt Command to force dismount all volumes
        subprocess.call('veracrypt -d -f', shell=True)
        # TODO: See how VeraCrypt paths are on Linux

if CURRENT_PLATFORM.startswith( 'WIN' ):
    import ctypes
    if is_admin():
        # Run VeraCrypt Command to force dismount all volumes, wipes cached passwords, and quit without user prompts
        subprocess.call('"C:\Program Files\VeraCrypt\VeraCrypt.exe" /d /f /w /q /s', shell=True)
        veracrypt_wipe(veracrypt_volume = "C:")
    else:
        # Re-run with Admin Writes
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

if CURRENT_PLATFORM.startswith( 'DARWIN' ):
    # No Veracrypt FDE on MacOS
    print('MacOS is currently not supported as it cannot use Veracrypt FDE, a FileVault needs to be created.')
    sys.exit()


