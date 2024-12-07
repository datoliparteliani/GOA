result = 0

for i in range(5):
    number = int(input(f"enter number {i + 1}: "))
    result += number

mean = result / 5

print(f"total of the numbers is: {result}")
print(f"arithmetic mean is: {mean}")
