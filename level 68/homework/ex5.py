def myfunc(arr):
    return [(lambda x : x ** 2)(x) for x in arr if x % 2 == 0]
print(myfunc([1, 4, 2]))