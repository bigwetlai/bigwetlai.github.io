from string import ascii_uppercase as upper

def rows(letter):
    diamond = []
    N = upper.index(letter)
    for i_row in range(2*N+1):
        row = ""
        if i_row <= N:
            for indx in range(2*N+1):
                if indx == (N - i_row) or indx == (N + i_row):
                    row += upper[i_row]
                else:
                    row += ' '

        if i_row > N:
            for indx in range(2*N+1):
                if indx == (i_row - N) or indx == (3*N - i_row):
                    row += upper[2*N-i_row]
                else:
                    row += ' '
        diamond.append(row)
            

    return diamond