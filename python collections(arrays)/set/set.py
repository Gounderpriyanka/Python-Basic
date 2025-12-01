# num = {"asd", 3 , "eds"}
# print(num)
# print(type(num))
# print(len(num))

# for i in num:
#     print(i)

# if "sia" in num:
#     print("yes")

# num.add("mik")
# print(num)

# names = { "aed", "lila", 34}
# num.update(names)
# print(num)

# num.remove("lila")
# print(num)

# num.discard("lion")
# print(num)


s1 = {1, 2, 3}
s2 = {4, 5, 6,2,3}

# s3 = s1.union(s2)
# print(s3)

# s1.update(s2)
# print(s1)

# s1.intersection_update(s2)
# print(s1)

s1.symmetric_difference_update(s2)
print(s1)

