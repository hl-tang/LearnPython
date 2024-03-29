# HashSet
# can search in O(1) time
# set本质是哈希表，会对其内部元素去重，检查一个元素是否在set内部的时间复杂度是O(1)
mySet = set()

# can insert value also in constant time
mySet.add(1)
mySet.add(2)
print(mySet)
# Unlike list,there can't be any duplicates in hash set

#要素数
print(len(mySet))
# search
print(1 in mySet)
print(2 in mySet)
print(3 not in mySet)

mySet.remove(2) # remove also in constant time
print(2 in mySet)

# Initialize a set with a bunch of values, we can pass in a list
# list to set
print(set([1, 2, 3]))
a = set([0] * 4)
print(a)

# Set comprehension
mySet = {i for i in range(5)}
print(mySet)
print(type(mySet))
print(min(mySet))
print(max(mySet))

# mySet2 = {}   #这样空初始化默认是dict
# mySet2 = set()    #所以空set初始化这样干
mySet2 ={1,2,3,4,5,6}   #但这样带值的初始化是ok的
print(type(mySet2))
print(mySet2)
for i in range(1,6):
    mySet2.add(str(i))
print(mySet2)

print(list(mySet2))

# print(mySet2[0]) #错误 set是不能带下标的 'set' object is not subscriptable

# 清空
mySet2.clear()
print(mySet2)
del mySet2
# print(mySet2) #'mySet2' is not defined

# 数学中的集合类计算
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
print(x.difference(y))  #差
print(y.difference(x))
print(x.intersection(y))    #交
print(x.union(y))   #并