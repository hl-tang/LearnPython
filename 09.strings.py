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

# split 分割
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