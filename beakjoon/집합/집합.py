
import sys

input = sys.stdin.readline

m = int(input())

mylist =  set()
for i in range(m) :

    li = input().split()
    command = li[0]
    if len(li) == 1:
        if command == "all":
            mylist = set([i for i in range(1,21)])
        elif command =="empty":
            mylist = set()
        continue
    
    num = int(li[1])
    if command == "add":
        mylist.add(num)
    elif command == "remove" and (num in mylist):
        mylist.remove(num)
    elif command == "check":
        if int(num) in mylist:
            print(1)
        else:
            print(0)
    elif command=="toggle":
        if num in mylist:
            mylist.remove(num)
        else:
            mylist.add(num)
    
