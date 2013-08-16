from Crypto.Cipher import AES
from Crypto import Random
import binascii
import os


key = '1234567891111111'
iv = Random.get_random_bytes(16)

def generate_key():
    key = os.urandom(16).encode('base_64')
    return key

def encrypt(txt_str):
    encoded_AES = AES.new(key, AES.MODE_CFB, iv)
    ciphertext = encoded_AES.encrypt(txt_str)
    return ciphertext.encode('hex')
    
def decrypt(hex_str):
    ciphertext = binascii.unhexlify(hex_str)
    decoded_AES = AES.new(key, AES.MODE_CFB, iv)
    txt_str = decoded_AES.decrypt(ciphertext)
    return txt_str

def test():
    test_str = "Testing encryption/decription of text!"
    hex_str = encrypt(plain_text)
    decrypted_str = decrypt(hex_str).rstrip()
    if decrypted_str == test_str:
        print("[!] SUCCESS: Test successful!")
    else:
        print("[!] FAILURE: Test was not successful!")
        
test()