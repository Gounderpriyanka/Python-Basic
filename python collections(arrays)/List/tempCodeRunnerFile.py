num = ["apple","banana","cherry","abs"]


# to print the lenght number of the variable
print(len(num))

# to check value is their in the list or not using if else
if "banana" in num:
    print("yes")
if "abs" not in num:
    print("no")

# to add a lichi in the list using append
num.append("lichi")
print(num)

# to insert newdata in the particular index no 
num.insert(2,"saled")
print(num)

# to cobinning the two variable using "EXTEND" method 
num2 = ["ice","cream"]
num.extend(num2)
print(num) 

# to remove the value from the list      
num.remove("saled")
print(num)

# by giving the index number removing the value from the list using the "pop" method
num.pop(1)
print(num)

# to remove the last value using "pop" method leaving the blank space in it
num.pop()
print(num)

#changing or updating item in the list
num[1] = "strawberry"
print(num)

#
num[2:5] = ["cherry"]
print(num)

#sorting method alphabet wise   
num.sort()#asscending way
print(num)

num.sort(reverse=True)# deccending order
print(num)

num.reverse()#to reverse the list
print(num)

friuts = [i for i in num if "a" in i ]
print(friuts)

new  = friuts.copy()
print(new)