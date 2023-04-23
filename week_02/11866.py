import sys 
from collections import deque

input = sys.stdin.readline
N, K = list(map(int, input().split())) # 7,3 

L = deque( x+1 for x in range(N)) # [1, 2, 3, 4, 5, 6, 7]
q = [] # [3, 6, 2, 7, 5, 1, 4]
count = 1

while L:
    if K == count: # 3번째 순서 일때
        q.append(L.popleft()) # q리스트에 숫자 추가 (#3번째 순서일때 K == count)
        count = 1
    else:
        L.append(L.popleft()) # L 리스트에서 첫번째 숫자를 pop 하고 바로 맨 뒤로 그 숫자 추가 해준다.
        count += 1 


print('<', end = '')
for i in q:
    if q[-1] == i:
        print(i, end = '')
    else:
        print(i, end = ', ')
print('>') 
