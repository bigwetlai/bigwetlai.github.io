"""
a function that flattens an array
"""

def flatten(iterable):
    """
    check if input is an iterable and recursively flatten the iterable
    input: iterable
    output: a flattened list
    """
    flat = []
    try: 
        for item in iterable:
            flat += flatten(item)
      
    except TypeError:
        if iterable is not None:
            flat.append(iterable)
    
    return flat