from heapq import *
from random import shuffle

# heap 是优先队列的一种，使用优先队列能够以任意顺序增加对象
# 并且能在任何时间（可能在增加对象的同时）找到（也可能是移除）最小的元素，比列表的 min 方法效率高

# heappush(heap,x)    将x入堆
# heappop(heap)       将堆中最小的元素推出
# heapify(heap)       将heap中属性强制应用到任意一个列表
# heapreplace(heap,x) 将堆中最小的元素弹出，同时将x入堆
# nlargest(n.iter)    返回iter中最n大的元素
# nsmallest(n,iter)   返回iter中最n小的元素

data = list(range(10))
shuffle(data)
heap = []
for n in data:
    heappush(heap, n)
print(heap)

# [0, 2, 1, 4, 5, 3, 9, 8, 6, 7]
# 第i位元素总比 2*i 和 2*i+1 位置的元素小

print(heappop(heap))
print(heappop(heap))
print(heap)

# heappop 弹出最小的元素，一般来说在索引0的位置，并且会确保剩余元素中
# 最小的那个占据这个位置（堆属性）

heap = list(range(10))
shuffle(heap)
heapify(heap)
print(heap)

min = heapreplace(heap, 2.5)
print(min)
print(heap)
# heapreplace 弹出最小元素，并且将新元素推入，这样做比先heapop再heappush更高效

result = nlargest(3, heap)
print(result)
# nlargest 和 nsmallest 可以用sorted 和分片完成，但是堆更有效的使用内存
