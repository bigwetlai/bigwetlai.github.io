from string import ascii_lowercase

def is_pangram(sentence):
    if set(ascii_lowercase) <= set(sentence.lower()):
        return True

    return False
