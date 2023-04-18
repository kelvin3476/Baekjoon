import sys 
from collections import deque

input = sys.stdin.readline
N, K = list(map(int, input().split()))

L = deque( x+1 for x in range(N))
q = []
count = 1

while L:
    if K == count:
        q.append(L.popleft())
        count = 1
    else:
        L.append(L.popleft())
        count += 1 


print('<', end = '')
for i in q:
    if q[-1] == i:
        print(i, end = '')
    else:
        print(i, end = ', ')
print('>') 
