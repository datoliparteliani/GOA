def to_alternating_case(string):
    result = ""
    for i in string:
        if i.islower():
            result += i.upper()
        elif i.isupper():
            result += i.lower()
        else:
            result += i
    return result