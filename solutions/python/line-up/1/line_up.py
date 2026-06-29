def line_up(name, number):
    
    if number % 100 in (11, 12, 13):
        ordinal = str(number)+"th"
    elif number % 10 == 1:
        ordinal = str(number)+"st"
    elif number % 10 == 2:
        ordinal = str(number)+"nd"
    elif number % 10 == 3:
        ordinal = str(number)+"rd"
    else:
        ordinal = str(number)+"th"

    return f"{name}, you are the {ordinal} customer we serve today. Thank you!"