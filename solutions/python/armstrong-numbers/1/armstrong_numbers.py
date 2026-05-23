def is_armstrong_number(number):
    num_str = str(number)
    digits = len(num_str)
    total = sum(int(digit) ** digits for digit in num_str)

    return total == number 
