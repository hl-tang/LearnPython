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

print("Alice" in myMap) # search in O(1) time
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
dic = {'f':100, 'aaaa':500, 'bb':30, 'ccccccc':48}
# sorted()返回list
print(sorted(dic))  #直接传字典名默认按key排
print(sorted(dic.keys(), key=len))
print(sorted(dic.values(), reverse=True))
# 指定排序依据，同时返回 key-value
print(sorted(dic.items(), key=lambda s: s[0]))
print(sorted(dic.items(), key=lambda s: s[1]))
print((sorted(dic.items(), key=lambda s: s[1], reverse=True))[0])

print(max(dic, key=dic.get))    #max()返回的只是key