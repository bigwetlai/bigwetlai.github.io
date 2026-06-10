def is_valid(isbn):
    isbn = isbn.replace('-', '')
    verify = 0
    
    if len(isbn) != 10:
        return False
    for digit in isbn[:-1]:
        if not digit.isnumeric():
            return False

    if isbn[-1] == 'X':
        verify += 10
    elif not isbn[-1].isnumeric():
        return False
    else:
        verify += int(isbn[-1])
    
    for i in range(10, 1, -1):
        verify += i * int(isbn[-i])

    return verify % 11 == 0
