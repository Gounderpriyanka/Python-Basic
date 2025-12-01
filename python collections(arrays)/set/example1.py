# ar1 = [1,5,10,20,40,80]
# ar2 = [6,7,20,80,100]
# ar3 = [3,4,15,20,30,70,80,120]

ar1 = [1,5,5]
ar2 = [3,4,5,5,10]
ar3 = [5,5,10,20,1]

s1 = set(ar1)
s2 = set(ar2)
s3 = set(ar3)

final_set = s1.intersection(s2,s3)
final_list = list(final_set)
print(type(final_list))
print(final_list)


