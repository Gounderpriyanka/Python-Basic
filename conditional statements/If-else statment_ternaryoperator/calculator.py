num = float(input("Enter a number1:"))
num2 = float(input("Enter a number2:"))

operators  = input("enter any operators = (+, -, *, %, /):")
match operators:
    case"+":
        print("Sum is:",num + num2)
    case"-":
        print("Subtraction is:",num - num2)
    case"*":
        print("Multiplication is:",num * num2)
    case"%":
        print("Quotient is:",num % num2)
    case"/":
        print("Division is:",num /num2)
    