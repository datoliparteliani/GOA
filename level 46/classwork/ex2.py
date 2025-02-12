def disemvowel(string_):
    vowels = "aeiouAEIOU"
    result = []
    
    for i in string_:
        if i not in vowels:
            result.append(i)
    
    return ''.join(result)