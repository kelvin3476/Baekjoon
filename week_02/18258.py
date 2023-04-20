import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
L = deque([])    

for i in range(N):
    q = input().split()

    if q[0] == 'push':
        L.append(q[1])
    elif q[0] == 'pop':
        if len(L) == 0:
            print(-1)
        else:
            print(L.popleft())
    elif q[0] == 'size':
        print(len(L))
    elif q[0] == 'empty':
        if len(L) == 0:
            print(1)
        else:
            print(0)
    elif q[0] == 'front':
        if len(L) == 0:
            print(-1)
        else:
            print(L[0])
    elif q[0] == 'back':
        if len(L) == 0:
            print(-1)
        else:
            print(L[-1])