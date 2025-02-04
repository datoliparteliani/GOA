def row_sum_odd_numbers(n):
    first_num = n * (n - 1) + 1
    total = 0
    
    for i in range(n):
        total += first_num + 2 * i
    return total