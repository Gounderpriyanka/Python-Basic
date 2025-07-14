num = [1,2,3,4,5]
num.append(6)
num.insert(2,6)
print(num)
print(num.sort())
num.sort()
print(num)
num.sort(reverse=True)
print(num)
num.reverse()
print(num)


def findWordsContaining(words, x):
    return [i for i, word in enumerate(words) if x in word]


words_list = ["apple", "banana", "cherry", "date"]
substring = "an"
sat = findWordsContaining(words_list, substring)
print(sat)  


set = [24 , 45, 67,89]
newone = [ i for i in set if i > 25  ]
print(newone) 

a = [i for i in words_list if "a" in i ]
print(a)

words_list.insert(2,["mango","stawberry"])
print(words_list)
print(words_list[2][0])



def manipulate_list(nums):
    nums.append(6)
    nums.insert(2, 6)
    nums.sort()
    nums.reverse()
    return nums

nums = [1,2,3,4,5]
abc = manipulate_list(nums)
print(nums)
