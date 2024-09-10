from itertools import combinations, permutations
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n,m = map(int, input().split())
li = list(map(int,input().split()))
li = sorted(list(set(li))) # 중복 제거후 정렬
n = len(li)
answer = list()
seq = set()

def comb(a,st):
    if len(st) ==m:
        for i in range(len(st)):
            print(st[i],end=' ')
        print()
        return
    for i in range(a,n):
        s = []
        s.append(li[i])
        s = st+s
        comb(i,s)
        
comb(0,[])

