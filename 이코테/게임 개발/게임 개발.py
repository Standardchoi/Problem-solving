n,m =  map(int,input().split())
sx,sy,d = map(int,input().split())
dl = [0,1,2,3]
dx = [0,1,0,-1]
dy = [-1,0,1,0]

li = []
for i in range(n):
    li.append(list(map(int,input().split())))
tmp = 0
while True:
    if li[sx][sy] == 0:
        li[sx][sy]=1
        tmp+=1
        tt = 0
        for i in range(4):
            nx = sx + dx[i]
            ny = sy + dy[i]
            if nx<n and ny<m and  li[nx][ny] == 0:
                sx = nx
                sy = ny
                continue
            tt+=1
        if tt ==4:
            break
print(tmp)
