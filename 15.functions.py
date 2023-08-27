# Functions
def myFunc(n, m):
    return n * m

print(myFunc(3,4))

# 可以像c++一样，直接return，也能不return


# 指定函数的返回值类型
def add_numbers(a: float, b: float) -> float:
    sum = a + b
    return sum

print(add_numbers(2.2, 3.6))


# 一个老生常谈的按值传参
def mySwap(a,b):
    tmp = a
    a = b
    b = tmp

a = 5; b=8
print(a,b)
mySwap(a,b)
print(a,b)

def mySwap2(a, b):
    return b, a

a = 5; b = 8
print(a, b)
a, b = mySwap2(a, b)
print(a, b)

# 深堀り https://zhuanlan.zhihu.com/p/362702418
a = 1
b = a
a = a + 1
print(b)

l1 = [1, 2, 3]
l2 = l1
l1.append(4)
del l1  # l1被删除了，但list对象被l2引用所以依然在内存里，不会被回收
print(l2)   # l2也变了
