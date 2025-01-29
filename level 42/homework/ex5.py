def sum_str(a, b):
    if a == "":
        num1 = 0
    else:
        num1 = int(a)

    if b == "":
        num2 = 0
    else:
        num2 = int(b)

    result = num1 + num2
    return str(result)