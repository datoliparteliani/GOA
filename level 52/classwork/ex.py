def find_next_square(sq):
    sqroot = int(sq ** 0.5)
    nextnumsq = (sqroot + 1) ** 2
    
    if sqroot * sqroot == sq:
        return nextnumsq
    return -1