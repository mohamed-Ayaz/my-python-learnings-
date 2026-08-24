#calculator program
print ("select the operation you want to perform(+,-,*,/):")
num1 = int(input("enter the first number:"))
num2 = int(input("enter the second number:"))
operation = input("enter the operation you want to perform:")
if operation == "+":
    result = num1 + num2
    print(f"the result of {num1} + {num2} is {result}") 
elif operation == "-":
    result = num1 - num2
    print(f"the result of {num1} - {num2} is {result}") 
elif operation == "*":
    result = num1 * num2
    print(f"the result of {num1} * {num2} is {result}")
elif operation == "/":
    if num2 == 0:
        print("division by zero is not allowed")
    else:
        result = num1 / num2
        print(f"the result of {num1} / {num2} is {result}")
else:
    print("invalid operation")