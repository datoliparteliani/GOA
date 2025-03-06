def print_array(arr):
    list = []
    
    for i in arr:
        list.append(str(i))
    
    result = ",".join(list)
    return result