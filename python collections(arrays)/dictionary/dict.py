phones = {
    "tama" : 8656,
    "Nima" : 6789,
    "lila" : 8123,
    "sila" : 7345
}

print(phones)
# print(type(phones))
# print(len(phones))

#to print the value of the particular key
# print(phones["Nima"])

#same but using the (get)  method with curly brackets
# print(phones.get("Nima"))

#to print all the keys of the dict variable 
# print(phones.keys())

#to change the keys value directly  
# phones["Nima"] = 1234
# print(phones)

#to add another key and key value directly in dict variable 
# phones["kia"] = 7023
# print(phones)

#created another dict varible 
# more_phones = {
#     "edi" : 789
# }

#to combine the two dict variable together using the (update) method 
# phones.update(more_phones)
# print(phones)

#to delete the paticular key value in the dict variable 
# phones.pop("edi")
# print(phones)

#to remove the lastly added keyvalue in the dict variable
# phones.popitem()
# print(phones)

#to clear all the key and key value of the dict variable
# phones.clear()
# print(phones)

#to print the keys of the dict variable
# for i in phones:
#     print(i)

# to print the key vales of the dict variable
# for x in phones:
#     print(phones[x])

#to print all the keys and keys value line by line in the loop
for i in phones.items():
    print(i)
