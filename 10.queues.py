# Queues (double ended queue by default)
from collections import deque   #各种数据结构揃ってるcollections
# 默认用双端队列
queue = deque() #构造函数 constructor?
queue.append(1) # 默认添加到右端
queue.append(2)
queue.append(3)
print(queue)

queue.pop()
print(queue) # 默认也是右边弹出，这样就是stack了

# 队列用popleft()
# queue.popleft() # 不返回也是可以的
cur_head = queue.popleft()
print("弹出队的是: ", cur_head)
print(queue)

queue.appendleft(1) #双端队列deque两头都可以操作
print(queue)

# 用list初始化
l1 = ['a', 'b', 'c']
q1 = deque(l1)
print(q1)
print(len(q1))
