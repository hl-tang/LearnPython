# https://zhuanlan.zhihu.com/p/79541418

a = list(range(10))

# 超出有效索引范围
print(a[-100:5])
print(a[5:100])
print(a[-100:100])
print(a[-100:-4])
print(a[10:100])

# start的位置比stop还靠后？不会抛出异常，而是直接返回空序列
print(a[6:5])
print(a[-4:5]) #-4在有效索引范围内 a[-4] == a[6], a[-1] == a[9], a[-10] == a[0]
print(a[-4:1000])

# 缺省 在是start,stop缺省的情况下，Python的行为是尽可能取最大区间
# 按照扩充索引范围的观点，start的缺省值是无穷小()，stop的缺省值是无穷大()
print(a[:5])
print(a[5:])
print(a[::])

# step为正数
print(a[0:6:2])
print(a[::2])
print(a[:-2:2])
print(a[4::2])
# step为负数
# step为负时，start位置应在stop后面
print(a[5:1:-1])
""" 在缺省的情况下,Python的行为是尽可能取最大区间
此时访问是逆序的,start应尽量取大,stop应尽量取小,才能保证区间最大
此时,按照扩充索引范围的观点,start的缺省值是无穷大(),stop的缺省值是无穷小() """
print(a[5::-1])
print(a[:4:-2])
print(a[::-1]) #可用于逆置字符串
str = "abcdefg"
print(str[::-1])
print(str)