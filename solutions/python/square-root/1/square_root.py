def square_root(number):
    #initial guess
    exp = 0
    while number > 10**(exp+1):
        exp += 1
        
    if exp % 2:
        exp = exp - 1
        
    if number / 10**(exp-1) >= 10 :
        init = 6 * 10**exp
    else:
        init = 2 * 10**exp


    #Newton's method
    x_n = init
    while abs(number - x_n**2) > 1e-6:
        x_n = 1/2 * (x_n + number/x_n)

    return round(x_n, 2)