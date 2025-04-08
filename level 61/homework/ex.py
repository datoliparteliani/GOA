def first_non_consecutive(arr):
    index = 1
    while index < len(arr):
        if arr[index] != arr[index - 1] + 1:
            return arr[index]
        index += 1
    return None