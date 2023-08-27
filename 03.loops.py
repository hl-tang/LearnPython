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
