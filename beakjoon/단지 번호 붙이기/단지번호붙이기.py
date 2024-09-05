
n = int(input())

total = []
check = []
lenlist = []
sumbu = 0
tmp = 0
for _ in range(n):
    total.append(list(map(int, input())))
    check.append([0 for i in range(n)])
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def df(x,y):
    if x<0 or y<0 or x==n or y==n:
        return 
    elif total[x][y] == 1 and check[x][y] ==0:
        check[x][y] = 1
        global tmp
        tmp+=1
        df(x+dx[0],y+dy[0])
        df(x+dx[1],y+dy[1])
        df(x+dx[2],y+dy[2])
        df(x+dx[3],y+dy[3])
for a in range(n):
    for b in range(n):
        if total[a][b] == 1 and check[a][b] ==0:
            sumbu+=1
            tmp = 0
            df(a,b)
            lenlist.append(tmp)

print(sumbu)
lenlist.sort()
for i in lenlist:
    print(i)