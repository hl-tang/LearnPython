# Nested functions have access to outer variables
# 嵌套
def outer(a,b):
    c = 'c'

    def inner():
        return a+b+c
    return inner()

print(outer("aaaa", "啊啊啊啊"))

# Can modify objects but not reassign
# unless using nonlocal keyword
def double(arr, val):
    def helper():
        # Modifying array works
        for i, n in enumerate(arr):
            arr[i] *= 2
        
        # will not modify val in the helper scope
        #val *= 2
        # #UnboundLocalError: local variable 'val' referenced before assignment

        # this will modify val outside helper scope
        nonlocal val
        val *= 2
    helper()
    print(arr, val)

x=[1,2,3]
y=10
double(x,y)
print(x,y) #但实际y的修改没有保留