def distance(strand_a, strand_b):
    Hamming = 0
    while len(strand_a) == len(strand_b):
        for pos, nu in enumerate(strand_a):
            if nu != strand_b[pos]:
                Hamming += 1
        return Hamming

    raise ValueError("Strands must be of equal length.")
