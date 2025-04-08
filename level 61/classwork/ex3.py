def no_space(x):
    x = x.split()
    for i in x:
        if i == " ":
            no_space.remove(i)
    return "".join(x)