# HashMap (aka dict)
# C++的map: key-value 键值对
# maybe the single most common data structure you're going to use
# Like hashset, key不能重复
myMap = {}
myMap["Alice"] = 88
myMap["Bob"] = 77
print(myMap)
print(len(myMap))

myMap["Alice"] = 80 #modify the value
print(myMap["Alice"])
print(myMap.get('Alice'))   #dict的get()返回该键对应的值
print(myMap.get("Alice", 0))   #get()可以设定默认值，如果没找到的话
# get()方法 和 dict[key] 取值的区别
# print(myMap['Charles']) #key不在，报错KeyError
print(myMap.get("Charles")) #None key若不存在就返回默认值None
print(myMap.get("Charles", 0)) #0 或者设定的值
# get仅仅是防止dict[key]的KeyError报错，不会把不存在的key:val插入

print("Charles" in myMap)
print("Alice" in myMap) # search in O(1) time
# dict删除用pop，没有remove方法
myMap.pop("Alice") # remove the key also remove the value
print("Alice" in myMap)

# Initialize
myMap = {"Alice": 90, "Bob": 70} # just like manually insert
print(myMap)

# hash map is basically called dictionary in Python
# Dict comprehension
myMap = {i: 2*i for i in range(3)}
print(myMap)

# Looping through maps
#注目するのはkeys() values() items()
print(myMap.keys())
# for key in myMap: #这样直接写map名也行，但不清楚
for key in myMap.keys():
    print(key, myMap[key])

print(myMap.values())
for val in myMap.values():
    print(val)

print(myMap.items())
for key, val in myMap.items():
    print(key, val)

# hash map的排序
dic = {'f':100, 'e':500, 'aaaa':500, 'bb':30, 'ccccccc':48}
# sorted()返回list
print(sorted(dic))  #直接传字典名默认按key排
print(sorted(dic.keys(), key=len))  #f在e前面
print(sorted(dic.keys(), key=lambda x: (len(x), x))) #长度相同，则按字典序排，e在f前面;同时注意x就是key，故不要再给x下标了
print(sorted(dic.values(), reverse=True))
# 指定排序依据，同时返回 key-value
print(sorted(dic.items(), key=lambda s: s[0]))
print(sorted(dic.items(), key=lambda s: s[1])) #e在a前面
# 按val从大到小，val一样则按字典序从小到大
print(sorted(dic.items(), key=lambda x: (-x[1], x[0]))) #a在e前面
print((sorted(dic.items(), key=lambda s: s[1], reverse=True))[0])

print(max(dic, key=dic.get))    #max()返回的只是key
