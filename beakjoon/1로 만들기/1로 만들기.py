result = 0
min = 10000000
def dp(x,count):
    global min
    if x==1 and count<min:
        min = count
    elif count>min:
        return
    else:
        if x%3==0:
            dp(x//3,count+1)
        if x%2 ==0:
            dp(x//2,count+1)
        dp(x-1,count+1)

num = int(input())
dp(num,0)

print(min)