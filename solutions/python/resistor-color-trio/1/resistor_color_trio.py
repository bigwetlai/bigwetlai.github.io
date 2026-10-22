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

def label(colors):
    d1 = color_dict[colors[0]]
    d2 = color_dict[colors[1]]
    d3 = color_dict[colors[2]]

    ohm =  (d1 *10 + d2) * 10**(d3)
    
    prefix = ""
    metric = 0
    while ohm/1000 >= 1:
        metric += 1
        ohm /= 1000
    if metric == 1: 
        prefix  = "kilo"
    elif metric == 2:
        prefix = "mega"
    elif metric == 3:
        prefix = "giga"

    
    return f"{str(int(ohm))} {prefix}ohms"
    
    

    
