# https://docs.python.org/3/tutorial/classes.html

import random
# Class
class MyClass:
    # Constructor
    def __init__(self, nums):   # self相当于C++的this指针
        # Create member variables
        self.nums = nums #只是这成员变量名和参数名一样
        self.size = len(nums)
        self.id = random.randint(0, 9999)

    # To create a method
    # self key word required as param
    # that will give us access to our member variable
    # 第一个参数不写self的话，就没法object.method()这样调用
    def getLength(self): #其实按照naming conventions最好是带underscore的
        return self.size
    
    def getDoubleLength(self):
        return 2 * self.getLength()	#call成员函数不需要再传入self参数了
    
    # 另一个特殊函数，返回string，可用于输出object
    # 若不override这个str method，直接输出的话是那个对象的内存地址
    def __str__(self):
        return f"obj{self.id}: {self.nums}"

    # 当然不带self参数的method也可以，只是这个method就不和特定的对象紐付ける了
    # 调用方式可以Class.method()，通常这个方法也是和整个类全局相关的
    # static method
    def print_all_objects(objects):
        for object in objects:
            print(object)
    
    # 重载等号
    def __eq__(self, other):
        # 自定义的相等规则，不看id。所以两个不同的对象(内存地址就不一样)判定为相等
        if self.nums == other.nums:
            return True
        return False


obj1 = MyClass([1,1,1])
print(obj1)
print(obj1.size)
print(obj1.getDoubleLength())

arr_obj = [MyClass([i,i,i]) for i in range(5)]
MyClass.print_all_objects(arr_obj)

print(obj1 == arr_obj[1]) #不重载等号的话，就是False。因为压根就不是同一个对象
print(id(obj1), id(arr_obj[1])) #memory address就不一样