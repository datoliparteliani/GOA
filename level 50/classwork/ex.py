def is_isogram(string):
    string = string.lower()
    seen = []
    return len([seen.append(letter) for letter in string if letter not in seen]) == len(string)