def is_pangram(sentence):
    sentence_strip = ''.join(filter(str.isalpha, sentence.lower()))

    if len(set(sentence_strip)) == 26:
        return True

    return False
    
