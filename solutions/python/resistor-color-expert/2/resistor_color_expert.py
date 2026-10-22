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
              "white": 9,
             }

tolerance_dict = {
    "grey": "0.05%",
    "violet": "0.1%",
    "blue": "0.25%",
    "green": "0.5%",
    "brown": "1%",
    "red": "2%",
    "gold": "5%",
    "silver": "10%",
}

def resistor_label(colors):
    if len(colors) == 1:
        return "0 ohms"
    tol = colors.pop()
    mul = colors.pop() 
    ohm = 0 
    for color in colors:
        ohm = ohm * 10 + color_dict[color]
    ohm = ohm * 10**color_dict[mul]
    
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


    return f"{ohm:g} {prefix}ohms ±{tolerance_dict[tol]}"
