number = int(input("enter number: "))

if number > 100 and number % 2 == 0:
    print("number is more than 100 and is even")
elif number > 100 and number % 2 != 0:
    print("number is more than 100 and is odd")
else:
    print("number is less than 100 and is odd")