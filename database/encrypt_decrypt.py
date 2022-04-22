from cryptography.fernet import Fernet
def genwrite_key():
    key = Fernet.generate_key()
    with open('P4Output.txt', 'w') as f:
        f.write(key)

