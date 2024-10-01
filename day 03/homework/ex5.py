number = int(input("enter number between 10-99: "))

digit_one = number // 10
digit_two = number % 10
digits_sum = digit_one + digit_two

print(f"the sum of two digits is: {digits_sum}")