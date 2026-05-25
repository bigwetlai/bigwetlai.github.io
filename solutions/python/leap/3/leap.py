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
        
    return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0) 
