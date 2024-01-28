# Division is decimal by default    相当于默认是double型，不是int
print(5 / 2)

# Double slash rounds down
print(5 // 2)

# CAREFUL: most languages round towards 0 by default
# but in Python negative integer division will round down
print(-3 // 2)
print(-3 / 2)
print(int(-3/2))


# Modulo is similar to most languages
print(11 % 3)
# Except for negative values
print(-10 % 3)      #和数论一样，-10+3*4

# To be consistent with other languages modulo
import math
print(math.fmod(-10, 3))

# More math helpers
print(math.floor(3/2))  #向下取整
print(math.ceil(3/2))  #向上取整
print(math.sqrt(2))
print(math.pow(2,3))

# Infinity integer 要float括起来
float("inf")    # Maximum integer
print(float("inf"))
float("-inf")    # Minimum integer
print(float("-inf"))

'''
Why float("inf") & float("-inf") come up?
Python numbers are infinite so they never overflow
'''
print(math.pow(2,200))  #约1.6e60，C++ int最大就2e10
# But still less than infinity
print(math.pow(2,200) < float("inf"))

# 排列组合
from scipy.special import perm, comb
print(perm(6,3))
print(comb(6,3))
print(comb(64,32)%1000000000) #数字大了以后不精确了，正解应该942590534

def my_comb(m: int, n: int) -> int:
    # return math.factorial(m) / (math.factorial(n) * math.factorial(m-n))
    return math.factorial(m) // (math.factorial(n) * math.factorial(m-n))
# /除结果也是942590464, //除结果对了
print(my_comb(64,32) % 1000000000)