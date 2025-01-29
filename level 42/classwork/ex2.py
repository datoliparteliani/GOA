def num_to_binary(num):
    result = ""

    while num > 0:
        remain = num % 2
        result = str(remain) + result
        num //= 2
    if result == "":
        result = "0"
    return result