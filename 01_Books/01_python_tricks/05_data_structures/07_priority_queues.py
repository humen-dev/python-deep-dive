import heapq
from queue import PriorityQueue

q = []
q.append((2, "code"))
q.append((1, "eat"))
q.append((3, "sleep"))

# NOTE: Remember to re-sort every time
# a new element is inserted, or use
# bisect.insort().
q.sort(reverse=True)

while q:
    next_item = q.pop()
    print(next_item)


########## heapq ##########
heap: list[tuple[int, str]] = []
heapq.heappush(heap, (2, "code"))
heapq.heappush(heap, (1, "eat"))
heapq.heappush(heap, (3, "sleep"))

while q:
    next_item = heapq.heappop(q)
    print(next_item)


########## queue.PriorityQueue ##########
pq = PriorityQueue()
pq.put((2, "code"))
pq.put((1, "eat"))
pq.put((3, "sleep"))
while not pq.empty():
    next_item = pq.get()
    print(next_item)
