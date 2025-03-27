def elimination(arr):
    set_ = set()
    
    for i in arr:
        if i in set_:
            return i
        set_.add(i)
    return None