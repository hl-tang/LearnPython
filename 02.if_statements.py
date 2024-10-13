# 条件语句不用 小括号条件   花括号范围
# 缩进代表
# 条件判断记得有 ：
# elif : else if

n = 1
if n > 2:
    n -= 1
elif n == 2:
    n *= 2
else:
    n += 2
print('n =', n)

# 多个条件的判断才需要小括号
# and   &&
# or    ||
n, m = 1, 2
if ((n > 2 and n != m) or n == m):
    pass
print(n)

# Ternary Operator 三目运算符
# Syntax: [on_true] if [expression] else [on_false]
m, n = 10, 20
max_mn = m if m > n else n
# max_mn = max(m, n)
print(max_mn)

print(not False)