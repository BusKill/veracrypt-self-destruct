import secrets
veracrypt_volume = input("What is the fullpath of the Veracrypt volume?:\n")
random_bytes = secrets.token_bytes(2000000)
random_byte_array = list(random_bytes)
f = open(veracrypt_volume, 'r+b')
f.seek(0)
f.write(bytearray(random_byte_array))
f.close()

