"""
binary search
"""

def find(search_list, value):
    """
    search value in the list search_list
    input: 
        search_list: list
        value: int

    output:
        int: index of the value in the search_list 
        or 
        ValueError
    """
    
    index = 0
    while search_list:
        mid = len(search_list) // 2
        if value == search_list[mid]:
            index += mid
            return index
            
        if value < search_list[mid]:
            search_list = search_list[:mid]
            continue
            
        if value > search_list[mid]:
            search_list = search_list[ mid + 1: ]
            index += mid + 1

    raise ValueError("value not in array")
