# bisect就是binary search
# https://docs.python.org/zh-cn/3.12/library/bisect.html

import bisect

arr = [1, 5, 9, 9, 20, 46]
"""
bisect和bisect_right是一样的
bisect_right: 插入点左边的值<= x
bisect_left: 插入点左边的值< x
"""

# 当然要插入的值x不在数组里的话，都是一样的
index1 = bisect.bisect(arr, 8)
print(index1) # 2
index2 = bisect.bisect_right(arr, 8)
print(index2)
index3 = bisect.bisect_left(arr, 8)
print(index3)

index1 = bisect.bisect(arr, 9)
print(index1)
index2 = bisect.bisect_right(arr, 9)
print(index2) # 4
index3 = bisect.bisect_left(arr, 9)
print(index3) # 2
