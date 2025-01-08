def square_digits(num):
    num_str = str(num)
    result_str = ''
    
    for i in num_str:
        result_str += str(int(i) ** 2)
    
    return int(result_str)