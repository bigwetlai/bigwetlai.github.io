"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""



EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

"""
define the constants
EXPECTED_BAKE_TIME (int): the time to make a lasagna
PREPARATION_TIME (int): the time to prepare a layer of lasagna
"""

def bake_time_remaining(elapsed_bake_time):
    """
    Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
"""
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """
    evaluate the time of the preparation
    Param: 
    number_of_layers (int): number of layers of the lasagna
    assuming each layer requires PREPARATION_TIME minutes

    Return: 
        int: the time (in minutes) of preparation based on the nubmer of layers and PREPARATION_TIME
        for each layers
    """
    return PREPARATION_TIME * number_of_layers



def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
   
    """
evalutate the time consumed for this lasagna
Param: 
number_of_layers (int)
elapsed_bake_time
    """ 
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time


