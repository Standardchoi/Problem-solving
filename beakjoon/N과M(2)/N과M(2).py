import itertools




n,m = map(int,input().split())
nl = []
for i in range(n):
    nl.append(i+1)
a = list(itertools.combinations(nl,m))

for i in a:
    for w in i:
        print(w,end=' ')
    print()