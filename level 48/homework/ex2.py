def invert(lst):
    result = []
    
    for i in lst:
        result.append(-i)
        if result == []:
            return []
        elif result == [0]:
            return [0]
    return result