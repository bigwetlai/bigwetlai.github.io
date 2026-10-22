def sum_of_multiples(limit, multiples):
    points = 0
    for number in range(1, limit):
        for item in multiples:
            if item == 0:
                break
            if number % item == 0:
                points += number
                break

    return points
        
