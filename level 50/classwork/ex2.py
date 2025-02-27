def accum(st):
    result = []
    index = 0
    
    for i in st:
        part = i.upper() + i.lower() * index
        result.append(part)
        index += 1
    
    return "-".join(result)