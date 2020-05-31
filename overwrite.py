################################################################################
# File:    overwrite.py
# Purpose: Self-destruct trigger script for BusKill Kill Cord
#          For more info, see: https://buskill.in/
# WARNING: THIS IS EXPERIMENTAL SOFTWARE THAT IS DESIGNED TO CAUSE PERMANENT,
#          COMPLETE AND IRREVERSIBLE DATA LOSS!
# Usage:   Put the FULL path of the veracrypt volume as an argument
# Authors: Jacob Neplokh <me at jacobneplokh dot com>
# Created: 2020-05-29
# Updated: 2020-05-31
# Version: 0.1
#############################################################################

# Import modules
import sys
import os
import secrets

# Exit and tell user to give argument
if len(sys.argv) != 2:
    print("Usage: overwrite.py <path to veracrypt volume>")
    exit(1)

# Set veracrypt volume
veracrypt_volume = sys.argv[1]

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
