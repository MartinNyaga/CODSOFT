def calculator(x, operator, y):

    if operator == "+":
        result = x + y
    elif operator == "-":
        result = x - y
    elif operator == "/":
        result = x / y
    elif operator == "*":
        result = x * y
    

    return result

x = float(input("Enter the first number: "))
operator = input("Enter Operator: ")
y = float(input("Enter the second number: "))

output = calculator(x, operator, y)

print("The output of calculation is : ", output)