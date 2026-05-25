def equilateral(sides):
    if isTrangle(sides):
        a, b, c = sides
        return a == b and b == c
    else:
        return False

def isosceles(sides):
    if isTrangle(sides):
        a, b, c = sides
        return a == b or ( b == c or a == c )
    else:
        return False

def scalene(sides):
    if isTrangle(sides):
        a, b, c = sides
        return a != b and ( b != c and a != c )
    else:
        return False

        
def isTrangle(sides):
    a, b, c = sides

    return a + b > c and ( b + c > a and a + c > b )

