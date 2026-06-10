from string import ascii_lowercase

def is_isogram(strings):
    strip = list(c for c in strings.lower() if c.isalpha())
    if len(set(strip)) == len(strip):
        return True

    return False