# while loops are similar
n = 0
while n < 5:
    print(n)
    n += 1

print(range(5))
print(list(range(5)))

# for loop
# Looping from i=0 to i=4
for i in range(5):      # for(int i=0;i<5;i++)
    if i != 4:
        print(i,end=" ")
    else:
        print(i)
print()

# Looping from i=2 to i=5
#很多这种都是左闭右开
for i in range(2,6):
    print(i)

# Looping from i=5 to i=2
for i in range(5,1,-1):     # for(int i=5;i>1;i--)
    print(i)


# for循环range最初确定了后，即使循环中改了长度，i也会按照最初的range自增
# 然后可能引发下标越界
""" s = "aabbcc"
for i in range(len(s)):
    if s[i] == 'b': #IndexError: string index out of range
        s = s.replace('b', '',1)
print(s) """


""" 
虽然之前遇到好多次了用for遍历list, 循环体内改变了list的长度(通常是减小), 会导致数组越界
还是有必要拿出来讲一下, Python的for in range写法其实和C++式的for(int i=0; i<len(a); i++)是不一样的
for-in会把一开始定义好的iterator全部遍历到,不会去有i<len(a)的判断
说到底是Python的for循环没有C++式的for(int i=0; i<len(a); i++), 只有for-in range式的
"""
a = [1, 2, 3, 4, 5]
for i in range(len(a)): # !!! 即使len改了,一开始range(0,5)也不会重新生成了,i照样从0遍历到4 !!! 所以下面主动加个判断,才起到了for(int i=0; i<len(a); i++)等价的效果
    if i >= len(a):
        break
    print("len: ", len(a))
    print("i: ", i)
    del a[i]
    print(a)

print("########")
a = [1, 2, 3, 4, 5]
i = 0
while i<len(a):
    print("len: ", len(a))
    print("i: ", i)
    del a[i]
    print(a)
    i += 1


# 循环中不需要使用循环变量的值，可以使用下划线 _ 来代替循环变量名
# N = int(input())

# a = []
# b = []
# c = []

# for _ in range(N):
#     line = input().split()
#     name = line[0]
#     age = int(line[1])
#     country = line[2]

#     a.append(name)
#     b.append(age)
#     c.append(country)

# # 打印数据
# for i in range(N):
#     print(a[i], b[i], c[i])

# 输入数据
# 3
# John 25 USA
# Emily 30 UK
# Michael 40 Australia
