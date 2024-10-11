
n = int(input())
t1 = 0
li = [0 for i in range(n+1)]
li[0] = 1
for i in range(1,n+1):
    for j in range(i):
        li[i] += li[j]*li[i-j-1]
print(li[-1])