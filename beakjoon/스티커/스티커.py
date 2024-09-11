import sys
input = sys.stdin.readline
t = int(input())
#15684
for _ in range(t):
    n = int(input())
    li = []
    ans1 = [0 for i in range(n)]
    ans2 = [0 for i in range(n)]
    a2 = 0
    for _ in range(2):
        li.append(list(map(int, input().split())))
    
    if n == 1:
        a = li[0][0]
        b = li[1][0]
        print(max(a,b))
        continue
    elif n==2:
        print(max(li[0][1]+li[1][0],li[1][1]+li[0][0]))
        continue

    ans1[0]= li[0][0]
    ans2[0]= li[1][0]
    ans1[1]= li[0][1]+ans2[0]
    ans2[1]= li[1][1]+ans1[0]
    for i in range(2,n):
        ans1[i] += li[0][i]+max(ans2[i-1],ans2[i-2])
        ans2[i] +=li[1][i]+max(ans1[i-1],ans1[i-2])
    print(max(ans1[n-1],ans2[n-1]))