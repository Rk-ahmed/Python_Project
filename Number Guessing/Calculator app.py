num1 = float(input("Enter your first number: "))
operator = input("Enter an operator(+, -,*, /): ")
num2 = float(input("Enter your second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Cannot divide by Zero"
else:
    result = "Invalid Operator"

print("Result: ", result)