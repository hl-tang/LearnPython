# List comprehension
# リスト内包表記 https://www.youtube.com/watch?v=Fj0ejL9Rmr4
# 初始化list的高级方法
arr = [i for i in range(5)] #i从0遍历到4，每次都把i(for左边)加入到数组
print(arr)

arr = []
for i in range(1,6):
    arr.append(i)
print(arr)

import math
arr = [math.pow(i,2) for i in range(5)]
print(arr)

arr = [pow(i,2) for i in range(5)]
print(arr)

# list comprehension还可以带if条件判断
arr = [pow(i,2) for i in range(11) if i % 2 == 0]
print(arr)
# 其实相当于用list comprehension做filter(), 当然list comprehension也可以实现map()的功能
kd_str_list = ['{"K": "a", "D": "1"}', '', '{"K": "b", "D": "2"}', ' '] #遇到'' json.loads就bug了
import json
kd_dict_list = [json.loads(item) for item in kd_str_list if item.strip()] # 防止有item是空
print(kd_dict_list)
