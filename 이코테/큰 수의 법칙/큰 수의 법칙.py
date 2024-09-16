n,m,k = map(int, input().split())
li = list(map(int,input().split()))
li.sort(reverse=True)
print(li)
a = 1
ans = 0
for i in range(m):
    if a%(k+1) !=0:
        ans+= li[0]
    else:
        ans+=li[1]
    a+=1

print(ans)