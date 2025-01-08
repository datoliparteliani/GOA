def filter_list(l):
    result = []
    for i in l:
        if type(i) == int and i >= 0:
            result.append(i)
    return result