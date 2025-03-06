def string_clean(s):
    arr = []
    
    for i in s:
        if not i.isdigit():
            arr.append(i)
    return "".join(arr)