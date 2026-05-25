"""This function determines if it the input year is a leap year"""

def leap_year(year):
    """ determines if the input is a leap year
        param: 
            year (int): the year to be determine
        return:
            (bool)
    """
    if year <= 0:
        raise ValueError("not positive year")
        
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False
