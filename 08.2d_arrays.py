# 2-D lists    二维数组
arr = [[0]*4 for i in range(4)]
print(arr)
arr[0][0]=3
print(arr)

# This won't work
arr = [[0] * 4] * 4
print(arr)
arr[0][0]=3 #其他行也会修改
print(arr)

# 可以先定义个空list(数组)，然后要几行就append几次，这样各行的列数还可以不同
arr = []
for _ in range(3):
    # arr.append(input())
    arr.append([])
print(arr)

arr = [[] for _ in range(3)] #这样也行
# arr = [input() for _ in range(3)]
print(arr)

# 用numpy
import numpy as np
np_arr = np.ones((3,4), dtype=int)
print(np_arr)
np_arr[0][0]=0
print(np_arr)
# 三维数组
np_arr = np.zeros((3,2,1), dtype=int)
print(np_arr)