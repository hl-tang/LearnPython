# List comprehension
# 初始化list的高级方法
arr = [i for i in range(5)] #i从0遍历到4，每次都把i(for左边)加入到数组
print(arr)

arr = []
for i in range(1,6):
    arr.append(i)
print(arr)

import math
arr = [math.pow(i,2) for i in range(5)]
print(arr)

arr = [pow(i,2) for i in range(5)]
print(arr)