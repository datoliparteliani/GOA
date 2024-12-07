start = int(input("enter the starting number: "))
end = int(input("enter the ending number: "))

# Iterate through the range of numbers
for i in range(start, end + 1):
    if i % 2 == 0 and i % 3 == 0:
        print(f"{i} is a multiple of 2 and 3.")
    else:
        print(f"{i} is not a multiple of 2 and 3.")