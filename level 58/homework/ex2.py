def reduce_fraction(fraction):
    numerator = fraction[0]
    denominator = fraction[1]
    
    a = numerator
    b = denominator
    while b != 0:
        usg = b
        b = a % b
        a = usg
    
    reduced_n = numerator // a
    reduced_d = denominator // a
    return (reduced_n, reduced_d)