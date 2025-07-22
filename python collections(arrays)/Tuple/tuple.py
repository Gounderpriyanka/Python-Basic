car = ("bmw","bugguti","scropio")

num = ("3",)
#to check the type of tuple
print(type(num))

#to check the lenght og tuple
print(len(num))
color = ("red","yellow","blue","pink")

print(color[1])#positive indexes
print(color[-1])#negative indexes
print(color[1:3]) #range indexing
print(color[-2:]) #negative range indexing

#cheking an item in tuple
if "green" in color:
    print("yes")

#print the tuples
for i in color:
    print(i)

#concatenate the tuple
# new_color = ("green","orange")
# color += new_color 
# print(color) 

#unpacking
color1, color2, color3, color4 = color
print(color1, color2, color3, color4)
