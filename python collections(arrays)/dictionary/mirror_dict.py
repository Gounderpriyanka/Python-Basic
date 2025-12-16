n = list(input("Enter the word:"))
print (n)
num = int(input("Enter the N-th position: "))

s1 = n[0 : num-1]
s2 = n[num-2 : ]

print(s1)
print(s2)

a1 = "abcdefghijklmnopqrstuvwxyz"
a2 = a1[::-1] # i didnot mention the starting point and ending
#point so it will concat whole variable and using the -1 it take value from right to left
a3 = dict(zip(a1,a2))
print(a3)

