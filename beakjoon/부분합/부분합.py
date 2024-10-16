n,s = map(int,input().split())
li = list(map(int,input().split()))+[0]*10

start = 0
end =0
partsum = li[0]

ans = 10000000
while end<=n:
    if partsum<s:
        end+=1
        partsum+=li[end]
    else:
        ans = min(ans,end-start)
        start+=1
        partsum -= li[start-1]
if ans == 10000000:
    print(0)
else:
    print(ans+1)