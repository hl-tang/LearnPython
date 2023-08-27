# Class
class MyClass:
    # Constructor
    def __init__(self, nums):   # self相当于C++的this指针
        # Create member variables
        self.nums = nums #只是这成员变量名和参数名一样
        self.size = len(nums)

    # To create a method
    # self key word required as param
    # that will give us access to our member variable
    def getLength(self):
        return self.size
    
    def getDoubleLength(self):
        return 2 * self.getLength()
