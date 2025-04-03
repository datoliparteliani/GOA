def max_possible_score(points, seen):
    total = 0
    
    for i in points.items():
        if i[0] in seen:
            total += i[1] * 2
        else:
            total += i[1]
    return total