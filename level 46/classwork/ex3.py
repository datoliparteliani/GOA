def descending_order(num):
    num_list = list(str(num))
    num_list.sort()
    num_list = num_list[::-1]
    return int("".join(num_list))