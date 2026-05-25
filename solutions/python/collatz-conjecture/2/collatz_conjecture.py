"""
    evaluate the steps required to reach 1 in 3x + 1 conjecture
"""

def steps(number):
    """
        param:
            number: the number input
    """
    if number <= 0: 
        raise ValueError("Only positive integers are allowed")
    
    step = 0
    while number != 1:
        if number %2 == 1:
            number = number * 3 + 1
        else:
            number = number / 2
        step = step + 1

    return step