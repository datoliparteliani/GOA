def vowel_one(s):
    vowels = "aeiou"
    numbers = ""
    
    for i in s.lower():
        if i in vowels:
            numbers += "1"
        elif i not in vowels:
            numbers += "0"
    return numbers