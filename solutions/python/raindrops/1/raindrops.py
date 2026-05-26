def convert(number):
    ans = ""

    if number % 3 == 0:
        ans = ans + "Pling"
    if number % 5 == 0:
        ans = ans + "Plang"
    if number % 7 == 0:
        ans = ans + "Plong"
    if (number % 3 and number % 5) and number % 7:
        ans = ans + str(number)
    return ans