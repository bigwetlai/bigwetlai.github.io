#! /usr/bin/env python
"""
Atabash_Cipher.py
"""

from string import ascii_lowercase

ENCODING = str.maketrans(ascii_lowercase, ascii_lowercase[::-1])

def encode(plain_text):
    ciphered = "".join(char for char in plain_text.lower() if char.isalnum()).translate(ENCODING)
    ciphered = " ".join(ciphered[index:index+5] for index in range(0, len(ciphered), 5))
    return ciphered

def decode(ciphered_text):
    decoded = "".join(char for char in encode(ciphered_text) if not char.isspace())
    return decoded
    
