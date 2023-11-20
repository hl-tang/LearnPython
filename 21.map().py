# Python中的map()函数，而非hash map
# https://docs.python.org/3/library/functions.html#map

# map(function, iterable): func作用在每一个迭代对象上
# 返回一个与传入可迭代对象大小一样的map对象。Python2中返回的是list

# 经常这样处理输入
""" n, m = map(int, input().split()) #input两个数
a = list(map(int, input().split())) #input一个数组

n, m = list(map(int, input().split())) #list这样Unpacking赋值也是对的 """

# 其实用list comprehensions是等价的
# map(f, iterable)  [f(x) for x in iterable]
# https://stackoverflow.com/questions/10973766/understanding-the-map-function
# a, b = [int(x) for x in input().split()]
# print(a,b)

# 把[1, 2, 3]: list转为123: int
num = int(''.join(map(str,[1, 2, 3])))
print(num)

# 把"123": str转为[1, 2, 3]: list
# 这里没法直接用split()分割
arr = list(map(int, "123")) #"123"是可迭代的，int作用在每个字符上
print(arr)

s = "123"
arr = []
for s_ in s:
    arr.append(int(s_))
print(arr)

arr = [int(s_) for s_ in s]
print(arr)