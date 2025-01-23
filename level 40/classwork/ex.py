def password(st):
    if len(st) < 8:
        return False
    
    has_upper = False
    has_lower = False
    has_digit = False
    
    for char in st:
        if char >= 'A' and char <= 'Z':
            has_upper = True
        elif char >= 'a' and char <= 'z':
            has_lower = True
        elif char >= '0' and char <= '9':
            has_digit = True
    
    if has_upper and has_lower and has_digit:
        return True
    else:
        return False