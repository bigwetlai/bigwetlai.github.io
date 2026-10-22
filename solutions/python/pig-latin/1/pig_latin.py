from string import ascii_lowercase as alphabet
vowels = "aeiou"
consonant = ''.join(c for c in alphabet if c not in vowels)

def translate(text):
    word_list = text.split()
    pig_list = []

    for word in word_list:
        while not word[0] in vowels:
            if  word.startswith("xr") or word.startswith("yt"):
                break

            if word.startswith("qu"):
                word = word[2:] + word[:2]
                break

            word = word[1:] + word[0]

            if word.startswith('y'):
                break
                
        pig_list.append(word + "ay")

    return " ".join(pig_list)