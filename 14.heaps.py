# Heaps
import heapq

# in Python they're implemented with array
# To create an empty heap, just create an empty list
minHeap = []
# by default heaps in Python are Min heaps 默认小顶堆

# push用heapq.heappush()    heappush 往一个最小堆添加元素
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 6)
heapq.heappush(minHeap, 1)
heapq.heappush(minHeap, 4)
print(minHeap)

# Min is always at index 0
print(minHeap[0])

# heappop 弹出堆中的最小值并返回
heapq.heappop(minHeap)
print(minHeap)

while len(minHeap):
    print(heapq.heappop(minHeap))


'''
如果最大堆，取反之后再放入堆，取出的时候再取反
No max heap by default, work around is
to use min heap and multiply by -1 when push & pop
'''
maxHeap = []
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -4)

# Max is always at index 0
print(-1 * maxHeap[0])

while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap))


# heap本质就是list加上堆的特性
# heapfiy 将一个list转为最小堆  O(n)时间
l = [45,7,1,9,33,78]
heapq.heapify(l)
print(l)