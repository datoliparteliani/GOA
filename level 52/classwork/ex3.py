def series_sum(n):
    if n == 0:
        return "0.00"
    
    total = 0
    for i in range(n):
        total += 1 / (3 * i + 1)
    if len(str(total)) == 2:
        return str(result) + "0"
        
    result = round(total, 2)

    return str(result)