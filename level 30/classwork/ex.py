def highest_lowest(numbers):
    num_list = numbers.split()
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])

    highest = max(num_list)
    lowest = min(num_list)

    return str(highest) + " " + str(lowest)

print(highest_lowest("11 32 3 46 50"))