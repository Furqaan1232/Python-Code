def Calculator(num1,num2,num3):
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter 3rd number: "))
    operator = input("Enter operator (+, -, *, /): ")
    if operator == "+":
        result = num1 + num2 + num3
    elif operator == "-":
        result = num1 - num2 - num3
    elif operator == "*":
        result = num1 * num2 -num3
    elif operator == "/":
        result = num1 / num2 /num3
    else:
      print("The operator is invalid")
    print("the result is" , result)
Calculator(3,4,5)