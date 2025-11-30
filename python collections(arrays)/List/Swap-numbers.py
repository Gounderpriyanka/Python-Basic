n = int(input("enter the size of the list:"))
list1 = []
for i in range(n):
    num1 = int(input())
    list1.append(num1)

print(list1)
idx1 = int(input("enter the index number1:"))
idx2 = int(input("Enter the index number2:"))
temp = list1[idx1]
list1[idx1] = list1[idx2]
list1[idx2] = temp
print(list1)



