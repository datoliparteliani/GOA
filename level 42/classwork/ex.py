def points(games):
    total_points = 0
    
    for i in games:
        x = int(i.split(":")[0])
        y = int(i.split(":")[1])
        
        if x > y:
            total_points += 3
        elif x == y:
            total_points += 1
    
    return total_points