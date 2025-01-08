def find_short(s):
    words = s.split()
    
    shortest_length = float('inf')
    
    for word in words:
        word_length = len(word)
        if word_length < shortest_length:
            shortest_length = word_length
    
    return shortest_length