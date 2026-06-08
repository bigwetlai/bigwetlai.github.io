def score(x, y):
    dist = x**2 + y**2
    if dist > 100:
        return 0
    if dist > 25:
        return 1
    if dist > 1:
        return 5
    return 10
    
    
