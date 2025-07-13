num = float(input("Enter a number:"))
if(num%5==0 or num%3==0):
    if(num%15==0):
        print("It is divisible by 15:",num)
    else:
        print("The number is not divisible by 15 but its is divisible by 5 or 3:",num)
else:
    print("The number is not divisible by 5 or 3:",num)