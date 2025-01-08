def digitize(n):
    n_str = str(n)
    
    reversed_n = []
    
    for i in n_str[::-1]:
        reversed_n.append(int(i))
    
    return reversed_n