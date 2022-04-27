from cryptography.fernet import Fernet
key = Fernet.generate_key()


file = open('key.key', 'wb')  # Open the file as wb to write bytes
file.write(key)  # The key is type bytes still
file.close()


file = open('key.key', 'rb')  # Open the file as wb to read bytes
key = file.read()  # The key will be type bytes
file.close()


import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

password_provided = "password"  # This is input in the form of a string
password = password_provided.encode()  # Convert to type bytes
salt = b'salt_'  # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password))
# Can only use kdf once

#Encrypting

from cryptography.fernet import Fernet
message = "my deep dark secret".encode()

f = Fernet(key)
encrypted = f.encrypt(message)  # Encrypt the bytes. The returning object is of type bytes


# decryption

from cryptography.fernet import Fernet
encrypted = b"...encrypted bytes..."

f = Fernet(key)
decrypted = f.decrypt(encrypted)



# Dealing with Invalid key

from cryptography.fernet import Fernet, InvalidToken
encrypted = b"...encrypted bytes..."

f = Fernet(incorrect_key)  # An example of providing the incorrect key
try:
    decrypted = f.decrypt(encrypted)
    print("Valid Key - Successfully decrypted")
except InvalidToken as e:  # Catch any InvalidToken exceptions if the correct key was not provided
    print("Invalid Key - Unsuccessfully decrypted")




# Example of encryption and decryption


#encryption
from cryptography.fernet import Fernet
key = b'' # Use one of the methods to get a key (it must be the same when decrypting)
input_file = 'test.txt'
output_file = 'test.encrypted'

with open(input_file, 'rb') as f:
    data = f.read()  # Read the bytes of the input file

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

with open(output_file, 'wb') as f:
    f.write(encrypted)  # Write the encrypted bytes to the output file

# Note: You can delete input_file here if you want

#decryption

from cryptography.fernet import Fernet, InvalidToken
key = b'' # Use one of the methods to get a key (it must be the same as used in encrypting)
input_file = 'test.encrypted'
output_file = 'test.txt'

with open(input_file, 'rb') as f:
    data = f.read()  # Read the bytes of the encrypted file

fernet = Fernet(key)
try:
    decrypted = fernet.decrypt(data)

    with open(output_file, 'wb') as f:
        f.write(decrypted)  # Write the decrypted bytes to the output file

    # Note: You can delete input_file here if you want
except InvalidToken as e:
    print("Invalid Key - Unsuccessfully decrypted")

