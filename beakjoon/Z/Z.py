n,r,c = map(int,input().split())

l = 2**n
#li =  [[0 for _ in range(l)] for _ in range(l)]

num = -1
def divc(x,y,l):
    global num
    global r,c
    if x ==r and y==c:

        num+=1
        #li[x][y] = num
        return 
    if l == 2:
        num+=1
        #li[x][y] = num
        num+=1
        #li[x][y+1] = num
        num+=1
        #li[x+1][y] = num
        num+=1
        #li[x+1][y+1] = num
        return
    else:
        divc(x,y,l//2)
        divc(x,y+l//2,l//2)
        divc(x+l//2,y,l//2)
        divc(x+l//2,y+l//2,l//2)
        

divc(0,0,l)

print(num)