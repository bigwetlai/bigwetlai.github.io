L_Brackets = ["(", "[", "{"]
R_Brackets = [")", "]", "}"]
Brackets = dict(zip(R_Brackets, L_Brackets))

def is_paired(input_string):
    matcher = []
    for char in input_string:
        if char in L_Brackets:
            matcher.append(char)

        if char in R_Brackets:
            try:
                if matcher[-1] == Brackets[char]:
                    matcher.pop()

                else:
                    return False
            except:
                return False

    return not matcher