import secrets
veracrypt_container = input("What is the fullpath of the Veracrypt container?:\n")
random_bytes = secrets.token_bytes(2000000)
random_byte_array = list(random_bytes)
f = open(veracrypt_container, 'r+b')
f.seek(0)
f.write(bytearray(random_byte_array))
f.close()

