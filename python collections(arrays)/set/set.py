num = {"asd", 3 , "eds"}
print(num)
print(type(num))
print(len(num))

for i in num:
    print(i)

if "sia" in num:
    print("yes")

num.add("mik")
print(num)

names = { "aed", "lila", 34}
num.update(names)
print(num)

num.remove("lila")
print(num)

num.discard("lion")
print(num)
