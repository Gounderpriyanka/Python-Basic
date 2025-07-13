n = int(input("enter a size of list:"))

list = []
for i in range(n):
    num = int(input())
    list.append(num)

idx1 = int(input("enter a index number1:"))
idx2 = int(input("enter a index number2:"))

print(list)
temp = list[idx1]
list[idx1] = list[idx2] 
list[idx2] = temp
print(list)