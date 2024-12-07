arr = [9,5,94,711,52,96,71,8]
random_item = arr[0]

for i in arr:
    if i < random_item:
        random_item = i
print(random_item)