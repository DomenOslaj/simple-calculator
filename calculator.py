num1 = int(input("Please enter a first number: "))
num2 = int(input("Please enter a second number: "))
operation = input("Please choose one from the following operations (+, -, *, /) ")

if operation == "+":
    result = str(num1 + num2)
    print("Result: " + result)

elif operation == "-":
    result = str(num1 - num2)
    print("Result: " + result)

elif operation == "*":
    result = str(num1 * num2)
    print("Result: " + result)

elif operation == "/":
    result = str(num1 / num2)
    print("Result: " + result)

else:
    print("That`s not a valid operation!")