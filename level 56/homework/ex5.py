def geometric_sequence_elements(a, r, n):
    sequence = []
    sequence_str = []
    
    for i in range(n):
        sequence.append(a * r**i)
    
    for j in sequence:
        sequence_str.append(str(j))
    
    return ', '.join(sequence_str)