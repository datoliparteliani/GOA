def invert(lst):
    result = []
    
    for i in lst:
        result.append(-i)
        if result == []:
            return []
    return result