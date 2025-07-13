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
newone = [ i for i in set if i > 25 print(i) ] 