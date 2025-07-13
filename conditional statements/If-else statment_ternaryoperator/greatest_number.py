num1 = float(input("enter a first number:"))
num2 = float(input("Enter a second number:"))
num3 = float(input("Enter a third number:"))

if(num1>num2 and num1>num3):
    print("The first number is the greatest number:",num1)
elif(num2>num1 and num2>num3):
    print("The second number is greatest number:",num2)
elif(num3>num1 and num3>num2):
    print("The third number is greatest number:",num3)
else:
    print("The numbers are equal ",num1,"=",num2,"=",num3)