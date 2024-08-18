# Tuples are like arrays but immutable
tup = (1,2,3)   #list用[]，tuple用()，dict(hash map)/set用{}
print(tup)
print(tup[0])
print(tup[-1])

# Can't modify
#tup[0] = 0 # won't work

# Can be used as key for hash map/set
myMap = {(1,2): 'a'}
# print(myMap[[1,2]]) # TypeError: unhashable type: 'list'
print(myMap[(1,2)])

mySet = set()
mySet.add((1,2))
print((1,2) in mySet)

'''
Lists can't be keys
因为list可以改, tuple不能改
'''
#mySet.add([3,4])    # error
#myMap[[3,4]] = 'b'    # error

print(type(tup))
arr = [4,5,6]
print(type(arr))
arr_tuple = tuple(arr)
print(arr_tuple, type(arr_tuple))