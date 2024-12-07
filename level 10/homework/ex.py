ages = int(input("how many ages do you want to enter?: "))

for i in range(ages):
    age = input(f"enter age for person {i + 1}: ")
    print(f"person {i + 1} is {age} years old.")