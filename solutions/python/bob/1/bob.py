def response(hey_bob):
    if " ".join( hey_bob.split() ) == "":
        return "Fine. Be that way!"

    if hey_bob.isupper():
        if " ".join( hey_bob.split() )[-1] == "?":
            return "Calm down, I know what I'm doing!"
        return "Whoa, chill out!"

    if " ".join( hey_bob.split() )[-1] == "?":
        return "Sure."

    return "Whatever."