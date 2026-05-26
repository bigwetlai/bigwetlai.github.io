def is_Trangle(func):
    def wrapper(sides):
        return func(sides) and sum(sides) > 2 * max(sides)
        
    return wrapper

@is_Trangle
def equilateral(sides):
    return len(set(sides)) == 1

@is_Trangle
def isosceles(sides):
    return len(set(sides)) < 3
    
@is_Trangle
def scalene(sides):
    return len(set(sides)) == 3

        


