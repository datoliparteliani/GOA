def is_isogram(string):
    string =  string.lower()
    repeat = set()

    for i in string:
        if i in repeat:
            return False
        repeat.add(i)
    return True