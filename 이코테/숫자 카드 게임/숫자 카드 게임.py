n,m = map(int,input().split())

li = []

for _ in range(n):
    li.append(list(map(int,input().split())))
min1 = 0
for i in range(n):
    tmp = min(li[i])
    if tmp > min1:
        min1 = tmp
print(min1)