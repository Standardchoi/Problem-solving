from itertools import combinations, permutations

n,m = map(int, input().split())
li = list(map(int,input().split()))
li.sort()
print(li)
nn = len(li)
ans = []

def comb(a,st):
    global nn
    if a ==m:
        print(st)
        return
    else:
        for i in range(nn):
            st = st+f"{li[i]}"
            comb(a+1,st)
   
    
comb(0,'')


