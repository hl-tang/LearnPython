# 本节开始就不是原油管Python for Coding Interviews - Everything you need to Know的内容了
# 之后就自己总结了

# 十进制转二进制 bin()
# https://docs.python.org/3/library/functions.html#bin
print(bin(5))
print(type(bin(10)), bin(10)) #返回值是str
print(bin(-10))
# If the prefix “0b” is desired or not
a = f'{-10:b}'
print(a)
print('-'+bin(-10)[3::])
print("转换为八进制为：", oct(-10))
print("转换为十六进制为：", hex(-10))
#注意其他进制的参数都是str
print(int("-1010", 2)) # 二进制转换为十进制
print(int("-12", 8)) # 八进制转换为十进制
print(int("-a", 16)) # 十六进制转换为十进制


# 位运算
#好像操作符两边必须是int
print(5 << 2) #左移2位，乘4
print(0b101 << 2) #左移2位，乘4
print(type(0b101)) # 类型是int，不是str
# print(bin(5) << 2) #左边是str，跑不通

binary_string = bin(5)[2:]  # 将整数转换为二进制字符串，并去除开头的 '0b' 前缀
shifted_int = int(binary_string, 2) << 2  # 将二进制字符串转换为整数，并执行位左移操作
shifted_string = bin(shifted_int)  # 将左移后的整数转换回二进制字符串
print(shifted_string)  # 输出左移后的二进制字符串

print(5 >> 1) #右移1位，除以2
print(6 >> 1)

# 位运算: &与 |或 ~非 ^异或
print(0b110 | 0b101)
# print(bin(6) | bin(5)) #TypeError,两边要是数字，不能是字符串
print(6 | 5)

print(5 & 6)
print(5 ^ 6)
# XOR重要性质
print("X ^ X = 0:", 5 ^ 5)
print(f"X ^ 0 = X: {5 ^ 0}")

print(~100)