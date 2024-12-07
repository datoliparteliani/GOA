numbers = [12, 66, 100, 45, 35, 60]

multiples = []

for i in numbers:
    if i % 5 == 0 and i % 3 == 0:
        multiples += [i]
print(multiples)