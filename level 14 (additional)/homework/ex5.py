number = 0

while number >= 0:
    number = int(input("please enter a positive number (or a negative number to exit): "))
    if number >= 0:
        print(f"you entered: {number}")
    else:
        print("you have entered a negative number.")
