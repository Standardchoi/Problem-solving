import copy
n = int(input())
li = list(map(int,input().split()))
node = [[] for i in range(n)]
dele = int(input())
ans = 0
indd = li.index(-1)
for i in range(len(li)):
    if li[i]==-1:
        continue
    else:
        node[li[i]].append(i)
def caldfs(index):
    global ans
    global dele
    tmp = copy.deepcopy(node[index])
    if len(node[index]) == 0:
        ans+=1
        return
    for i in tmp:
        if i==dele:
            deldfs(i)
            node[index].remove(i)
        else:
            caldfs(i)

    if len(node[index]) == 0:
        ans+=1
        return
def deldfs(index):
    tmp = copy.deepcopy(node[index])
    if len(node[index]) == 0:
        return
    else:
        for i in tmp:
            deldfs(i)
            node[index].remove(i)
if indd == dele:
    print(0)
else:
    caldfs(indd)
    print(ans)
