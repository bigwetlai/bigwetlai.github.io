import math

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    if number == 1:
        return "deficient"
        
    divisors = 1
    
    divisor_max = math.floor(math.sqrt(number))
    for i in range(1, divisor_max):
        if number % (i+1) == 0:
            if number / (i+1) == (i+1) :
                divisors += i+1
            else:
                divisors += i+1 + int(number/(i+1))

    if divisors == number:
        return "perfect"

    if divisors > number:
        return "abundant"

    return "deficient"