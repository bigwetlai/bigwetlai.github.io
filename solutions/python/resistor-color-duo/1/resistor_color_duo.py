color_dict = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
    }

def value(colors):
    c1 = colors[0]
    c2 = colors[1]
    d1 = color_dict[c1]
    d2 = color_dict[c2]
    
    return d1*10 + d2
