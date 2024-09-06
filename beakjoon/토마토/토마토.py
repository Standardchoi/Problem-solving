from collections import deque
m,n = map(int, input().split())
li = []
for _ in range(n):
    li.append(list(map(int,input().split())))

l = deque()
dx = [0,0,1,-1]
dy = [1,-1,0,0]
for a in range(n):
    for b in range(m):
        if li[a][b]==1:
            l.append([a,b,0])
tmp = 0
while len(l)>0:
    x,y,c = l.popleft()
    tmp = max(c,tmp)
    #print(x,y,c)
    for i in range(4):
        a=x+dx[i]
        b=y+dy[i]
        if a<n and b<m and a>=0 and b>=0 and li[a][b]==0:
            li[a][b] = 1
            l.append([a,b,c+1])
        else:
            continue

isz = 0
for a in range(n):
    for b in range(m):
        if li[a][b]==0:
            isz = 1
            break
if isz ==1:
    print(-1)
else:
    print(tmp)