from collections import deque
from queue import LifoQueue

s = []
s.append("eat")
s.append("sleep")
s.append("code")

print(s.pop())
print(s.pop())
print(s.pop())


########## collections.deque ##########
d_stack = deque()
d_stack.append("eat")
d_stack.append("sleep")
d_stack.append("code")

print(d_stack)
print(d_stack.pop())
print(d_stack.pop())
print(d_stack.pop())


########## queue.LifoQueue ##########
lifo_stack = LifoQueue()
lifo_stack.put("eat")
lifo_stack.put("sleep")
lifo_stack.put("code")
print(lifo_stack)
print(lifo_stack.get())
print(lifo_stack.get())
print(lifo_stack.get())
