"""
Atabash_Cipher.py
"""

PLAIN  = "abcdefghijklmnopqrstuvwxyz"
CIPHER = "zyxwvutsrqponmlkjihgfedcba"

ENCODE_DICT = dict(zip(PLAIN, CIPHER))
DECODE_DICT = dict(zip(CIPHER, PLAIN))

CHUNCK_LENGTH = 5

def encode(plain_text):
    ciphered = ""
    count = 0
    for char in plain_text.lower():
        if char.isalnum():
            if count > 0 and count % 5 == 0:
                ciphered += " "
            if char in ENCODE_DICT:
                ciphered += ENCODE_DICT[char]
            else:
                ciphered += char
            count += 1
    return ciphered

def decode(ciphered_text):
    decoded = ""
    for char in ciphered_text:
        if char in DECODE_DICT :
            decoded += DECODE_DICT[char]
        elif char.isnumeric():
            decoded += char
    return decoded