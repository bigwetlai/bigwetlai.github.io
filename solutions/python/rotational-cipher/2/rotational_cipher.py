ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def rotate(text, key):
    rotated = ALPHABET[key:] + ALPHABET[:key]
    text = text.translate(
        str.maketrans(
            ALPHABET+ALPHABET.lower(), rotated+rotated.lower()
                     )
                        )

    return text