def find_short(s):
    spls = s.split()
    shortest = len(spls[0])
    
    for i in spls:
        _len = len(i)
        if _len < shortest:
            shortest = _len
            
    return shortest