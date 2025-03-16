def sort_by_length(arr):
    pairs = []  
    
    for i in arr:
        pairs.append([len(i), i])  

    pairs.sort()  

    sorted_words = []  
    for o in pairs:
        sorted_words.append(o[1])  

    return sorted_words