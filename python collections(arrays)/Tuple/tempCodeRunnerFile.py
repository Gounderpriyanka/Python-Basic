num = (1,2,3,4,5)
print(type(num))

tup = []

for i in reversed(num):
    tup.append(i)

num1 = tuple(tup)
print(tup)
