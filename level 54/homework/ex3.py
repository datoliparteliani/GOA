def series_sum(n):
    total_sum = 0
    
    for i in range(n):
        total_sum += 1 / (3 * i + 1)
    
    total_sum = round(total_sum, 2)
    
    return str(total_sum)