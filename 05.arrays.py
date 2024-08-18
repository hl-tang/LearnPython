# Arrays (called lists in python)
arr = [1,2,3]
print(arr)

# Arrays in Python are dynamic arrays by default
# so can be used as stack
# python的list就可以当stack，python没有单独的栈，在需要栈的时候往往使用list
arr.append(4)   # push
arr.append(5)
print(arr)

arr.pop()   # pop from the end
print(arr)

# 当然stack只是操作受限的数组，list is technically an array
# we can insert into the middle
arr.insert(1,"7") # index, value
print(arr)
# 任意位置insert,remove
x = ['a', 'b', 100, 200]
x.remove('b')   # remove()的参数是值
print(x)
del x[2]    # 按下标删除
print(x)
del x[:]; print(x)  # slices
del x   # del可以直接删对象
# print(x)    #NameError: name 'x' is not defined
'''
insert()  O(n)时间复杂度
index[] 根据下标访问    O(1)时间复杂度
所以Python的list是数组(顺序存储)，不是链表(链式存储)
'''
print(arr[0])
arr[3] = 0
print(arr)

# len()
print(len(arr))
# Careful: -1 is not out of bounds, it's the last value 
print(arr[-1] == arr[len(arr)-1])
# Indexing -2 is the second to last value, etc.
arr = [1, 2, 3]
print(arr[-2])

# Initialize an array of variable size n
# with default value of 1
n = 10
arr = [1] * n
print(arr)
print(len(arr))

# Sublists (aka slicing 切片)
#切片 python强大的语法糖之一，不仅可以用非负数索引，负数索引的合理使用可以节省不少代码量
arr = [1,2,3,4]
print(arr[1:3])
# Similar to for-loop ranges, last index is non-inclusive
print(arr[0:len(arr)])

# Unpacking 数组的所有单个元素赋值给变量
a,b,c=[1,2,3]
print(a,b,c)
#print([1,2,3])


# Loop through arrays   遍历数组 for(int i=0;i<n;i++){cout<<a[i]<<endl;}
nums = [1, 2, 3, 4, 5]

# Using index
for i in range(len(nums)):
    print(nums[i],end=" ")
print()

# Without index
for n in nums:
    print(n,end=" ")
print()

# With index and value
# 如果遍历的对象是dict，用items()
for i,n in enumerate(nums):
    print(i,n)

# Loop through multiple arrays simultaneously
# with unpacking
nums1 = [1,3,5]
nums2 = [2,4,6]
#print(zip(nums1, nums2))
for n1, n2 in zip(nums1, nums2):
    print(n1,n2)

# Reverse
nums.reverse()
#print(nums.reverse()) #.reverse()逆置后return None
print(nums)

# list.index(element, start, end)返回下标位置
arr = [1,2,3,3,4,5]
print(arr.index(3))
print(arr.index(3,3))

# list相加：合并
l1 = [1, 2, 3]
l2 = l1 + ['a', 'b']
print(l1)
print(l2)
l1.extend([4, 5]) # extend在原数组上改(相当于append multiple objects)
print(l1)