from itertools import combinations
from collections import deque

n, m = map(int, input().split())
lab_map = []
viruses = []

for i in range(n):
    row = list(map(int, input().split()))
    lab_map.append(row)
    for j, cell in enumerate(row):
        if cell == 2:
            viruses.append((i, j))

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(active_viruses):
    queue = deque(active_viruses)
    visited = [[False] * n for _ in range(n)]
    time = [[-1] * n for _ in range(n)]
    
    for x, y in queue:
        visited[x][y] = True
        time[x][y] = 0
    
    max_time = 0
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and lab_map[nx][ny] != 1:
                visited[nx][ny] = True
                time[nx][ny] = time[x][y] + 1
                queue.append((nx, ny))
                if lab_map[nx][ny] == 0:
                    max_time = max(max_time, time[nx][ny])
    
    return max_time if all(visited[i][j] or lab_map[i][j] == 1 for i in range(n) for j in range(n)) else -1

min_time = float('inf')
for active_viruses in combinations(viruses, m):
    result = bfs(active_viruses)
    if result != -1:
        min_time = min(min_time, result)
if sum(row.count(0) for row in lab_map) ==0 :
    print(0)
else:
    print(min_time if min_time != float('inf') else -1)