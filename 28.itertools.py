# https://docs.python.org/zh-cn/3/library/itertools.html
from itertools import permutations, combinations, product
# 全排列
for perm in permutations("abc"):
    print(perm)
# 数字全排列，不算前导0
for perm in permutations("301"):
    if perm[0] != "0":
        num = int(''.join(perm))
        print(num)
# 排列 4p2
for perm in permutations('ABCD', 2):
    print(perm)

# 组合
for tmp in combinations("abcd", 2):
    print(tmp)
for tmp in combinations(["物", '化', '生', '政', '史', '地'], 3):
    print(tmp)

# 笛卡尔积，相当于嵌套的for循环
a = (1,2,3)
b = ("A", 'B', 'C')
for elem in product(a, a, b):
    print(elem)
for elem in product(["物", '化', '生', '政', '史', '地'], repeat=3):
    print(elem)