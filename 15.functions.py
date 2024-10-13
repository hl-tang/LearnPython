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


# 一个老生常谈的按值传参 值传递
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

def changeArray(arr: list[int]):
    if len(arr) > 0:
        arr[0] = -100
    # arr.append(100) # work,因为在原list对象上修改
    arr = arr+ [100] # 不work,因为是产生了一个新的对象,parameter形参指向了新对象,和原list没关系了 (和Go的append效果类似)

# 内存管理，直接赋值与深浅拷贝
# 深堀り https://zhuanlan.zhihu.com/p/362702418
a = 1
b = a
a = a + 1
print(b)

l1 = [1, 2, 3]
l2 = l1
l1.append(4)
del l1  # l1被删除了，但list对象被l2引用所以依然在内存里，不会被回收
print("l2: ", l2)   # l2也变了
# !!! 要注意，很多bug就是这样出る的    同时list作为参数传进函数，函数里做的修改是会作用到这个list上的
changeArray(l2) # list会类似引用传递 其实都是pass by assignment即传对象引用pass by object reference(怎么直接赋值的就怎么传递,只是基本类型不可变，表现得像值传递；引用类型可变，表现得像引用传递)
print("l2: ", l2)
l3 = l2; print(l3)
l2.remove(2); print(l3) #l2的改动也会影响到l3，实际l2 l3指向一个对象

# 那怎么做才能赋值但不指向同一个对象？ shallow copy和deep copy
import copy
l4 = copy.copy(l2) #虽是浅拷贝，但复制的值是可变对象,且每个元素就一层，这里work；如果有元素是list(引用类型)那需要深拷贝
print(f"l4: {l4}")
l2.insert(1, 2) #l4不变，如果深拷贝就更不变了
print(l2, l3, l4)
print(id(l2), id(l3), id(l4))

# lambda函数
# https://www.youtube.com/watch?v=u3Hu2rTyXDg
# 可以用在sort(), filter(), map()里面作为参数，简化代码量
