def flatten(iterable):
    flat = []
    try: 
        for item in iterable:
            flat += flatten(item)
      
    except TypeError:
        if iterable != None:
            flat.append(iterable)
    
    return flat