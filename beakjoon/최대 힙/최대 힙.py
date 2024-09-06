import heapq
from sys import stdin
n = int(stdin.readline())
max_heap = []

for _ in range(n):
    i = int(stdin.readline()) 
    if i == 0 and len(max_heap)==0:
        print(0)
    elif i == 0:
        a = 0
        print(-heapq.heappop(max_heap))
    else:
        heapq.heappush(max_heap,-i)
