# -*- coding:utf-8 -*-

from collections import deque
# deque(maxlen=N)创建一个固定长度的队列。当有
# 新纪录加入而队列已满时会自动移除最老的那条纪录

q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)

print(q)

q.append(4)

print(q)


q.appendleft(5)

print(q)

print(q.pop())
print(q)
print(q.popleft())
print(q)
