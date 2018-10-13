# 双端队列在需要按照增加的顺序来移除元素时非常有用
# collections 模块中包含deque
from collections import deque

q = deque(range(5))
q.append(5)
q.appendleft(6)
print(q)
print(q.pop())
print(q)
print(q.popleft())
q.rotate(3)  # 向右移位  参数为负 向左移位
print(q)

q.extendleft([11, 12, 13])
print(q)
