number = int(input("enter number: "))

if number % 10 == 0 and number % 5 == 0:
    print("number is multiple of 10 and 5")
elif number % 10 != 0 and number % 5 == 0:
    print("number is multiple of only 5")
else:
    print("number is not multiple of 10 and 5")