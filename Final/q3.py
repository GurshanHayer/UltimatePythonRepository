expression = input("Enter expression: ")
total = 0

if expression[1] == "+":
    total = int(expression[0]) + int(expression[2])
elif expression[1] == "-":
    total = int(expression[0]) - int(expression[2])
elif expression[1] == "*":
    total = int(expression[0]) * int(expression[2])
elif expression[1] == "/":
    total = int(expression[0]) / int(expression[2])

equation = str(expression) + "=" + str(total)

print(equation)