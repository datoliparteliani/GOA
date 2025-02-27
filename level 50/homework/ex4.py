def longest(a1, a2):
    combined = set(a1 + a2)
    
    return ''.join(sorted(combined))