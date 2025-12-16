n = int(input("Enter the total data of the dictionary:"))

num = {}

for i in range(n):
    key, value = input("Enter the key and value separetly with the space:").split()
    num[key] = int(value)

print(num)

print(sum(num.values()))