import itertools as iter
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
li1 = []
li2 = []
for x in range(n):
    line = list(map(int, input().split()))
    for i in range(n):
        if line[i] == 1:
            li1.append([x,i])
        elif line[i] == 2:
            li2.append([x,i])
comblist = list(iter.combinations(li2,m))
if len(comblist) == 0:
    print("asdasd",li2)


def brutef(ll):
    length = 0
    for i1 in li1:
        tmpl = 111111110
        for l in ll:
            tmp = abs(i1[0]-l[0])+abs(i1[1]-l[1])
            if tmp<tmpl:
                tmpl = tmp
        length+=tmpl        
    
    return length
min = 10000000
for tl in comblist:
    tmp1 = brutef(tl)   
    if tmp1<min:
        min = tmp1
print(min)