n,r,c = map(int,input().split())

l = 2**n
#li =  [[0 for _ in range(l)] for _ in range(l)]

num = 0
def divc(x,y,l):
    global num
    global r,c
    
    if l == 1:
        return
    
    if x<l//2 and y<l//2:
        divc(x,y,l//2)
    elif x<l//2 and y>=l//2:
        num+=(l//2)**2
        divc(x,y-l//2,l//2)
    elif x>=l//2 and y<l//2:
        num+=2*(l//2)**2
        divc(x-l//2,y,l//2)
    else:
        num+=3*(l//2)**2
        divc(x-l//2,y-l//2,l//2)
divc(r,c,l)

print(num)