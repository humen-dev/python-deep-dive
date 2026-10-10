from collections import deque
from multiprocessing import Queue as ProcessQueue
from queue import Queue

########## collections.deque ##########
print("-" * 10, "collections.deque", "-" * 10)
dq: deque[str] = deque()
dq.append("eat")
dq.append("sleep")
dq.append("code")
print(dq)
print(dq.popleft())
print(dq.popleft())
print(dq.popleft())


########## queue.Queue ##########

q: Queue[str] = Queue()
q.put("eat")
q.put("sleep")
q.put("code")
print(q)
print(q)


########## multiprocessing.Queue ##########
mq: ProcessQueue[str] = ProcessQueue()
mq.put("eat")
mq.put("sleep")
mq.put("code")
print(q)
print(q.get())
print(q.get())
print(q.get())
