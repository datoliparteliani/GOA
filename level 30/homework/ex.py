def positive_sum(arr):
    _sum = 0
    for num in arr:
        if num > 0:
            _sum += num
    return _sum