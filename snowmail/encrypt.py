from Crypto.Cipher import AES
from Crypto import Random
import binascii
import os
import hashlib


class Crypter(object):

    def __init__(self, key):
        self.key = hashlib.md5(key).digest()
        self.iv = '\x00'*16

    def encrypt(self, txt_str):
        encoded_AES = AES.new(self.key, AES.MODE_CFB, self.iv)
        ciphertext = encoded_AES.encrypt(txt_str)
        return ciphertext.encode('hex')
        
    def decrypt(self, hex_str):
        ciphertext = binascii.unhexlify(hex_str)
        decoded_AES = AES.new(self.key, AES.MODE_CFB, self.iv)
        txt_str = decoded_AES.decrypt(ciphertext)
        return txt_str


def generate_key():
    key = hashlib.sha224("testkey").hexdigest()
    return key


# def test(cr):
#     test_str = "Testing encryption/decription of text!"
#     hex_str = cr.encrypt(test_str)
#     decrypted_str = cr.decrypt(hex_str).rstrip()
#     if decrypted_str == test_str:
#         print("[!] SUCCESS: Test successful!")
#     else:
#         print("[!] FAILURE: Test was not successful!")

# if __name__ == "__main__":
#     test_key = generate_key()
#     cr = Crypter(test_key)
#     test(cr)
