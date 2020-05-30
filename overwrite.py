import secrets
import os

# Get veracrypt volume and size
veracrypt_volume = input("What is the full path of the Veracrypt volume?:\n")
volume_size = os.path.getsize(veracrypt_volume)

# Overwrite all metadata until byte 131072 (data area, includes erasing hidden volume too)
random_bytes = secrets.token_bytes(131072)
random_byte_array = list(random_bytes)
f = open(veracrypt_volume, 'r+b')
f.seek(0)
f.write(bytearray(random_byte_array))

# Regenerate random bytes and overwrite all metadata from S-131072 onwards
random_bytes = secrets.token_bytes(131072)
random_byte_array = list(random_bytes)
f.seek(int(volume_size - 131072))
f.write(bytearray(random_byte_array))
f.close()
