""" Python for Coding Interviews - Everything you need to Know
https://www.youtube.com/watch?v=0K_eZGS5NsU """

# Dynamic type variable 运行时才决定变量的type
n=0
print("n =",n)
print(f"n ={n}")

n="abc"
print("n =",n)

# Multiple assignments
n, m = 0, 'abc'
print(n,m)
print(f"{n}{m}")

# Increment
n = n+1 #good
n+=1 #good
#n++ #bad syntax error
print(n)

# None : null 空值
n = None
print(n)