def manual_difference(set1, set2):
    result = set()
    for i in set1:
        if i not in set2:
            result.add(i)
    return result