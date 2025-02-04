def binary_array_to_number(arr):
    binary_str = ""
    
    for i in arr:
        binary_str += str(i)
    decimal_value = int(binary_str, 2)
    return decimal_value