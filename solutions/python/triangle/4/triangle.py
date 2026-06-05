"""
evalueate if give 3 integer can form a triangle

"""

def validtriangle(trangle_func):
    def wrapper(sides):
        return sum(sides) > 2 * max(sides) and trangle_func(sides)

    return wrapper

    
@validtriangle
def equilateral(sides):
    return len(set(sides)) == 1

@validtriangle
def isosceles(sides):
   return len(set(sides)) < 3

@validtriangle
def scalene(sides):
    return len(set(sides)) == 3