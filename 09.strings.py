# Strings are similar to arrays
# double quotes or single quotes 都可以
s = "abc"
print(s)
print(s[0:len(s)])

# But they are immutable
# means that we can't modify the string
#s[0]='A'  #error, can't reassign

'''
We can update the string, 
but updating will actually create a new string
Modifing a string is O(n) operation
'''
s += "def"  # So this creates a new string
print(s)
s = "This is just a test string"
print(s)

# 判断字符串是否只包含数字 str.isdigit()
print("123".isdigit())  # True
print("Abc123".isdigit())

# 判断字符串是否只包含字母 str.isalpha()
print("Abc".isalpha())  # True
print("Abc123".isalpha())

# Valid numeric strings can be converted
print("123" + "123")
print(int("123") + int("123"))

# And numbers can be converted to strings
print(str(123) + str(123))

# In rare cases you may need the ASCII value of a character
print(ord("a")) #97
print(ord('b')) #98

# Combine a list of strings (with delimitor)
strings = ["ab", "cd", "ef"]
print("".join(strings)) # delimitor here is empty string
print(" ".join(strings))
print(", ".join(strings))

# split 分割 返回的是list
print("  a     b    c   ".split()) #If sep is not specified or is None,就按连续空格作为分割符
print("  a     b    c   ".split(' ')) #分割符不能是空串''
print("  a     b    c   ".split('  ', 3)) #指定maxsplit,三刀四段
s = "Both list.sort() and sorted() have a key parameter\
 to specify a function (or other callable) to be called\
  on each list element prior to making comparisons."
print(s)
a = s.split()   # split()也太方便了，C++真不知道要怎么整
print(a)
a.sort()    # 字典序，大写字母排前面
print(a)
a.sort(key=str.lower)   #不管首字母大小写了
print(a)

# Return the lowest index in the string where substring sub is found
print("PythonPy".find('Py'))
# To check if sub is a substring or not, use the in operator
print('Py' in 'Python')

""" 更多参考官方文档
https://docs.python.org/3/library/stdtypes.html """

# replace 本质是替换字符，但也可以用来删除特定字符
# str.replace(old, new[, count])
s= "hello! welcome to china!!!."
print(s.replace('!', ''))
print(s.replace('!', '', 1))
#记住，字符串是不可改变的。原有的字符串保持不变——replace() 返回一个新的字符串，不会修改原有的字符串。
print(s) #原来的不变

# 逆置字符串
s = "abcdefg"
print(s[::-1]) #利用slice切片，step为负时，start默认最大，stop默认最小
print(s)
print(''.join(reversed(s))) #但这个慢，推荐用切片
print(s)