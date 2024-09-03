n = int(input())
li = []
for i in range(n):
    li.append([i for i in(map(int,input().split()))])
one = 0
zero = 0

def slice(a,b,n):
    global one
    global zero

    color = li[a][b] # 색종이의 색
    for i in range(a, a+n):
        for j in range(b,b+n):
            if color != li[i][j]:
                    slice(a,b+n//2,n//2)
                    slice(a+n//2,b+n//2,n//2)
                    slice(a,b,n//2)
                    slice(a+n//2,b,n//2)
                    return
    if color == 0: 
        zero += 1 
    else : 
        one += 1 
    
slice(0,0,n)  

print(zero)
print(one)