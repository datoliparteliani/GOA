a = int(input("enter first num: "))
b = int(input("enter second num: "))
operation = "divide"

if operation == "add":
    result = a + b
elif operation == "subtract":
    result = a - b
elif operation == "multiply":
    result = a * b
elif operation == "divide":
    if b != 0:
        result = a / b
    else:
        result = "error: division by zero"
else:
    result = "invalid operation"

print(result)