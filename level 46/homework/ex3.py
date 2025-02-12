def odd_or_even(arr):
    
    
    if arr == []:
        arr == [0]
        
    if sum(arr) % 2 == 0:
        return "even"
    return "odd"