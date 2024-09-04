from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    inputcommand = input().strip()
    command = deque(inputcommand)
    emp = int(input().strip())

    inputtarget = input().strip()
    if len(inputtarget)>3:
        tar = deque(inputtarget[1:-1].split(','))
    else:
        tar = []
    state = 'safe'
    dir = 'lef'
    while len(command)>0:
        i = command.popleft()
        
        if dir == 'lef':
            if i == 'R':
                dir = 'rig'
            elif i =='D' and len(tar)==0:
                state = 'error'
                break
            elif i == 'D':
                tar.popleft()
        else:
            if i == 'R':
                dir = 'lef'
            elif i =='D' and len(tar)==0:
                state = 'error'
                break
            elif i == 'D':
                tar.pop()
    

        
    ans = []
    if state=='safe':
        while len(tar)>0:
            if dir == 'lef':
                ans.append(int(tar.popleft()))
            else:
                ans.append(int(tar.pop()))
        if len(ans)>0:
            print(f'[{ans[0]}',end='')
            for i in range(1,len(ans)):
                print(f',{ans[i]}',end='')
            print(']')
        else:
            print('[]')
    else:
        print('error')