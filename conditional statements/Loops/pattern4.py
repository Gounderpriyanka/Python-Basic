num = int(input("Enter a number:"))
for i in range(num+1):
    for i in range(1,i+1):
        print(chr(64+i),end="")
    print()