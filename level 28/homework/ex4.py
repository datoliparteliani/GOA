def no_space(x):
    result = []
    for i in x:
        if i != " ":
            result.append(i)
    return "".join(result)