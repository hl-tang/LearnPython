# https://zhuanlan.zhihu.com/p/348370957
# 写dp，懒得手动搞个记忆化数组，就可以装饰器cache
from functools import lru_cache

@lru_cache()
def factorial(n):
    print(f"计算 {n} 的阶乘")
    return 1 if n <= 1 else n * factorial(n - 1)
print(f'5! = {factorial(5)}')
print(f'3! = {factorial(3)}') #有了cache就不会再去算1,2,3了
print(factorial.cache_info())

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
print([fib(n) for n in range(16)])
print(fib.cache_info())