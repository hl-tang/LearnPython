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