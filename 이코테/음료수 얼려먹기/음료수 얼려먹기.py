n,m = map(int,input().split())

li = []
visit = []
for _ in range(n):
    li.append(list(map(int,input().split())))
    visit.append([0 for i in range(m)])
dx = [0,1,0,-1]
dy = [-1,0,1,0]

def dps(x,y):
    visit[x][y] = 1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx< n and nx >=0 and ny<m and  ny>=0 and visit[nx][ny] ==0 and li[nx][ny] == 0:
            dps(nx,ny)
        else:
            continue
tmp = 0
for x in range(n):
    for y in range(m):
        if li[x][y] == 0 and visit[x][y] ==0:
            tmp +=1
            dps(x,y)
print(tmp)