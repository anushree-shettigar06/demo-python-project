from cryptography.fernet import Fernet


def load_key():
    return open("C://Users//Hari Priya//Desktop//pythondemo//demo-python-project//key.key", "rb").read()


key = load_key()

f = Fernet(key)


def encrypt_pass(data):
    return f.encrypt(data.encode())


# encrypted = encrypt_pass('Anuj').decode()
# encrypted = encrypt_pass("Anuj")
# print(encrypted)

def decrypt_pass(data):
    return f.decrypt(data)

# print(decrypt_pass(encrypted.encode()).decode())
# print(decrypt_pass(encrypted))
