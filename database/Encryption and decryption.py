from cryptography.fernet import Fernet
file = open('D:\demo-python-project\key.key', 'rb')
key = file.read()
print(key)

password = input("please enter the password").encode()
f = Fernet(key)
encrypted_password = f.encrypt(password)
print(encrypted_password)


# decryption

f = Fernet(key)
decrypted_password = f.decrypt(encrypted_password)
print(decrypted_password)

password1 = input("please enter the password ")
password1 == decrypted_password
print("please choose it from menu  1. insert\n 2. update \n 3. delete ")
