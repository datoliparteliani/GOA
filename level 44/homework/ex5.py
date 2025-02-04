def divisors(integer):
    result = []
    
    for i in range(2, integer - 1):
        if integer % i == 0:
            result.append(i)
            
    if result:
        return result
    else:
        return f"{integer} is prime"