def find_average(numbers):
    if not numbers:
        return 0
    total = 0
    for num in numbers:
        total += num
    avarage = total / len(numbers)
    return avarage