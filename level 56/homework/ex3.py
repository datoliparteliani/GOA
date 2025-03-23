def even_numbers(arr,n):
    nums = []
    
    for i in arr:
        if i % 2 == 0:
            nums.append(i)
    return nums[-n:]