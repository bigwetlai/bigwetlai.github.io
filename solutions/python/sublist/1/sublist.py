"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = None
SUPERLIST = None
EQUAL = None
UNEQUAL = None


SUBLIST = "<"
SUPERLIST = ">"
EQUAL = "="
UNEQUAL = "!="


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    if len(list_one) < len(list_two):
        if list_one == []:
            return SUBLIST
        if list_one[0] not in list_two:
            return UNEQUAL
        else:
            start_list = [index for index, item in enumerate(list_two) if item == list_one[0]]
            for start in start_list:
                if list_two[start:start+len(list_one)] == list_one:
                    return SUBLIST
            return UNEQUAL

    else:
        if list_two == []:
            return SUPERLIST
        if list_two[0] not in list_one:
            return UNEQUAL
        else:
            start_list = [index for index, item in enumerate(list_one) if item == list_two[0]]
            for start in start_list:
                if list_one[start:start+len(list_two)] == list_two:
                    return SUPERLIST
            return UNEQUAL


