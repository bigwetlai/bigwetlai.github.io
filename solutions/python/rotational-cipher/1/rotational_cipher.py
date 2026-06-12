def rotate(text, key):
    rotated = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                char = chr(  (ord(char) - ord('a') + key ) % 26 + ord('a')  )
            else:
                char = chr(  (ord(char) - ord('A') + key ) % 26 + ord('A')  )
        rotated += char

    return rotated