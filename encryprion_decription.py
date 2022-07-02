# File Encrypytion and Decryption
# pip install pyAesCrypt

import pyAesCrypt

def Encrypt_File(filename, password):    
    pyAesCrypt.encryptFile(filename, filename + ".aes", password)
    print("File Encrypted")

def Decrypt_File(filename, password):
    pyAesCrypt.decryptFile(filename + ".aes", filename, password)
    print("File Decrypted")

Encrypt_File("test.py", "pass1243")
Decrypt_File("test.py.aes", "pass1243")
