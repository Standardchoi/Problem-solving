

n = int(input())

nl = list(map( int,input().split()))

m =  int(input())

ml =  list(map( int,input().split()))

nl.sort()
result = []

def binary(arr, tar):
    lef= 0
    rig = len(arr)-1
    while lef<=rig:
        mid = (lef+rig)//2
        if arr[mid] ==tar:
            return True
        elif arr[mid]>tar:
            rig = mid-1
        else:
            lef = mid+1


for i in ml:
    if binary(nl ,i)==True:
        result.append(1)
    else:
        result.append(0)


for i in result:
    print(i ,end=' ')
