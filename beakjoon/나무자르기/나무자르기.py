n,m = map(int, input().split())
ts = [i for i in map(int, input().split())]
ts.sort()
left = 1
right = max(ts)
while left<=right:
    mid = (left+right)//2
    cal = 0
    for t in ts:
        if t<=mid:
            continue
        elif t>mid:
            cal+=t-mid
    if cal>=m:
        left = mid+1
    else:
        right = mid-1
print(right)