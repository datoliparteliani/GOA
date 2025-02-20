def fake_bin(x):
    result = []
    for i in x:
        if int(i) < 5:
            result.append("0")
        else:
            result.append("1")
    return "".join(result)