def sums(n1,n2=0):
    print("n1:",n1)
    print("n2:",n2)
    total = n1 + n2
    return total

#possitional arguments
print("The sum of two number:",sums(2,3))

#keyword argument (named arguments)
print("The sum of two numbers:",sums(n2=23,n1=22))

#default arguments
print("The sum of two numbers:",sums(3))
