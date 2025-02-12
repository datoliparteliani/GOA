def high_and_low(numbers):
    num_list = numbers.split()
    int_list = []
    for i in num_list:
        int_list.append(int(i))
    result = f"{max(int_list)} {min(int_list)}"
    return result