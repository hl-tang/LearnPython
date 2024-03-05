# https://www.youtube.com/watch?v=64xmy9_FtoM
# filter用法其实和map一样的，第一个parameter是函数，第二个para是可迭代变量

# 提取含有'7'的数 & 只含有'7'的数
def is_contain_7(n: int) -> bool:
    # while n:
    #     if n % 10 == 7:
    #         return True
    #     n /= 10
    # return False
    if '7' in str(n):
        return True
    else:
        return False

def is_only_contain_7(n: int) -> bool:
    for i in range(len(str(n))):
        if str(n)[i] != '7':
            return False
    return True

arr = [10, 700, 17, 77]
print(list(filter(is_contain_7, arr)))
print(list(filter(is_only_contain_7, arr)))
print([x for x in arr if is_only_contain_7(x)]) # list comprehension也能做到


from datetime import datetime
viewedNewsID_latestDate = {}
viewedNewsID_latestDate["aaa"] = datetime.fromisoformat("2023-11-01 12:00:00")
viewedNewsID_latestDate["bbb"] = datetime.fromisoformat("2023-11-01 18:00:00")
viewedNewsID_latestDate["ccc"] = datetime.fromisoformat("2023-11-02 12:00:00")
viewedNewsID_latestDate["d"] = datetime.fromisoformat("2022-11-02 12:00:00")
viewedNewsID_latestDate["e"] = datetime.fromisoformat("2021-11-02 12:00:00")
viewedNewsID_latestDate["f"] = datetime.fromisoformat("2020-11-02 12:00:00")

s = {"aaa", "ccc"}
# print(type(s))
exist = dict(filter(lambda x: x[0] in s, viewedNewsID_latestDate.items()))
exist_list = list(filter(lambda x: x[0] in s, viewedNewsID_latestDate.items()))
print(exist)
print(type(exist))
print(exist_list)
