import sys
sys.setrecursionlimit(10**6)
def findcat(x,y):
    if x == m or y == n or x<0 or y<0:
        return
    if li[x][y] == 1 and nl[x][y]==0:
        nl[x][y] = 1
        findcat(x,y+1)
        findcat(x,y-1)
        findcat(x+1,y)
        findcat(x-1,y)
    else:
        return
    

t = int(input())
li = list()
ans = 0
for _ in range(t):
    m,n,k = map(int, input().split())
    nl = []
    li = []
    for i in range(m):
        nl.append([0 for a in range(n)])
        li.append([0 for a in range(n)])
    for _ in range(k):
        x,y = map(int,input().split())
        li[x][y] = 1
    
    for a in range(m):
        for b in range(n):
            if li[a][b] == 1 and nl[a][b]==0:
                ans+=1
                findcat(a,b)
    print(ans)
    ans = 0

