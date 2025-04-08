def correct(s):
    result = ""
    for i in s:
        if i == "5":
            result += i.replace("5", "S")
        elif i == "0":
            result += i.replace("0", "O")
        elif i == "1":
            result += i.replace("1", "I")
        else:
            result += i
    return result