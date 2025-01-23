def capitals(word):
    uppercase = []
    
    for i in range(len(word)):
        if word[i].isupper():
            uppercase.append(i)
    
    return uppercase